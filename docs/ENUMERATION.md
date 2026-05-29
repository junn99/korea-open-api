# 전수화(Full Enumeration) 방법

이 카탈로그는 **기관/서비스 단위의 대표 오픈API를 폭넓게 큐레이션**한 것입니다.
하지만 GOAL.md의 "정말 없을 때까지(전수)"에 도달하려면, 손으로 검색하는 큐레이션으로는
부족합니다 — **data.go.kr 한 곳만 해도 데이터셋 단위 오픈API가 수만 건**이며 매일 변하기 때문입니다.

## 왜 수동 큐레이션으로는 '전수'가 안 되나

- 약 18라운드(70여 회) 교차 검색 결과, **기관/서비스 단위**에서는 신규 발견이 급감(포화 근접)했습니다.
- 그러나 동일 기관 안에서도 하위 데이터셋(예: "○○부_△△정보서비스")이 끝없이 존재합니다.
- 이 하위 데이터셋까지 모두 담는 "데이터셋 단위 전수"는 **프로그램적 enumerate** 없이는 불가능합니다.

## 유일한 길: data.go.kr 목록조회 API

- 데이터셋 **15077093 "공공데이터활용지원센터_목록조회서비스"** 가 포털의 전체 오픈API/데이터셋 목록을 반환합니다.
- 호스트 `apis.data.go.kr` 은 (포털 웹과 달리) 본 실행 환경에서 **차단되지 않았습니다**(HTTP 500 = 키/파라미터 없는 요청에 대한 정상 게이트웨이 응답).
- 즉, **무료 서비스키 1개만 있으면** 전체 목록을 페이지네이션으로 긁어 거의 '전수'에 도달할 수 있습니다.

## 절차

1. https://www.data.go.kr 회원가입(무료).
2. "공공데이터활용지원센터_목록조회서비스"(15077093) 활용신청 → **인증키(serviceKey)** 발급(즉시).
3. 발급키를 환경변수로 두고 아래 스크립트를 실행:

   ```bash
   export DATAGO_SERVICE_KEY='발급받은_Decoding_키'
   python3 scripts/fetch_datago.py --resource open-data-list --out data/datago_raw.json
   python3 scripts/normalize_datago.py   # → data/datago_apis.json
   python3 scripts/build_readme.py        # README 부록 A 갱신
   ```

4. 산출된 원천 목록을 카탈로그 스키마(`data/datago_apis.json`)로 정규화.

## 실행 결과 (실측, 2026-05-29)

키 발급 후 실제로 전수 수집을 완료했습니다.

- **호스트/경로 확정**: 이 서비스는 odcloud 호스팅이며 OAS 문서
  (`https://infuser.odcloud.kr/oas/docs?namespace=15077093/v1`)에서 리소스 경로를 확인:
  - `https://api.odcloud.kr/api/15077093/v1/open-data-list` — 오픈 API **17,305** operation행
  - `.../file-data-list` — 파일데이터 201,842 · `.../standard-data-list` — 표준데이터 12,655
- 파라미터는 `serviceKey`, `page`, `perPage` (odcloud 표준). 앞서 추정했던
  `apis.data.go.kr/15077093/getDataList` 류는 전부 HTTP 500 → odcloud 경로가 정답이었음.
- 정규화 결과: 서비스(list_id) 단위 **무료 오픈 API 12,081건**, 순수 유료 1건만 제외.

### "2022년 미갱신" 오해에 대하여

데이터셋 페이지에 표시되는 갱신주기/표본 갱신일과 무관하게, **목록 API 자체는 최신**입니다.
수집 데이터 기준 `created_at` 최신 **2026-05-22**, `updated_at` 최신 **2026-05-28**,
2025년 등록 2,250건·2026년 593건. 전 항목 `is_deleted=N`(활성). 즉 enumerate 결과는 현행 목록입니다.

## 대안

- **지자체/부처 자체 포털**(서울 열린데이터광장, 경기데이터드림, 제주데이터허브 등)도 각자 목록 API를 제공하므로,
  같은 방식으로 포털별 enumerate가 가능합니다.
- 민간(네이버·카카오·넥슨·업비트 등)은 집계처가 없으므로 **수동 큐레이션이 최선**입니다.
