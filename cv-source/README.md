# CV source

`build.py` writes the three CV variants as HTML (social media, event, general);
`render.mjs` prints them to one-page A4 PDFs with Playwright.

```sh
cd cv-source
python3 build.py
node render.mjs CV_Ahmad_Fajri_Social_Media CV_Ahmad_Fajri_Event CV_Ahmad_Fajri
cp CV_Ahmad_Fajri.pdf ../resume.pdf   # the copy linked from the site
```

## Portfolio PDFs

`portfolio/` builds the landscape A4 portfolio in two versions: the general one and the Community Organizer one.

```
cd portfolio
ln -s <path-to>/node_modules node_modules   # needs playwright
python3 build.py && CHROMIUM=/path/to/chromium node render.mjs
```

The PDFs land in `portfolio/build/`, which git ignores.
