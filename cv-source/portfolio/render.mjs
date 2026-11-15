// Print build/*.html to landscape A4 PDFs. Run after build.py.
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const names = ['Portfolio_Ahmad_Fajri', 'Portfolio_Ahmad_Fajri_Community'];
const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const p = await b.newPage();
for (const n of names) {
  await p.goto(pathToFileURL(path.resolve('build', n + '.html')).href, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.resolve('build', n + '.pdf'), width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  console.log(n);
}
await b.close();
