#!/usr/bin/env python3
"""data.go.kr 목록조회서비스(15077093)로 포털의 전체 목록을 enumerate 한다.

GOAL.md의 'A. 전수형'에 도달하기 위한 스크립트. 배경은 docs/ENUMERATION.md 참고.

이 서비스는 odcloud(api.odcloud.kr) 호스팅이며, OAS 문서에서 확인한 리소스 경로:
    /15077093/v1/open-data-list      오픈 API 목록      (약 1.7만 건)
    /15077093/v1/file-data-list      파일데이터 목록     (약 20만 건)
    /15077093/v1/standard-data-list  표준데이터 목록     (약 1.3만 건)
    /15077093/v1/dataset             통합 데이터셋

사용법:
    export DATAGO_SERVICE_KEY='발급받은_Decoding_serviceKey'
    python3 scripts/fetch_datago.py --resource open-data-list --out data/datago_raw.json
"""
import argparse
import json
import os
import sys
import time
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

BASE = "https://api.odcloud.kr/api/15077093/v1"
VALID_RESOURCES = ("open-data-list", "file-data-list", "standard-data-list", "dataset")


def fetch_page(service_key: str, resource: str, page: int, per_page: int) -> dict:
    params = {"serviceKey": service_key, "page": page, "perPage": per_page}
    url = f"{BASE}/{resource}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "korea-open-api-catalog/1.0"})
    with urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    return json.loads(body)


def main() -> int:
    ap = argparse.ArgumentParser(description="data.go.kr 목록 전수 수집 (odcloud 15077093)")
    ap.add_argument("--resource", default="open-data-list", choices=VALID_RESOURCES,
                    help="수집 대상 리소스 (기본: open-data-list = 오픈 API 목록)")
    ap.add_argument("--per-page", type=int, default=1000, help="페이지당 건수")
    ap.add_argument("--max-pages", type=int, default=100000, help="안전 상한")
    ap.add_argument("--sleep", type=float, default=0.15, help="요청 간 대기(초)")
    ap.add_argument("--out", default="data/datago_raw.json", help="출력 파일")
    args = ap.parse_args()

    key = os.environ.get("DATAGO_SERVICE_KEY")
    if not key:
        print("ERROR: 환경변수 DATAGO_SERVICE_KEY 가 필요합니다. docs/ENUMERATION.md 참고.", file=sys.stderr)
        return 2

    all_items: list = []
    total = None
    for page in range(1, args.max_pages + 1):
        try:
            payload = fetch_page(key, args.resource, page, args.per_page)
        except HTTPError as e:
            print(f"[page {page}] HTTP {e.code}: {e.read()[:200]!r}", file=sys.stderr)
            return 1
        except (URLError, json.JSONDecodeError) as e:
            print(f"[page {page}] 요청/파싱 실패: {e}", file=sys.stderr)
            return 1

        if total is None:
            total = payload.get("totalCount")
            print(f"totalCount = {total}")
        items = payload.get("data") or []
        if not items:
            break
        all_items.extend(items)
        print(f"[page {page}] +{len(items)} (누적 {len(all_items)} / {total})")
        if total is not None and len(all_items) >= total:
            break
        if len(items) < args.per_page:
            break
        time.sleep(args.sleep)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    print(f"완료: {len(all_items)}건 → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
