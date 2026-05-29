# Korea Free Open API Catalog

한국에서 제공되는 무료 오픈 API 카탈로그. GOAL.md 기준(무료 한정, 회원가입/승인 허용, 전 분야 포괄)에 따라 수집.

![APIs](https://img.shields.io/badge/큐레이션_API-240-blue) ![Categories](https://img.shields.io/badge/분야-37-green) ![data.go.kr](https://img.shields.io/badge/data.go.kr_전수-12%2C073-orange)

> 이 파일은 자동 생성됩니다. 원본 데이터는 [`data/korea-open-apis.json`](data/korea-open-apis.json) 이며 `python3 scripts/build_readme.py` 로 재생성합니다. **README를 직접 수정하지 마세요.**

- 최종 갱신: **2026-05-29** · 버전: **0.15.0**
- 큐레이션 API: **240** · 분야: **37** · 요금: free **212** / free-tier **28** · 회원가입·승인 필요: **235**
- 이와 별개로 공공데이터포털(data.go.kr) 오픈 API **전수 12,073건**을 [`data/datago_apis.json`](data/datago_apis.json) 으로 제공합니다 ([부록 A](#부록-a-datagokr-오픈-api-전수)).

## 목차

- [분야별 분포](#분야별-분포)
- **분야별 API 목록**
  - [🏛 공공·행정](#공공행정) (22)
  - [🚍 교통](#교통) (19)
  - [🎭 문화·관광·체육](#문화관광체육) (19)
  - [💵 금융](#금융) (18)
  - [🎓 교육·학술](#교육학술) (15)
  - [☀️ 날씨·환경](#날씨환경) (14)
  - [💬 생활·소셜](#생활소셜) (13)
  - [🌾 농축수산](#농축수산) (10)
  - [🏥 보건·식품](#보건식품) (10)
  - [📺 콘텐츠·미디어](#콘텐츠미디어) (10)
  - [🚨 재난·안전](#재난안전) (9)
  - [🗺 지도·위치](#지도위치) (8)
  - [🏘 부동산](#부동산) (6)
  - [💳 결제·핀테크](#결제핀테크) (5)
  - [🏪 상권·창업](#상권창업) (5)
  - [⚡ 에너지](#에너지) (5)
  - [🤖 인공지능](#인공지능) (5)
  - [💼 채용·고용](#채용고용) (5)
  - [📨 커뮤니케이션](#커뮤니케이션) (5)
  - [🔬 과학기술·특허](#과학기술특허) (4)
  - [📦 물류·배송](#물류배송) (4)
  - [🔎 검색](#검색) (3)
  - [🎮 게임](#게임) (3)
  - [🔗 블록체인·암호화폐](#블록체인암호화폐) (3)
  - [📖 언어·사전](#언어사전) (3)
  - [🏠 IoT·스마트홈](#iot스마트홈) (2)
  - [🚢 무역·통상](#무역통상) (2)
  - [• 미디어·콘텐츠](#미디어콘텐츠) (2)
  - [⚖️ 법령·사법](#법령사법) (2)
  - [📡 통신·인터넷](#통신인터넷) (2)
  - [• 검색·생활](#검색생활) (1)
  - [📊 과학·통계](#과학통계) (1)
  - [• 기타](#기타) (1)
  - [🏭 산업·고용](#산업고용) (1)
  - [🛍 쇼핑](#쇼핑) (1)
  - [☁️ 클라우드](#클라우드) (1)
  - [• 통신](#통신) (1)
- [부록 A: data.go.kr 오픈 API 전수](#부록-a-datagokr-오픈-api-전수)
- [한계 및 주의](#한계-및-주의)

## 분야별 분포

| 분야 | 개수 |
|------|------:|
| 🏛 [공공·행정](#공공행정) | 22 |
| 🚍 [교통](#교통) | 19 |
| 🎭 [문화·관광·체육](#문화관광체육) | 19 |
| 💵 [금융](#금융) | 18 |
| 🎓 [교육·학술](#교육학술) | 15 |
| ☀️ [날씨·환경](#날씨환경) | 14 |
| 💬 [생활·소셜](#생활소셜) | 13 |
| 🌾 [농축수산](#농축수산) | 10 |
| 🏥 [보건·식품](#보건식품) | 10 |
| 📺 [콘텐츠·미디어](#콘텐츠미디어) | 10 |
| 🚨 [재난·안전](#재난안전) | 9 |
| 🗺 [지도·위치](#지도위치) | 8 |
| 🏘 [부동산](#부동산) | 6 |
| 💳 [결제·핀테크](#결제핀테크) | 5 |
| 🏪 [상권·창업](#상권창업) | 5 |
| ⚡ [에너지](#에너지) | 5 |
| 🤖 [인공지능](#인공지능) | 5 |
| 💼 [채용·고용](#채용고용) | 5 |
| 📨 [커뮤니케이션](#커뮤니케이션) | 5 |
| 🔬 [과학기술·특허](#과학기술특허) | 4 |
| 📦 [물류·배송](#물류배송) | 4 |
| 🔎 [검색](#검색) | 3 |
| 🎮 [게임](#게임) | 3 |
| 🔗 [블록체인·암호화폐](#블록체인암호화폐) | 3 |
| 📖 [언어·사전](#언어사전) | 3 |
| 🏠 [IoT·스마트홈](#iot스마트홈) | 2 |
| 🚢 [무역·통상](#무역통상) | 2 |
| • [미디어·콘텐츠](#미디어콘텐츠) | 2 |
| ⚖️ [법령·사법](#법령사법) | 2 |
| 📡 [통신·인터넷](#통신인터넷) | 2 |
| • [검색·생활](#검색생활) | 1 |
| 📊 [과학·통계](#과학통계) | 1 |
| • [기타](#기타) | 1 |
| 🏭 [산업·고용](#산업고용) | 1 |
| 🛍 [쇼핑](#쇼핑) | 1 |
| ☁️ [클라우드](#클라우드) | 1 |
| • [통신](#통신) | 1 |
| **합계** | **240** |

## 분야별 API 목록

### 공공·행정

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [공공데이터포털 (Public Data Portal)](https://www.data.go.kr) | 행정안전부 / 한국지능정보사회진흥원(NIA) | 국가 공공데이터를 데이터셋·오픈API로 개방하는 중앙 플랫폼. 수만 건의 오픈API 보유. | API Key | free | ✅ |
| [공공데이터포털 목록조회서비스](https://www.data.go.kr/data/15077093/openapi.do) | 공공데이터활용지원센터 | 공공데이터포털에 등록된 데이터/오픈API 목록을 조회하는 메타 API. 전수 수집의 진입점. | API Key | free | ✅ |
| [정부24 OpenAPI](https://www.gov.kr/openapi) | 행정안전부 | 정부 민원·공공서비스 관련 오픈 API. | API Key | free | ✅ |
| [서울 열린데이터광장](https://data.seoul.go.kr) | 서울특별시 | 서울시 행정·교통·환경·생활 등 데이터를 오픈API로 제공하는 지자체 포털. | API Key | free | ✅ |
| [국세청 사업자등록정보 진위확인·상태조회 API](https://www.data.go.kr/data/15081808/openapi.do) | 국세청 | 사업자등록번호 진위확인 및 휴·폐업 상태조회 오픈 API. | API Key | free | ✅ |
| [경기데이터드림 Open API](https://data.gg.go.kr/portal/intro/develop/searchBulletinPage.do) | 경기도 | 경기도 보유 공공데이터 오픈 API 포털(지자체). | API Key | free | ✅ |
| [조달청 나라장터 입찰공고·낙찰 정보 API](https://www.data.go.kr/data/15129394/openapi.do) | 조달청 | 입찰공고, 낙찰정보, 계약현황, 발주계획 등 공공조달 오픈 API. | API Key | free | ✅ |
| [중앙선거관리위원회 선거정보 API](https://www.data.go.kr/data/15000900/openapi.do) | 중앙선거관리위원회 | 투·개표 결과, 당선인, 사전투표, 선거코드 등 선거 오픈 API. | API Key | free | ✅ |
| [병무청 오픈 API](https://open.mma.go.kr/caisGGGS/ggda/openApiList.do?menu_id=mma0000037) | 병무청 | 병무행정(병역판정, 사회복무, 입영 등) 관련 오픈 API. | API Key | free | ✅ |
| [통일부 북한정보포털 통합검색 API](https://www.data.go.kr/data/15079225/openapi.do) | 통일부 | 북한 정치·경제·군사·사회·교육문화 등 북한정보 통합검색 오픈 API. | API Key | free | ✅ |
| [행정표준코드 법정동코드 API](https://www.data.go.kr/data/15077871/openapi.do) | 행정안전부 | 법정동코드·행정표준코드 조회 오픈 API. 주소/지역 기반 서비스의 기초 코드. | API Key | free | ✅ |
| [지방재정365 재정정보 API](https://www.data.go.kr/data/15058102/openapi.do) | 행정안전부 | 지방자치단체 재정자립도·세입세출 등 지방재정 통합공개 오픈 API. | API Key | free | ✅ |
| [행정안전부 주민등록 인구·세대현황 API](https://www.data.go.kr/data/15108065/openapi.do) | 행정안전부 | 행정동/법정동/도로명별 주민등록 인구·세대수·연령·남녀 통계 오픈 API. | API Key | free | ✅ |
| [국가보훈부 현충시설·독립유공자 Open API](https://www.mpva.go.kr/mpva/contents.do?key=17) | 국가보훈부 | 현충시설, 국외사적지, 독립유공자 공훈록 등 보훈 정보 오픈 API. | API Key | free | ✅ |
| [국민연금공단 가입 사업장 내역 API](https://www.data.go.kr/data/3046071/openapi.do) | 국민연금공단 | 국민연금 가입 사업장 정보·기간별 현황 등 연금 오픈 API. | API Key | free | ✅ |
| [ALIO 공공기관 경영정보 Open API](https://opendata.alio.go.kr/public_inst/list) | 기획재정부(공공기관 경영정보 공개시스템) | 공공기관 임직원·재무·복리후생 등 경영정보(알리오) 오픈 API. | API Key | free | ✅ |
| [제주데이터허브 Open API](https://www.jejudatahub.net/) | 제주특별자치도 | 제주 지역 관광·교통·환경·생활 등 데이터를 제공하는 지자체 데이터 포털. | API Key | free | ✅ |
| [비즈노 API](https://bizno.net/openapi) | 비즈노 | 사업자등록번호·상호로 사업자정보 조회 | API Key | free-tier | ✅ |
| [전국공중화장실 표준데이터 Open API](https://www.data.go.kr/data/15012892/standard.do) | 행정안전부 | 전국 공중화장실 위치(좌표)·남녀/장애인/어린이 칸 수·개방시간·비상벨 등 표준 항목. | API Key(serviceKey) | free | ✅ |
| [전국공공시설개방정보 표준데이터 Open API](https://www.data.go.kr/data/15013117/standard.do) | 행정안전부 | 주민센터·체육관 등 공공시설 개방(대관) 정보 표준 항목(시설명·주소·개방시간·예약). | API Key(serviceKey) | free | ✅ |
| [e하늘 장사정보(장사시설) 시스템](https://www.ehaneul.go.kr/) | 보건복지부 / 한국장례문화진흥원 | 전국 화장시설·봉안당·자연장지 등 장사시설 현황 및 화장로 예약 정보. | API Key(serviceKey) | free | ✅ |
| [경찰청 습득물(유실물) 정보 조회 API](https://www.data.go.kr/data/15058696/openapi.do) | 경찰청 | 전국 습득물·유실물 보관 정보 조회(lost112 연계). | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 교통

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [TMAP API](https://tmapapi.sktelecom.com/) | SK텔레콤 | 경로안내, 대중교통, 보행자 길찾기, POI 검색 등. | API Key(App Key) | free-tier | ✅ |
| [국가대중교통정보(TAGO)](https://www.data.go.kr/data/15098534/openapi.do) | 국토교통부 | 전국 버스 도착정보, 노선, 정류소, 지하철 등 대중교통 오픈 API. | API Key | free | ✅ |
| [서울 버스정보 Open API](http://api.bus.go.kr/) | 서울특별시 / 서울교통정보과(TOPIS) | 서울 버스 도착정보, 노선/정류소 정보. | API Key | free | ✅ |
| [ITS 국가교통정보센터 오픈데이터](https://www.its.go.kr/opendata/) | 국토교통부 ITS | 실시간 소통정보, 돌발정보, CCTV 등 도로교통 오픈 API. | API Key | free | ✅ |
| [한국교통안전공단 자동차종합정보 API](https://www.data.go.kr/data/15059401/openapi.do) | 한국교통안전공단(TS) | 자동차 신규등록·검사 등 자동차 통계/정보 오픈 API. | API Key | free | ✅ |
| [고속도로 공공데이터 포털 Open API](https://data.ex.co.kr/openapi/intro/introduce01) | 한국도로공사 | 실시간 고속도로 교통량·소통·휴게소·통행료 등 오픈 API. | API Key | free | ✅ |
| [레일포털(철도산업정보센터) Open API](https://data.kric.go.kr/rips/serviceInfo/openapi/introduce.do) | 국토교통부 / 한국철도기술연구원(KRIC) | 철도 노선·역사·운행 등 철도산업 정보 오픈 API. | API Key | free | ✅ |
| [한국공항공사 항공기 운항정보 API](https://www.data.go.kr/data/15000126/openapi.do) | 한국공항공사(KAC) | 국내/국제선 운항 스케줄, 실시간 운항정보, 공항코드 등 항공 오픈 API. | API Key | free | ✅ |
| [인천국제공항 Open API](http://openapi.airport.kr/) | 인천국제공항공사 | 인천공항 출도착 운항현황, 주차장, 혼잡도 등 오픈 API. | API Key | free | ✅ |
| [해양수산부 선박운항정보(PORT-MIS) API](https://www.data.go.kr/data/15006353/openapi.do) | 해양수산부 | 선박 입출항 시간, 선박 제원, 항만 관제 등 해운항만 오픈 API. | API Key | free | ✅ |
| [서울 따릉이 공공자전거 실시간 대여정보 API](https://data.seoul.go.kr/dataList/OA-15493/A/1/datasetView.do) | 서울특별시 | 대여소별 실시간 거치 자전거 수, 거치율, 대여소 위치 등 오픈 API. | API Key | free | ✅ |
| [도로교통공단 TAAS 교통사고분석 Open API](https://opendata.koroad.or.kr/) | 한국도로교통공단(KOROAD) | 교통사고 다발지(13종), 교통안전정보(3종) 등 교통사고 오픈 API. | API Key | free | ✅ |
| [서울 지하철 실시간 도착정보 API](https://www.data.go.kr/data/15058052/openapi.do) | 서울특별시(TOPIS) | 서울 전체 역의 실시간 지하철 도착·열차위치 정보 오픈 API. | API Key | free | ✅ |
| [한국철도공사(코레일) 열차운행정보 API](https://www.data.go.kr/data/15125762/openapi.do) | 한국철도공사 | 여객열차 운행계획·운행정보 등 KTX·일반열차 오픈 API. | API Key | free | ✅ |
| [부산교통공사 부산도시철도 운행정보 API](https://www.data.go.kr/data/15001019/openapi.do) | 부산교통공사 | 부산 도시철도 운행정보·시각표 등 지방 도시철도 오픈 API. | API Key | free | ✅ |
| [ODsay 대중교통 API](https://lab.odsay.com/guide/guide) | ODsay | 전국 대중교통·고속버스·항공 통합 길찾기 | API Key | free-tier | ✅ |
| [카카오모빌리티 API](https://developers.kakaomobility.com/product/api) | 카카오모빌리티 | 길찾기 등 모빌리티 개발 API | API Key | free-tier | ✅ |
| [현대자동차 Developers](https://developers.hyundai.com/) | 현대자동차 | 차량 제원·운행·주행거리·운전습관 | OAuth | free | ✅ |
| [기아 Developers](https://developers.kia.com/) | 기아 | KIA Connect 차량 데이터 | OAuth | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 문화·관광·체육

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [한국관광공사 TourAPI](https://api.visitkorea.or.kr/) | 한국관광공사 | 관광지·숙박·축제·문화시설·여행코스·이미지 등 관광 콘텐츠 오픈 API(15종, 약 26만 건). | API Key | free | ✅ |
| [공연예술통합전산망(KOPIS) Open API](https://www.kopis.or.kr/por/cs/openapi/openApiList.do) | 예술경영지원센터 | 공연 목록·상세·예매상황 등 공연예술 통계/정보 오픈 API. | API Key | free | ✅ |
| [문화공공데이터광장(문화포털) Open API](https://www.culture.go.kr/data/) | 한국문화정보원 | 문화·예술·관광·도서 등 문화 분야 공공데이터 오픈 API. | API Key | free | ✅ |
| [고캠핑(GoCamping) 캠핑장 정보 API](https://www.data.go.kr/data/15101933/openapi.do) | 한국관광공사 | 전국 등록 야영장(캠핑장) 위치·시설·안전정보 등 오픈 API. | API Key | free | ✅ |
| [해양수산부 해수욕장정보 서비스 API](https://www.data.go.kr/data/15058519/openapi.do) | 해양수산부 | 전국 해수욕장 위치·제원·비상연락처·이미지 등 오픈 API. | API Key | free | ✅ |
| [산림청 산·등산로·식물 정보 API](https://www.data.go.kr/data/15058682/openapi.do) | 산림청 | 전국 산 정보, 등산로, 숲에 사는 식물, 수목 이미지 등 산림 오픈 API. | API Key | free | ✅ |
| [국립중앙박물관 e뮤지엄 유물정보 API](https://www.data.go.kr/data/15104964/openapi.do) | 문화체육관광부 / 국립중앙박물관 | 전국 박물관 소장품(유물) 명칭·시대·재질·이미지 등 통합검색 오픈 API. | API Key | free | ✅ |
| [국민체육진흥공단 공공체육시설 정보 API](https://www.data.go.kr/data/15107764/openapi.do) | 서울올림픽기념국민체육진흥공단 | 전국 공공체육시설 위치·규모·운영상태 등 체육시설 오픈 API. | API Key | free | ✅ |
| [한국관광공사 두루누비(코리아둘레길) 정보 API](https://www.data.go.kr/data/15101974/openapi.do) | 한국관광공사 | 코리아둘레길 284개 코스 GPX·걷기여행길·자전거길 정보 오픈 API. | API Key | free | ✅ |
| [한국마사회 경마경주정보 API](https://www.data.go.kr/data/15063951/openapi.do) | 한국마사회 | 경주계획, 경주결과, 경주마·기수 정보 등 경마 오픈 API. | API Key | free | ✅ |
| [국가유산청 문화재 공간정보(GIS) API](https://www.data.go.kr/data/3070426/openapi.do) | 국가유산청 | 문화재 위치·속성·사진·도면 등 GIS 기반 국가유산 공간정보 오픈 API. | API Key | free | ✅ |
| [문화체육관광부 공연정보(통합) API](https://www.data.go.kr/data/15121487/openapi.do) | 문화체육관광부 | 예술의전당·국립극장 등 10개 기관 공연/전시 정보 통합 오픈 API. | API Key | free | ✅ |
| [국립현대미술관 미술작품 정보 API](https://www.data.go.kr/dataset/3059104/openapi.do) | 국립현대미술관(MMCA) | 소장 미술작품 명칭·작가·재질·이미지 등 정보 오픈 API. | API Key | free | ✅ |
| [한국관광공사 무장애(배리어프리) 여행정보 API](https://www.data.go.kr/data/15101897/openapi.do) | 한국관광공사 | 장애인·고령자 등 이동약자를 위한 무장애 관광지·편의시설 정보. | API Key(serviceKey) | free | ✅ |
| [국가유산청 국가유산포털 Open API](https://www.khs.go.kr/html/HtmlPage.do?pg=/publicinfo/pbinfo3_0201.jsp&mn=NS_04_04_03) | 국가유산청(구 문화재청) | 국보·보물·사적·명승·천연기념물·궁궐·왕릉·세계유산 등 지정 국가유산 통합 정보(공간정보 포함). | API Key 또는 키 불필요(서비스별 상이) | free | — |
| [국립무형유산원 무형유산 정보 API](https://www.data.go.kr/data/15028215/openapi.do) | 국가유산청 국립무형유산원 | 국가무형문화재 현황, 전승 공방·공예품, 공연/전시/교육 디지털 기록 등 무형유산 정보. | API Key(serviceKey) | free | ✅ |
| [한국문화정보원 전통문양 Open API](https://www.data.go.kr/data/15015644/openapi.do) | 한국문화정보원 / 국가유산청 국립문화유산연구원 | 한국 전통문양·단청 등 디자인 활용 가능한 문양 이미지·메타데이터. | API Key(serviceKey) | free | ✅ |
| [국립민속박물관 한국민속대백과/아카이브 API](https://www.data.go.kr/data/15126343/openapi.do) | 문화체육관광부 국립민속박물관 | 한국민속대백과사전(세시풍속·전통놀이·민간신앙 등) 및 민속 아카이브 사진·자료. | API Key(serviceKey) | free | ✅ |
| [국립문화유산연구원 전통건축·전통재료 API](https://www.data.go.kr/data/15015627/openapi.do) | 국가유산청 국립문화유산연구원 | 향교·서원 등 전통건축 기록, 석탑 3D, 한지 등 문화유산 전통재료 정보. | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 금융

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [한국은행 경제통계시스템(ECOS) Open API](https://ecos.bok.or.kr/api/) | 한국은행 | 금리·환율·국민계정 등 경제통계 조회 오픈 API. | API Key | free | ✅ |
| [오픈뱅킹 공동업무 API](https://openapi.kftc.or.kr/) | 금융결제원(KFTC) | 계좌조회·이체 등 은행 공동 오픈뱅킹 API. | OAuth 2.0 | free | ✅ |
| [OpenDART 전자공시 API](https://opendart.fss.or.kr/) | 금융감독원 | 상장·외부감사 기업의 전자공시(사업보고서, 재무제표 등) 오픈 API. | API Key | free | ✅ |
| [한국수출입은행 환율 Open API](https://www.koreaexim.go.kr) | 한국수출입은행 | 현재/대출 환율 등 환율정보 오픈 API. | API Key | free | ✅ |
| [KRX OPEN API](https://openapi.krx.co.kr/) | 한국거래소(KRX) | 주식·채권·파생·지수 등 거래소 시장정보 오픈 API. | API Key | free | ✅ |
| [한국예탁결제원(SEIBro) Open API](https://api.seibro.or.kr/pubc/pubr/cmm/CMPubrHome/viewCMPubrHome.do) | 한국예탁결제원 | 주식·기업·증권 발행정보 등 예탁결제 데이터 오픈 API. | API Key | free | ✅ |
| [금융위원회 주식시세정보 API](https://www.data.go.kr/data/15094808/openapi.do) | 금융위원회 | 상장 주식의 시가·종가·거래량 등 시세 정보 오픈 API. | API Key | free | ✅ |
| [한국투자증권 KIS Developers Open API](https://apiportal.koreainvestment.com/intro) | 한국투자증권 | 주식/선물 시세 조회 및 주문·자동매매 REST/WebSocket 트레이딩 API. | API Key(App Key/Secret) + OAuth | free | ✅ |
| [키움증권 Open API+](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView) | 키움증권 | 주식 시세·주문 등 트레이딩 API. | 계정 인증 | free | ✅ |
| [업비트(Upbit) Open API](https://docs.upbit.com/kr/docs/developer-center-overview) | 업비트(두나무) | 가상자산 시세(캔들·현재가·호가·체결), 잔고·주문·출금 등 거래소 API. | 없음(시세) / API Key(거래) | free | — |
| [토스페이먼츠 결제 API](https://docs.tosspayments.com/) | 토스페이먼츠 | 카드·간편결제(네이버페이/카카오페이 등) 통합 결제 연동 API. | API Key(시크릿/클라이언트 키) | free-tier | ✅ |
| [포트원(PortOne, 구 아임포트) 결제연동 API](https://developers.portone.io/) | 포트원(코리아포트원) | 여러 PG·간편결제를 단일 연동으로 통합 처리하는 결제 연동 API. | API Key | free-tier | ✅ |
| [우체국금융(예금·보험) Open API](https://www.epostlife.go.kr/IPUIOP0000.do) | 우정사업본부 | 우체국 예금상품, 보험상품, 공시이율, 보험료 조회 등 우체국금융 API. | API Key | free | ✅ |
| [금융결제원 어카운트인포 계좌통합관리 API](https://developers.kftc.or.kr/dev/openapi/account-info) | 금융결제원(KFTC) | 전 금융기관 계좌·카드·보험 통합조회 및 휴면계좌 정리 등 어카운트인포 API. | OAuth 2.0 | free | ✅ |
| [한국주택금융공사(HF) 주택금융 통계 API](https://houstat.hf.go.kr/research/portal/openapi/openApiIntroPage.do) | 한국주택금융공사(HF) | 보금자리론, 주택연금, 전세자금보증 등 주택금융 통계 오픈 API. | API Key | free | ✅ |
| [하나금융그룹 Open API](https://www.hanafnapimarket.com/) | 하나금융그룹 | 하나금융 API 마켓플레이스 | OAuth | free | ✅ |
| [KB금융 API 포탈](https://apiportal.kbfg.com/) | KB금융그룹 | KB금융 종합 금융 API(800+) | OAuth | free | ✅ |
| [금융상품한눈에(금융상품 통합비교공시) Open API](https://finlife.fss.or.kr/finlife/api/fdrmDsclsApiUse/list.do?menuNo=700060) | 금융감독원(FSS) | 정기예금·적금·신용대출·주택담보대출·전세대출·연금저축 등 금융상품을 회사별 금리로 비교 조회. | API Key(인증키) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 교육·학술

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [도서관 정보나루 Open API](https://www.data4library.kr/apiUtilization) | 문화체육관광부 / 국립중앙도서관 | 전국 도서관 대출·소장·인기도서 등 도서관 빅데이터 오픈 API. | API Key | free | ✅ |
| [NEIS 교육정보 개방 포털 Open API](https://open.neis.go.kr/) | 한국교육학술정보원(KERIS) | 전국 학교 기본정보, 급식, 시간표, 학사일정 등 교육 오픈 API. | API Key | free | ✅ |
| [국립중앙도서관 Open API](https://www.nl.go.kr) | 국립중앙도서관 | 서지정보 검색, LOD, 전거데이터 등 도서/서지 오픈 API. | API Key | free | ✅ |
| [커리어넷 진로·직업정보 Open API](https://www.career.go.kr/cnet/front/openapi/jobCenter.do) | 교육부 / 한국직업능력연구원 | 직업정보, 학과정보, 진로심리검사, 진로상담 등 오픈 API. | API Key | free | ✅ |
| [KCI 한국학술지인용색인 논문정보 API](https://www.data.go.kr/data/15085348/openapi.do) | 한국연구재단 | 국내 학술지·논문 서지정보, 인용/피인용 등 학술 오픈 API. | API Key | free | ✅ |
| [ScienceON Open API](https://scienceon.kisti.re.kr/por/oapi/openApi.do) | 한국과학기술정보연구원(KISTI) | 논문·특허·보고서·연구자 등 과학기술 지식 통합검색 오픈 API. | API Key | free | ✅ |
| [학교알리미 Open API](https://www.schoolinfo.go.kr/ng/go/pnnggo_a01_l0.do) | 교육부 / 한국교육학술정보원 | 전국 초·중·고 학교 기본정보 및 공시정보 오픈 API. | API Key(네이버/카카오 로그인) | free | ✅ |
| [유치원알리미 공시정보 API](https://www.data.go.kr/data/15020786/openapi.do) | 교육부 / 한국교육학술정보원 | 전국 유치원 기본정보, 급식, 예산, 교육과정 등 공시 오픈 API. | API Key | free | ✅ |
| [어린이집정보공개포털 보육정보 API](https://info.childcare.go.kr/info_html5/oais/openapi/OpenApiSlL.jsp) | 보건복지부 / 한국사회보장정보원 | 전국 어린이집 위치·정원·평가 등 보육시설 정보 오픈 API. | API Key | free | ✅ |
| [국가기록원 나라기록물정보 서비스 API](https://www.data.go.kr/data/15000153/openapi.do) | 행정안전부 국가기록원 | 국가 기록물 메타데이터(제목·생산기관·관리번호 등) 검색 오픈 API. | API Key | free | ✅ |
| [대학알리미 대학정보공시 API](https://www.data.go.kr/data/15037507/openapi.do) | 한국대학교육협의회 | 전국 대학 기본정보, 학과, 등록금, 장학금 등 대학 공시정보 오픈 API. | API Key | free | ✅ |
| [RISS 학술연구정보 Open API](https://www.riss.kr/apicenter/apiMain.do) | 한국교육학술정보원(KERIS) | 학위논문·학술논문·단행본·연구보고서 등 학술정보 검색 오픈 API. | API Key | free | ✅ |
| [국회도서관 Open API](https://www.nanet.go.kr/usermadang/etc/openApiView.do) | 국회도서관 | 국회전자도서관 소장자료·국가학술정보 검색 오픈 API. | API Key | free | ✅ |
| [국가정책연구포털(NKIS) Open API](https://www.nkis.re.kr/openSvcList.do) | 경제·인문사회연구회 | 국책연구기관 정책연구보고서 등 정책연구 정보 오픈 API. | API Key | free | ✅ |
| [클래스101 Business API](https://docs.class101.net/) | 클래스101 | 클래스 관리·수강신청·진도율·SSO | Bearer Token | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 날씨·환경

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [기상청 API 허브](https://apihub.kma.go.kr) | 기상청 | 단기/중기예보, 실황, 지상/해양 관측 등 기상 데이터 오픈 API 통합 허브. | API Key | free | ✅ |
| [에어코리아 대기오염정보 API](https://www.data.go.kr/data/15073861/openapi.do) | 한국환경공단 | 미세먼지·대기질 실시간 측정정보 오픈 API. | API Key | free | ✅ |
| [한국환경공단 전기차 충전소 정보 API](https://www.data.go.kr/data/15076352/openapi.do) | 한국환경공단 | 전국 전기차 충전소 위치·상태 정보 오픈 API. | API Key | free | ✅ |
| [바다누리 해양정보 서비스 Open API](http://www.khoa.go.kr/oceangrid/khoa/takepart/openapi/openApiDeveloperGuide.do) | 국립해양조사원 | 조위·조류·수온 등 해양 관측/예측 정보 오픈 API. | API Key | free | ✅ |
| [K-water 공공데이터 개방포털 Open API](https://opendata.kwater.or.kr/) | 한국수자원공사(K-water) | 댐·보 수문정보(수위·강우·방류량 등), 수자원 데이터 오픈 API. | API Key | free | ✅ |
| [환경부 화학물질정보 API](https://www.data.go.kr/data/15029194/openapi.do) | 환경부 화학물질안전원 | 화학물질 명칭·CAS번호·분자식·분류 등 화학물질 정보 오픈 API. | API Key | free | ✅ |
| [국립생물자원관 한반도 생물다양성 API](https://species.nibr.go.kr/) | 환경부 국립생물자원관 | 국가생물종목록, 생물다양성, 종별 멀티미디어 등 생태 정보 오픈 API. | API Key | free | ✅ |
| [한강홍수통제소 수문·홍수 Open API](https://www.hrfco.go.kr/web/openapiPage/openApi.do) | 환경부 한강홍수통제소 | 하천 수위·강우·댐 방류, 홍수예보, 강우레이더 등 수문 오픈 API. | API Key | free | ✅ |
| [국가지하수정보센터(GIMS) Open API](https://www.gims.go.kr/apiIntro.do) | 환경부 / 한국수자원공사 | 지하수 관측(수위·수질), 관정·조사시설 등 지하수 공간정보 오픈 API. | API Key | free | ✅ |
| [한국환경공단 올바로(Allbaro) 폐기물·자원순환 API](https://www.recycling-info.or.kr/sds/apiKeyControl.do) | 한국환경공단 | 폐기물 배출·운반·처리 관리(올바로) 코드 및 자원순환 정보 오픈 API. | API Key | free | ✅ |
| [국립생태원 생태자연도 서비스 API](https://www.data.go.kr/data/15057288/openapi.do) | 국립생태원(NIE) | 전 국토 생태·자연도 등급, 지형평가 등 생태 공간정보 오픈 API. | API Key | free | ✅ |
| [국립수목원 국가표준식물목록 서비스 API](https://www.data.go.kr/data/15000236/openapi.do) | 산림청 국립수목원 | 국가표준식물목록(학명·국명·문헌 등), 식물자원 정보 오픈 API. | API Key | free | ✅ |
| [기상청 기상특보 조회서비스 API](https://www.data.go.kr/data/15000415/openapi.do) | 기상청(KMA) | 폭염·한파·호우·태풍·황사 등 기상특보 발효 현황 및 예비특보. | API Key(serviceKey) | free | ✅ |
| [기상청 항공기상청 항공기상 정보 API](https://www.data.go.kr/data/15123139/openapi.do) | 기상청 항공기상청(KAMC) | 공항예보(TAF)·공항기상관측(METAR/AMOS)·항공기상전문(IWXXM) 등 항공·공항 기상 정보. | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 생활·소셜

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [카카오톡 메시지/소셜 API](https://developers.kakao.com/docs/latest/ko/kakaologin/common) | 카카오 | 카카오 로그인, 메시지 전송, 카카오톡 채널, 프로필 등. | OAuth 2.0 | free | ✅ |
| [네이버 로그인 / 회원 API](https://developers.naver.com/docs/login/api/api.md) | 네이버 | 네이버 아이디 로그인(OAuth) 및 회원 프로필 조회. | OAuth 2.0 | free | ✅ |
| [우정사업본부 Open API](https://www.koreapost.go.kr/user/extra/kpost/330/bbs/openApi/openApiSet/jsp/ExtraUser.do) | 우정사업본부(우정청) | 우편번호, 우편물 추적, 우체국 위치 등 우편 오픈 API. | API Key | free | ✅ |
| [한국천문연구원 음양력·특일 정보 API](https://www.data.go.kr/data/15012679/openapi.do) | 한국천문연구원(KASI) | 음력/양력 변환, 공휴일·국경일·24절기, 일출·일몰 등 천문/달력 오픈 API. | API Key | free | ✅ |
| [국가동물보호정보시스템 구조(유기)동물 조회 API](https://www.data.go.kr/data/15098931/openapi.do) | 농림축산식품부 농림축산검역본부 | 전국 유기·구조동물, 보호소, 동물등록 현황 등 동물보호 오픈 API. | API Key | free | ✅ |
| [동행복권 로또 6/45 당첨번호 조회 (비공식)](https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1) | 동행복권 | 회차별 로또 당첨번호·당첨금 조회. 공식 문서 없는 내부 엔드포인트. | 없음 | free | — |
| [전국무료와이파이 표준데이터 API](https://www.data.go.kr/data/15013116/standard.do) | 행정안전부 / 한국지능정보사회진흥원 | 전국 무료 와이파이 설치장소, SSID, 좌표 등 표준데이터 오픈 API. | API Key | free | ✅ |
| [복지로 복지서비스 Open API](https://www.data.go.kr/data/15090532/openapi.do) | 보건복지부 / 한국사회보장정보원 | 중앙부처·지자체 복지서비스 목록·상세 등 복지정보 오픈 API. | API Key | free | ✅ |
| [공유누리 Open API](https://www.eshare.go.kr/OpenApi/Info/index.do) | 행정안전부 | 공공시설·자원(회의실·체육시설·주차장 등) 개방·예약 정보 오픈 API. | API Key | free | ✅ |
| [국방부 군 부대 식단 정보 API](https://www.data.go.kr/data/15056563/openapi.do) | 국방부 | 부대별 일자별 조·중·석식 메뉴 및 칼로리 등 군 급식 정보 오픈 API. | API Key | free | ✅ |
| [외교부 해외안전여행 여행경보 API](https://www.data.go.kr/data/15076237/openapi.do) | 외교부 | 국가·지역별 여행경보, 특별여행경보, 여행금지 등 해외안전여행 오픈 API. | API Key | free | ✅ |
| [온통청년 청년정책 API](https://www.data.go.kr/data/15143273/openapi.do) | 한국고용정보원 | 중앙·지자체 청년정책, 청년센터 등 청년 지원정보 오픈 API. | API Key | free | ✅ |
| [소비자24 제품안전·리콜 Open API](https://www.consumer.go.kr/user/ftc/consumer/openApiSvcUser/120/selectOpenApiSvcList.do) | 공정거래위원회 / 한국소비자원 | 제품 리콜정보, 인증정보, 피해주의보 등 소비자 안전 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 농축수산

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KAMIS 농수산물유통정보 Open API](https://www.kamis.or.kr/customer/reference/openapi_list.do) | 한국농수산식품유통공사(aT) | 농수산물 도·소매 가격, 거래동향 등 17종 유통정보 오픈 API. | API Key | free | ✅ |
| [농사로 Open API](https://www.nongsaro.go.kr/portal/ps/psz/psza/contentMain.ps?menuId=PS00191) | 농촌진흥청 | 농업기술·작물·병해충 등 농업정보 오픈 API. | API Key | free | ✅ |
| [농림축산식품 공공데이터 포털](https://data.mafra.go.kr/) | 농림축산식품부 | 농림축산식품 분야 데이터·오픈API를 제공하는 부처 포털. | API Key | free | ✅ |
| [축산물이력제 Open API](https://mtrace.go.kr/openService.jsp) | 농림축산식품부 / 축산물품질평가원 | 소·돼지 등 축산물 이력정보(개체식별번호) 조회 오픈 API. | API Key | free | ✅ |
| [스마트팜코리아 Open API](https://data.smartfarmkorea.net/openApi/openApiUseInfo.do) | 농림수산식품교육문화정보원(EPIS) | 스마트팜 시설원예·노지 빅데이터(환경·생육·제어) 등 농업 오픈 API. | API Key | free | ✅ |
| [한국농어촌공사 농촌용수 저수지 수위정보 API](https://www.data.go.kr/data/15099919/openapi.do) | 한국농어촌공사 | 농업용 저수지 수위·저수율·수질 등 농촌용수 오픈 API. | API Key | free | ✅ |
| [국립농업과학원 농업기상 관측데이터 API](https://www.data.go.kr/data/15078057/openapi.do) | 농촌진흥청 국립농업과학원 | 농업기상 기본·상세 관측(기온·강수·일사·토양수분 등), 주산지 분석 오픈 API. | API Key | free | ✅ |
| [국립수산과학원 어장·해양관측 Open API](https://www.nifs.go.kr/openApi/actionOpenapiInfoList.do) | 국립수산과학원(NIFS) | 실시간 어장정보, 수온·염분 등 해양관측, 수산 정보 오픈 API. | API Key | free | ✅ |
| [국립농산물품질관리원 친환경인증정보 API](https://www.data.go.kr/data/15000935/openapi.do) | 국립농산물품질관리원(NAQS) | 친환경(유기·무농약)·전통식품 등 농식품 인증정보 오픈 API. | API Key | free | ✅ |
| [한국임업진흥원 임산물정보 API](https://www.data.go.kr/data/15022797/openapi.do) | 한국임업진흥원(KOFPI) | 임산물 기초정보·유통 등 임업 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 보건·식품

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [식품안전나라 Open API](https://www.foodsafetykorea.go.kr/api/) | 식품의약품안전처 | 식품·의약품·건강기능식품 정보, 회수/판매중지 등 식의약 오픈 API. | API Key | free | ✅ |
| [건강보험심사평가원(HIRA) 공공 API](https://opendata.hira.or.kr) | 건강보험심사평가원 | 병원·약국 정보, 의약품, 비급여 진료비 등 보건의료 오픈 API. | API Key | free | ✅ |
| [E-Gen 중앙응급의료센터 Open API](https://www.e-gen.or.kr/nemc/open_api.do) | 국립중앙의료원 중앙응급의료센터 | 실시간 응급실 가용병상, 응급의료기관, 외상센터 등 응급의료 오픈 API. | API Key | free | ✅ |
| [국가건강정보포털 Open API](https://health.kdca.go.kr/healthinfo/biz/health/portalUseGuidance/openApiReqst/openApiReqstRegist.do) | 질병관리청 | 질병·건강정보 콘텐츠 오픈 API. | API Key | free | ✅ |
| [국민건강보험공단 검진기관 정보 API](https://www.data.go.kr/data/15001672/openapi.do) | 국민건강보험공단 | 건강검진기관 위치·검진종류 등 정보 오픈 API. | API Key | free | ✅ |
| [식약처 의약품개요정보(e약은요) API](https://www.data.go.kr/data/15075057/openapi.do) | 식품의약품안전처 | 일반·전문 의약품의 효능·용법·주의사항·상호작용 등 개요 정보 오픈 API. | API Key | free | ✅ |
| [식약처 의약품안전사용서비스(DUR) API](https://www.data.go.kr/data/15059486/openapi.do) | 식품의약품안전처 | 병용금기, 연령·임부 금기, 중복효능 등 의약품 안전사용(DUR) 오픈 API. | API Key | free | ✅ |
| [초록누리(생활환경안전정보) Open API](https://ecolife.me.go.kr/ecolife/infoCenter/openApi?pMENU_NO=588) | 기후에너지환경부(환경부) / 국립환경과학원 | 생활화학제품 전성분(함유 화학물질·유해성) 및 안전기준 위반 회수대상 제품 정보. | API Key(인증키) | free | ✅ |
| [대한적십자사 헌혈·혈액 정보 Open API](https://www.data.go.kr/data/15050729/fileData.do) | 대한적십자사 혈액관리본부 | 전국 헌혈의 집 정보, 혈액 통계 등 헌혈·혈액 관련 공공데이터. | API Key(serviceKey) | free | ✅ |
| [질병관리청 예방접종 정보 API](https://www.data.go.kr/data/15084296/openapi.do) | 질병관리청(KDCA) | 예방접종 대상 감염병 정보 및 국가예방접종 위탁의료기관 현황. | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 콘텐츠·미디어

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KOBIS 영화관입장권통합전산망 Open API](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do) | 영화진흥위원회(KOFIC) | 일별/주간 박스오피스, 영화/영화인/영화사 정보 오픈 API. | API Key | free | ✅ |
| [KMDb 한국영화데이터베이스 Open API](https://www.kmdb.or.kr/info/api/apiList) | 한국영상자료원 | 영화 상세정보(스태프/줄거리/스틸 등) 검색 오픈 API. | API Key | free | ✅ |
| [알라딘 상품 검색 Open API](https://www.aladin.co.kr/ttb/apiguide.aspx) | 알라딘(Aladin) | 도서 상품 검색/조회/베스트셀러 등 도서 정보 오픈 API. | API Key(TTBKey) | free | ✅ |
| [빅카인즈(BIGKINDS) 뉴스 빅데이터 API](https://www.bigkinds.or.kr/) | 한국언론진흥재단 | 뉴스 기사 검색, 메타데이터, 개체명·토픽 분석 등 뉴스 빅데이터 오픈 API. | API Key | free | ✅ |
| [한국콘텐츠진흥원(KOCCA) Open API](https://www.kocca.kr/kocca/subPage.do?menuNo=204795) | 한국콘텐츠진흥원 | 방송·게임·만화·음악 등 콘텐츠 산업 통계·정보 오픈 API. | API Key | free | ✅ |
| [영상물등급위원회 등급분류정보 API](https://www.data.go.kr/data/15127675/openapi.do) | 영상물등급위원회 | 비디오물 등급분류 정보(제명·감독·관람등급·내용정보) 오픈 API. | API Key | free | ✅ |
| [한국저작권위원회 공유마당 API](https://gongu.copyright.or.kr/gongu/useReqst/apiKey/info.do?menuNo=200245) | 한국저작권위원회 | CCL/만료저작물 등 자유이용 저작물(사진·음악·미술·어문 등) 검색 오픈 API. | API Key | free | ✅ |
| [국립국악원 국악 디지털음원 API](https://www.data.go.kr/data/15097515/openapi.do) | 문화체육관광부 국립국악원 | 국악 디지털 음원·아카이브(음향·영상·이미지) 정보 오픈 API. | API Key | free | ✅ |
| [한국국제교류재단 한류현황 API](https://www.data.go.kr/data/15076252/openapi.do) | 한국국제교류재단(KF) | 전 세계 한류 동호회·팬 규모 등 분야별 한류 현황 통계. | API Key(serviceKey) | free | ✅ |
| [영화진흥위원회 영화인 정보 API](https://www.data.go.kr/data/3058452/openapi.do) | 영화진흥위원회(KOFIC) | 영화 감독·배우 등 영화인 인물 DB 및 필모그래피 상세정보. | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 재난·안전

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [재난안전데이터 공유플랫폼 Open API](https://www.safetydata.go.kr/) | 행정안전부 | 재난·안전 분야 데이터를 통합 제공하는 플랫폼 오픈 API. | API Key | free | ✅ |
| [생활안전지도(SafeMap) Open API](https://www.safemap.go.kr/dvct/openAPI.do) | 행정안전부 | 치안·교통·재난 등 생활안전 공간정보 오픈 API. | API Key | free | ✅ |
| [소방청 구급정보 서비스 API](https://www.data.go.kr/data/15099423/openapi.do) | 소방청 | 구급·구급통계, 출동 등 119 구급 정보 오픈 API. | API Key | free | ✅ |
| [경찰청 치안·교통 Open API](https://www.data.go.kr/data/15148511/openapi.do) | 경찰청 | 교통 CCTV 영상, 안전Dream 실종자 정보, 범죄 통계 등 치안 오픈 API. | API Key | free | ✅ |
| [한국승강기안전공단 승강기 정보 API](https://www.data.go.kr/data/15000476/openapi.do) | 한국승강기안전공단 | 건물별 승강기 목록·검사이력·사고/고장이력 등 승강기 안전 오픈 API. | API Key | free | ✅ |
| [경찰청 실종경보정보 서비스 API](https://www.data.go.kr/data/3051810/openapi.do) | 경찰청 | 실종아동·치매환자 등 실종경보 발령 대상자 정보 조회. | API Key(serviceKey) | free | ✅ |
| [기상청 지진정보 조회서비스 API](https://www.data.go.kr/data/15000420/openapi.do) | 기상청(KMA) | 국내외 지진 발생 정보(규모·진앙·발생시각) 및 지진해일 정보 조회. | API Key(serviceKey) | free | ✅ |
| [행정안전부 무더위쉼터 Open API](https://www.data.go.kr/data/15138456/openapi.do) | 행정안전부 | 전국 무더위쉼터(경로당·복지관 등) 위치·운영 정보. | API Key(serviceKey) | free | ✅ |
| [행정안전부 민방위대피시설 조회서비스 API](https://www.data.go.kr/data/15155067/openapi.do) | 행정안전부 | 전국 민방위 대피시설(지하 대피소 등) 위치·수용규모 조회. | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 지도·위치

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [SGIS 통계지리정보서비스](https://sgis.kostat.go.kr/developer/) | 통계청 | 통계 기반 지리정보(인구·사업체·경계 등) 오픈 API. | API Key | free | ✅ |
| [VWorld(브이월드) 오픈 API](https://www.vworld.kr/dev/v4api.do) | 국토교통부 / 국토지리정보원 | 2D/3D 지도, 배경지도, 공간정보(WMS/WFS), 지오코더 등 공간정보 오픈 API. | API Key | free | ✅ |
| [카카오맵 / 로컬 API](https://developers.kakao.com/docs/latest/ko/local/dev-guide) | 카카오 | 지도 표시, 장소 검색, 주소-좌표 변환(지오코딩) 등. | API Key(REST/JavaScript) | free | ✅ |
| [네이버 지도(Maps) API](https://www.ncloud.com/product/applicationService/maps) | 네이버클라우드플랫폼(NCP) | 지도, 길찾기(Directions), 지오코딩 등. | API Key(Client ID/Secret) | free-tier | ✅ |
| [도로명주소 API](https://business.juso.go.kr/addrlink/openApi/apiExprn.do) | 행정안전부 | 도로명주소 검색, 영문주소, 좌표제공 등 주소 오픈 API. | API Key | free | ✅ |
| [국토교통부 연속지적도·토지특성 정보 API](https://www.data.go.kr/data/15057558/openapi.do) | 국토교통부 / 국토지리정보원 | 연속지적도형정보, 토지특성, 토지이용 등 공간정보 오픈 API. | API Key | free | ✅ |
| [한국국토정보공사(LX) LX맵 서비스 API](https://www.data.go.kr/data/15020966/openapi.do) | 한국국토정보공사(LX) | 국토정보 기본도·정사영상 기반 지도 및 국토변화 정보 오픈 API. | API Key | free | ✅ |
| [카카오내비 API](https://developers.kakao.com/docs/latest/ko/kakaonavi/common) | 카카오 | 카카오내비 앱 연동 길 안내, 다중 경유지·다중 목적지 경로 탐색. | API Key(REST/SDK) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 부동산

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [국토교통부 실거래가 공개시스템 API](https://rt.molit.go.kr) | 국토교통부 | 아파트/연립/단독 등 부동산 매매·전월세 실거래가 오픈 API. | API Key | free | ✅ |
| [한국부동산원 R-ONE 부동산통계 Open API](https://www.reb.or.kr/r-one/portal/openapi/openApiIntroPage.do) | 한국부동산원 | 지가·주택가격지수·거래량 등 부동산 통계 오픈 API. | API Key | free | ✅ |
| [국토교통부 개별공시지가·공동주택가격 API](https://www.data.go.kr/data/15124014/openapi.do) | 국토교통부 | 개별공시지가, 공동주택가격(WMS/WFS/속성) 등 부동산 공시가격 오픈 API. | API Key | free | ✅ |
| [국토교통부 건축HUB 건축물대장·인허가 API](https://www.data.go.kr/data/15134735/openapi.do) | 국토교통부 | 건축물대장(표제부·전유부·층별 등), 건축인허가 등 건축데이터 오픈 API. | API Key | free | ✅ |
| [한국토지주택공사(LH) 임대·분양 주택정보 API](https://www.data.go.kr/data/15058476/openapi.do) | 한국토지주택공사(LH) | 공공임대주택 단지정보, 분양·임대 공고별 공급정보 등 주택 오픈 API. | API Key | free | ✅ |
| [주택도시보증공사(HUG) Open API](https://www.khug.or.kr/openapi/web/se/ap/seap000002.jsp) | 주택도시보증공사(HUG) | 분양보증, 주택사업, 주택도시 관련 통계·정보 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 결제·핀테크

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [토스페이](https://docs-pay.toss.im/reference) | 비바리퍼블리카(토스) | 토스 간편결제·정기결제 API | API Key | free | ✅ |
| [부트페이](https://docs.bootpay.co.kr/) | 부트페이 | 다중 PG(이니시스·KCP·다날 등) 통합 결제 연동 | API Key | free | ✅ |
| [페이플](https://developer.payple.kr/) | 페이플 | 간편·정기·링크결제 서비스 | API Key | free | ✅ |
| [페이코(PAYCO)](https://developers.payco.com/guide) | NHN페이코 | NHN 통합 ID·결제·멤버십 연동 | OAuth | free | ✅ |
| [하이픈 API 마켓플레이스](https://hyphen.im/) | 케이에스넷 | 금융·공공 데이터 스크래핑 API 마켓(500+) | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 상권·창업

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [소상공인시장진흥공단 상가(상권)정보 API](https://www.data.go.kr/data/15012005/openapi.do) | 소상공인시장진흥공단 | 전국 상가업소 상호·업종·좌표 등 상권정보 오픈 API. | API Key | free | ✅ |
| [K-Startup 창업지원 정보 API](https://www.data.go.kr/data/15125364/openapi.do) | 창업진흥원 / 중소벤처기업부 | 창업지원 사업공고, 사업소개, 콘텐츠 등 창업 오픈 API. | API Key | free | ✅ |
| [공정거래위원회 가맹사업(프랜차이즈) 정보 API](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=가맹사업) | 공정거래위원회 | 브랜드별 가맹점·직영점 수, 매출액, 계약현황 등 프랜차이즈 정보 오픈 API. | API Key | free | ✅ |
| [기업마당(Bizinfo) 정부지원사업 API](https://www.bizinfo.go.kr/web/lay1/program/S1T175C174/apiList.do) | 중소벤처기업부 | 중앙부처·지자체·유관기관 중소기업 지원사업 공고·정책정보 오픈 API. | API Key | free | ✅ |
| [지방행정인허가데이터개방(LOCALDATA) Open API](https://www.localdata.go.kr/devcenter/apiGuide.do?menuNo=20002) | 행정안전부 / 한국지역정보개발원 | 일반·휴게음식점 등 전국 인허가 업소(약 20만+) 정보. 그룹/업종별 전체·변동분 오픈API. | API Key(인증키) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 에너지

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [한국전력 전력데이터 개방포털 Open API](https://bigdata.kepco.co.kr/) | 한국전력공사(KEPCO) | 지역별 전력사용량, 계약종별, 발전원 등 전력 데이터 오픈 API. | API Key | free | ✅ |
| [전력거래소(KPX) 공공데이터 API](https://www.kpx.or.kr/menu.es?mid=a10107020000) | 한국전력거래소(KPX) | 전력 수급, SMP, 발전량 등 전력시장 데이터 오픈 API. | API Key | free | ✅ |
| [한국에너지공단 신재생에너지 Open API](https://www.energy.or.kr/web/kem_home_new/data_offer/OPEN_API_3.asp) | 한국에너지공단 | 신재생에너지 보급·설비 등 에너지 통계/정보 오픈 API. | API Key | free | ✅ |
| [한국가스공사 도시가스 공급열량 API](https://www.data.go.kr/data/15138871/openapi.do) | 한국가스공사 | 도시가스 공급예상열량·공급열량실적 등 가스 오픈 API. | API Key | free | ✅ |
| [오피넷(Opinet) 유가정보 Open API](https://www.opinet.co.kr/user/custapi/custApiInfo.do) | 한국석유공사 | 전국/시도/시군구 평균 유가, 최저가 주유소, 주유소 위치·상세 등 유가 API. | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 인공지능

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [ETRI 공공 인공지능 Open API](https://aiopen.etri.re.kr/) | 한국전자통신연구원(ETRI) | 한국어 형태소분석, 질의응답, 음성인식, OCR 등 AI 오픈 API. | API Key | free | ✅ |
| [네이버 CLOVA AI API](https://www.ncloud.com/product/aiService) | 네이버클라우드플랫폼(NCP) | CLOVA OCR, Speech(STT/TTS), Face, CLOVA Studio(생성형) 등. | API Key | free-tier | ✅ |
| [네이버 Papago 번역 API](https://www.ncloud.com/product/aiService/papagoTranslation) | 네이버클라우드플랫폼(NCP) | 기계 번역(Papago) 및 언어감지 API. | API Key | free-tier | ✅ |
| [업스테이지(Upstage) Document AI·OCR API](https://console.upstage.ai/docs) | 업스테이지(Upstage) | 한국어 특화 OCR, Document Parse(문서 구조화), Solar LLM 등 AI API. | API Key | free-tier | ✅ |
| [AI허브(AI-Hub) 한국어 방언 발화 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=122) | 한국지능정보사회진흥원(NIA) / 과학기술정보통신부 | 경상·전라·충청·강원·제주 등 권역별 방언 음성+전사(표준어 대응) AI 학습용 데이터. | 회원가입 후 다운로드 승인(aihubshell) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 채용·고용

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [고용24 / 고용노동부 일자리 API](https://www.work24.go.kr) | 고용노동부 / 한국고용정보원 | 채용공고, 직업정보, 고용통계 등 일자리 오픈 API. | API Key | free | ✅ |
| [워크넷 Open API](https://openapi.work.go.kr/opiMain.do) | 한국고용정보원 | 채용정보, 직업정보, 학과정보 등 고용 오픈 API. | API Key | free | ✅ |
| [한국산업인력공단(큐넷) 국가자격 정보 API](https://openapi.hrdkorea.or.kr/main) | 한국산업인력공단 | 국가기술자격 종목·시험일정·교부수수료 등 자격정보 오픈 API. | API Key | free | ✅ |
| [근로복지공단 고용·산재보험 현황정보 API](https://www.data.go.kr/data/15059256/openapi.do) | 근로복지공단 | 사업장 고용·산재보험 가입 현황(사업장명·주소·근로자수 등) 오픈 API. | API Key | free | ✅ |
| [사람인(Saramin) 채용정보 API](https://oapi.saramin.co.kr/) | 사람인 | 채용공고 검색·조회 등 민간 채용정보 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 커뮤니케이션

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [가비아 문자/알림톡 API](https://message.gabia.com/api/documentation/) | 가비아 | SMS/LMS/MMS·카카오 알림톡 통합 발송 | OAuth | free-tier | ✅ |
| [센드버드 API](https://sendbird.com/docs) | 센드버드 | 실시간 채팅·음성/영상·AI 챗봇 | API Key | free-tier | ✅ |
| [잔디(JANDI) 웹훅](https://support.jandi.com/) | 토스랩 | 외부 서비스 인커밍 웹훅 연동 | Webhook | free | — |
| [네이버웍스 API](https://developers.worksmobile.com/kr) | 네이버웍스 | Bot·조직/그룹 관리·파일 등 협업 API | OAuth | free-tier | ✅ |
| [하이웍스 API](https://developers.hiworks.com/) | 하이웍스 | 전자결재·푸시 등 기업 협업 API | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 과학기술·특허

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KIPRIS PLUS 특허정보 Open API](https://plus.kipris.or.kr/) | 한국특허정보원 / 특허청 | 특허·실용신안·디자인·상표 등 지식재산권 정보 오픈 API. | API Key | free-tier | ✅ |
| [e나라표준인증 국가표준(KS) Open API](https://standard.go.kr/KSCI/onlineSvc/openApiIntro.do) | 산업통상자원부 국가기술표준원 | 한국산업표준(KS), 인증, 기술기준 등 표준·인증 정보 오픈 API. | API Key | free | ✅ |
| [KIGAM 지오빅데이터 오픈플랫폼 API](https://data.kigam.re.kr/guide/openapi) | 한국지질자원연구원(KIGAM) | 지질주제도, 지진·지진해일 정보 등 지질자원 데이터 오픈 API. | API Key | free | ✅ |
| [우주항공청 우주환경(우주날씨) API](https://www.data.go.kr/data/15128884/openapi.do) | 우주항공청(KASA) 우주환경센터 | 태양흑점폭발(R)·태양입자유입(S)·지자기교란(G) 등 우주환경 예보확률 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 물류·배송

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [스위트트래커 스마트택배](https://tracking.sweettracker.co.kr/) | 스위트트래커 | 24개 택배사 통합 배송조회 | API Key | free-tier | ✅ |
| [한진택배 배송조회](https://developers.hanjin.com/guides) | 한진택배 | 한진택배 배송추적 서비스 | 없음 | free | — |
| [로지스팟 물류 Open API](https://logi-spot.com/) | 로지스팟 | 통합 물류관리(운송배차·차량·정산) | API Key | free-tier | ✅ |
| [KOMSA MTIS Open API](https://mtisopenapi.komsa.or.kr/) | 한국해양교통안전공단 | 연안여객선 운항·통계·제원·안전 정보 | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 검색

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [네이버 검색 API](https://developers.naver.com/docs/serviceapi/search/news/news.md) | 네이버 | 뉴스·블로그·책·백과사전·이미지·웹·쇼핑·지역 등 통합검색 오픈 API. | API Key(Client ID/Secret) | free | ✅ |
| [네이버 데이터랩(DataLab) API](https://developers.naver.com/docs/serviceapi/datalab/search/search.md) | 네이버 | 검색어 트렌드, 쇼핑인사이트 등 트렌드 데이터 오픈 API. | API Key(Client ID/Secret) | free | ✅ |
| [카카오 검색(다음) API](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide) | 카카오 | 웹/동영상/이미지/블로그/책/카페 등 다음 검색 오픈 API. | API Key(REST) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 게임

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [NEXON Open API](https://openapi.nexon.com/ko/) | 넥슨(NEXON) | 메이플스토리·던전앤파이터·FC온라인 등 13종 게임의 캐릭터·랭킹·전적 데이터 API. | API Key | free | ✅ |
| [펄어비스 검은사막 API](https://documenter.getpostman.com/view/4028519/2s9Y5YRhp4) | 펄어비스 | 검은사막 게임·캐릭터 데이터 | API Key | free | ✅ |
| [게임물관리위원회 게임물 등급분류 정보 API](https://www.data.go.kr/data/15120667/openapi.do) | 게임물관리위원회(GRAC) | 국내 유통 게임물의 등급분류 결정 정보(게임명·신청사·결정등급·결정일 등). | API Key(serviceKey) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 블록체인·암호화폐

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [두나무 노딧(Nodit)](https://docs.nodit.io/) | 두나무 | 블록체인 개발 플랫폼·인프라(Web3) | API Key | free-tier | ✅ |
| [클레이튼 KAS](https://docs.klaytnapi.com/) | 그라운드X | 노드 운영 없는 블록체인 개발 API | API Key | free-tier | ✅ |
| [카이아(KAIA) API](https://docs.kaia.io/) | 카이아 재단 | 클레이튼+핀시아 통합 블록체인 API | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 언어·사전

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [표준국어대사전 Open API](https://stdict.korean.go.kr/openapi/openApiInfo.do) | 국립국어원 | 표준국어대사전 표제어·뜻풀이 검색 오픈 API. | API Key | free | ✅ |
| [우리말샘 개방형 사전 Open API](https://opendict.korean.go.kr/) | 국립국어원 | 신어·방언·북한어 등을 포함한 개방형 국어사전 검색 오픈 API. | API Key | free | ✅ |
| [국립국어원 지역어(방언) 종합정보 Open API](https://dialect.korean.go.kr/dialect/openAPI/apiInfo) | 문화체육관광부 국립국어원 | 전국 지역어(사투리·방언) 어휘·뜻풀이·용례 등 지역어 사전 정보 조회. | API Key(인증키) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### IoT·스마트홈

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [삼성 SmartThings API](https://developer.smartthings.com/docs/api/public) | 삼성전자 | 스마트홈 기기 제어·자동화·장소 관리 | OAuth | free | ✅ |
| [LG ThinQ API](https://smartsolution.developer.lge.com/) | LG전자 | AI 가전 제어·상업용 설비 관리 | OAuth | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 무역·통상

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [관세청 수출입무역통계(UNIPASS) Open API](https://unipass.customs.go.kr/ets/index.do?menuId=ETS_MNU_00000107) | 관세청 | 수출입 무역통계, 수출이행내역, 환율 등 관세·무역 오픈 API. | API Key | free | ✅ |
| [KOTRA 해외시장뉴스 API](https://www.data.go.kr/data/15034831/openapi.do) | 대한무역투자진흥공사(KOTRA) | 국가별 해외시장 뉴스, 단신속보, 국가정보(GDP·인구·규제 등) 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 미디어·콘텐츠

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [딥서치 뉴스 API](https://news.deepsearch.com) | 딥서치 | 국내외 200개 언론사 뉴스 수집 | API Key | free-tier | ✅ |
| [만화규장각 Open API](https://www.kmas.or.kr/guide/openapi) | 한국만화영상진흥원 | 만화·웹툰·작가 정보 제공 | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 법령·사법

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [국가법령정보 공동활용 API](https://open.law.go.kr/LSO/openApi/guideList.do) | 법제처 | 법령·행정규칙·자치법규·판례·헌재결정례 등 법령정보 오픈 API. | API Key(이메일 ID 기반) | free | ✅ |
| [열린국회정보 Open API](https://open.assembly.go.kr/portal/openapi/main.do) | 국회사무처 | 의안, 의원, 표결, 회의록 등 국회 정보 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 통신·인터넷

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KISA WHOIS 인터넷주소 정보검색 API](https://www.data.go.kr/data/15094277/openapi.do) | 한국인터넷진흥원(KISA) | 도메인·IP·AS번호 등록/할당 정보 조회(WHOIS) 오픈 API. | API Key | free | ✅ |
| [네이버 클라우드 SENS(문자·알림톡) API](https://www.ncloud.com/product/applicationService/sens) | 네이버클라우드플랫폼(NCP) | SMS/LMS/MMS 문자 및 카카오 알림톡·친구톡 발송 메시징 API. | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 검색·생활

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [카카오톡 채널 API](https://developers.kakao.com/docs/latest/ko/kakaotalk-channel/common) | 카카오 | 카카오톡 채널 추가/친구 관계 조회, 채널 기반 메시지·소셜 연동. | OAuth/API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 과학·통계

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KOSIS 국가통계포털 공유서비스](https://kosis.kr/openapi/) | 통계청 | 국가통계 자료를 조회하는 오픈 API. | API Key | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 기타

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [네이버 캡차(CAPTCHA) API](https://developers.naver.com/docs/utils/captcha/) | 네이버 | 자동입력 방지용 이미지/음성 보안문자 생성 및 입력값 검증. | API Key(Client ID/Secret) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 산업·고용

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [에어브릿지 API](https://help.airbridge.io/ko/references/introduction) | 에어브릿지 | 모바일 앱 마케팅 어트리뷰션 | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 쇼핑

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [네이버 쇼핑 검색 API](https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md) | 네이버 | 쇼핑 상품 검색(네이버 검색 API의 쇼핑 분야). | API Key(Client ID/Secret) | free | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 클라우드

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KT Cloud API](https://cloud.kt.com/) | KT클라우드 | 공공·금융·제조 특화 클라우드 API | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

### 통신

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 |
|-----|----------|------|------|------|:----:|
| [KT API Link](https://apilink.kt.co.kr/) | KT | Geo Master·Cloud·GiGA Genie AI 등 KT API | API Key | free-tier | ✅ |

<sub>[⬆ 맨 위로](#목차)</sub>

## 부록 A: data.go.kr 오픈 API 전수

위 큐레이션과 별개로, 공공데이터포털 **목록조회 API(15077093)** 로 오픈 API 목록을 **전수 수집**했습니다. 기계 판독용 전체 목록은 [`data/datago_apis.json`](data/datago_apis.json) 에 있습니다.

- 수집일: **2026-05-29** · 무료 오픈 API 서비스: **12,073** (operation 단위 원천 행 **17,305**, 순수 유료 제외 1)
- 신선도: 수집된 목록은 **현재 활성(is_deleted=N)** 항목만 포함하며, 최근 등록·갱신분(2025–2026년 등록 다수)까지 반영됩니다.

| 분야(공공데이터포털 분류) | 개수 |
|------|------:|
| 공공행정 | 1,668 |
| 문화관광 | 1,297 |
| 농축수산 | 1,282 |
| 교통물류 | 1,269 |
| 산업고용 | 901 |
| 사회복지 | 864 |
| 환경기상 | 820 |
| 식품건강 | 712 |
| 재정금융 | 635 |
| 재난안전 | 624 |
| 보건의료 | 553 |
| 국토관리 | 544 |
| 교육 | 417 |
| 과학기술 | 276 |
| 통일외교안보 | 186 |
| 법률 | 25 |

> 전체 12,000여 건은 README 표에 모두 싣지 않고 JSON으로만 제공합니다(가독성·용량). 분야별 핵심 API는 위 큐레이션 섹션을 참고하세요.

<sub>[⬆ 맨 위로](#목차)</sub>

## 한계 및 주의

- 이 카탈로그는 두 층위: (1) 전 분야 대표 무료 API 큐레이션(README 본문), (2) data.go.kr 오픈 API 전수 12,073건(부록 A, data/datago_apis.json).
- data.go.kr 전수는 공식 목록조회 API(15077093)로 수집 완료 — 현재 활성(is_deleted=N) 항목만 포함, 2025~2026 등록분까지 반영. 재현 절차는 docs/ENUMERATION.md 참고.
- 민간(네이버·카카오·토스·업비트 등) 무료 API는 집계처가 없어 '전수'가 아니라 '대표 큐레이션'이다.
- 시점 스냅샷(2026-05) — 신규 추가/폐기로 시간이 지나면 낡음. 일부 항목은 폐기·대체 안내가 있어 note에 표기.
- 일부 docs_url은 포털 루트만 확보 — 정확한 딥링크는 note에 표기하거나 '(미확인)'.
- GitHub 모음 2차 교차검증(dl0312/open-apis-korea, 711행): 신규+생존+무료+한국제공은 3건(카카오내비·카카오톡채널·네이버캡차)뿐. 나머지는 해외 API(범위 밖)·기보유·폐기(카카오 비전/번역/음성 2022종료, 카카오스토리 2023종료, 네이버 me2.do 2024종료). 즉 공개 모음들은 상당수 폐기 항목을 포함하므로 그대로 신뢰 불가.
- 주제별 커버리지 점검(노래/화장실/공공장소/식당) 중 큐레이션 본문에 화장실·식당 '간판'이 비어 있던 공백을 보완: 전국공중화장실 표준데이터, LOCALDATA(음식점 인허가), 전국공공시설개방정보 표준데이터 추가. data.go.kr 전수(부록 A)에는 이미 다수 존재했으나 대표 API를 본문으로 끌어올림.
- 주제 점검(의약품·위생/유해성분)에서 의약품(e약은요·DUR)·식품안전은 충분했으나 '생활화학제품 유해성분/회수' 간판이 비어 초록누리 OpenAPI 추가. 식품·의약품 회수·판매중단은 기존 식품안전나라 API에 포함.
- 주제 점검(금융·엔터): 금융은 충실했으나 '금융상품 비교(예적금/대출/연금 금리)' 간판이 비어 금융감독원 금융상품한눈에 API 추가. 엔터는 공공(영화/공연/게임/등급위 등)은 충실하나 민간 음원·웹툰·OTT·티켓예매·프로스포츠는 공식 공개 API가 부재하여 미수록(카탈로그 공백이 아닌 실제 부재).
- 특이 주제 점검(천문·헌혈·실종·지진·장례 등): 헌혈(적십자)·실종경보(경찰청)·지진(기상청)·장사시설(e하늘) 간판을 추가. 천문(KASI 음양력·특일)·북한(통일부 북한정보포털)·해양조석(바다누리)은 이미 존재. 일부 docs_url은 list_id 미확정으로 포털/운영 사이트 루트를 기재(note에 명시).
- 특이 주제 '공백만' 집중 점검(큐레이션 0건이던 폭염쉼터·민방위대피소·기상특보·예방접종·유실물·무장애여행)에서 6종 추가. URL은 전수(datago)에서 실제 list_id 확인. 독도는 지명 오탐(전용 API 없음), 국립공원 탐방로 전용 API는 본 환경에서 list_id 미확정으로 보류, 반려동물동반은 지자체 단위만 존재해 간판 보류.
- 특이 주제 점검(사투리/방언): data.go.kr 자동수집으로는 방언 전용 API가 잡히지 않았으나(키워드 오탐만), 국립국어원 '지역어 종합정보' 전용 오픈API와 AI허브 방언 발화 데이터(다운로드형)가 실재하여 추가. AI허브는 호출형 API가 아닌 데이터셋이므로 note에 명시.
- K-문화 주제 공백 점검(무형유산·전통문양·세시풍속·한옥/사찰·한지 등 큐레이션 0건이던 것): 국가유산청 국가유산포털을 분야 대표 간판으로, 국립무형유산원·국립민속박물관·국립문화유산연구원·한국문화정보원 전용 API를 추가(URL은 datago 전수에서 확인). 한복/족보/서예는 전국 단위 간판 API 부재로 보류(국가유산포털·우리말샘으로 일부 대체 가능).
- K-콘텐츠 산업 공백 점검(게임산업·한류·영화인 등): 게임물 등급분류(GRAC)·한류현황(KF)·영화인 DB(KOFIC) 추가(URL은 datago 전수 확인). 전통주·애니메이션·웹소설·콘텐츠펀드·관광통역은 전국 단위 간판 API 부재(지자체/채용/면세유 오탐만)로 보류. K-푸드 수출은 기보유 관세청 UNIPASS로 커버.
- 산업/인프라 24개 주제 점검: 대부분 충실(기상·통계·재난·교통·국방 등 두 자리수 보유). 진짜 공백은 항공기상뿐이라 기상청 항공기상청 API 추가. '동네예보/단기예보'는 기존 '기상청 API 허브'(단기/중기예보 포함)로 이미 커버되어 별도 미추가.
