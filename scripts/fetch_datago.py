#!/usr/bin/env python3
"""data.go.kr 목록조회서비스(15077093)로 전체 오픈API 목록을 enumerate 한다.

GOAL.md의 '전수'에 도달하기 위한 스크립트. 자세한 배경은 docs/ENUMERATION.md 참고.

사용법:
    export DATAGO_SERVICE_KEY='발급받은_Decoding_serviceKey'
    python3 scripts/fetch_datago.py --type API --out data/datago_raw.json

주의:
- 본 실행 환경에서는 data.go.kr 웹(www)이 차단되어 사전 검증을 못 했다.
  단, apis.data.go.kr 은 차단이 아니므로(키/파라미터 없는 요청에 HTTP 500 응답) 키가 있으면 동작 가능.
- 아래 CONFIG 의 ENDPOINT / 파라미터명은 키 발급 시 받는 '활용가이드' 기준으로 1~2줄만 맞추면 된다.
  (operation 경로·파라미터명은 서비스마다 미세하게 다를 수 있다.)
"""
import argparse
import json
import os
import sys
import time
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

# --- CONFIG: 활용가이드로 확정해야 하는 부분 (docs/ENUMERATION.md 참고) ---
# 공공데이터활용지원센터_목록조회서비스 (data.go.kr dataset 15077093)
ENDPOINT = "https://apis.data.go.kr/15077093/getDataList"  # TODO: 가이드의 정확한 operation 경로로 확정
PARAM_PAGE = "pageNo"        # 페이지 번호 파라미터명
PARAM_ROWS = "numOfRows"     # 페이지당 건수 파라미터명
PARAM_TYPE = "type"          # 응답 포맷 (json/xml) — 서비스에 따라 _type / dataType 일 수 있음
# ----------------------------------------------------------------------


def fetch_page(service_key: str, page: int, rows: int) -> dict:
    params = {
        "serviceKey": service_key,
        PARAM_PAGE: page,
        PARAM_ROWS: rows,
        PARAM_TYPE: "json",
    }
    url = f"{ENDPOINT}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "korea-open-api-catalog/1.0"})
    with urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    return json.loads(body)


def extract_items(payload: dict) -> list:
    """응답 구조에서 목록 배열을 최대한 견고하게 추출한다.

    data.go.kr 응답은 보통 response.body.items[...] 또는 {data:[...]} 형태.
    구조가 다르면 가이드에 맞춰 이 함수만 수정하면 된다.
    """
    if not isinstance(payload, dict):
        return []
    # 흔한 패턴들 시도
    body = payload.get("response", {}).get("body", payload)
    if isinstance(body, dict):
        items = body.get("items") or body.get("data") or body.get("list")
        if isinstance(items, dict):  # {item: [...]}
            items = items.get("item")
        if isinstance(items, list):
            return items
    if isinstance(payload.get("data"), list):
        return payload["data"]
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description="data.go.kr 오픈API 목록 전수 수집")
    ap.add_argument("--type", default="API", help="수집 대상 유형(API 등) — 가이드 파라미터로 매핑")
    ap.add_argument("--rows", type=int, default=100, help="페이지당 건수")
    ap.add_argument("--max-pages", type=int, default=10000, help="안전 상한")
    ap.add_argument("--sleep", type=float, default=0.2, help="요청 간 대기(초)")
    ap.add_argument("--out", default="data/datago_raw.json", help="출력 파일")
    args = ap.parse_args()

    key = os.environ.get("DATAGO_SERVICE_KEY")
    if not key:
        print("ERROR: 환경변수 DATAGO_SERVICE_KEY 가 필요합니다. docs/ENUMERATION.md 참고.", file=sys.stderr)
        return 2

    all_items: list = []
    for page in range(1, args.max_pages + 1):
        try:
            payload = fetch_page(key, page, args.rows)
        except HTTPError as e:
            print(f"[page {page}] HTTP {e.code} — ENDPOINT/파라미터를 활용가이드로 확인하세요.", file=sys.stderr)
            return 1
        except (URLError, json.JSONDecodeError) as e:
            print(f"[page {page}] 요청/파싱 실패: {e}", file=sys.stderr)
            return 1

        items = extract_items(payload)
        if not items:
            break
        all_items.extend(items)
        print(f"[page {page}] +{len(items)} (누적 {len(all_items)})")
        if len(items) < args.rows:
            break
        time.sleep(args.sleep)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    print(f"완료: {len(all_items)}건 → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
