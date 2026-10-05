// Renders share/report.html -> PDF and share/infographic.html -> PNG with the preinstalled Chromium.
const path = require('path');
const { chromium } = require(process.env.PW_MODULE || 'playwright');
(async () => {
  const dir = path.join(__dirname, 'share');
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--allow-file-access-from-files'] });
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, 'report.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(dir, 'two_calendars_report.pdf'), format: 'Letter', printBackground: true,
    preferCSSPageSize: true });
  const q = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 2 });
  await q.goto('file://' + path.join(dir, 'infographic.html'));
  await q.evaluate(() => document.fonts.ready);
  await q.screenshot({ path: path.join(dir, 'two_calendars_infographic.png'), fullPage: true });
  await b.close();
})();
