const puppeteer = require('puppeteer');
const path = require('path');

const FILE = 'file://' + path.resolve(__dirname, 'youth_survival.html');
const OUT = path.resolve(__dirname, 'shots');
require('fs').mkdirSync(OUT, {recursive:true});

const sleep = ms => new Promise(r=>setTimeout(r,ms));

(async ()=>{
  const browser = await puppeteer.launch({
    headless: 'new',
    args:['--no-sandbox','--disable-setuid-sandbox','--force-color-profile=srgb']
  });
  const page = await browser.newPage();
  await page.setViewport({width:420, height:880, deviceScaleFactor:2});

  async function shot(name){ await page.screenshot({path: path.join(OUT,name)}); console.log('  ✓', name); }

  // 1) 온보딩 Q1 (나이)
  await page.goto(FILE, {waitUntil:'networkidle0'});
  await sleep(400);
  await shot('01_onboard_age.png');

  // 나이 24 유지하고 다음 → Q2 지역 선택
  await page.click('#nextBtn');               // Q2
  await sleep(300);
  await page.click('#regionChips .chip[data-v="서울 관악구"]');
  await sleep(200);
  await shot('02_onboard_region.png');

  await page.click('#nextBtn');               // Q3 상태
  await sleep(300);
  await page.click('#statusOpts .opt[data-v="취업준비생"]');
  await sleep(200);
  await page.click('#nextBtn');               // Q4 소득
  await sleep(300);
  await page.click('#incomeOpts .opt[data-v="월 200만원 이하"]');
  await sleep(200);
  await page.click('#nextBtn');               // Q5 관심
  await sleep(300);
  await page.click('#interestChips .chip[data-v="주거"]');
  await page.click('#interestChips .chip[data-v="금융"]');
  await sleep(200);
  await shot('03_onboard_interest.png');

  // 내 정책 찾기 → 홈 레이더
  await page.click('#nextBtn');
  await sleep(500);
  await shot('04_home_radar.png');

  // 정책 카드 첫번째 클릭 → 상세 시트
  await page.click('#list .pcard');
  await sleep(450);
  await shot('05_detail_sheet.png');

  // 시트 닫고 → 마감임박 필터 + 푸시 토스트
  await page.click('#sheetBg');
  await sleep(250);
  await page.click('#pushBtn');
  await sleep(500);
  await shot('06_push_toast.png');

  await browser.close();
  console.log('완료. shots/ 폴더에 6장.');
})().catch(e=>{ console.error('ERR', e); process.exit(1); });
