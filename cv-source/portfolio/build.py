"""Build the landscape A4 portfolio PDFs (general and community organizer) as HTML; render.mjs prints them.

Run from this folder: python3 build.py && node render.mjs
Images come from ../../img, shrunk to JPEG in build/jpg so the PDFs stay small.
"""
import os
import subprocess

SITE = "https://ahmadfajriportfolio.vercel.app"
ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, "..", "..", "img")
OUT = os.path.join(ROOT, "build")

IMAGES = [
    "content/volunteer-call", "content/batch2-report", "content/soft-news", "content/recap-reel-poster",
    "content/feed-grid", "content/profile", "projects/kitabahagia-web", "projects/duta-ipb-video-poster",
    "projects/glukodiab-video-poster", "projects/assignment-video-poster", "projects/photo-edit-1",
    "projects/photo-edit-2", "gallery/dsc02453", "gallery/dsc04231", "gallery/dsc04303", "gallery/dscn0195",
    "gallery/dscn0046", "gallery/img0452",
]


def jpgs():
    for name in IMAGES:
        dst = os.path.join(OUT, "jpg", name + ".jpg")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst):
            subprocess.run(["convert", os.path.join(IMG, name + ".webp"), "-resize", "1200x1200>", "-quality", "80",
                            "-sampling-factor", "4:2:0", "-strip", dst], check=True)


CSS = open(os.path.join(ROOT, "fonts", "fonts.css")).read().replace("url(fonts/", "url(../fonts/") + r'''
@page{size:297mm 210mm;margin:0}
:root{--bg:#f4f6f1;--ink:#151b16;--muted:#5a645c;--line:#dde2da;--leaf:#386b3d;--leaf-soft:#e7efe5;--forest:#144724;--deep:#0c2614;--cream:#eef2ea;--sage:#a9bfa3;--lime:#b9d58a;
 --display:"Schibsted Grotesk",sans-serif;--body:"Source Sans 3",sans-serif;--cond:Anton,Impact,sans-serif}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{font:10.5pt/1.5 var(--body);color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
p{margin:0}h1,h2,h3,h4{margin:0;font-family:var(--display);letter-spacing:-.015em}
a{color:inherit;text-decoration:none}img{display:block}
.page{position:relative;width:297mm;height:210mm;overflow:hidden;background:var(--bg);page-break-after:always;padding:16mm 18mm 14mm}
.page:last-child{page-break-after:auto}
.folio{position:absolute;left:18mm;right:18mm;bottom:8mm;display:flex;justify-content:space-between;font-size:8pt;color:var(--muted)}
.dark{background:var(--deep);color:var(--cream)}
.dark .folio{color:var(--sage)}
.ambient{position:absolute;inset:0;z-index:0;background:
  radial-gradient(60% 75% at 8% 105%,rgba(56,107,61,.95),rgba(56,107,61,0) 70%),
  radial-gradient(45% 55% at 95% -5%,rgba(224,217,95,.38),rgba(224,217,95,0) 70%),
  radial-gradient(35% 45% at 60% 55%,rgba(137,175,63,.25),rgba(137,175,63,0) 70%),var(--deep)}
.z{position:relative;z-index:1}
.kicker{font-weight:600;color:var(--leaf);font-size:10pt}
.dark .kicker{color:var(--lime)}
.title{font:700 24pt/1.1 var(--display);letter-spacing:-.025em;margin-top:3mm}
.meta{color:var(--muted);font-size:9.5pt;margin-top:2mm}
.lead{font:600 15pt/1.3 var(--display);letter-spacing:-.015em}
ul{margin:0;padding-left:4.5mm}li{margin:1.2mm 0}li::marker{color:var(--muted)}
.result{margin-top:5mm;padding:4mm 5mm;background:var(--leaf-soft);border-radius:2mm;font-weight:600;color:var(--forest)}
.shot{border-radius:1.6mm;overflow:hidden;background:var(--line)}
.shot img{width:100%;height:100%;object-fit:cover}
.cap{margin-top:1.6mm;font-size:8.5pt;line-height:1.35;color:var(--muted)}
.cap b{display:block;color:var(--ink);font-weight:600;font-size:9pt}
.link{color:var(--leaf);font-weight:600;text-decoration:underline;text-underline-offset:2px}
.dark .link{color:var(--lime)}
.rel{position:relative}
.play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);padding:1.4mm 3.4mm;border-radius:5mm;background:rgba(21,27,22,.82);color:#fff;font-weight:600;font-size:8.5pt}

.cover{display:flex;flex-direction:column}
.cover .top{display:flex;justify-content:space-between;font-size:10pt}
.cover .top .r{color:var(--lime);font-weight:600}.cover .top .w{text-align:right;color:var(--sage)}
.name{margin:auto 0 0;font:400 132pt/.9 var(--cond);text-transform:uppercase;color:var(--cream)}
.name span{display:block}.name .l2{text-align:right}
.cover .values{position:absolute;left:18mm;bottom:28mm;max-width:62mm;font:600 13pt/1.3 var(--display)}
.cover .bottom{margin-top:6mm;padding-top:4mm;border-top:.3mm solid rgba(238,242,234,.18);display:flex;justify-content:space-between;font-size:9pt;color:var(--sage)}

.about{display:grid;grid-template-columns:1.1fr 1fr;gap:16mm;height:100%;align-content:center}
.status{display:inline-flex;gap:2mm;align-items:flex-start;margin-top:5mm;padding:1.6mm 4mm 1.6mm 3mm;background:var(--leaf-soft);border-radius:4mm;font-weight:600;color:var(--forest);font-size:9.5pt}
.status::before{content:"";flex:none;margin-top:1.6mm;width:2mm;height:2mm;border-radius:50%;background:var(--leaf)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;margin:12mm 0 0}
.stat{border-top:.6mm solid var(--forest);padding-top:3mm}
.stat dt{font:700 34pt/1 var(--display);letter-spacing:-.035em;color:var(--forest)}
.stat dd{margin:2mm 0 0;color:var(--muted);font-size:10pt;line-height:1.35}
.why{margin-top:12mm;padding-top:5mm;border-top:.3mm solid var(--line);font-size:11pt;color:var(--muted)}
.why b{color:var(--ink)}
.does h3{font-size:13pt;margin-top:7mm}.does h3:first-child{margin-top:0}
.does p{color:var(--muted);margin-top:1.6mm;font-size:11pt}

.case{display:grid;grid-template-columns:100mm 1fr;gap:12mm;height:100%}
.case .text p.desc{margin-top:4mm}
.case .text ul{margin-top:4mm}
.gpb{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;align-content:start}
.gpb .tall img{object-position:top}
.kb{display:grid;gap:4mm;align-content:start}
.kb .web{aspect-ratio:1328/830}
.kb .web img{object-position:top}

.numbers{display:grid;grid-template-columns:1fr 1fr;gap:6mm;align-content:center;padding:10mm;background:var(--deep);color:var(--cream);border-radius:3mm;position:relative;overflow:hidden}
.numbers .ambient{border-radius:3mm}
.numbers .n{position:relative;z-index:1;border-top:.5mm solid rgba(238,242,234,.3);padding-top:3mm}
.numbers dt{font:400 46pt/1 var(--cond);color:var(--cream)}
.numbers dd{margin:2mm 0 0;color:var(--sage);font-size:10pt;line-height:1.35}

.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm 6mm;margin-top:8mm}
.gal .shot{height:56mm}

.cv{display:grid;grid-template-columns:1.1fr 1fr;gap:12mm;margin-top:4mm}
.job{display:grid;grid-template-columns:30mm 1fr;gap:1mm 5mm;padding:1.6mm 0;border-bottom:.3mm solid var(--line);line-height:1.35}
.job:last-child{border-bottom:none}
.job .when{color:var(--muted);font-size:8.5pt;padding-top:.6mm}
.job h4{font-size:10.5pt}.job .org{color:var(--muted);font-size:8.5pt}.job .d{font-size:8.7pt;margin-top:.4mm}
.rows .row{display:grid;grid-template-columns:24mm 1fr auto;gap:1mm 4mm;padding:2.2mm 0;border-bottom:.3mm solid var(--line);font-size:9pt}
.rows .row:last-child{border-bottom:none}
.rows .k{font-weight:600}.rows .sub{color:var(--muted);font-size:8.5pt}.rows .when{color:var(--muted);font-size:8.5pt;white-space:nowrap}
.sh{font:700 13pt var(--display);margin:5mm 0 1mm}.sh:first-child{margin-top:0}

.contact{display:flex;flex-direction:column;height:100%}
.contact .big{margin-top:10mm;font:400 64pt/.95 var(--cond);text-transform:uppercase}
.contact .email{margin-top:10mm;font:600 26pt var(--display);letter-spacing:-.02em;color:var(--lime);text-decoration:underline;text-underline-offset:2mm;text-decoration-thickness:.5mm}
.contact .lines{margin-top:8mm;display:grid;grid-template-columns:30mm 1fr;gap:2.5mm 6mm;font-size:12pt}
.contact .lines dt{color:var(--sage)}.contact .lines dd{margin:0}

.fit{margin-top:7mm;display:grid}
.fit .r{display:grid;grid-template-columns:78mm 1fr;gap:10mm;padding:4.4mm 0;border-bottom:.3mm solid var(--line)}
.fit .r:last-child{border-bottom:none}
.fit .need{font:600 13pt/1.3 var(--display)}
.fit .need small{display:block;margin-top:1mm;font:400 9.5pt var(--body);color:var(--muted)}
.fit .have{font-size:11pt;line-height:1.45}
.fit .have b{color:var(--forest)}
.prog{display:grid;grid-template-columns:repeat(2,1fr);gap:6mm 12mm;margin-top:8mm}
.prog .p{border-top:.6mm solid var(--forest);padding-top:2.4mm}
.prog h4{font-size:13pt}.prog .o{color:var(--muted);font-size:9.5pt}.prog .d{font-size:11pt;margin-top:1.2mm}
.strip{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:10mm}
.strip .shot{height:58mm}
'''


def folio(n, label):
    return f'<div class="folio"><span>Ahmad Fajri · {label}</span><span>{n:02d}</span></div>'


def j(name):
    return f"jpg/{name}.jpg"


# ---------- shared facts ----------
JOBS = [
    ("Oct – Nov 2026", "Social Media &amp; Digital Marketing Intern", "52 Group (Hypr Caffeine &amp; Kazuhiro), Tangerang",
     "Ran KOL and local media outreach for two F&amp;B brands (130+ creators and media accounts), evaluated rate cards by real Reels views, managed a paid Reels collab that reached 16K+ views (96% non-followers), and coordinated an 11.11 cross-brand promo."),
    ("Apr – Oct 2026", "Social Media Officer", "Gerakan Pendidikan Berdampak, South Tangerang",
     "Ran the Instagram account: content plan, posting schedule, captions, flyers, carousels and reels. 84.4K views in 30 days."),
    ("Feb 2026 – now", "Event Coordinator", "Kita Bahagia, Jakarta",
     "Lead a community program for 100+ participants: concept, budget (RAB), vendors and partners."),
    ("Mar – Jun 2026", "Event Staff", "POSF 2026, IPB Physics sports and arts festival, Bogor",
     "Handled logistics and coordination on competition days."),
    ("Dec 2025 – Jan 2026", "Volunteer Teacher", "Gerakan Mengajar Desa, Bogor", "Taught elementary students in a village community."),
    ("Oct – Nov 2025", "Mentoring Staff", "Physics Gathering, Bogor",
     "Ran bonding activities between Physics Class of 61 and 62 and mentored incoming students."),
    ("2025", "Volunteer", "Social and educational programs", "Orphanage teaching, educational trips and environmental conservation."),
]
ROWS = [
    ("Education", "IPB University (Institut Pertanian Bogor)", "Undergraduate, Physics", "2024 – 2028 (expected)"),
    ("Education", "SMAS Kartika I-2 Medan", "Senior high school, final score 91.30/100", "2021 – 2024"),
    ("Certificate", "Introduction to Social Media Marketing", "Meta, via Coursera", "Oct 2026"),
    ("Award", "Finalist, Paper Competition", "PRESENT X TAZKIA JUARA", "2025"),
    ("Award", "Winner, Mobile Legends: Bang Bang Competition", "Festival Pelajar Nusantara by RRI Medan", "2023"),
]


def cover(roles, label):
    return f'''<section class="page dark cover"><div class="ambient"></div>
<div class="z top"><p class="r">{roles}</p><p class="w">Depok, Indonesia<br/>Physics at IPB University</p></div>
<h1 class="z name"><span>Ahmad</span><span class="l2">Fajri</span></h1>
<p class="z values">Bringing people together, on the ground and on the feed.</p>
<div class="z bottom"><span>{label}</span><a href="{SITE}">ahmadfajriportfolio.vercel.app</a></div></section>'''


def p52(n, kicker="Brand social media"):
    return f'''<section class="page"><div class="case">
<div class="text"><p class="kicker">{kicker}</p><h2 class="title">KOL outreach and a paid Reels collab for two F&amp;B brands</h2>
<p class="meta">Social Media &amp; Digital Marketing Intern · 52 Group (Hypr Caffeine &amp; Kazuhiro) · Tangerang · Oct – Nov 2026</p>
<ul><li>Ran KOL and local media outreach for two F&amp;B brands, across 130+ creators and media accounts</li>
<li>Evaluated rate cards against each creator&rsquo;s real Reels views to recommend who to prioritise</li>
<li>Managed a paid Reels collab with a creator</li>
<li>Coordinated an 11.11 cross-brand promotion with Operations, Finance and IT</li></ul>
<p class="result">16K+ views on the paid Reels collab · 96% of viewers were non-followers</p></div>
<dl class="numbers"><div class="ambient"></div>
<div class="n"><dt>130+</dt><dd>creators and media accounts reached out to</dd></div>
<div class="n"><dt>16K+</dt><dd>views on the paid Reels collab</dd></div>
<div class="n"><dt>96%</dt><dd>of the collab&rsquo;s viewers were non-followers</dd></div>
<div class="n"><dt>2</dt><dd>F&amp;B brands, plus an 11.11 cross-brand promo</dd></div></dl>
</div>{folio(n, "52 Group")}</section>'''


def gpb(n, kicker, title, desc):
    return f'''<section class="page"><div class="case">
<div class="text"><p class="kicker">{kicker}</p><h2 class="title">{title}</h2>
<p class="meta">Social Media Officer · Gerakan Pendidikan Berdampak · South Tangerang · Apr – Oct 2026</p>
<p class="desc">{desc}</p>
<ul><li>Planned the content calendar and wrote the captions</li><li>Ran the feed: volunteer-call flyers for each batch, program-report carousels, recap reels and quote posts</li></ul>
<p class="result">84.4K views in 30 days · 683 followers · reels up to 1.8K views each</p>
<p class="meta" style="margin-top:4mm"><a class="link" href="https://www.instagram.com/gerakanpendidikanberdampak/">@gerakanpendidikanberdampak</a></p></div>
<div class="gpb">
<div><div class="shot" style="height:60mm"><img src="{j('content/volunteer-call')}"/></div><p class="cap">Volunteer call, Batch 3</p></div>
<div><div class="shot" style="height:60mm"><img src="{j('content/batch2-report')}"/></div><p class="cap">Batch 2 program report</p></div>
<div><div class="shot" style="height:60mm"><img src="{j('content/soft-news')}"/></div><p class="cap">Quote post</p></div>
<div><div class="shot tall" style="height:72mm"><img src="{j('content/recap-reel-poster')}"/></div><p class="cap">Recap reel of a program day</p></div>
<div><div class="shot tall" style="height:72mm"><img src="{j('content/feed-grid')}"/></div><p class="cap">Feed · reels up to 1.8K views</p></div>
<div><div class="shot tall" style="height:72mm"><img src="{j('content/profile')}"/></div><p class="cap">683 followers, 84.4K views / 30 days</p></div>
</div></div>{folio(n, "GPB")}</section>'''


def kb(n, kicker="Event"):
    return f'''<section class="page"><div class="case">
<div class="text"><p class="kicker">{kicker}</p><h2 class="title">Leading a community program at Kita Bahagia</h2>
<p class="meta">Event Coordinator and Project Leader · Jakarta · Feb 2026 to now</p>
<ul><li>Lead the program for 100+ participants as Project Leader</li><li>Designed the program structure and the event concept</li><li>Wrote the budget plan (RAB) and allocated resources</li><li>Coordinate third-party vendors and partners</li></ul>
<p class="kicker" style="margin-top:8mm">Website</p><h3 style="font-size:14pt;margin-top:2mm">I also built kitabahagia.id</h3>
<p class="meta">Solo project · Started Aug 2026</p>
<p style="margin-top:3mm">My concept and design, built step by step through vibe coding. People browse the programs, check the schedule, sign up as volunteers and check their registration status. <a class="link" href="https://kitabahagia.id/">kitabahagia.id</a></p></div>
<div class="kb"><div class="shot web"><img src="{j('projects/kitabahagia-web')}"/></div><p class="cap">kitabahagia.id: programs, schedule, volunteer stories, partnerships, sign-up and status check</p></div>
</div>{folio(n, "Kita Bahagia")}</section>'''


def experience(n, jobs):
    return f'''<section class="page"><p class="kicker">Experience</p><h2 class="title">Where I&rsquo;ve worked and studied</h2>
<div class="cv"><div>{"".join(f'<div class="job"><p class="when">{w}</p><div><h4>{t}</h4><p class="org">{o}</p><p class="d">{d}</p></div></div>' for w, t, o, d in jobs)}</div>
<div><h3 class="sh">Education, certificates and awards</h3><div class="rows">{"".join(f'<div class="row"><p class="k">{k}</p><div><p>{a}</p><p class="sub">{b}</p></div><p class="when">{w}</p></div>' for k, a, b, w in ROWS)}</div>
<h3 class="sh">Languages</h3><p style="font-size:9.5pt">Indonesian (native), English (active, spoken and written)</p></div></div>{folio(n, "Experience")}</section>'''


def contact(n, big, based):
    return f'''<section class="page dark"><div class="ambient"></div><div class="z contact">
<p class="kicker">Contact</p>
<p class="big">{big}</p>
<a class="email" href="mailto:ahmadfajri2211@gmail.com">ahmadfajri2211@gmail.com</a>
<dl class="lines"><dt>WhatsApp</dt><dd><a href="https://wa.me/6282362330813">+62 823-6233-0813</a></dd>
<dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/ahmad-fajri-43b877323">linkedin.com/in/ahmad-fajri-43b877323</a></dd>
<dt>Website</dt><dd><a href="{SITE}">ahmadfajriportfolio.vercel.app</a></dd>
<dt>Based in</dt><dd>{based}</dd></dl></div>{folio(n, "Contact")}</section>'''


def general():
    P = [cover("Social Media &amp; Digital Marketing · Events", "Portfolio · 2026")]
    P.append(f'''<section class="page"><div class="about">
<div><p class="kicker">About</p>
<p class="lead" style="margin-top:4mm;font-size:21pt;line-height:1.2">I run social media and KOL outreach for F&amp;B brands, and coordinate community events.</p>
<p class="status">Open to Social Media &amp; Event roles · available now, full-time on-site</p>
<dl class="stats">
<div class="stat"><dt>100+</dt><dd>participants in the Kita Bahagia program I lead</dd></div>
<div class="stat"><dt>84.4K</dt><dd>Instagram views in 30 days on the GPB account I ran</dd></div>
<div class="stat"><dt>16K+</dt><dd>views on a paid Reels collab I managed for an F&amp;B brand</dd></div></dl>
<p class="why"><b>Physics student at IPB University (2024–2028), based in Depok.</b> I&rsquo;ve finished my required classes, so I can work full-time on-site.</p>
</div>
<div class="does"><h3>Social media</h3><p>Content planning and calendars, KOL and influencer outreach, rate card evaluation, captions, short-form video editing, graphic design, trend research, basic paid ads.</p>
<h3>Events</h3><p>Event concept and program design, budgeting (RAB), vendor and partner coordination, on-ground logistics.</p>
<h3>Platforms</h3><p>Instagram Insights, Meta Business Suite, Meta Ads Manager (basic), TikTok Studio, Google Trends.</p>
<h3>Tools</h3><p>Canva, CapCut, Adobe Premiere, Notion, Google Workspace, Microsoft Office.</p>
<h3>Certificate</h3><p>Introduction to Social Media Marketing, Meta via Coursera (Oct 2026) · <a class="link" href="https://coursera.org/verify/SHZWTNZSU5Q8">Verify</a></p>
</div></div>{folio(2, "About")}</section>''')
    P.append(p52(3))
    P.append(gpb(4, "Social media", "Running Instagram for Gerakan Pendidikan Berdampak",
                 "GPB runs literacy and character programs for children with volunteers. The account recruits volunteers for each batch and reports on each program."))
    P.append(kb(5))
    vid = lambda src, dur, title, meta, body, style: f'''<div><div class="shot rel" style="{style}"><img src="{j('projects/' + src)}"/><span class="play">Video · {dur}</span></div><p class="cap"><b>{title}</b>{meta}<br/>{body}</p></div>'''
    P.append(f'''<section class="page"><p class="kicker">Video and photo editing</p><h2 class="title">Edits for friends&rsquo; projects and a photo competition</h2>
<div style="display:grid;grid-template-columns:1.35fr .62fr 1.35fr;gap:6mm;margin-top:7mm;align-items:start">
{vid("duta-ipb-video-poster", "2:30", "Duta IPB profile video", "Edit and subtitles · CapCut · 2025", "Narrated #IPBinDiversity piece on growing up Betawi, shot around Monas, Istiqlal and Kota Tua.", "aspect-ratio:16/9")}
{vid("glukodiab-video-poster", "1:52", "Duta IPB product video", "Edit and captions · CapCut · 2025", "Vertical video introducing Glukodiab Drink.", "height:66mm")}
{vid("assignment-video-poster", "3:23", "Conversation video", "Edit · CapCut", "Two-person conversation for a friend&rsquo;s class assignment.", "aspect-ratio:16/9")}
</div>
<div style="display:grid;grid-template-columns:1fr 1.33fr 1.1fr;gap:6mm;margin-top:6mm;align-items:end">
<div class="shot" style="height:44mm"><img src="{j('projects/photo-edit-1')}"/></div>
<div class="shot" style="height:44mm"><img src="{j('projects/photo-edit-2')}"/></div>
<p class="cap"><b>Campus photos for a photo competition</b>Photo editing · Picsart · 2026<br/>Two IPB campus photos I edited and entered: one moody and rain-soaked, one warm and bright.<br/><br/>Watch the videos at <a class="link" href="{SITE}/#projects">ahmadfajriportfolio.vercel.app/#projects</a></p>
</div>{folio(6, "Editing")}</section>''')
    gal = [("dsc02453", "Outdoor session with the team and participants"), ("dsc04231", "Working with participants during the program"),
           ("dsc04303", "Closing session with the full cohort"), ("dscn0195", "Program team and participants"),
           ("dscn0046", "Checking on activities in progress"), ("img0452", "Teaching at an elementary school")]
    P.append(f'''<section class="page"><p class="kicker">On the ground</p><h2 class="title">From community programs and volunteer work I&rsquo;ve joined</h2>
<div class="gal">{"".join(f'<div><div class="shot"><img src="{j("gallery/" + g)}"/></div><p class="cap">{c}</p></div>' for g, c in gal)}</div>{folio(7, "Photos")}</section>''')
    P.append(experience(8, JOBS))
    P.append(contact(9, "Available now for<br/>Social Media &amp; Event<br/>roles", "Depok · full-time on-site"))
    return "Ahmad Fajri · Portfolio", P


def community():
    P = [cover("Community Programs · Events · Social Media", "Portfolio · Community Organizer · 2026")]
    P.append(f'''<section class="page"><div class="about">
<div><p class="kicker">About</p>
<p class="lead" style="margin-top:4mm;font-size:21pt;line-height:1.2">I run community and education programs, and keep the people around them engaged, on the ground and online.</p>
<p class="status">Available for a 6-month program, online and offline · based in Depok</p>
<dl class="stats">
<div class="stat"><dt>100+</dt><dd>participants in the Kita Bahagia program I lead</dd></div>
<div class="stat"><dt>130+</dt><dd>creators and media accounts I reached out to at 52 Group</dd></div>
<div class="stat"><dt>84.4K</dt><dd>Instagram views in 30 days for an education movement</dd></div></dl>
<p class="why"><b>Physics student at IPB University (2024–2028).</b> I&rsquo;ve finished my required classes, so I have the time to commit to a full program cycle.</p>
</div>
<div class="does"><h3>Community and events</h3><p>Program concept and structure, running programs for 100+ participants, budgeting (RAB), vendor and partner coordination, on-ground logistics.</p>
<h3>Education and young people</h3><p>Volunteer teaching in a village, mentoring new students, orphanage teaching and educational trips, and a literacy movement for children.</p>
<h3>Outreach and engagement</h3><p>Creator and media outreach, volunteer recruitment posts, program reports, recap reels, captions, event documentation.</p>
<h3>Tools</h3><p>Google Sheets and Google Workspace, Notion, Canva, CapCut, Microsoft Office.</p>
<h3>Certificate</h3><p>Introduction to Social Media Marketing, Meta via Coursera (Oct 2026) · <a class="link" href="https://coursera.org/verify/SHZWTNZSU5Q8">Verify</a></p>
</div></div>{folio(2, "About")}</section>''')
    fit = [("Engaging a community", "Keeping members in touch and active",
            "At <b>GPB</b> I ran the Instagram that recruited volunteers for every batch and reported back on each program (84.4K views in 30 days). At <b>Physics Gathering</b> I ran bonding activities between two student classes."),
           ("Running programs and tracking participants", "Program execution and participant progress",
            "At <b>Kita Bahagia</b> I lead a program for 100+ participants as Project Leader: I designed its structure and concept, planned the budget (RAB) and coordinate vendors and partners."),
           ("Outreach and coordination", "Reaching people and working across teams",
            "At <b>52 Group</b> I reached out to 130+ creators and media accounts for two F&amp;B brands and coordinated an 11.11 promo with Operations, Finance and IT."),
           ("Education and youth development", "Interest in education and young people",
            "Volunteer teacher at <b>Gerakan Mengajar Desa</b>, mentoring staff for incoming students, orphanage teaching and educational trips, and social media for <b>GPB</b>&rsquo;s literacy programs for children."),
           ("Google Workspace", "Daily tools", "Google Sheets and Google Workspace, Notion and Microsoft Office."),
           ("Six months, online and offline", "Commitment",
            "Required classes are done and I&rsquo;m based in Depok, so I can join on-site activities and work online across the whole period.")]
    P.append(f'''<section class="page"><p class="kicker">Why I fit</p><h2 class="title">What a community organizer needs, and where I&rsquo;ve done it</h2>
<div class="fit">{"".join(f'<div class="r"><p class="need">{a}<small>{b}</small></p><p class="have">{c}</p></div>' for a, b, c in fit)}</div>{folio(3, "Why I fit")}</section>''')
    P.append(kb(4, "Community program"))
    P.append(gpb(5, "Community engagement", "Keeping an education movement&rsquo;s community engaged",
                 "GPB runs literacy and character programs for children with volunteers. The account was how each batch found its volunteers and how the community saw what each program achieved."))
    progs = [("Volunteer Teacher", "Gerakan Mengajar Desa, Bogor · Dec 2025 – Jan 2026", "Taught elementary students in a village community."),
             ("Mentoring Staff", "Physics Gathering, Bogor · Oct – Nov 2025", "Ran bonding activities between Physics Class of 61 and 62 and mentored incoming students."),
             ("Event Staff", "POSF 2026, IPB Physics sports and arts festival · Mar – Jun 2026", "Handled logistics and coordination on competition days."),
             ("Volunteer", "Social and educational programs · 2025", "Orphanage teaching, educational trips and environmental conservation.")]
    gal = [("dsc02453", "Outdoor session with the team and participants"), ("dsc04231", "Working with participants during the program"),
           ("dscn0046", "Checking on activities in progress"), ("img0452", "Teaching at an elementary school")]
    P.append(f'''<section class="page"><p class="kicker">On the ground</p><h2 class="title">More community and education work</h2>
<div class="prog">{"".join(f'<div class="p"><h4>{t}</h4><p class="o">{o}</p><p class="d">{d}</p></div>' for t, o, d in progs)}</div>
<div class="strip">{"".join(f'<div><div class="shot"><img src="{j("gallery/" + g)}"/></div><p class="cap">{c}</p></div>' for g, c in gal)}</div>{folio(6, "On the ground")}</section>''')
    order = [JOBS[2], JOBS[1], JOBS[0], JOBS[4], JOBS[5], JOBS[3], JOBS[6]]
    P.append(experience(7, order))
    P.append(contact(8, "Ready to join<br/>a community program<br/>for six months", "Depok · online and offline"))
    return "Ahmad Fajri · Portfolio · Community", P


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    jpgs()
    for fname, fn in [("Portfolio_Ahmad_Fajri", general), ("Portfolio_Ahmad_Fajri_Community", community)]:
        title, pages = fn()
        with open(os.path.join(OUT, fname + ".html"), "w") as f:
            f.write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"/><title>{title}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
        print(fname)
