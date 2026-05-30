# 상세 스펙 — 프로필 데이터 모델 & 매칭 규칙

> PRODUCT_youth_v2(기획)를 **빌드 가능한 수준**으로 내린 명세. 프로필 필드 정의, 온보딩 카피,
> 정책 자격요건 스키마, 잠금해제 IF-THEN 규칙, 매칭 의사코드, 엣지케이스.
> 자격요건 수치는 2026-05 웹검증 기준(정책은 매년 변동 → `verified_at` 보유). 대상 브랜치 `claude/api-mashup-ideation`

---

## 1. 프로필 데이터 모델 (UserProfile)

> 모든 필드 nullable. `null` = "아직 안 받음" → 매칭 시 "조건 불명"으로 처리(배제 아님).
> `layer`는 수집 시점. 저장은 로컬 우선(민감도 높은 L2는 세션·온디맨드).

```ts
type Layer = 0 | 1 | 2;

interface UserProfile {
  // ── Layer 0 : 가입 필수 (6) ──
  age: number | null;                    // 만 나이
  regionCode: string | null;            // 법정동/행정 시군구 코드 (예: "11620" 관악구)
  regionLabel: string | null;           // 표시용 "서울 관악구"
  employment: 'student'|'jobseeker'|'employed'|'selfemp' | null;
  incomeBand: 'none'|'u200'|'200_300'|'o300' | null;  // 월소득 구간(만원)
  gender: 'M'|'F' | null;
  housing: 'independent'|'withParents'|'dorm' | null;  // 자취/부모님과/기숙사

  // ── Layer 1 : 점진 보강 (넛지로 1개씩) ──
  isHomeless: boolean | null;           // 무주택 여부
  isHouseholder: boolean | null;        // 세대주 여부
  maritalStatus: 'single'|'married'|'preMarriage' | null;
  deposit: number | null;               // 임차보증금(만원) — housing=independent일 때만
  monthlyRent: number | null;           // 월세(만원)
  militaryDone: boolean | null;         // 병역 이행(남성) → 연령상한 가산
  smeWorker: boolean | null;            // 중소기업 재직
  education: 'highschool'|'college'|'enrolled'|'graduate' | null;

  // ── Layer 2 : 정밀 진단 (정책 신청 직전 온디맨드) ──
  exactIncomeYear: number | null;       // 연 총급여(만원)
  householdSize: number | null;         // 가구원수
  carValue: number | null;              // 자동차가액(만원)
  welfareTier: 'basic'|'nearpoor'|'none' | null;  // 기초수급/차상위
  special: ('disabled'|'multicultural'|'veteran'|'singleParent')[] | null;

  // ── 메타 ──
  interests: ('housing'|'money'|'job'|'living'|'edu')[];  // 관심(추천 가중치)
  completeness: number;                 // 0~100 (진행률 표시)
}
```

### 진행률 계산 (gamification)
```
completeness = round(
   L0채움수/6 * 50      // L0가 절반 비중
 + L1채움수/8 * 35
 + L2채움수/5 * 15 )
```
홈에 "프로필 60% · **4칸 더 채우면 정책 7건 더**" 표기에 사용.

---

## 2. 온보딩 6문항 — 확정 카피 & 입력 위젯

| # | 위젯 | 질문(헤드) | 보조문구 | 선택지 |
|---|---|---|---|---|
| 1 | 슬라이더(15~45) | 나이가 어떻게 되세요? | 청년정책은 보통 만 19~34세 대상이에요 | (정수) + 실시간 힌트 |
| 2 | 칩/검색 | 어디 살고 계세요? | 사는 시·군·구 기준 (지자체 사업 필터) | 시군구 코드 |
| 3 | 4지선다 | 지금 어떤 상황인가요? | 상태에 따라 받을 수 있는 게 갈려요 | 대학생·대학원생 / 취준·구직 / 직장인(재직) / 프리랜서·자영업 |
| 4 | 3지선다 | 어디서 지내세요? | 주거지원의 핵심 기준이에요 | 혼자 자취 / 부모님과 / 기숙사·하숙 |
| 5 | 4지선다 | 월 소득이 대략 어느 정도? | 정확하지 않아도 돼요 | 없음 / 200만↓ / 200~300 / 300만↑ |
| 6 | 버튼 | 성별이 어떻게 되세요? | 여성 특화·병역 관련 정책 분기에 써요 | 남 / 여 |

> 관심사(interests)는 온보딩 마지막 또는 홈 첫 진입 시 1회 — 추천 정렬 가중치용(필수 아님).

### 나이 슬라이더 실시간 힌트 규칙
```
19 ≤ age ≤ 34 → "✅ 대부분의 청년정책 대상"
35 ≤ age ≤ 39 → "🟡 일부 정책(만 39세까지) 가능"
gender=M & militaryDone=null & 35≤age≤40 → "🟡 병역 이행했다면 아직 대상일 수 있어요"  // L1 넛지 트리거
else → "⚠️ 청년정책 대상이 아닌 경우가 많아요"
```

---

## 3. 정책 자격요건 스키마 (PolicyRule)

각 정책은 아래 규칙 객체를 가진다. 매칭 엔진이 UserProfile과 대조.

```ts
interface PolicyRule {
  id: string; name: string; org: string; category: Category;
  // 정량 게이트 (있으면 검사, profile값 null이면 'unknown')
  ageMin?: number; ageMax?: number; ageMilitaryBonus?: number; // 병역 가산 상한
  incomeType?: 'personalYear'|'householdMedian'|'coupleYear';
  incomeMax?: number;            // personalYear/coupleYear=만원, householdMedian=% (예:150,250)
  // 정성 게이트 (boolean 요구)
  needHomeless?: boolean; needHouseholder?: boolean;
  maritalReq?: 'single'|'married'|'any';
  needSmeWorker?: boolean; needIndependent?: boolean;
  depositMax?: number; rentMax?: number;     // 주거형
  // 신청 실행정보 (온통청년 API 매핑)
  applyUrl?: string; docs?: string[]; period?: string; dday?: number|null;
  // 잠금조건: 이 프로필 필드들이 채워져야 "정확 판정" 가능
  requiresFields: (keyof UserProfile)[];
  verified_at: string;           // "2026-05" — 수치 신뢰 시점
}
```

---

## 4. 매칭 엔진 — 3-State 판정 (의사코드)

각 정책 × 사용자 → **eligible / possible / blocked** 3상태.

```
function judge(policy, profile):
  reasons = []        // 사용자에게 보여줄 근거
  state = 'eligible'  // 낙관적 시작, 게이트 통과 못하면 강등

  for gate in policy.gates:
     v = profile[gate.field]
     if v == null:
        state = downgrade(state, 'possible')      // 모르면 '가능성'으로
        reasons.push(missing(gate))               // "무주택 여부 확인 필요"
        continue
     if not gate.test(v):
        return { state:'blocked', reasons:[fail(gate)] }  // 하나라도 명확히 탈락 → blocked
     reasons.push(pass(gate))                      // "만 24세 → 연령 충족"

  score = baseScore(policy, profile)               // 관심사·마감임박 가중
  return { state, score, reasons }
```

### state별 UX
- **eligible** (모든 게이트 명확 통과): 🟢 "받을 수 있어요" — 신청 유도 강조
- **possible** (일부 게이트 unknown): 🟡 "가능성 높음 — N개 더 확인하면 확정" → **L1 넛지 연결**
- **blocked** (하나라도 명확 탈락): 기본 숨김, "왜 안 보이나요?"에서만 사유와 함께 노출

### downgrade 표
```
eligible + unknown → possible
possible + unknown → possible
any + fail        → blocked   (즉시 종료)
```

---

## 5. 잠금해제 IF-THEN 규칙집 (검증된 수치 기반)

> 아래는 §SPEC_catalog의 정책에 실제 적용되는 규칙. 수치는 2026-05 웹검증.

```
R1  housing=independent & isHomeless=true
     → UNLOCK [청년월세지원, 버팀목전세대출, 행복주택]
     → TIP   ["전입신고+확정일자 당일", "자취방 시세 신호등"]

R2  employment=employed & smeWorker=true
     → UNLOCK [청년내일채움공제(입사6개월내), 중소기업취업자 소득세감면(청년 90%/5년)]
     → TIP   ["연말정산 때 감면명세서 제출", "재직 6개월 넘기 전 공제 신청"]

R3  age 19~34 & incomeType=householdMedian ≤250%  (도약계좌)
     → UNLOCK [청년도약계좌]   // 개인 총급여 ≤7,500만 동시
     → TIP   ["만기 5년 — 중도해지 주의", "비과세 한도 월70만"]

R4  employment=jobseeker & age 15~34
     → UNLOCK [국민취업지원제도 II유형(청년은 소득무관), 청년수당(지역)]
     → TIP   ["구직활동계획서 미리", "II유형은 소득·재산 무관"]

R5  incomeBand in (none,u200)  OR welfareTier in (basic,nearpoor)
     → UNLOCK [햇살론유스(연소득3,500만↓), 근로장려금]
     → TIP   ["근로장려금 정기신청 5.1~5.31"]

R6  gender=M & militaryDone=true
     → RECALC ageMax += min(병역기간, 6년)  // 모든 정책 연령상한 재계산
     → TIP   ["군 복무로 연령 가산 — 아직 청년 대상"]

R7  regionCode set
     → UNLOCK [해당 시군구 전입지원금·이사비·청년수당 지역형]
     → TIP   ["{지역} 이사비 지원", "{지역} 음식물 배출요일"]

R8  maritalStatus in (married,preMarriage)
     → UNLOCK [신혼부부 전세·특별공급, 신혼희망타운]
     → TIP   ["혼인신고 전후 자격 차이 확인"]
```

---

## 6. 넛지 엔진 — "1개 더 답하면 N건 더"

홈 상단에 L1 질문을 **하나씩** 노출. 어떤 걸 먼저 물을지 = **잠금해제 기대값** 순.

```
nudgeValue(field) = (그 field가 unlock하는 possible→eligible 전환 정책수)
                    × (그 정책들의 관심사 가중)
                    − 피로페널티(이미 많이 물었으면 ↓)

show top1 nudge where profile[field]==null
규칙:
 - 하루 최대 2개까지만 노출
 - housing=independent인데 isHomeless=null → R1 가치 큼 → 최우선
 - 한 번 "나중에" 누르면 그 field 48h 쿨다운
```

예: 자취+무주택 미답 사용자 → "🏠 무주택이세요? **1번 답하면 주거정책 3건 더 보여요**" (토글 즉답 → 즉시 카드 추가)

---

## 7. 엣지케이스 & 정직성 규칙
- **정책 수치는 매년 변동**: 각 카드에 `verified_at` 노출, 90일 지나면 "기준 변동 가능, 신청처 확인" 배지.
- **blocked 오판 방지**: profile이 자연어/구간이라 애매하면 blocked 대신 possible 유지. 명확한 정수 비교에서만 blocked.
- **소득 구간 ↔ 중위소득%**: incomeBand(구간)로는 householdMedian 정밀판정 불가 → 항상 possible, L2에서 exactIncome+householdSize 받아야 eligible 승격.
- **지역 누락**: 온통청년이 일부 기초지자체 사업 미수록 가능 → "누락 제보" 버튼.
- **중복 제거**: 온통청년 + 복지로 동일 정책 → name+org 정규화 dedupe.
- **개인정보**: L2(소득·자산·수급)는 저장 안 하고 그 판정 1회만 사용 옵션 제공.

## 8. 구현 우선순위 (MVP cut)
1. L0 6문항 + R1·R4·R7(주거·구직·지역) 규칙만 → 가장 페인 큰 3축 커버
2. possible/eligible 2상태 + 넛지 1종(무주택)
3. 생존팁은 §SPEC_catalog의 'static/region' 먼저, 'data기반(시세·물가)' 다음
