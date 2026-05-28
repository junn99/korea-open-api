#!/usr/bin/env python3
"""data/korea-open-apis.json 으로부터 README.md 카탈로그를 생성한다.

JSON을 단일 진실 소스(single source of truth)로 두고 README를 항상 동기화한다.
사용법: python3 scripts/build_readme.py
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "korea-open-apis.json"
OUT = ROOT / "README.md"


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def main() -> None:
    doc = json.loads(DATA.read_text(encoding="utf-8"))
    meta = doc["meta"]
    apis = doc["apis"]

    cats = Counter(a["category"] for a in apis)
    pricing = Counter(a["pricing"] for a in apis)
    auth_signup = sum(1 for a in apis if a.get("signup_required"))

    lines = []
    lines.append(f"# {meta['title']}")
    lines.append("")
    lines.append(meta["description"])
    lines.append("")
    lines.append(
        f"> 자동 생성 파일입니다. 원본은 `data/korea-open-apis.json` 이며 "
        f"`python3 scripts/build_readme.py` 로 재생성합니다. 직접 수정하지 마세요."
    )
    lines.append("")
    lines.append(
        f"- 생성일: **{meta['generated']}** · 버전: **{meta['version']}**"
    )
    lines.append(f"- 총 API 수: **{len(apis)}** · 분야 수: **{len(cats)}**")
    lines.append(
        f"- 요금: free **{pricing.get('free', 0)}** / free-tier "
        f"**{pricing.get('free-tier', 0)}** · 회원가입·승인 필요: **{auth_signup}**"
    )
    lines.append("")

    # 분야별 요약
    lines.append("## 분야별 분포")
    lines.append("")
    lines.append("| 분야 | 개수 |")
    lines.append("|------|------|")
    for cat, n in sorted(cats.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {esc(cat)} | {n} |")
    lines.append("")

    # 분야별 상세 표
    lines.append("## 분야별 API 목록")
    lines.append("")
    for cat, _ in sorted(cats.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"### {cat}")
        lines.append("")
        lines.append("| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |")
        lines.append("|-----|----------|------|------|------|------|------|------|")
        for a in [x for x in apis if x["category"] == cat]:
            signup = "필요" if a.get("signup_required") else "불필요"
            doc_link = f"[link]({a['docs_url']})" if a.get("docs_url") else ""
            lines.append(
                "| {name} | {provider} | {desc} | {auth} | {pricing} | {signup} | {fmt} | {doc} |".format(
                    name=esc(a["name"]),
                    provider=esc(a["provider"]),
                    desc=esc(a["description"]),
                    auth=esc(a["auth"]),
                    pricing=esc(a["pricing"]),
                    signup=signup,
                    fmt=esc(a.get("format", "")),
                    doc=doc_link,
                )
            )
        lines.append("")

    # 한계
    lines.append("## 한계 및 주의")
    lines.append("")
    for lim in meta.get("limitations", []):
        lines.append(f"- {lim}")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({len(apis)} apis, {len(cats)} categories)")


if __name__ == "__main__":
    main()
