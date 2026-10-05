# CV source

`build.py` writes the three CV variants as HTML (social media, event, general);
`render.mjs` prints them to one-page A4 PDFs with Playwright.

```sh
cd cv-source
python3 build.py
node render.mjs CV_Ahmad_Fajri_Social_Media CV_Ahmad_Fajri_Event CV_Ahmad_Fajri
cp CV_Ahmad_Fajri.pdf ../resume.pdf   # the copy linked from the site
```
