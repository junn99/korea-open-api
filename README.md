# Korea Free Open API Catalog

한국에서 제공되는 무료 오픈 API 카탈로그. GOAL.md 기준(무료 한정, 회원가입/승인 허용, 전 분야 포괄)에 따라 수집.

> 자동 생성 파일입니다. 원본은 `data/korea-open-apis.json` 이며 `python3 scripts/build_readme.py` 로 재생성합니다. 직접 수정하지 마세요.

- 생성일: **2026-05-28** · 버전: **0.3.0**
- 총 API 수: **135** · 분야 수: **26**
- 요금: free **127** / free-tier **8** · 회원가입·승인 필요: **133**

## 분야별 분포

| 분야 | 개수 |
|------|------|
| 금융 | 13 |
| 공공·행정 | 12 |
| 교통 | 12 |
| 생활·소셜 | 12 |
| 교육·학술 | 11 |
| 문화·관광·체육 | 9 |
| 콘텐츠·미디어 | 8 |
| 날씨·환경 | 7 |
| 보건·식품 | 7 |
| 농축수산 | 5 |
| 지도·위치 | 5 |
| 에너지 | 4 |
| 검색 | 3 |
| 부동산 | 3 |
| 인공지능 | 3 |
| 재난·안전 | 3 |
| 채용·고용 | 3 |
| 과학기술·특허 | 2 |
| 무역·통상 | 2 |
| 법령·사법 | 2 |
| 상권·창업 | 2 |
| 언어·사전 | 2 |
| 통신·인터넷 | 2 |
| 게임 | 1 |
| 과학·통계 | 1 |
| 쇼핑 | 1 |

## 분야별 API 목록

### 금융

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 한국은행 경제통계시스템(ECOS) Open API | 한국은행 | 금리·환율·국민계정 등 경제통계 조회 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://ecos.bok.or.kr/api/) |
| 오픈뱅킹 공동업무 API | 금융결제원(KFTC) | 계좌조회·이체 등 은행 공동 오픈뱅킹 API. | OAuth 2.0 | free | 필요 | REST(JSON) | [link](https://openapi.kftc.or.kr/) |
| OpenDART 전자공시 API | 금융감독원 | 상장·외부감사 기업의 전자공시(사업보고서, 재무제표 등) 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://opendart.fss.or.kr/) |
| 한국수출입은행 환율 Open API | 한국수출입은행 | 현재/대출 환율 등 환율정보 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://www.koreaexim.go.kr) |
| KRX OPEN API | 한국거래소(KRX) | 주식·채권·파생·지수 등 거래소 시장정보 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://openapi.krx.co.kr/) |
| 한국예탁결제원(SEIBro) Open API | 한국예탁결제원 | 주식·기업·증권 발행정보 등 예탁결제 데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://api.seibro.or.kr/pubc/pubr/cmm/CMPubrHome/viewCMPubrHome.do) |
| 금융위원회 주식시세정보 API | 금융위원회 | 상장 주식의 시가·종가·거래량 등 시세 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15094808/openapi.do) |
| 한국투자증권 KIS Developers Open API | 한국투자증권 | 주식/선물 시세 조회 및 주문·자동매매 REST/WebSocket 트레이딩 API. | API Key(App Key/Secret) + OAuth | free | 필요 | REST/WebSocket(JSON) | [link](https://apiportal.koreainvestment.com/intro) |
| 키움증권 Open API+ | 키움증권 | 주식 시세·주문 등 트레이딩 API. | 계정 인증 | free | 필요 | OCX/COM(Windows), REST(신규) | [link](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView) |
| 업비트(Upbit) Open API | 업비트(두나무) | 가상자산 시세(캔들·현재가·호가·체결), 잔고·주문·출금 등 거래소 API. | 없음(시세) / API Key(거래) | free | 불필요 | REST/WebSocket(JSON) | [link](https://docs.upbit.com/kr/docs/developer-center-overview) |
| 토스페이먼츠 결제 API | 토스페이먼츠 | 카드·간편결제(네이버페이/카카오페이 등) 통합 결제 연동 API. | API Key(시크릿/클라이언트 키) | free-tier | 필요 | REST(JSON) | [link](https://docs.tosspayments.com/) |
| 포트원(PortOne, 구 아임포트) 결제연동 API | 포트원(코리아포트원) | 여러 PG·간편결제를 단일 연동으로 통합 처리하는 결제 연동 API. | API Key | free-tier | 필요 | REST(JSON) | [link](https://developers.portone.io/) |
| 우체국금융(예금·보험) Open API | 우정사업본부 | 우체국 예금상품, 보험상품, 공시이율, 보험료 조회 등 우체국금융 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.epostlife.go.kr/IPUIOP0000.do) |

### 공공·행정

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 공공데이터포털 (Public Data Portal) | 행정안전부 / 한국지능정보사회진흥원(NIA) | 국가 공공데이터를 데이터셋·오픈API로 개방하는 중앙 플랫폼. 수만 건의 오픈API 보유. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |
| 공공데이터포털 목록조회서비스 | 공공데이터활용지원센터 | 공공데이터포털에 등록된 데이터/오픈API 목록을 조회하는 메타 API. 전수 수집의 진입점. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15077093/openapi.do) |
| 정부24 OpenAPI | 행정안전부 | 정부 민원·공공서비스 관련 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.gov.kr/openapi) |
| 서울 열린데이터광장 | 서울특별시 | 서울시 행정·교통·환경·생활 등 데이터를 오픈API로 제공하는 지자체 포털. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.seoul.go.kr) |
| 국세청 사업자등록정보 진위확인·상태조회 API | 국세청 | 사업자등록번호 진위확인 및 휴·폐업 상태조회 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://www.data.go.kr/data/15081808/openapi.do) |
| 경기데이터드림 Open API | 경기도 | 경기도 보유 공공데이터 오픈 API 포털(지자체). | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.gg.go.kr/portal/intro/develop/searchBulletinPage.do) |
| 조달청 나라장터 입찰공고·낙찰 정보 API | 조달청 | 입찰공고, 낙찰정보, 계약현황, 발주계획 등 공공조달 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15129394/openapi.do) |
| 중앙선거관리위원회 선거정보 API | 중앙선거관리위원회 | 투·개표 결과, 당선인, 사전투표, 선거코드 등 선거 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15000900/openapi.do) |
| 병무청 오픈 API | 병무청 | 병무행정(병역판정, 사회복무, 입영 등) 관련 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://open.mma.go.kr/caisGGGS/ggda/openApiList.do?menu_id=mma0000037) |
| 통일부 북한정보포털 통합검색 API | 통일부 | 북한 정치·경제·군사·사회·교육문화 등 북한정보 통합검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15079225/openapi.do) |
| 행정표준코드 법정동코드 API | 행정안전부 | 법정동코드·행정표준코드 조회 오픈 API. 주소/지역 기반 서비스의 기초 코드. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15077871/openapi.do) |
| 지방재정365 재정정보 API | 행정안전부 | 지방자치단체 재정자립도·세입세출 등 지방재정 통합공개 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15058102/openapi.do) |

### 교통

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| TMAP API | SK텔레콤 | 경로안내, 대중교통, 보행자 길찾기, POI 검색 등. | API Key(App Key) | free-tier | 필요 | REST(JSON) | [link](https://tmapapi.sktelecom.com/) |
| 국가대중교통정보(TAGO) | 국토교통부 | 전국 버스 도착정보, 노선, 정류소, 지하철 등 대중교통 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |
| 서울 버스정보 Open API | 서울특별시 / 서울교통정보과(TOPIS) | 서울 버스 도착정보, 노선/정류소 정보. | API Key | free | 필요 | REST(XML/JSON) | [link](http://api.bus.go.kr/) |
| ITS 국가교통정보센터 오픈데이터 | 국토교통부 ITS | 실시간 소통정보, 돌발정보, CCTV 등 도로교통 오픈 API. | API Key | free | 필요 | REST(XML/JSON) | [link](https://www.its.go.kr/opendata/) |
| 한국교통안전공단 자동차종합정보 API | 한국교통안전공단(TS) | 자동차 신규등록·검사 등 자동차 통계/정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15059401/openapi.do) |
| 고속도로 공공데이터 포털 Open API | 한국도로공사 | 실시간 고속도로 교통량·소통·휴게소·통행료 등 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.ex.co.kr/openapi/intro/introduce01) |
| 레일포털(철도산업정보센터) Open API | 국토교통부 / 한국철도기술연구원(KRIC) | 철도 노선·역사·운행 등 철도산업 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.kric.go.kr/rips/serviceInfo/openapi/introduce.do) |
| 한국공항공사 항공기 운항정보 API | 한국공항공사(KAC) | 국내/국제선 운항 스케줄, 실시간 운항정보, 공항코드 등 항공 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15000126/openapi.do) |
| 인천국제공항 Open API | 인천국제공항공사 | 인천공항 출도착 운항현황, 주차장, 혼잡도 등 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](http://openapi.airport.kr/) |
| 해양수산부 선박운항정보(PORT-MIS) API | 해양수산부 | 선박 입출항 시간, 선박 제원, 항만 관제 등 해운항만 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15006353/openapi.do) |
| 서울 따릉이 공공자전거 실시간 대여정보 API | 서울특별시 | 대여소별 실시간 거치 자전거 수, 거치율, 대여소 위치 등 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.seoul.go.kr/dataList/OA-15493/A/1/datasetView.do) |
| 도로교통공단 TAAS 교통사고분석 Open API | 한국도로교통공단(KOROAD) | 교통사고 다발지(13종), 교통안전정보(3종) 등 교통사고 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://opendata.koroad.or.kr/) |

### 생활·소셜

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 카카오톡 메시지/소셜 API | 카카오 | 카카오 로그인, 메시지 전송, 카카오톡 채널, 프로필 등. | OAuth 2.0 | free | 필요 | REST(JSON) | [link](https://developers.kakao.com/docs/latest/ko/kakaologin/common) |
| 네이버 로그인 / 회원 API | 네이버 | 네이버 아이디 로그인(OAuth) 및 회원 프로필 조회. | OAuth 2.0 | free | 필요 | REST(JSON) | [link](https://developers.naver.com/docs/login/api/api.md) |
| 우정사업본부 Open API | 우정사업본부(우정청) | 우편번호, 우편물 추적, 우체국 위치 등 우편 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.koreapost.go.kr/user/extra/kpost/330/bbs/openApi/openApiSet/jsp/ExtraUser.do) |
| 한국천문연구원 음양력·특일 정보 API | 한국천문연구원(KASI) | 음력/양력 변환, 공휴일·국경일·24절기, 일출·일몰 등 천문/달력 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.data.go.kr/data/15012679/openapi.do) |
| 국가동물보호정보시스템 구조(유기)동물 조회 API | 농림축산식품부 농림축산검역본부 | 전국 유기·구조동물, 보호소, 동물등록 현황 등 동물보호 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15098931/openapi.do) |
| 동행복권 로또 6/45 당첨번호 조회 (비공식) | 동행복권 | 회차별 로또 당첨번호·당첨금 조회. 공식 문서 없는 내부 엔드포인트. | 없음 | free | 불필요 | REST(JSON) | [link](https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1) |
| 전국무료와이파이 표준데이터 API | 행정안전부 / 한국지능정보사회진흥원 | 전국 무료 와이파이 설치장소, SSID, 좌표 등 표준데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15013116/standard.do) |
| 복지로 복지서비스 Open API | 보건복지부 / 한국사회보장정보원 | 중앙부처·지자체 복지서비스 목록·상세 등 복지정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15090532/openapi.do) |
| 공유누리 Open API | 행정안전부 | 공공시설·자원(회의실·체육시설·주차장 등) 개방·예약 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.eshare.go.kr/OpenApi/Info/index.do) |
| 국방부 군 부대 식단 정보 API | 국방부 | 부대별 일자별 조·중·석식 메뉴 및 칼로리 등 군 급식 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15056563/openapi.do) |
| 외교부 해외안전여행 여행경보 API | 외교부 | 국가·지역별 여행경보, 특별여행경보, 여행금지 등 해외안전여행 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15076237/openapi.do) |
| 온통청년 청년정책 API | 한국고용정보원 | 중앙·지자체 청년정책, 청년센터 등 청년 지원정보 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.data.go.kr/data/15143273/openapi.do) |

### 교육·학술

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 도서관 정보나루 Open API | 문화체육관광부 / 국립중앙도서관 | 전국 도서관 대출·소장·인기도서 등 도서관 빅데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data4library.kr/apiUtilization) |
| NEIS 교육정보 개방 포털 Open API | 한국교육학술정보원(KERIS) | 전국 학교 기본정보, 급식, 시간표, 학사일정 등 교육 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://open.neis.go.kr/) |
| 국립중앙도서관 Open API | 국립중앙도서관 | 서지정보 검색, LOD, 전거데이터 등 도서/서지 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.nl.go.kr) |
| 커리어넷 진로·직업정보 Open API | 교육부 / 한국직업능력연구원 | 직업정보, 학과정보, 진로심리검사, 진로상담 등 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.career.go.kr/cnet/front/openapi/jobCenter.do) |
| KCI 한국학술지인용색인 논문정보 API | 한국연구재단 | 국내 학술지·논문 서지정보, 인용/피인용 등 학술 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15085348/openapi.do) |
| ScienceON Open API | 한국과학기술정보연구원(KISTI) | 논문·특허·보고서·연구자 등 과학기술 지식 통합검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://scienceon.kisti.re.kr/por/oapi/openApi.do) |
| 학교알리미 Open API | 교육부 / 한국교육학술정보원 | 전국 초·중·고 학교 기본정보 및 공시정보 오픈 API. | API Key(네이버/카카오 로그인) | free | 필요 | REST(JSON/XML) | [link](https://www.schoolinfo.go.kr/ng/go/pnnggo_a01_l0.do) |
| 유치원알리미 공시정보 API | 교육부 / 한국교육학술정보원 | 전국 유치원 기본정보, 급식, 예산, 교육과정 등 공시 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15020786/openapi.do) |
| 어린이집정보공개포털 보육정보 API | 보건복지부 / 한국사회보장정보원 | 전국 어린이집 위치·정원·평가 등 보육시설 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://info.childcare.go.kr/info_html5/oais/openapi/OpenApiSlL.jsp) |
| 국가기록원 나라기록물정보 서비스 API | 행정안전부 국가기록원 | 국가 기록물 메타데이터(제목·생산기관·관리번호 등) 검색 오픈 API. | API Key | free | 필요 | REST(RSS/XML) | [link](https://www.data.go.kr/data/15000153/openapi.do) |
| 대학알리미 대학정보공시 API | 한국대학교육협의회 | 전국 대학 기본정보, 학과, 등록금, 장학금 등 대학 공시정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15037507/openapi.do) |

### 문화·관광·체육

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 한국관광공사 TourAPI | 한국관광공사 | 관광지·숙박·축제·문화시설·여행코스·이미지 등 관광 콘텐츠 오픈 API(15종, 약 26만 건). | API Key | free | 필요 | REST(JSON/XML) | [link](https://api.visitkorea.or.kr/) |
| 공연예술통합전산망(KOPIS) Open API | 예술경영지원센터 | 공연 목록·상세·예매상황 등 공연예술 통계/정보 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.kopis.or.kr/por/cs/openapi/openApiList.do) |
| 문화공공데이터광장(문화포털) Open API | 한국문화정보원 | 문화·예술·관광·도서 등 문화 분야 공공데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.culture.go.kr/data/) |
| 고캠핑(GoCamping) 캠핑장 정보 API | 한국관광공사 | 전국 등록 야영장(캠핑장) 위치·시설·안전정보 등 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15101933/openapi.do) |
| 해양수산부 해수욕장정보 서비스 API | 해양수산부 | 전국 해수욕장 위치·제원·비상연락처·이미지 등 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15058519/openapi.do) |
| 산림청 산·등산로·식물 정보 API | 산림청 | 전국 산 정보, 등산로, 숲에 사는 식물, 수목 이미지 등 산림 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15058682/openapi.do) |
| 국립중앙박물관 e뮤지엄 유물정보 API | 문화체육관광부 / 국립중앙박물관 | 전국 박물관 소장품(유물) 명칭·시대·재질·이미지 등 통합검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15104964/openapi.do) |
| 국민체육진흥공단 공공체육시설 정보 API | 서울올림픽기념국민체육진흥공단 | 전국 공공체육시설 위치·규모·운영상태 등 체육시설 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15107764/openapi.do) |
| 한국관광공사 두루누비(코리아둘레길) 정보 API | 한국관광공사 | 코리아둘레길 284개 코스 GPX·걷기여행길·자전거길 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15101974/openapi.do) |

### 콘텐츠·미디어

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KOBIS 영화관입장권통합전산망 Open API | 영화진흥위원회(KOFIC) | 일별/주간 박스오피스, 영화/영화인/영화사 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do) |
| KMDb 한국영화데이터베이스 Open API | 한국영상자료원 | 영화 상세정보(스태프/줄거리/스틸 등) 검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kmdb.or.kr/info/api/apiList) |
| 알라딘 상품 검색 Open API | 알라딘(Aladin) | 도서 상품 검색/조회/베스트셀러 등 도서 정보 오픈 API. | API Key(TTBKey) | free | 필요 | REST(JSON/XML) | [link](https://www.aladin.co.kr/ttb/apiguide.aspx) |
| 빅카인즈(BIGKINDS) 뉴스 빅데이터 API | 한국언론진흥재단 | 뉴스 기사 검색, 메타데이터, 개체명·토픽 분석 등 뉴스 빅데이터 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://www.bigkinds.or.kr/) |
| 한국콘텐츠진흥원(KOCCA) Open API | 한국콘텐츠진흥원 | 방송·게임·만화·음악 등 콘텐츠 산업 통계·정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kocca.kr/kocca/subPage.do?menuNo=204795) |
| 영상물등급위원회 등급분류정보 API | 영상물등급위원회 | 비디오물 등급분류 정보(제명·감독·관람등급·내용정보) 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15127675/openapi.do) |
| 한국저작권위원회 공유마당 API | 한국저작권위원회 | CCL/만료저작물 등 자유이용 저작물(사진·음악·미술·어문 등) 검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://gongu.copyright.or.kr/gongu/useReqst/apiKey/info.do?menuNo=200245) |
| 국립국악원 국악 디지털음원 API | 문화체육관광부 국립국악원 | 국악 디지털 음원·아카이브(음향·영상·이미지) 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15097515/openapi.do) |

### 날씨·환경

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 기상청 API 허브 | 기상청 | 단기/중기예보, 실황, 지상/해양 관측 등 기상 데이터 오픈 API 통합 허브. | API Key | free | 필요 | REST(JSON/XML/텍스트) | [link](https://apihub.kma.go.kr) |
| 에어코리아 대기오염정보 API | 한국환경공단 | 미세먼지·대기질 실시간 측정정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15073861/openapi.do) |
| 한국환경공단 전기차 충전소 정보 API | 한국환경공단 | 전국 전기차 충전소 위치·상태 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15076352/openapi.do) |
| 바다누리 해양정보 서비스 Open API | 국립해양조사원 | 조위·조류·수온 등 해양 관측/예측 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](http://www.khoa.go.kr/oceangrid/khoa/takepart/openapi/openApiDeveloperGuide.do) |
| K-water 공공데이터 개방포털 Open API | 한국수자원공사(K-water) | 댐·보 수문정보(수위·강우·방류량 등), 수자원 데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://opendata.kwater.or.kr/) |
| 환경부 화학물질정보 API | 환경부 화학물질안전원 | 화학물질 명칭·CAS번호·분자식·분류 등 화학물질 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15029194/openapi.do) |
| 국립생물자원관 한반도 생물다양성 API | 환경부 국립생물자원관 | 국가생물종목록, 생물다양성, 종별 멀티미디어 등 생태 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://species.nibr.go.kr/) |

### 보건·식품

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 식품안전나라 Open API | 식품의약품안전처 | 식품·의약품·건강기능식품 정보, 회수/판매중지 등 식의약 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.foodsafetykorea.go.kr/api/) |
| 건강보험심사평가원(HIRA) 공공 API | 건강보험심사평가원 | 병원·약국 정보, 의약품, 비급여 진료비 등 보건의료 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |
| E-Gen 중앙응급의료센터 Open API | 국립중앙의료원 중앙응급의료센터 | 실시간 응급실 가용병상, 응급의료기관, 외상센터 등 응급의료 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.e-gen.or.kr/nemc/open_api.do) |
| 국가건강정보포털 Open API | 질병관리청 | 질병·건강정보 콘텐츠 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://health.kdca.go.kr/healthinfo/biz/health/portalUseGuidance/openApiReqst/openApiReqstRegist.do) |
| 국민건강보험공단 검진기관 정보 API | 국민건강보험공단 | 건강검진기관 위치·검진종류 등 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15001672/openapi.do) |
| 식약처 의약품개요정보(e약은요) API | 식품의약품안전처 | 일반·전문 의약품의 효능·용법·주의사항·상호작용 등 개요 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15075057/openapi.do) |
| 식약처 의약품안전사용서비스(DUR) API | 식품의약품안전처 | 병용금기, 연령·임부 금기, 중복효능 등 의약품 안전사용(DUR) 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15059486/openapi.do) |

### 농축수산

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KAMIS 농수산물유통정보 Open API | 한국농수산식품유통공사(aT) | 농수산물 도·소매 가격, 거래동향 등 17종 유통정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kamis.or.kr/customer/reference/openapi_list.do) |
| 농사로 Open API | 농촌진흥청 | 농업기술·작물·병해충 등 농업정보 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.nongsaro.go.kr/portal/ps/psz/psza/contentMain.ps?menuId=PS00191) |
| 농림축산식품 공공데이터 포털 | 농림축산식품부 | 농림축산식품 분야 데이터·오픈API를 제공하는 부처 포털. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.mafra.go.kr/) |
| 축산물이력제 Open API | 농림축산식품부 / 축산물품질평가원 | 소·돼지 등 축산물 이력정보(개체식별번호) 조회 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://mtrace.go.kr/openService.jsp) |
| 스마트팜코리아 Open API | 농림수산식품교육문화정보원(EPIS) | 스마트팜 시설원예·노지 빅데이터(환경·생육·제어) 등 농업 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://data.smartfarmkorea.net/openApi/openApiUseInfo.do) |

### 지도·위치

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| SGIS 통계지리정보서비스 | 통계청 | 통계 기반 지리정보(인구·사업체·경계 등) 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://sgis.kostat.go.kr/developer/) |
| VWorld(브이월드) 오픈 API | 국토교통부 / 국토지리정보원 | 2D/3D 지도, 배경지도, 공간정보(WMS/WFS), 지오코더 등 공간정보 오픈 API. | API Key | free | 필요 | REST/OGC(JSON/XML) | [link](https://www.vworld.kr/dev/v4api.do) |
| 카카오맵 / 로컬 API | 카카오 | 지도 표시, 장소 검색, 주소-좌표 변환(지오코딩) 등. | API Key(REST/JavaScript) | free | 필요 | REST(JSON) | [link](https://developers.kakao.com/docs/latest/ko/local/dev-guide) |
| 네이버 지도(Maps) API | 네이버클라우드플랫폼(NCP) | 지도, 길찾기(Directions), 지오코딩 등. | API Key(Client ID/Secret) | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/applicationService/maps) |
| 도로명주소 API | 행정안전부 | 도로명주소 검색, 영문주소, 좌표제공 등 주소 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://business.juso.go.kr/addrlink/openApi/apiExprn.do) |

### 에너지

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 한국전력 전력데이터 개방포털 Open API | 한국전력공사(KEPCO) | 지역별 전력사용량, 계약종별, 발전원 등 전력 데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://bigdata.kepco.co.kr/) |
| 전력거래소(KPX) 공공데이터 API | 한국전력거래소(KPX) | 전력 수급, SMP, 발전량 등 전력시장 데이터 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.kpx.or.kr/menu.es?mid=a10107020000) |
| 한국에너지공단 신재생에너지 Open API | 한국에너지공단 | 신재생에너지 보급·설비 등 에너지 통계/정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.energy.or.kr/web/kem_home_new/data_offer/OPEN_API_3.asp) |
| 한국가스공사 도시가스 공급열량 API | 한국가스공사 | 도시가스 공급예상열량·공급열량실적 등 가스 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15138871/openapi.do) |

### 검색

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 네이버 검색 API | 네이버 | 뉴스·블로그·책·백과사전·이미지·웹·쇼핑·지역 등 통합검색 오픈 API. | API Key(Client ID/Secret) | free | 필요 | REST(JSON/XML) | [link](https://developers.naver.com/docs/serviceapi/search/news/news.md) |
| 네이버 데이터랩(DataLab) API | 네이버 | 검색어 트렌드, 쇼핑인사이트 등 트렌드 데이터 오픈 API. | API Key(Client ID/Secret) | free | 필요 | REST(JSON) | [link](https://developers.naver.com/docs/serviceapi/datalab/search/search.md) |
| 카카오 검색(다음) API | 카카오 | 웹/동영상/이미지/블로그/책/카페 등 다음 검색 오픈 API. | API Key(REST) | free | 필요 | REST(JSON) | [link](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide) |

### 부동산

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 국토교통부 실거래가 공개시스템 API | 국토교통부 | 아파트/연립/단독 등 부동산 매매·전월세 실거래가 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://www.data.go.kr) |
| 한국부동산원 R-ONE 부동산통계 Open API | 한국부동산원 | 지가·주택가격지수·거래량 등 부동산 통계 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.reb.or.kr/r-one/portal/openapi/openApiIntroPage.do) |
| 국토교통부 개별공시지가·공동주택가격 API | 국토교통부 | 개별공시지가, 공동주택가격(WMS/WFS/속성) 등 부동산 공시가격 오픈 API. | API Key | free | 필요 | REST/OGC(JSON/XML) | [link](https://www.data.go.kr/data/15124014/openapi.do) |

### 인공지능

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| ETRI 공공 인공지능 Open API | 한국전자통신연구원(ETRI) | 한국어 형태소분석, 질의응답, 음성인식, OCR 등 AI 오픈 API. | API Key | free | 필요 | REST(JSON) | [link](https://aiopen.etri.re.kr/) |
| 네이버 CLOVA AI API | 네이버클라우드플랫폼(NCP) | CLOVA OCR, Speech(STT/TTS), Face, CLOVA Studio(생성형) 등. | API Key | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/aiService) |
| 네이버 Papago 번역 API | 네이버클라우드플랫폼(NCP) | 기계 번역(Papago) 및 언어감지 API. | API Key | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/aiService/papagoTranslation) |

### 재난·안전

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 재난안전데이터 공유플랫폼 Open API | 행정안전부 | 재난·안전 분야 데이터를 통합 제공하는 플랫폼 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.safetydata.go.kr/) |
| 생활안전지도(SafeMap) Open API | 행정안전부 | 치안·교통·재난 등 생활안전 공간정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.safemap.go.kr/dvct/openAPI.do) |
| 소방청 구급정보 서비스 API | 소방청 | 구급·구급통계, 출동 등 119 구급 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15099423/openapi.do) |

### 채용·고용

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 고용24 / 고용노동부 일자리 API | 고용노동부 / 한국고용정보원 | 채용공고, 직업정보, 고용통계 등 일자리 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr) |
| 워크넷 Open API | 한국고용정보원 | 채용정보, 직업정보, 학과정보 등 고용 오픈 API. | API Key | free | 필요 | REST(XML) | [link](https://openapi.work.go.kr/opiMain.do) |
| 한국산업인력공단(큐넷) 국가자격 정보 API | 한국산업인력공단 | 국가기술자격 종목·시험일정·교부수수료 등 자격정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://openapi.hrdkorea.or.kr/main) |

### 과학기술·특허

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KIPRIS PLUS 특허정보 Open API | 한국특허정보원 / 특허청 | 특허·실용신안·디자인·상표 등 지식재산권 정보 오픈 API. | API Key | free-tier | 필요 | REST(XML) | [link](https://plus.kipris.or.kr/) |
| e나라표준인증 국가표준(KS) Open API | 산업통상자원부 국가기술표준원 | 한국산업표준(KS), 인증, 기술기준 등 표준·인증 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://standard.go.kr/KSCI/onlineSvc/openApiIntro.do) |

### 무역·통상

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 관세청 수출입무역통계(UNIPASS) Open API | 관세청 | 수출입 무역통계, 수출이행내역, 환율 등 관세·무역 오픈 API. | API Key | free | 필요 | REST(XML/JSON) | [link](https://unipass.customs.go.kr/ets/index.do?menuId=ETS_MNU_00000107) |
| KOTRA 해외시장뉴스 API | 대한무역투자진흥공사(KOTRA) | 국가별 해외시장 뉴스, 단신속보, 국가정보(GDP·인구·규제 등) 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15034831/openapi.do) |

### 법령·사법

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 국가법령정보 공동활용 API | 법제처 | 법령·행정규칙·자치법규·판례·헌재결정례 등 법령정보 오픈 API. | API Key(이메일 ID 기반) | free | 필요 | REST(XML/JSON/HTML) | [link](https://open.law.go.kr/LSO/openApi/guideList.do) |
| 열린국회정보 Open API | 국회사무처 | 의안, 의원, 표결, 회의록 등 국회 정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://open.assembly.go.kr/portal/openapi/main.do) |

### 상권·창업

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 소상공인시장진흥공단 상가(상권)정보 API | 소상공인시장진흥공단 | 전국 상가업소 상호·업종·좌표 등 상권정보 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15012005/openapi.do) |
| K-Startup 창업지원 정보 API | 창업진흥원 / 중소벤처기업부 | 창업지원 사업공고, 사업소개, 콘텐츠 등 창업 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15125364/openapi.do) |

### 언어·사전

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 표준국어대사전 Open API | 국립국어원 | 표준국어대사전 표제어·뜻풀이 검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://stdict.korean.go.kr/openapi/openApiInfo.do) |
| 우리말샘 개방형 사전 Open API | 국립국어원 | 신어·방언·북한어 등을 포함한 개방형 국어사전 검색 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://opendict.korean.go.kr/) |

### 통신·인터넷

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KISA WHOIS 인터넷주소 정보검색 API | 한국인터넷진흥원(KISA) | 도메인·IP·AS번호 등록/할당 정보 조회(WHOIS) 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://www.data.go.kr/data/15094277/openapi.do) |
| 네이버 클라우드 SENS(문자·알림톡) API | 네이버클라우드플랫폼(NCP) | SMS/LMS/MMS 문자 및 카카오 알림톡·친구톡 발송 메시징 API. | API Key | free-tier | 필요 | REST(JSON) | [link](https://www.ncloud.com/product/applicationService/sens) |

### 게임

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| NEXON Open API | 넥슨(NEXON) | 메이플스토리·던전앤파이터·FC온라인 등 13종 게임의 캐릭터·랭킹·전적 데이터 API. | API Key | free | 필요 | REST(JSON) | [link](https://openapi.nexon.com/ko/) |

### 과학·통계

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| KOSIS 국가통계포털 공유서비스 | 통계청 | 국가통계 자료를 조회하는 오픈 API. | API Key | free | 필요 | REST(JSON/XML) | [link](https://kosis.kr/openapi/) |

### 쇼핑

| API | 제공기관 | 설명 | 인증 | 요금 | 가입 | 포맷 | 문서 |
|-----|----------|------|------|------|------|------|------|
| 네이버 쇼핑 검색 API | 네이버 | 쇼핑 상품 검색(네이버 검색 API의 쇼핑 분야). | API Key(Client ID/Secret) | free | 필요 | REST(JSON/XML) | [link](https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md) |

## 한계 및 주의

- data.go.kr 전체(수만 건) 자동 전수 수집은 IP 차단으로 미수행 — 대표 API 위주 큐레이션.
- 민간 무료 API는 '전수'가 아니라 '대표 큐레이션'.
- 시점 스냅샷(2026-05) — 신규 추가/폐기로 시간이 지나면 낡음.
- 일부 docs_url은 포털 루트만 확보 — 정확한 딥링크는 note에 표기하거나 '(미확인)'.
