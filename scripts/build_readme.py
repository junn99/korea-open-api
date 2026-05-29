#!/usr/bin/env python3
"""data/korea-open-apis.json 으로부터 README.md 카탈로그를 생성한다.

JSON을 단일 진실 소스(single source of truth)로 두고 README를 항상 동기화한다.
사용법: python3 scripts/build_readme.py
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "korea-open-apis.json"
DATAGO = ROOT / "data" / "datago_apis.json"
OUT = ROOT / "README.md"

# 분야별 아이콘 (표시용 — 헤더 앵커에는 영향 없음, 분포표에만 사용)
CAT_ICON = {
    "공공·행정": "🏛", "교통": "🚍", "금융": "💵", "교육·학술": "🎓",
    "문화·관광·체육": "🎭", "생활·소셜": "💬", "날씨·환경": "☀️", "농축수산": "🌾",
    "콘텐츠·미디어": "📺", "지도·위치": "🗺", "보건·식품": "🏥", "부동산": "🏘",
    "채용·고용": "💼", "재난·안전": "🚨", "에너지": "⚡", "인공지능": "🤖",
    "과학기술·특허": "🔬", "상권·창업": "🏪", "검색": "🔎", "법령·사법": "⚖️",
    "언어·사전": "📖", "무역·통상": "🚢", "게임": "🎮", "통신·인터넷": "📡",
    "쇼핑": "🛍", "과학·통계": "📊", "결제·핀테크": "💳", "클라우드": "☁️",
    "커뮤니케이션": "📨", "물류·배송": "📦", "IoT·스마트홈": "🏠",
    "블록체인·암호화폐": "🔗", "산업·고용": "🏭",
}


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def slug(text: str) -> str:
    """GitHub 호환 헤더 앵커 생성 (한글/영문/숫자/하이픈 유지, 그 외 제거)."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)  # ·, /, (), 이모지 등 제거
    s = s.replace(" ", "-")
    return s


def main() -> None:
    doc = json.loads(DATA.read_text(encoding="utf-8"))
    meta = doc["meta"]
    apis = doc["apis"]

    cats = Counter(a["category"] for a in apis)
    ordered_cats = [c for c, _ in sorted(cats.items(), key=lambda x: (-x[1], x[0]))]
    pricing = Counter(a["pricing"] for a in apis)
    auth_signup = sum(1 for a in apis if a.get("signup_required"))

    L = []
    a = L.append

    # ── 헤더 ──
    a(f"# {meta['title']}")
    a("")
    a(meta["description"])
    a("")
    a(f"![APIs](https://img.shields.io/badge/큐레이션_API-{len(apis)}-blue) "
      f"![Categories](https://img.shields.io/badge/분야-{len(cats)}-green) "
      f"![data.go.kr](https://img.shields.io/badge/data.go.kr_전수-12%2C073-orange)")
    a("")
    a(f"> 이 파일은 자동 생성됩니다. 원본 데이터는 [`data/korea-open-apis.json`](data/korea-open-apis.json) 이며 "
      f"`python3 scripts/build_readme.py` 로 재생성합니다. **README를 직접 수정하지 마세요.**")
    a("")
    a(f"- 최종 갱신: **{meta['generated']}** · 버전: **{meta['version']}**")
    a(f"- 큐레이션 API: **{len(apis)}** · 분야: **{len(cats)}** "
      f"· 요금: free **{pricing.get('free', 0)}** / free-tier **{pricing.get('free-tier', 0)}** "
      f"· 회원가입·승인 필요: **{auth_signup}**")
    a("- 이와 별개로 공공데이터포털(data.go.kr) 오픈 API **전수 12,073건**을 "
      "[`data/datago_apis.json`](data/datago_apis.json) 으로 제공합니다 ([부록 A](#부록-a--datagokr-오픈-api-전수)).")
    a("")

    # ── 목차 ──
    a("## 목차")
    a("")
    a("- [분야별 분포](#분야별-분포)")
    a("- **분야별 API 목록**")
    for c in ordered_cats:
        icon = CAT_ICON.get(c, "•")
        a(f"  - [{icon} {c}](#{slug(c)}) ({cats[c]})")
    a("- [부록 A — data.go.kr 오픈 API 전수](#부록-a--datagokr-오픈-api-전수)")
    a("- [한계 및 주의](#한계-및-주의)")
    a("")

    # ── 분야별 분포 ──
    a("## 분야별 분포")
    a("")
    a("| 분야 | 개수 |")
    a("|------|------:|")
    for c in ordered_cats:
        icon = CAT_ICON.get(c, "•")
        a(f"| {icon} [{esc(c)}](#{slug(c)}) | {cats[c]} |")
    a(f"| **합계** | **{len(apis)}** |")
    a("")

    # ── 분야별 상세 표 ──
    a("## 분야별 API 목록")
    a("")
    for c in ordered_cats:
        icon = CAT_ICON.get(c, "•")
        a(f"### {icon} {c}")
        a("")
        a("| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |")
        a("|-----|----------|------|------|------|:----:|")
        for x in [y for y in apis if y["category"] == c]:
            signup = "✅" if x.get("signup_required") else "—"
            name = esc(x["name"])
            link = f"[{name}]({x['docs_url']})" if x.get("docs_url") else name
            a("| {link} | {prov} | {desc} | {auth} | {price} | {signup} |".format(
                link=link, prov=esc(x["provider"]), desc=esc(x["description"]),
                auth=esc(x["auth"]), price=esc(x["pricing"]), signup=signup))
        a("")
        a("<sub>[⬆ 맨 위로](#목차)</sub>")
        a("")

    # ── 부록 A: data.go.kr 전수 ──
    if DATAGO.exists():
        dg = json.loads(DATAGO.read_text(encoding="utf-8"))
        dm = dg["meta"]
        a("## 부록 A — data.go.kr 오픈 API 전수")
        a("")
        a("위 큐레이션과 별개로, 공공데이터포털 **목록조회 API(15077093)** 로 오픈 API 목록을 "
          "**전수 수집**했습니다. 기계 판독용 전체 목록은 "
          "[`data/datago_apis.json`](data/datago_apis.json) 에 있습니다.")
        a("")
        a(f"- 수집일: **{dm['generated']}** · 무료 오픈 API 서비스: **{dm['service_count']:,}** "
          f"(operation 단위 원천 행 **{dm['source_total_rows']:,}**, 순수 유료 제외 {dm['skipped_paid']})")
        a("- 신선도: 수집된 목록은 **현재 활성(is_deleted=N)** 항목만 포함하며, "
          "최근 등록·갱신분(2025–2026년 등록 다수)까지 반영됩니다.")
        a("")
        a("| 분야(공공데이터포털 분류) | 개수 |")
        a("|------|------:|")
        for cat, n in dm["categories"].items():
            a(f"| {esc(cat)} | {n:,} |")
        a("")
        a("> 전체 12,000여 건은 README 표에 모두 싣지 않고 JSON으로만 제공합니다(가독성·용량). "
          "분야별 핵심 API는 위 큐레이션 섹션을 참고하세요.")
        a("")
        a("<sub>[⬆ 맨 위로](#목차)</sub>")
        a("")

    # ── 한계 ──
    a("## 한계 및 주의")
    a("")
    for lim in meta.get("limitations", []):
        a(f"- {lim}")
    a("")

    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {OUT} ({len(apis)} apis, {len(cats)} categories)")


main()
