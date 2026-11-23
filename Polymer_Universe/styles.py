"""Theme stylesheet for the Under the Moonlight POLYVERSE design."""

CSS = r'''<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root {
 --bg: #171735; --surface: #22224a; --surface2: #2d2d5b; --ink: #f4f1ff; --muted: #c2bfdf;
 --primary: #5C5C99; --secondary: #A3A3CC; --accent: #CCCCFF; --border: rgba(163,163,204,.3);
 --sidebar: #292966; --sidebar2: #171735; --strong1: #292966; --strong2: #5C5C99;
 --hero-text: #ffffff; --hero-muted: #e0defb; --shadow: 0 16px 38px rgba(0,0,0,.26); --accent-soft: rgba(204,204,255,.17); --primary-glow: rgba(92,92,153,.28); --watermark: rgba(204,204,255,.11); --avatar-bg: rgba(204,204,255,.20); --mascot-filter: hue-rotate(205deg) saturate(1.1);
}
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background:radial-gradient(circle at 92% 8%, var(--accent-soft), transparent 26%), var(--bg); color:var(--ink); }
[data-testid="stHeader"] { background:transparent; }
.block-container { padding-top:1.5rem; padding-bottom:3.2rem; max-width:1360px; }
[data-testid="stSidebar"] { background:linear-gradient(165deg,var(--sidebar) 0%,var(--sidebar2) 100%); border-right:1px solid var(--border); }
[data-testid="stSidebar"] * { color:var(--sidebar-text, #f8f8ff) !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { padding:.55rem .7rem; border-radius:12px; transition:background .18s ease; }
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background:rgba(255,255,255,.11); }
[data-testid="stSidebar"] hr { border-color:rgba(255,255,255,.2); }
[data-testid="stSidebar"] .stCaption { color:rgba(255,255,255,.72) !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color:rgba(255,255,255,.88); }
.stMarkdown, .stText, .stCaption { color:var(--ink); }
.stMarkdown p, .stMarkdown li { color:var(--muted); line-height:1.65; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 { color:var(--ink); font-family:Manrope,sans-serif; }
.stButton > button, .stFormSubmitButton > button { border:1px solid var(--primary); border-radius:999px; background:linear-gradient(120deg,var(--primary),var(--strong2)); color:#fff !important; font-weight:750; padding:.68rem 1.2rem; transition:all .2s ease; box-shadow:0 7px 20px var(--primary-glow); }
.stButton > button:hover, .stFormSubmitButton > button:hover { border-color:var(--accent); filter:brightness(1.08); transform:translateY(-2px); box-shadow:0 10px 26px var(--primary-glow); }
.stSelectbox > div > div, .stTextInput > div > div, .stNumberInput > div > div { border-radius:14px; background:var(--surface); border-color:var(--border); }
.stTextInput input, .stNumberInput input { background:var(--surface) !important; color:var(--ink) !important; border-color:var(--border) !important; }
[data-baseweb="select"] > div { background:var(--surface); border-color:var(--border); color:var(--ink); }
[data-testid="stMetric"] { background:var(--surface); border:1px solid var(--border); padding:1rem 1.1rem; border-radius:18px; box-shadow:var(--shadow); }
[data-testid="stAlert"] { border-radius:16px; }
hr { border-color:var(--border); }
.poly-logo { display:flex; align-items:center; gap:10px; margin:.2rem 0 1.2rem; }
.poly-logo-mark { width:36px; height:36px; display:grid; place-items:center; border-radius:13px; background:var(--accent); color:var(--sidebar) !important; font-size:21px; box-shadow:0 0 22px var(--primary-glow); }
.poly-logo-name { font-family:Manrope,sans-serif; font-size:1.25rem; font-weight:850; letter-spacing:.08em; color:#fff; }
.poly-logo-sub { color:rgba(255,255,255,.72); font-size:.66rem; letter-spacing:.13em; text-transform:uppercase; }
.kicker { color:var(--primary); font:600 .72rem 'DM Mono',monospace; letter-spacing:.15em; text-transform:uppercase; margin-bottom:.55rem; }
.hero { background:linear-gradient(100deg,rgba(41,41,102,.96) 0%,rgba(92,92,153,.65) 62%,rgba(0,0,0,.12) 100%),url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNDQwIiBoZWlnaHQ9IjU2MCIgdmlld0JveD0iMCAwIDE0NDAgNTYwIj4KPGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJiZyIgeDE9IjAiIHkxPSIwIiB4Mj0iMSIgeTI9IjEiPjxzdG9wIHN0b3AtY29sb3I9IiMxNzE3MzUiLz48c3RvcCBvZmZzZXQ9Ii41NSIgc3RvcC1jb2xvcj0iIzI5Mjk2NiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzVjNWM5OSIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJmbGFzayIgeDE9IjAiIHkxPSIwIiB4Mj0iMSIgeTI9IjEiPjxzdG9wIHN0b3AtY29sb3I9IiNjY2NjZmYiIHN0b3Atb3BhY2l0eT0iLjQiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM2OGRkZmYiIHN0b3Atb3BhY2l0eT0iLjkiLz48L2xpbmVhckdyYWRpZW50PjxmaWx0ZXIgaWQ9Imdsb3ciPjxmZUdhdXNzaWFuQmx1ciBzdGREZXZpYXRpb249IjgiLz48L2ZpbHRlcj48L2RlZnM+CjxyZWN0IHdpZHRoPSIxNDQwIiBoZWlnaHQ9IjU2MCIgZmlsbD0idXJsKCNiZykiLz48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNhM2EzY2MiIG9wYWNpdHk9Ii4yIj48Y2lyY2xlIGN4PSIxMTQwIiBjeT0iMjYwIiByPSIyMTAiIHN0cm9rZS13aWR0aD0iMiIvPjxjaXJjbGUgY3g9IjExNDAiIGN5PSIyNjAiIHI9IjI2MCIvPjxwYXRoIGQ9Ik0wIDQ4MFEzNDAgMzYwIDY4MCA0OTBUMTQ0MCA0MzAiIHN0cm9rZS13aWR0aD0iMiIvPjwvZz4KPGcgc3Ryb2tlPSIjYTRlOGZmIiBzdHJva2Utd2lkdGg9IjUiIGZpbGw9Im5vbmUiIG9wYWNpdHk9Ii44NSI+PHBhdGggZD0iTTc2MCAxMDBMODcwIDQ1TDk4MCAxMDBMMTA5MCA0NUwxMjAwIDEwMEwxMzEwIDQ1TDE0MDAgOTAiLz48cGF0aCBkPSJNODIwIDI2MEw5MzAgMjA1TDEwNDAgMjYwTDExNTAgMjA1TDEyNjAgMjYwTDEzNzAgMjA1Ii8+PHBhdGggZD0iTTkzMCA0MDVMMTA0MCAzNTBMMTE1MCA0MDVMMTI2MCAzNTBMMTM3MCA0MDUiLz48L2c+CjxnIGZpbGw9IiNjY2NjZmYiIHN0cm9rZT0iIzhlZWFmZiIgc3Ryb2tlLXdpZHRoPSI0Ij48Y2lyY2xlIGN4PSI3NjAiIGN5PSIxMDAiIHI9IjE4Ii8+PGNpcmNsZSBjeD0iODcwIiBjeT0iNDUiIHI9IjIyIi8+PGNpcmNsZSBjeD0iOTgwIiBjeT0iMTAwIiByPSIxOCIvPjxjaXJjbGUgY3g9IjEwOTAiIGN5PSI0NSIgcj0iMjIiLz48Y2lyY2xlIGN4PSIxMjAwIiBjeT0iMTAwIiByPSIxOCIvPjxjaXJjbGUgY3g9IjEzMTAiIGN5PSI0NSIgcj0iMjIiLz48Y2lyY2xlIGN4PSI4MjAiIGN5PSIyNjAiIHI9IjE4Ii8+PGNpcmNsZSBjeD0iOTMwIiBjeT0iMjA1IiByPSIyMiIvPjxjaXJjbGUgY3g9IjEwNDAiIGN5PSIyNjAiIHI9IjE4Ii8+PGNpcmNsZSBjeD0iMTE1MCIgY3k9IjIwNSIgcj0iMjIiLz48Y2lyY2xlIGN4PSIxMjYwIiBjeT0iMjYwIiByPSIxOCIvPjxjaXJjbGUgY3g9IjEzNzAiIGN5PSIyMDUiIHI9IjIyIi8+PC9nPgo8IS0tIGdsb3dpbmcgbGFiIHR1YmVzIC0tPgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg5MDAgMzEwKSIgc3Ryb2tlPSIjY2NjY2ZmIiBzdHJva2Utd2lkdGg9IjciIGZpbGw9InVybCgjZmxhc2spIiBvcGFjaXR5PSIuOSI+PHBhdGggZD0iTTMwIDBWODVMLTUgMTg1US0xMCAyMDUgMTUgMjEwSDEwMFExMjUgMjA1IDExNSAxODVMODAgODVWMCIvPjxwYXRoIGQ9Ik0yNSAwSDg1IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48cGF0aCBkPSJNLTEgMTc0UTUyIDE1MCAxMTIgMTc0TDEyMCAxOTdRMTIwIDIxMCAxMDAgMjEwSDE1US0xMCAyMTAgLTUgMTkwWiIgZmlsbD0iIzY1ZGNmZiIgc3Ryb2tlPSJub25lIi8+PHBhdGggZD0iTTE0NSAyMFYxNDBMMTIwIDIxMFExMTUgMjMwIDEzOCAyMzJIMjA1UTIyOCAyMzAgMjIwIDIxMEwxOTUgMTQwVjIwIi8+PHBhdGggZD0iTTE0MCAyMEgyMDAiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPjwvZz4KPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTIxMCAzNzUpIiBmaWxsPSJub25lIiBzdHJva2U9IiNhNGE1ZjUiIHN0cm9rZS13aWR0aD0iMTAiIG9wYWNpdHk9Ii44NSI+PHBhdGggZD0iTTAgMFYxMDBMLTU1IDE5MFEtNzAgMjIwIC0zNSAyMzBIMTMwUTE2NSAyMjAgMTUwIDE5MEw5NSAxMDBWMCIvPjxwYXRoIGQ9Ik0tNDggMTg1UTQ1IDE1MCAxNDUgMTg1IiBzdHJva2U9IiM2N2U5ZmYiIHN0cm9rZS13aWR0aD0iOCIvPjwvZz4KPGcgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iLjciPjxjaXJjbGUgY3g9IjExNTAiIGN5PSIxNDAiIHI9IjMiLz48Y2lyY2xlIGN4PSIxMzIwIiBjeT0iMzEwIiByPSI0Ii8+PGNpcmNsZSBjeD0iODIwIiBjeT0iNDQwIiByPSIzIi8+PGNpcmNsZSBjeD0iNzIwIiBjeT0iMzMwIiByPSI1Ii8+PGNpcmNsZSBjeD0iMTM3MCIgY3k9IjQ4MCIgcj0iMyIvPjwvZz4KPC9zdmc+") center right/cover no-repeat; border:1px solid var(--border); border-radius:30px; padding:2.6rem 2.7rem; color:var(--hero-text); position:relative; overflow:hidden; min-height:330px; box-shadow:var(--shadow); }
.hero:after { content:'⌬'; position:absolute; right:2%; top:3%; font-size:10rem; line-height:1; color:rgba(255,255,255,.09); transform:rotate(15deg); pointer-events:none; }
.hero h1 { font:850 clamp(2.45rem,5.2vw,4.4rem)/1.0 Manrope,sans-serif; letter-spacing:-.06em; color:var(--hero-text); margin:.25rem 0 1rem; max-width:720px; text-shadow:0 3px 18px rgba(0,0,0,.12); }
.hero p { color:var(--hero-muted); font-size:1.04rem; max-width:650px; line-height:1.65; }
.hero-chip { display:inline-block; border:1px solid rgba(255,255,255,.44); border-radius:999px; padding:.42rem .8rem; font:600 .66rem 'DM Mono',monospace; letter-spacing:.12em; color:var(--hero-text); background:rgba(255,255,255,.08); backdrop-filter:blur(8px); }
.hero-art { position:absolute; right:4%; bottom:-7px; width:190px; z-index:1; filter:drop-shadow(0 12px 22px rgba(0,0,0,.2)) var(--mascot-filter); }
.section-title { font:850 1.7rem Manrope,sans-serif; color:var(--ink); letter-spacing:-.04em; margin:.35rem 0 .3rem; }
.section-sub { color:var(--muted); line-height:1.6; margin-bottom:1.1rem; }
.matex-message { display:flex; align-items:center; gap:14px; background:linear-gradient(110deg,var(--surface2),var(--surface)); border:1px solid var(--border); border-radius:22px; padding:13px 18px 13px 12px; margin:.85rem 0 1.45rem; box-shadow:var(--shadow); position:relative; overflow:hidden; }
.matex-message:after { content:'⌬'; position:absolute; right:14px; bottom:-26px; font-size:6rem; color:var(--watermark); }
.matex-avatar { flex:0 0 68px; width:68px; height:68px; display:grid; place-items:center; background:var(--avatar-bg); border:1px solid var(--border); border-radius:20px; overflow:hidden; }
.matex-avatar svg { width:68px; height:68px; filter:var(--mascot-filter); }
.matex-eyebrow { color:var(--primary); font:600 .64rem 'DM Mono',monospace; letter-spacing:.12em; margin-bottom:4px; }
.matex-copy { color:var(--ink); font-weight:650; line-height:1.55; position:relative; z-index:1; }
.feature-card { background:linear-gradient(145deg,var(--surface),var(--surface2)); border:1px solid var(--border); border-radius:22px; padding:1.25rem 1.3rem; min-height:174px; box-shadow:var(--shadow); position:relative; overflow:hidden; transition:transform .2s ease,border-color .2s ease; }
.feature-card:after { content:'⌬'; position:absolute; right:9px; top:4px; font-size:4.3rem; line-height:1; color:var(--watermark); pointer-events:none; }
.feature-card:hover { transform:translateY(-3px); border-color:var(--accent); }
.feature-card .emoji { font-size:1.65rem; margin-bottom:.55rem; position:relative; z-index:1; }
.feature-card h3 { font:750 1.06rem Manrope,sans-serif; margin:0 0 .4rem; color:var(--ink); position:relative; z-index:1; }
.feature-card p { color:var(--muted); font-size:.9rem; line-height:1.5; margin:0; position:relative; z-index:1; }
.poly-card { background:var(--surface); border:1px solid var(--border); border-radius:20px; padding:1.1rem; min-height:180px; box-shadow:var(--shadow); position:relative; overflow:hidden; }
.poly-card:after { content:'◈'; position:absolute; right:12px; bottom:0; font-size:3.4rem; color:var(--watermark); }
.poly-card .poly-dot { width:10px; height:10px; border-radius:50%; display:inline-block; margin-right:7px; box-shadow:0 0 10px currentColor; }
.poly-card h3 { font:750 1.06rem Manrope,sans-serif; color:var(--ink); margin:.6rem 0 .35rem; position:relative; z-index:1; }
.poly-card p { color:var(--muted); font-size:.88rem; line-height:1.48; position:relative; z-index:1; }
.poly-meta { color:var(--primary); font:600 .62rem 'DM Mono',monospace; letter-spacing:.09em; text-transform:uppercase; }
.info-panel { background:var(--surface); border:1px solid var(--border); border-radius:22px; padding:1.35rem 1.5rem; box-shadow:var(--shadow); }
.info-panel h2, .info-panel h3 { font:750 1.08rem Manrope,sans-serif; color:var(--ink) !important; margin:.1rem 0 .65rem; }
.info-panel p, .info-panel li { color:var(--muted) !important; line-height:1.65; }
.fact-panel { background:linear-gradient(130deg,var(--surface2),var(--surface)); border:1px solid var(--border); border-radius:26px; padding:1.6rem; box-shadow:var(--shadow); }
.fact-panel .fact-word { color:var(--primary); font:600 .68rem 'DM Mono',monospace; letter-spacing:.14em; text-transform:uppercase; }
.fact-panel .fact-copy { color:var(--ink); font:750 1.35rem/1.5 Manrope,sans-serif; margin-top:.65rem; }
.molecule-note { background:var(--surface2); border:1px solid var(--border); border-radius:14px; padding:.75rem 1rem; color:var(--muted); font-size:.82rem; line-height:1.5; }
.selector-options-title { color:var(--primary); font:600 .72rem 'DM Mono',monospace; letter-spacing:.15em; margin:.8rem 0 .7rem; }
.selector-option { background:var(--surface); border:1px solid var(--border); border-radius:19px; padding:1rem 1.1rem; min-height:160px; margin-bottom:.75rem; box-shadow:var(--shadow); }
.selector-option-top { display:flex; justify-content:space-between; align-items:center; gap:.5rem; }
.selector-number { display:grid; place-items:center; width:30px; height:30px; border-radius:10px; background:var(--surface2); color:var(--primary); font:800 .9rem Manrope,sans-serif; }
.selector-tag { color:var(--muted); font:600 .6rem 'DM Mono',monospace; letter-spacing:.08em; text-transform:uppercase; text-align:right; }
.selector-option-icon { font-size:1.45rem; margin:.65rem 0 .2rem; }
.selector-option h3 { color:var(--ink); font:750 .98rem/1.35 Manrope,sans-serif; margin:.2rem 0 0; }
.selector-result { background:linear-gradient(125deg,var(--strong1),var(--strong2)); border:1px solid var(--border); border-radius:25px; padding:1.5rem 1.7rem; margin:1.25rem 0 1rem; box-shadow:var(--shadow); }
.selector-result-kicker { color:var(--accent); font:600 .68rem 'DM Mono',monospace; letter-spacing:.14em; }
.selector-result-row { display:flex; align-items:center; gap:1rem; margin:1rem 0 1.2rem; }
.selector-result-icon { display:grid; place-items:center; flex:0 0 54px; height:54px; border-radius:17px; background:rgba(255,255,255,.14); font-size:1.8rem; }
.selector-result-label, .selector-reason-label { color:rgba(255,255,255,.72); font:600 .62rem 'DM Mono',monospace; letter-spacing:.12em; }
.selector-result-name { color:#fff; font:850 clamp(1.5rem,3vw,2.15rem)/1.15 Manrope,sans-serif; letter-spacing:-.04em; margin-top:.15rem; }
.selector-reason { color:#fff; font-size:1rem; line-height:1.6; margin:.35rem 0 0; max-width:850px; }
.mono { font-family:'DM Mono',monospace; }
.small-muted { color:var(--muted); font-size:.8rem; }
.footer { border-top:1px solid var(--border); padding-top:1rem; color:var(--muted); font-size:.78rem; margin-top:2.5rem; }
/* Keep inputs readable in every theme, including the dark variants. */
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input { background:var(--surface) !important; color:var(--ink) !important; -webkit-text-fill-color:var(--ink) !important; }
[data-testid="stTextInput"] input::placeholder { color:var(--muted) !important; opacity:.8; }
[data-testid="stForm"] { background:transparent; }
[data-testid="stRadio"] label, [data-testid="stCheckbox"] label { color:var(--ink); }
@media (max-width: 700px) {
 .hero { padding:1.65rem; min-height:360px; background-position:center right; }
 .hero-art { width:122px; right:2%; opacity:.95; }
 .hero h1 { font-size:2.55rem; max-width:100%; }
 .hero p { max-width:100%; font-size:.94rem; }
 .matex-message { align-items:flex-start; }
 .feature-card { min-height:150px; }
}
</style>'''
