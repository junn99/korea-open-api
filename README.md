# Korea Free Open API Catalog

한국에서 제공되는 무료 오픈 API 카탈로그. GOAL.md 기준(무료 한정, 회원가입/승인 허용, 전 분야 포괄)에 따라 수집.

> 자동 생성 파일입니다. 원본은 `data/korea-open-apis.json` 이며 `python3 scripts/build_readme.py` 로 재생성합니다. 직접 수정하지 마세요.

- 생성일: **2026-05-28** · 버전: **0.1.0**
- 총 API 수: **44** · 분야 수: **17**
- 요금: free **40** / free-tier **4** · 회원가입·승인 필요: **44**

## 분야별 분포

| 분야 | 개수 |
|------|------|
| 지도·위치 | 5 |
| 공공·행정 | 4 |
| 금융 | 4 |
| 검색 | 3 |
| 교육·학술 | 3 |
| 교통 | 3 |
| 날씨·환경 | 3 |
| 문화·관광·체육 | 3 |
| 인공지능 | 3 |
| 콘텐츠·미디어 | 3 |
| 법령·사법 | 2 |
| 보건·식품 | 2 |
| 생활·소셜 | 2 |
| 과학·통계 | 1 |
| 부동산 | 1 |
| 쇼핑 | 1 |
| 채용·고용 | 1 |

## 분야별 API 목록

### 지도·위치

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| SGIS 통계지리정보서비스 | 통계청 | 통계 기반 지리정보(인구·사업체·경계 등) 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://sgis.kostat.go.kr/developer/) |
| VWorld(브이월드) 오픈 API | 국토교통부 / 국토지리정보원 | 2D/3D 지도, 배경지도, 공간정보(WMS/WFS), 지오코더 등 공간정보 오픈 API. | API Key | free | 필요 | REST/OGC(JSON/XML) | [link](https://www.vworld.kr/dev/v4api.do) |
| 카카오맵 / 로컬 API | 카카오 | 지도 표시, 장소 검색, 주소-좌표 변환(지오코딩) 등. | API Key(REST/JavaScript) | free | 필요 | REST(JSON) | [link](https://developers.kakao.com/docs/latest/ko/local/dev-guide) |
| 네이버 지도(Maps) API | 네이버클라우드플랫폼(NCP) | 지도, 길찾기(Directions), 지오코딩 등. | API Key(Client ID/Secret) | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/applicationService/maps) |
| 도로명주소 API | 행정안전부 | 도로명주소 검색, 영문주소, 좌표제공 등 주소 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://business.juso.go.kr/addrlink/openApi/apiExprn.do) |

### 공공·행정

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 공공데이터포털 (Public Data Portal) | 행정안전부 / 한국지능정보사회진흥원(NIA) | 국가 공공데이터를 데이터셋·오픈API로 개방하는 중앙 플랫폼. 수만 건의 오픈API 보유. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |
| 공공데이터포털 목록조회서비스 | 공공데이터활용지원센터 | 공공데이터포털에 등록된 데이터/오픈API 목록을 조회하는 메타 API. 전수 수집의 진입점. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15077093/openapi.do) |
| 정부24 OpenAPI | 행정안전부 | 정부 민원·공공서비스 관련 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.gov.kr/openapi) |
| 서울 열린데이터광장 | 서울특별시 | 서울시 행정·교통·환경·생활 등 데이터를 오픈API로 제공하는 지자체 포털. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.seoul.go.kr) |

### 금융

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 한국은행 경제통계시스템(ECOS) Open API | 한국은행 | 금리·환율·국민계정 등 경제통계 조회 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://ecos.bok.or.kr/api/) |
| 오픈뱅킹 공동업무 API | 금융결제원(KFTC) | 계좌조회·이체 등 은행 공동 오픈뱅킹 API. | OAuth 2.0 | free | 필요 | REST(JSON) | [link](https://openapi.kftc.or.kr/) |
| OpenDART 전자공시 API | 금융감독원 | 상장·외부감사 기업의 전자공시(사업보고서, 재무제표 등) 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://opendart.fss.or.kr/) |
| 한국수출입은행 환율 Open API | 한국수출입은행 | 현재/대출 환율 등 환율정보 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://www.koreaexim.go.kr) |

### 검색

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 네이버 검색 API | 네이버 | 뉴스·블로그·책·백과사전·이미지·웹·쇼핑·지역 등 통합검색 오픈 API. | API Key(Client ID/Secret) | free | 필요 | REST(JSON/XML) | [link](https://developers.naver.com/docs/serviceapi/search/news/news.md) |
| 네이버 데이터랩(DataLab) API | 네이버 | 검색어 트렌드, 쇼핑인사이트 등 트렌드 데이터 오픈 API. | API Key(Client ID/Secret) | free | 필요 | REST(JSON) | [link](https://developers.naver.com/docs/serviceapi/datalab/search/search.md) |
| 카카오 검색(다음) API | 카카오 | 웹/동영상/이미지/블로그/책/카페 등 다음 검색 오픈 API. | API Key(REST) | free | 필요 | REST(JSON) | [link](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide) |

### 교육·학술

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 도서관 정보나루 Open API | 문화체육관광부 / 국립중앙도서관 | 전국 도서관 대출·소장·인기도서 등 도서관 빅데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data4library.kr/apiUtilization) |
| NEIS 교육정보 개방 포털 Open API | 한국교육학술정보원(KERIS) | 전국 학교 기본정보, 급식, 시간표, 학사일정 등 교육 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://open.neis.go.kr/) |
| 국립중앙도서관 Open API | 국립중앙도서관 | 서지정보 검색, LOD, 전거데이터 등 도서/서지 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.nl.go.kr) |

### 교통

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| TMAP API | SK텔레콤 | 경로안내, 대중교통, 보행자 길찾기, POI 검색 등. | API Key(App Key) | free-tier | 필요 | REST(JSON) | [link](https://tmapapi.sktelecom.com/) |
| 국가대중교통정보(TAGO) | 국토교통부 | 전국 버스 도착정보, 노선, 정류소, 지하철 등 대중교통 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |
| 서울 버스정보 Open API | 서울특별시 / 서울교통정보과(TOPIS) | 서울 버스 도착정보, 노선/정류소 정보. | API Key | free | 필요 | REST(XML/JSON) | [link](http://api.bus.go.kr/) |

### 날씨·환경

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 기상청 API 허브 | 기상청 | 단기/중기예보, 실황, 지상/해양 관측 등 기상 데이터 오픈 API 통합 허브. | API Key | free | 필요 | REST(JSON/XML/텍스트) | [link](https://apihub.kma.go.kr) |
| 에어코리아 대기오염정보 API | 한국환경공단 | 미세먼지·대기질 실시간 측정정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15073861/openapi.do) |
| 한국환경공단 전기차 충전소 정보 API | 한국환경공단 | 전국 전기차 충전소 위치·상태 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |

### 문화·관광·체육

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 한국관광공사 TourAPI | 한국관광공사 | 관광지·숙박·축제·문화시설·여행코스·이미지 등 관광 콘텐츠 오픈 API(15종, 약 26만 건). | API Key | free | 필요 | REST(JSON/XML) | [link](https://api.visitkorea.or.kr/) |
| 공연예술통합전산망(KOPIS) Open API | 예술경영지원센터 | 공연 목록·상세·예매상황 등 공연예술 통계/정보 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.kopis.or.kr/por/cs/openapi/openApiList.do) |
| 문화공공데이터광장(문화포털) Open API | 한국문화정보원 | 문화·예술·관광·도서 등 문화 분야 공공데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.culture.go.kr/data/) |

### 인공지능

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| ETRI 공공 인공지능 Open API | 한국전자통신연구원(ETRI) | 한국어 형태소분석, 질의응답, 음성인식, OCR 등 AI 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://aiopen.etri.re.kr/) |
| 네이버 CLOVA AI API | 네이버클라우드플랫폼(NCP) | CLOVA OCR, Speech(STT/TTS), Face, CLOVA Studio(생성형) 등. | API Key | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/aiService) |
| 네이버 Papago 번역 API | 네이버클라우드플랫폼(NCP) | 기계 번역(Papago) 및 언어감지 API. | API Key | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/aiService/papagoTranslation) |

### 콘텐츠·미디어

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KOBIS 영화관입장권통합전산망 Open API | 영화진흥위원회(KOFIC) | 일별/주간 박스오피스, 영화/영화인/영화사 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do) |
| KMDb 한국영화데이터베이스 Open API | 한국영상자료원 | 영화 상세정보(스태프/줄거리/스틸 등) 검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kmdb.or.kr/info/api/apiList) |
| 알라딘 상품 검색 Open API | 알라딘(Aladin) | 도서 상품 검색/조회/베스트셀러 등 도서 정보 오픈 API. | API Key(TTBKey) | free | 필요 | REST(JSON/XML) | [link](https://www.aladin.co.kr/ttb/apiguide.aspx) |

### 법령·사법

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 국가법령정보 공동활용 API | 법제처 | 법령·행정규칙·자치법규·판례·헌재결정례 등 법령정보 오픈 API. | API Key(이메일 ID 기반) | free | 필요 | REST(XML/JSON/HTML) | [link](https://open.law.go.kr/LSO/openApi/guideList.do) |
| 열린국회정보 Open API | 국회사무처 | 의안, 의원, 표결, 회의록 등 국회 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://open.assembly.go.kr/portal/openapi/main.do) |

### 보건·식품

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 식품안전나라 Open API | 식품의약품안전처 | 식품·의약품·건강기능식품 정보, 회수/판매중지 등 식의약 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.foodsafetykorea.go.kr/api/) |
| 건강보험심사평가원(HIRA) 공공 API | 건강보험심사평가원 | 병원·약국 정보, 의약품, 비급여 진료비 등 보건의료 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |

### 생활·소셜

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 카카오톡 메시지/소셜 API | 카카오 | 카카오 로그인, 메시지 전송, 카카오톡 채널, 프로필 등. | OAuth 2.0 | free | 필요 | REST(JSON) | [link](https://developers.kakao.com/docs/latest/ko/kakaologin/common) |
| 네이버 로그인 / 회원 API | 네이버 | 네이버 아이디 로그인(OAuth) 및 회원 프로필 조회. | OAuth 2.0 | free | 필요 | REST(JSON) | [link](https://developers.naver.com/docs/login/api/api.md) |

### 과학·통계

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KOSIS 국가통계포털 공유서비스 | 통계청 | 국가통계 자료를 조회하는 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://kosis.kr/openapi/) |

### 부동산

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 국토교통부 실거래가 공개시스템 API | 국토교통부 | 아파트/연립/단독 등 부동산 매매·전월세 실거래가 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.data.go.kr) |

### 쇼핑

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 네이버 쇼핑 검색 API | 네이버 | 쇼핑 상품 검색(네이버 검색 API의 쇼핑 분야). | API Key(Client ID/Secret) | free | 필요 | REST(JSON/XML) | [link](https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md) |

### 채용·고용

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 고용24 / 고용노동부 일자리 API | 고용노동부 / 한국고용정보원 | 채용공고, 직업정보, 고용통계 등 일자리 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |

## 한계 및 주의

- data.go.kr 전체(수만 건) 자동 전수 수집은 IP 차단으로 미수행 — 대표 API 위주 큐레이션.
- 민간 무료 API는 '전수'가 아니라 '대표 큐레이션'.
- 시점 스냅샷(2026-05) — 신규 추가/폐기로 시간이 지나면 낡음.
- 일부 docs_url은 포털 루트만 확보 — 정확한 딥링크는 note에 표기하거나 '(미확인)'.
