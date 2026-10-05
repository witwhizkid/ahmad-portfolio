import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const files = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
for (const f of files) {
  await p.goto(pathToFileURL(path.resolve(f + '.html')).href, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const fonts = await p.evaluate(() => [...document.fonts].filter((x) => x.status === 'loaded').map((x) => x.family + ' ' + x.weight));
  await p.pdf({ path: f + '.pdf', format: 'A4', preferCSSPageSize: true, printBackground: true });
  console.log(f, 'fonts:', fonts.join(', '));
}
await b.close();
