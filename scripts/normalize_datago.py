#!/usr/bin/env python3
"""data/datago_raw.json(목록조회 전수 결과)을 카탈로그 스키마로 정규화한다.

- 입력 행은 operation 단위라 같은 서비스(list_id)가 여러 번 등장한다.
- 서비스(list_id) 단위로 묶어 1건의 오픈 API로 만든다.
- GOAL.md 기준: 순수 유료(무료 구간 없음)는 제외한다.

출력: data/datago_apis.json  (meta + apis[])
"""
import json
from collections import defaultdict, Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "datago_raw.json"
OUT = ROOT / "data" / "datago_apis.json"


def clean(s):
    return (s or "").replace("​", "").replace("﻿", "").strip()


def main() -> None:
    rows = json.loads(RAW.read_text(encoding="utf-8"))

    groups = defaultdict(list)
    for r in rows:
        groups[r.get("list_id")].append(r)

    apis = []
    skipped_paid = 0
    for list_id, items in groups.items():
        rep = items[0]
        is_charged = clean(rep.get("is_charged"))
        if is_charged == "유료":  # 무료 구간이 없는 순수 유료만 제외
            skipped_paid += 1
            continue
        api_type = clean(rep.get("api_type")) or "REST"
        data_format = clean(rep.get("data_format"))
        fmt = "/".join(x for x in (api_type, data_format) if x)
        # 최신 갱신일(해당 서비스 operation 중 최댓값)
        updated = max((clean(x.get("updated_at")) for x in items), default="")
        created = min((clean(x.get("created_at")) for x in items if x.get("created_at")), default="")

        apis.append({
            "name": clean(rep.get("list_title")) or clean(rep.get("title")),
            "provider": clean(rep.get("org_nm")),
            "category": clean(rep.get("new_category_nm")) or clean(rep.get("category_nm")),
            "description": clean(rep.get("desc")),
            "docs_url": f"https://www.data.go.kr/data/{list_id}/openapi.do",
            "auth": "없음" if api_type == "LINK" else "API Key",
            "pricing": "free",
            "signup_required": True,
            "format": fmt,
            "rate_limit": "(미확인)",
            "source": "data.go.kr 목록조회API(15077093) open-data-list",
            "note": f"list_id={list_id}; operations={len(items)}; "
                    f"created={created}; updated={updated}"
                    + ("; 형태=링크(LINK)" if api_type == "LINK" else ""),
        })

    apis.sort(key=lambda a: (a["category"], a["provider"], a["name"]))

    cats = Counter(a["category"] for a in apis)
    doc = {
        "meta": {
            "title": "data.go.kr 오픈 API 전수 목록",
            "description": "공공데이터포털 목록조회 API(15077093, open-data-list)로 수집한 "
                           "오픈 API 전수. 서비스(list_id) 단위로 정규화.",
            "generated": date.today().isoformat(),
            "source_total_rows": len(rows),
            "service_count": len(apis),
            "skipped_paid": skipped_paid,
            "categories": dict(sorted(cats.items(), key=lambda x: (-x[1], x[0]))),
            "note": "rows는 operation 단위라 서비스 수보다 많다. 전부 is_deleted=N(활성).",
        },
        "apis": apis,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {OUT}: {len(apis)} services (raw rows {len(rows)}, skipped 유료 {skipped_paid})")
    print("categories:", doc["meta"]["categories"])


if __name__ == "__main__":
    main()
