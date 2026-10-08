"""Build Ahmad Fajri's CV variants as HTML; render.mjs turns them into PDFs."""
import html

CONTACT = [
    ("+62 823-6233-0813", "https://wa.me/6282362330813"),
    ("ahmadfajri2211@gmail.com", "mailto:ahmadfajri2211@gmail.com"),
    ("linkedin.com/in/ahmad-fajri-43b877323", "https://www.linkedin.com/in/ahmad-fajri-43b877323"),
    ("ahmadfajriportfolio.vercel.app", "https://ahmadfajriportfolio.vercel.app"),
]

GPB = dict(
    org="Gerakan Pendidikan Berdampak", place="South Tangerang", role="Social Media Officer", when="Apr 2026 – Present",
    bullets=[
        "Develop and execute the Instagram content strategy for a volunteer movement focused on children&rsquo;s literacy and character education",
        "Plan the content calendar and write captions for volunteer-call flyers, program-report carousels, recap reels, and soft-news posts",
        "Account reached <b>84.4K views in 30 days</b> with 683 followers; recap reels reach up to 1.8K views each",
    ],
)
KITA = dict(
    org="Kita Bahagia", place="Jakarta", role="Event Coordinator", when="Feb 2026 – Present",
    bullets=[
        "Lead a community program for <b>100+ participants</b> as Project Leader, from planning through on-ground execution",
        "Designed the program structure and event concept to fit community objectives",
        "Prepared the budget plan (RAB) and coordinate third-party vendors and partners",
        "Built the community website <b>kitabahagia.id</b>: my concept and design, coded with AI help",
    ],
)
POSF = dict(
    org="POSF 2026 (IPB Physics Sports &amp; Arts Festival)", place="Bogor", role="Event Staff", when="Mar 2026 – Jun 2026",
    bullets=[
        "Supported the organization of a sports and arts festival for IPB physics students",
        "Handled on-ground logistics and coordination during competition days",
    ],
)
GMD = dict(
    org="Gerakan Mengajar Desa", place="Bogor", role="Volunteer Teacher", when="Dec 2025 – Jan 2026",
    bullets=["Taught elementary students and supported foundational learning in a village community"],
)
PG = dict(
    org="Physics Gathering", place="Bogor", role="Mentoring Staff", when="Oct 2025 – Nov 2025",
    bullets=[
        "Facilitated bonding activities between Physics Class of 61 and Class of 62",
        "Introduced incoming students to the Physics Department through mentoring sessions",
    ],
)
VOL = dict(
    org="Social &amp; Educational Volunteer Programs", place="Indonesia", role="Volunteer", when="2025",
    bullets=["Orphanage teaching, educational trips, and environmental conservation; helped with logistics, teaching assistance, and community engagement"],
)
ROHIS = dict(
    org="Rohani Islam, SMAS Kartika I-2", place="Medan", role="Staff", when="Aug 2022 – Aug 2023",
    bullets=["Supported religious program activities within the school community"],
)

SKILLS_SOCIAL = ("Social media &amp; content", "Content strategy &amp; planning, content calendar &amp; scheduling, copywriting (captions), short-form video editing, graphic design, trend research, basic paid ads")
SKILLS_PLATFORMS = ("Platforms", "Instagram Professional Dashboard (Insights), Meta Business Suite, Meta Ads Manager (basic), TikTok Studio, Google Trends")
SKILLS_EVENT = ("Event management", "Event concept &amp; program design, budgeting (RAB), vendor &amp; partner coordination, on-ground logistics, timeline management")
ACHIEVEMENTS = ("Achievements", "Finalist, Paper Competition by PRESENT X TAZKIA JUARA (2025); Winner, Mobile Legends: Bang Bang Competition at Festival Pelajar Nusantara by RRI Medan (2023)")
SKILLS_TOOLS = ("Tools", "Canva, CapCut, Adobe Premiere, Notion, Google Sheets &amp; Workspace, Microsoft Office, ChatGPT &amp; Claude, Python (basic)")
LANGUAGES = ("Languages", "Indonesian (native), English (active, spoken and written)")
SKILLS_SOFT = ("Soft skills", "Teamwork, cross-team communication, problem solving, adaptability")

VARIANTS = {
    "social": dict(
        file="CV_Ahmad_Fajri_Social_Media",
        headline="Social Media Internship Candidate",
        summary=(
            "Physics undergraduate at IPB University and Social Media Officer at Gerakan Pendidikan Berdampak, "
            "where I plan and produce the Instagram content for a volunteer education movement (84.4K views in 30 days). "
            "I also lead community events as Event Coordinator at Kita Bahagia, so I know how to run an event and how to tell its story online. "
            "Looking for a Social Media internship; available immediately, full-time on-site."
        ),
        exp=[GPB, KITA, POSF, GMD, PG, VOL],
        skills=[SKILLS_SOCIAL, SKILLS_PLATFORMS, SKILLS_TOOLS, SKILLS_EVENT, LANGUAGES, ACHIEVEMENTS],
    ),
    "event": dict(
        file="CV_Ahmad_Fajri_Event",
        headline="Event Internship Candidate",
        summary=(
            "Physics undergraduate at IPB University and Event Coordinator at Kita Bahagia, leading a community program for 100+ participants "
            "from concept, budget (RAB) and vendor coordination to on-ground execution. "
            "Event staff at POSF 2026 and mentoring staff at Physics Gathering. I also run Instagram for Gerakan Pendidikan Berdampak, "
            "so I can promote and document events, not just run them. Looking for an Event internship; available immediately, full-time on-site."
        ),
        exp=[KITA, POSF, PG, GPB, GMD, VOL],
        skills=[SKILLS_EVENT, SKILLS_SOCIAL, SKILLS_PLATFORMS, SKILLS_TOOLS, LANGUAGES, ACHIEVEMENTS],
    ),
    "general": dict(
        file="CV_Ahmad_Fajri",
        headline="Social Media &amp; Event",
        summary=(
            "Physics undergraduate at IPB University who coordinates community events and creates the social media content around them. "
            "Event Coordinator at Kita Bahagia (100+ participants) and Social Media Officer at Gerakan Pendidikan Berdampak "
            "(84.4K Instagram views in 30 days). Looking for Social Media and Event internships; available immediately, full-time on-site."
        ),
        exp=[GPB, KITA, POSF, GMD, PG, VOL],
        skills=[SKILLS_SOCIAL, SKILLS_PLATFORMS, SKILLS_EVENT, SKILLS_TOOLS, LANGUAGES, ACHIEVEMENTS],
    ),
}

CSS = open("fonts/fonts.css").read() + """
@page{size:A4;margin:12mm 15mm}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',sans-serif;font-size:9.3pt;line-height:1.42;color:#141414}
a{color:inherit;text-decoration:none}
header{border-bottom:1.2pt solid #141414;padding-bottom:9pt}
h1{font-family:'Fraunces',serif;font-weight:500;font-size:24pt;letter-spacing:-0.02em;margin:0;line-height:1.05}
.headline{margin:3pt 0 0;font-size:8.6pt;text-transform:uppercase;letter-spacing:0.04em;color:#555}
.contact{margin:7pt 0 0;font-size:8.6pt;color:#333}
.contact span{white-space:nowrap}
.contact span+span::before{content:"·";margin:0 6pt;color:#999}
h2{font-size:8.6pt;text-transform:uppercase;letter-spacing:0.04em;font-weight:600;color:#555;margin:11pt 0 6pt;padding-bottom:3pt;border-bottom:0.6pt solid #d6d6d6}
.summary{margin:9pt 0 0}
.item{margin:0 0 7pt;break-inside:avoid}
.row{display:flex;justify-content:space-between;gap:12pt;align-items:baseline}
.role{font-weight:600}
.org{color:#333}
.when{font-size:8.6pt;color:#555;white-space:nowrap}
ul{margin:2pt 0 0;padding-left:12pt}
li{margin:1pt 0}
li::marker{color:#999}
.skills{display:grid;grid-template-columns:118pt 1fr;gap:3pt 10pt;margin:0}
.skills dt{font-weight:600}
.skills dd{margin:0}
"""


def exp_item(e):
    lis = "".join(f"<li>{b}</li>" for b in e["bullets"])
    return f"""<div class="item">
<div class="row"><div><span class="role">{e['role']}</span> <span class="org">· {e['org']}, {e['place']}</span></div><div class="when">{e['when']}</div></div>
<ul>{lis}</ul></div>"""


def build(v):
    contact = "".join(f'<span><a href="{html.escape(u)}">{t}</a></span>' for t, u in CONTACT)
    skills = "".join(f"<dt>{k}</dt><dd>{d}</dd>" for k, d in v["skills"])
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CV — Ahmad Fajri</title><style>{CSS}</style></head><body>
<header><h1>Ahmad Fajri</h1><p class="headline">{v['headline']} · Depok, Indonesia</p><p class="contact">{contact}</p></header>
<p class="summary">{v['summary']}</p>
<h2>Experience</h2>{''.join(exp_item(e) for e in v['exp'])}
<h2>Education</h2>
<div class="item"><div class="row"><div><span class="role">IPB University (Institut Pertanian Bogor)</span> <span class="org">· Undergraduate, Physics</span></div><div class="when">Aug 2024 – Aug 2028 (expected)</div></div></div>
<div class="item"><div class="row"><div><span class="role">SMAS Kartika I-2 Medan</span> <span class="org">· Senior High School, final score 91.30/100</span></div><div class="when">Jul 2021 – Jul 2024</div></div></div>
<h2>Skills &amp; Achievements</h2><dl class="skills">{skills}</dl>
</body></html>"""


for key, v in VARIANTS.items():
    open(f"{v['file']}.html", "w").write(build(v))
    print(v["file"])
