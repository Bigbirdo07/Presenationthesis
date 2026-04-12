import base64, os

MEDIA = '/Users/albertopaz/Masterthesis/Claudemasterthesis/ppt/media'
OUT   = '/Users/albertopaz/Masterthesis/Claudemasterthesis/presentation.html'

def b64(fn):
    ext = fn.rsplit('.',1)[-1].lower()
    mime = 'image/jpeg' if ext in ('jpg','jpeg') else 'image/png'
    with open(os.path.join(MEDIA,fn),'rb') as f:
        d = base64.b64encode(f.read()).decode()
    return f'data:{mime};base64,{d}'

print("Loading images…")
I = {k:b64(v) for k,v in {
    # Numbered images (unchanged)
    'i1':'image1.png','i2':'image2.jpg','i8':'image8.png','i9':'image9.png',
    'i10':'image10.png','i12':'image12.png','i13':'image13.png',
    'i15':'image15.png','i16':'image16.png','i17':'image17.png',
    'i18':'image18.png','i19':'image19.png','i20':'image20.png','i21':'image21.png',
    'i22':'image22.png',
    # Renamed experimental design images (descriptive names from author)
    'exp':'Sourceclamandnormalfortrial1and2canalsoshow5dayand12day.png',  # bright exposure tank – use for trial 1&2, 5-day, 12-day
    'src':'Sourceclamwithnormalfortrial1and2.png',                         # dark bg: source neoplastic + normal clam being added
    'nrm':'onlynormal.png',                                                # confirmed normal pool
    'nrm2':'onlynormalforbothtrial1and2and5dayandnormal.png',              # dome-shaped normal clams (both trials & 5-day context)
    'seq':'outputoftrial1andtrial2issinglecellsequencing.png',             # scRNA-seq 10x workflow output
    'ctrl':'soleynormalfortrial1and2.png',                                 # solely normal control for trial 1&2
}.items()}
print("Images loaded.")

TOTAL = 46
AC = {'I':'#98FF98','II':'#AFEEEE','III':'#E6E6FA','IV':'#98FF98','V':'#E05555','VI':'#98FF98'}
AL = {'I':'ACT I — THE WORLD','II':'ACT II — THE PROBLEM','III':'ACT III — THE EXPEDITION',
      'IV':'ACT IV — THE DISCOVERY','V':'ACT V — THE BREAKTHROUGH','VI':'ACT VI — THE SOLUTION'}

def act(n):
    if n<=5: return 'I'
    if n<=12: return 'II'
    if n<=25: return 'III'
    if n<=35: return 'IV'
    if n<=43: return 'V'
    return 'VI'

NEURAL='''<svg class="neural-wm" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<circle cx="20" cy="25" r="4" fill="#AFEEEE"/><circle cx="65" cy="15" r="2.5" fill="#AFEEEE"/>
<circle cx="110" cy="45" r="3.5" fill="#AFEEEE"/><circle cx="45" cy="70" r="2" fill="#AFEEEE"/>
<circle cx="90" cy="90" r="4.5" fill="#AFEEEE"/><circle cx="140" cy="35" r="2" fill="#AFEEEE"/>
<circle cx="160" cy="75" r="3" fill="#AFEEEE"/><circle cx="30" cy="110" r="3" fill="#AFEEEE"/>
<circle cx="80" cy="130" r="2" fill="#AFEEEE"/>
<line x1="20" y1="25" x2="65" y2="15" stroke="#AFEEEE" stroke-width="0.8" opacity="0.6"/>
<line x1="65" y1="15" x2="110" y2="45" stroke="#AFEEEE" stroke-width="0.8" opacity="0.5"/>
<line x1="20" y1="25" x2="45" y2="70" stroke="#AFEEEE" stroke-width="0.8" opacity="0.4"/>
<line x1="45" y1="70" x2="90" y2="90" stroke="#AFEEEE" stroke-width="0.8" opacity="0.35"/>
<line x1="110" y1="45" x2="140" y2="35" stroke="#AFEEEE" stroke-width="0.8" opacity="0.3"/>
<line x1="140" y1="35" x2="160" y2="75" stroke="#AFEEEE" stroke-width="0.6" opacity="0.25"/>
<line x1="80" y1="130" x2="90" y2="90" stroke="#AFEEEE" stroke-width="0.6" opacity="0.2"/>
</svg>'''

CLAM='''<svg class="clam-wm" viewBox="0 0 120 100" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="60" cy="58" rx="54" ry="38" fill="none" stroke="#AFEEEE" stroke-width="2.5"/>
<path d="M 8 58 Q 60 12 112 58" fill="none" stroke="#AFEEEE" stroke-width="1.8"/>
<path d="M 15 65 Q 60 22 105 65" fill="none" stroke="#AFEEEE" stroke-width="1.4"/>
<path d="M 22 72 Q 60 34 98 72" fill="none" stroke="#AFEEEE" stroke-width="1.1"/>
<path d="M 30 78 Q 60 46 90 78" fill="none" stroke="#AFEEEE" stroke-width="0.9"/>
<path d="M 38 83 Q 60 56 82 83" fill="none" stroke="#AFEEEE" stroke-width="0.7"/>
<circle cx="60" cy="58" r="5" fill="#AFEEEE"/>
</svg>'''

def footer(n):
    return f'<div class="footer"><span class="fbrand">URI — Paz, 2025</span><button class="fcounter" onclick="toggleNav()" aria-label="Navigator">{n} / {TOTAL}</button></div>'

def al(a,d=0):
    return f'<div class="act-lbl" style="color:{AC[a]}" data-animate="title-fade" data-delay="{d}">{AL[a]}</div>'

def ti(text,d=0.1,extra=''):
    return f'<h2 class="slide-title{" "+extra if extra else ""}" data-animate="title-fade" data-delay="{d}">{text}</h2>'

def card(html,d=0.4,cls='card'):
    return f'<div class="{cls}" data-animate="text-emerge" data-delay="{d}">{html}</div>'

def acard(html,d=0.4,color='#98FF98'):
    return f'<div class="card-accent" style="border-left-color:{color}" data-animate="text-emerge" data-delay="{d}">{html}</div>'

def stcard(num,lbl,d=0.6):
    return f'<div class="stat-card" data-animate="stat-reveal" data-delay="{d}"><div class="stat-num">{num}</div><div class="stat-lbl">{lbl}</div></div>'

def figbox(key,label,caption,d=0.5,h=''):
    hs = f'height:{h};' if h else ''
    return f'''<div class="fig-frame" data-animate="scale-fade-in" data-delay="{d}" style="{hs}position:relative">
  <div class="fig-lbl">{label}</div>
  <img src="{I[key]}" alt="{label}" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
</div>
<div class="fig-cap" data-animate="text-emerge" data-delay="{d+0.4:.1f}">{caption}</div>'''

def pill(t,v='blue'):
    return f'<span class="pill pill-{v}">{t}</span>'

def mkslide(n,content,title=None):
    a = act(n)
    active = ''  # goTo(0) on begin handles activation
    title_html = ti(title) if title else ''
    slide_label = f'Slide {n}' + (f': {title}' if title else '')
    return f'''<div class="slide{active}" id="s{n}" data-index="{n-1}" role="region" aria-label="{slide_label}">
{NEURAL}
<div class="slide-inner">
{al(a)}
{title_html}
{content}
</div>
{CLAM}
{footer(n)}
</div>'''

# ─── Build all 42 slides ───────────────────────────────────────────────────

slides = []

# SLIDE 1 – Title
slides.append(mkslide(1,f'''
<div class="layout-d" style="gap:12px;text-align:center">
  <div style="font-size:0.7em;font-weight:600;color:#5a8099;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:4px" data-animate="text-emerge" data-delay="0.2">Master of Science Thesis · University of Rhode Island · 2025</div>
  <div style="font-size:1.6em;font-weight:600;color:#2D2D2D;line-height:1.25;max-width:70%" data-animate="title-fade" data-delay="0.35">Machine Learning as a Tool for Uncovering Transcriptional Signatures of Bivalve Transmissible Neoplasia in <em>Mercenaria mercenaria</em></div>
  <div style="width:60px;height:2px;background:#98FF98;margin:8px auto" data-animate="text-emerge" data-delay="0.55"></div>
  <div style="font-size:1em;font-weight:600;color:#2D2D2D" data-animate="text-emerge" data-delay="0.65">Alberto A. Paz</div>
  <div style="font-size:0.75em;color:#5a8099;line-height:1.8" data-animate="text-emerge" data-delay="0.8">Major Professor: Dr. Marta Gomez-Chiarri<br>Committee: Dr. Nic Fisk · Dr. Thomas Delomas · Dr. Hollie Putnam<br>Biological Environmental Sciences</div>
</div>'''))

# SLIDE 2 – Opening Hook
slides.append(mkslide(2,f'''
<div class="layout-d">
  <div style="font-size:1.1em;color:#5a8099;font-style:italic;max-width:65%" data-animate="text-emerge" data-delay="0.2">"As a bioinformatician, what is the most important thing to understand?"</div>
  <div style="font-size:2.4em;font-weight:600;color:#2D2D2D;margin-top:8px" data-animate="stat-reveal" data-delay="0.7">Knowing your study.</div>
</div>'''))

# SLIDE 3 – Study Organism
slides.append(mkslide(3,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:2% 5% 0;align-items:center;height:100%">
  <div data-animate="scale-fade-in" data-delay="0.3">
    <div class="fig-frame" style="height:390px;position:relative">
      <img src="{I['i17']}" alt="Hard-shell quahog" style="width:100%;height:100%;object-fit:cover;border-radius:8px" onerror="imgErr(this)">
    </div>
    <div class="fig-cap">The hard-shell clam (quahog), <em>Mercenaria mercenaria</em></div>
  </div>
  <div data-animate="scale-fade-in" data-delay="0.5">
    <div class="fig-frame" style="height:390px;position:relative">
      <img src="{I['i19']}" alt="Commercial hard-shell clams" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
    </div>
    <div class="fig-cap">A $4 million annual industry for Rhode Island alone</div>
  </div>
</div>''',title='Mercenaria mercenaria — The Hard-Shell Clam'))

# SLIDE 4 – Global Significance
# r=45, circumference=282.74; 80%=226.19 gap=56.55; 89%=251.64 gap=31.10; 14%=39.58 gap=243.16
slides.append(mkslide(4,f'''
<div style="display:grid;grid-template-columns:44% 1fr;gap:20px;padding:1% 5% 0;margin-top:1%;align-items:center">
  <div data-animate="scale-fade-in" data-delay="0.3">
    <svg viewBox="0 0 270 210" xmlns="http://www.w3.org/2000/svg" style="width:100%">
      <text x="135" y="16" text-anchor="middle" font-size="10" fill="#5a8099" font-style="italic">Bivalves dominate global marine aquaculture</text>
      <!-- Donut 1: 80% US -->
      <circle cx="68" cy="105" r="45" fill="none" stroke="rgba(152,255,152,0.15)" stroke-width="13"/>
      <circle cx="68" cy="105" r="45" fill="none" stroke="#98FF98" stroke-width="13"
              stroke-dasharray="226.19 56.55" transform="rotate(-90 68 105)"/>
      <text x="68" y="101" text-anchor="middle" font-size="20" font-weight="600" fill="#2D2D2D">80%</text>
      <text x="68" y="116" text-anchor="middle" font-size="8.5" fill="#5a8099">of U.S. share</text>
      <text x="68" y="168" text-anchor="middle" font-size="10" font-weight="600" fill="#2D2D2D">U.S. Marine</text>
      <text x="68" y="182" text-anchor="middle" font-size="9" fill="#5a8099">Aquaculture</text>
      <!-- Divider -->
      <line x1="135" y1="35" x2="135" y2="185" stroke="rgba(175,238,238,0.3)" stroke-width="1" stroke-dasharray="3,3"/>
      <!-- Donut 2: 89% Global -->
      <circle cx="202" cy="105" r="45" fill="none" stroke="rgba(175,238,238,0.2)" stroke-width="13"/>
      <circle cx="202" cy="105" r="45" fill="none" stroke="#AFEEEE" stroke-width="13"
              stroke-dasharray="251.64 31.10" transform="rotate(-90 202 105)"/>
      <text x="202" y="101" text-anchor="middle" font-size="20" font-weight="600" fill="#2D2D2D">89%</text>
      <text x="202" y="116" text-anchor="middle" font-size="8.5" fill="#5a8099">of global share</text>
      <text x="202" y="168" text-anchor="middle" font-size="10" font-weight="600" fill="#2D2D2D">Global Marine</text>
      <text x="202" y="182" text-anchor="middle" font-size="9" fill="#5a8099">Bivalve Production</text>
    </svg>
  </div>
  <div style="display:flex;flex-direction:column;gap:14px">
    {card('<div class="card-head">Fastest-growing food sector</div><div class="card-body">Aquaculture is critical to global food security — bivalve production exceeded <strong>15 million tons</strong> annually between 2010–2015, representing <strong>14%</strong> of total global marine production.</div>',0.5)}
    {card('<div class="card-head">Economic and cultural anchor</div><div class="card-body">Wild fisheries account for only 11% of global marine bivalve supply. The remainder is aquaculture — making disease resilience essential for coastal economies and communities.</div>',0.7)}
  </div>
</div>''',title='Global Significance of Bivalve Aquaculture'))

# SLIDE 5 – RI Stakes
slides.append(mkslide(5,f'''
<div style="display:grid;grid-template-columns:42% 1fr;gap:20px;padding:1% 5% 0;margin-top:1%;align-items:center">
  <div data-animate="scale-fade-in" data-delay="0.3">
    <svg viewBox="0 0 260 220" xmlns="http://www.w3.org/2000/svg" style="width:100%">
      <!-- Large clam shell centered -->
      <g transform="translate(130,100) scale(2.2)" opacity="0.9">
        <ellipse cx="0" cy="8" rx="44" ry="30" fill="none" stroke="#AFEEEE" stroke-width="2"/>
        <path d="M -44 8 Q 0 -32 44 8" fill="none" stroke="#AFEEEE" stroke-width="1.6"/>
        <path d="M -37 13 Q 0 -22 37 13" fill="none" stroke="#AFEEEE" stroke-width="1.2"/>
        <path d="M -28 18 Q 0 -12 28 18" fill="none" stroke="#AFEEEE" stroke-width="1.0"/>
        <path d="M -18 22 Q 0 -2 18 22" fill="none" stroke="#AFEEEE" stroke-width="0.8"/>
        <circle cx="0" cy="8" r="4" fill="#AFEEEE"/>
      </g>
      <!-- $4M label centered on shell -->
      <text x="130" y="92" text-anchor="middle" font-size="28" font-weight="600" fill="#2D2D2D">$4M</text>
      <text x="130" y="112" text-anchor="middle" font-size="11" fill="#5a8099">annual Rhode Island</text>
      <text x="130" y="126" text-anchor="middle" font-size="11" fill="#5a8099">hard clam landings</text>
      <!-- Bottom context row -->
      <rect x="20" y="155" width="220" height="1" fill="rgba(175,238,238,0.4)"/>
      <text x="130" y="175" text-anchor="middle" font-size="9.5" fill="#5a8099" font-style="italic">One of New England's most economically and culturally significant fisheries</text>
    </svg>
  </div>
  <div style="display:flex;flex-direction:column;gap:14px">
    {stcard('$4M','Annual commercial value — Rhode Island hard clam landings alone',0.5)}
    {acard('<div class="card-head">Cultural keystone</div><div class="card-body">Hard-shell clam harvesting is a vital cultural resource for coastal communities throughout New England — and a bellwether for coastal ecosystem health.</div>',0.7,AC['I'])}
  </div>
</div>''',title='The Stakes for Rhode Island'))

# SLIDE 6 – The Threat
slides.append(mkslide(6,f'''
<div class="layout-d">
  <div style="font-size:1.15em;color:#2D2D2D;max-width:65%;line-height:1.6" data-animate="text-emerge" data-delay="0.2">But these economic and cultural foundations are now under increasing threat from emerging infectious diseases —</div>
  <div style="font-size:1.8em;font-weight:600;color:{AC["II"]};margin-top:8px" data-animate="stat-reveal" data-delay="0.65">Bivalve Transmissible Neoplasia</div>
</div>'''))

# SLIDE 7 – What BTN Is
slides.append(mkslide(7,f'''
<div style="display:grid;grid-template-columns:52% 1fr;gap:20px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i22','BTN Diagram','Normal hemocytes match host genotype; neoplastic BTN cells are clonal, foreign, and spread horizontally between animals.',0.3,'400px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
    {acard('<div class="card-head">Leukemia-like condition</div><div class="card-body">Abnormal proliferation of hemocytes (immune blood cells); documented in mussels, clams, and cockles.</div>',0.45,AC['II'])}
    {acard('<div class="card-head">Clonal parasitism</div><div class="card-body">BTN malignant cells act as clonal parasites, spreading <em>horizontally</em> between host animals.</div>',0.6,AC['II'])}
    {acard('<div class="card-head">Broad reach</div><div class="card-body">At least <strong>8 independent BTN lineages</strong> documented across <strong>15 bivalve species</strong>; BTN cells survive up to <strong>19 days</strong> in seawater.</div>',0.75,AC['II'])}
  </div>
</div>''',title='Hemic Neoplasia and Bivalve Transmissible Cancer'))

# SLIDE 8 – Why We Care
slides.append(mkslide(8,f'''
<div class="layout-d">
  <div style="font-size:2em;font-weight:600;color:#2D2D2D" data-animate="stat-reveal" data-delay="0.3">So why do we care?</div>
</div>'''))

# SLIDE 9 – Wellfleet Outbreak
slides.append(mkslide(9,f'''
<div style="display:flex;flex-direction:column;gap:12px;padding:1% 5% 0;margin-top:0.5%">
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px">
    {card('<div class="card-head">First detection — 2009</div><div class="card-body">BTN first monitored in <strong>Wellfleet Harbor, MA</strong>. By 2012, disease had spread across multiple farms — no rapid containment tool existed.</div>',0.4)}
    {stcard('80–90%','Mortality rate in affected populations — one of the most impactful bivalve diseases known',0.55)}
    {acard('<div class="card-head">Diagnostic void</div><div class="card-body">No transferable, rapid, presymptomatic detection tool existed for quahogs at the time of the outbreak.</div>',0.7,AC['II'])}
  </div>
  <div data-animate="scale-fade-in" data-delay="0.85">
    <svg viewBox="0 0 700 100" xmlns="http://www.w3.org/2000/svg" style="width:100%">
      <!-- Timeline backbone -->
      <line x1="80" y1="42" x2="620" y2="42" stroke="#AFEEEE" stroke-width="1.8"/>
      <polygon points="618,36 632,42 618,48" fill="#AFEEEE"/>
      <!-- Node 1: 2009 -->
      <circle cx="150" cy="42" r="9" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.5"/>
      <text x="150" y="24" text-anchor="middle" font-size="12" font-weight="600" fill="#2D2D2D">2009</text>
      <text x="150" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#2D2D2D">First Detection</text>
      <text x="150" y="75" text-anchor="middle" font-size="8.5" fill="#5a8099">Wellfleet Harbor, MA</text>
      <!-- Node 2: 2012 -->
      <circle cx="350" cy="42" r="9" fill="{AC['II']}" stroke="#0C447C" stroke-width="1.5"/>
      <text x="350" y="24" text-anchor="middle" font-size="12" font-weight="600" fill="#2D2D2D">2012</text>
      <text x="350" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#2D2D2D">Outbreak Spreads</text>
      <text x="350" y="75" text-anchor="middle" font-size="8.5" fill="#5a8099">Multiple farms · 80–90% mortality</text>
      <!-- Node 3: 2025 -->
      <circle cx="560" cy="42" r="9" fill="{AC['V']}" stroke="#791F1F" stroke-width="1.5"/>
      <text x="560" y="24" text-anchor="middle" font-size="12" font-weight="600" fill="#2D2D2D">2025</text>
      <text x="560" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#2D2D2D">This Research</text>
      <text x="560" y="75" text-anchor="middle" font-size="8.5" fill="#5a8099">First ML diagnostic framework for <tspan font-style="italic">M. mercenaria</tspan></text>
    </svg>
  </div>
</div>''',title='The BTN Quahog Wellfleet Outbreak (2009)'))

# SLIDE 10 – Detection Challenge (merged 10+11)
slides.append(mkslide(10,f'''
<div class="layout-d" style="gap:20px">
  <div style="font-size:1.3em;color:#5a8099;max-width:60%" data-animate="text-emerge" data-delay="0.2">The central management challenge with BTN is not treatment…</div>
  <div style="font-size:2.8em;font-weight:600;color:#2D2D2D" data-animate="stat-reveal" data-delay="0.7">It is detection.</div>
</div>'''))

# SLIDE 11 – Why Detection Is Hard
slides.append(mkslide(11,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:1% 5% 0;margin-top:0.5%">
  <div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;height:305px">
      <div class="fig-frame" style="height:100%;position:relative" data-animate="scale-fade-in" data-delay="0.3">
        <div class="fig-lbl">Cytology</div>
        <img src="{I['i16']}" alt="Cytology" style="width:100%;height:100%;object-fit:cover" onerror="imgErr(this)">
      </div>
      <div class="fig-frame" style="height:100%;position:relative" data-animate="scale-fade-in" data-delay="0.5">
        <div class="fig-lbl">Histology</div>
        <img src="{I['i18']}" alt="Histology" style="width:100%;height:100%;object-fit:cover" onerror="imgErr(this)">
      </div>
    </div>
    <div class="fig-cap" data-animate="text-emerge" data-delay="0.7">Current diagnostic methods — cytological and histological techniques</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:14px;margin-top:4px">
    {acard('<div class="card-head">Current methods fall short</div><div class="card-body">Histological and cytological techniques are time-consuming, lack sensitivity and specificity, or are too expensive for routine use.</div>',0.55,AC['II'])}
    {acard('<div class="card-head">Not transferable to quahogs</div><div class="card-body">Molecular diagnostic tools developed for BTN in other bivalve species are not transferable to <em>M. mercenaria</em> (Santamarina et al., 2024).</div>',0.75,AC['II'])}
  </div>
</div>''',title='The Detection Gap'))

# SLIDE 12 – Research Question
slides.append(mkslide(12,f'''
<div class="layout-d" style="gap:16px">
  <div style="font-size:1.5em;font-weight:600;color:#2D2D2D;max-width:65%;line-height:1.4;text-align:center" data-animate="stat-reveal" data-delay="0.35">Can we create diagnostic tools capable of identifying BTN at the <em>presymptomatic</em> stage?</div>
  <div style="display:flex;gap:10px;margin-top:8px" data-animate="text-emerge" data-delay="0.8">
    {pill('Single-cell RNA-seq','blue')} {pill('Machine Learning','lavender')} {pill('Biomarker Discovery','mint')}
  </div>
</div>'''))

# SLIDE 13 – Roadmap
# NEW: horizontal SVG flow diagram (old 4-card layout preserved below as fallback)
slides.append(mkslide(13,f'''
<div style="display:flex;flex-direction:column;align-items:center;gap:16px;padding:2% 4% 0;margin-top:1%">
  <div style="display:grid;grid-template-columns:1fr 36px 1fr 36px 1fr 36px 1fr;align-items:center;gap:0;width:100%" data-animate="text-emerge" data-delay="0.3">
    <div style="background:#fff;border:1.5px solid {AC['III']};border-radius:12px;padding:18px 12px;text-align:center;position:relative">
      <div style="font-size:1.6em;font-weight:600;color:{AC['III']};line-height:1">01</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D;margin-top:6px">Experimental</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D">Design</div>
      <div style="font-size:0.72em;color:#5a8099;margin-top:6px;line-height:1.4">BTN exposure; scRNA-seq</div>
    </div>
    <div style="text-align:center;font-size:1.2em;color:{AC['III']};font-weight:600">&#8594;</div>
    <div style="background:#fff;border:1.5px solid {AC['III']};border-radius:12px;padding:18px 12px;text-align:center" data-animate="text-emerge" data-delay="0.5">
      <div style="font-size:1.6em;font-weight:600;color:{AC['III']};line-height:1">02</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D;margin-top:6px">ML</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D">Classification</div>
      <div style="font-size:0.72em;color:#5a8099;margin-top:6px;line-height:1.4">SVM · neoplastic vs. normal</div>
    </div>
    <div style="text-align:center;font-size:1.2em;color:{AC['III']};font-weight:600">&#8594;</div>
    <div style="background:#fff;border:1.5px solid {AC['III']};border-radius:12px;padding:18px 12px;text-align:center" data-animate="text-emerge" data-delay="0.65">
      <div style="font-size:1.6em;font-weight:600;color:{AC['III']};line-height:1">03</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D;margin-top:6px">Biomarker</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D">Discovery</div>
      <div style="font-size:0.72em;color:#5a8099;margin-top:6px;line-height:1.4">Feature importance; cancer hallmarks</div>
    </div>
    <div style="text-align:center;font-size:1.2em;color:{AC['III']};font-weight:600">&#8594;</div>
    <div style="background:#fff;border:1.5px solid {AC['III']};border-radius:12px;padding:18px 12px;text-align:center" data-animate="text-emerge" data-delay="0.8">
      <div style="font-size:1.6em;font-weight:600;color:{AC['III']};line-height:1">04</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D;margin-top:6px">Genotype</div>
      <div style="font-size:0.85em;font-weight:600;color:#2D2D2D">Validation</div>
      <div style="font-size:0.72em;color:#5a8099;margin-top:6px;line-height:1.4">SNP confirmation of ML predictions</div>
    </div>
  </div>
  <div style="font-size:0.78em;color:#5a8099;font-style:italic;text-align:center;max-width:70%;line-height:1.5" data-animate="text-emerge" data-delay="0.95">Each phase builds on the last — from controlled infection experiment through machine learning to biological validation</div>
</div>''',title='Flow of Today\'s Research'))
# OLD 4-card layout (kept for revert if needed):
# slides.append(mkslide(13,f'''
# <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:1% 5% 0;margin-top:1%">
#   {acard('<div style="font-size:1.4em;font-weight:600;color:#2D2D2D;margin-bottom:6px">01</div><div class="card-head">Experimental Design</div><div class="card-body">Controlled BTN exposure experiments; single-cell sequencing</div>',0.35,AC['III'])}
#   {acard('<div style="font-size:1.4em;font-weight:600;color:#2D2D2D;margin-bottom:6px">02</div><div class="card-head">ML Classification</div><div class="card-body">Train SVM to distinguish neoplastic from normal hemocytes</div>',0.5,AC['III'])}
#   {acard('<div style="font-size:1.4em;font-weight:600;color:#2D2D2D;margin-bottom:6px">03</div><div class="card-head">Biomarker Discovery</div><div class="card-body">Extract &amp; validate discriminative gene features; map to cancer hallmarks</div>',0.65,AC['III'])}
#   {acard('<div style="font-size:1.4em;font-weight:600;color:#2D2D2D;margin-bottom:6px">04</div><div class="card-head">Genotype Validation</div><div class="card-body">Confirm ML predictions against independent SNP genotyping</div>',0.8,AC['III'])}
# </div>''',title='Flow of Today\'s Research'))

# SLIDE 14 – Experimental Design Intro (merged 15+16)
slides.append(mkslide(14,f'''
<div class="layout-d" style="gap:14px">
  <div style="font-size:2.2em;font-weight:600;color:#2D2D2D" data-animate="stat-reveal" data-delay="0.25">Experimental Design</div>
  <div style="width:50px;height:2px;background:{AC["III"]};margin:4px auto" data-animate="text-emerge" data-delay="0.45"></div>
  <div style="font-size:1em;color:#5a8099;max-width:55%;line-height:1.6" data-animate="text-emerge" data-delay="0.55">To detect neoplasia, we need samples from animals confirmed to be infected — and from animals confirmed to be normal.</div>
</div>'''))

# SLIDE 15 – 1st Round
slides.append(mkslide(15,f'''
<div style="display:grid;grid-template-rows:1fr auto;padding:1% 5% 0;gap:10px;height:100%">
  <div style="display:flex;flex-direction:column;gap:8px">
    <div class="fig-frame" style="flex:1;min-height:0;position:relative" data-animate="scale-fade-in" data-delay="0.3">
      <div class="fig-lbl">Trial 1 — Exposure Tank</div>
      <img src="{I['exp']}" alt="Exposure tank" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
    </div>
    <div class="fig-cap" data-animate="text-emerge" data-delay="0.75">1st Round · Exposure timepoints: 33, 92, and 100 days</div>
  </div>
  <div style="display:flex;gap:10px" data-animate="text-emerge" data-delay="0.85">
    {pill('33 Days Exposure','blue')} {pill('92 Days Exposure','blue')} {pill('100 Days Exposure','blue')}
  </div>
  <div style="position:absolute;bottom:42px;left:0;right:0;text-align:right;padding:0 5%;font-size:0.6em;color:#5a8099;font-style:italic" data-animate="text-emerge" data-delay="1.0">Samson et al. 2025</div>
</div>''',title='First Round Exposure'))

# SLIDE 16 – Full Experimental Design (4 images)
slides.append(mkslide(16,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;padding:1% 5% 0;margin-top:0.5%">
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.3">
    <div class="fig-lbl">Source Clam → Tank</div>
    <img src="{I['ctrl']}" alt="Source clam added to tank" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.45">
    <div class="fig-lbl">Exposure Tank</div>
    <img src="{I['exp']}" alt="Exposure tank" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.6">
    <div class="fig-lbl">scRNA-seq Workflow</div>
    <img src="{I['seq']}" alt="10x Genomics workflow" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.75">
    <div class="fig-lbl">Single-Cell Capture</div>
    <img src="{I['i1']}" alt="Single-cell microscopy" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
</div>''',title='Single-Cell Transcriptomic Experimental Design'))

# SLIDE 17 – 2nd Round (comparison)
slides.append(mkslide(17,f'''
<div style="display:grid;grid-template-columns:1fr 48px 1fr;gap:10px;padding:1% 4% 0;align-items:center;margin-top:1%">
  <div>
    <div class="fig-frame" style="height:315px;position:relative" data-animate="scale-fade-in" data-delay="0.3">
      <div class="fig-lbl">Exposure Tank</div>
      <img src="{I['exp']}" alt="Exposure" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
    </div>
    <div class="fig-cap" data-animate="text-emerge" data-delay="0.7">Neoplastic source clam added — BTN cells transmitted to naive animals</div>
  </div>
  <div style="text-align:center;font-size:1.5em;color:#AFEEEE;font-weight:600" data-animate="text-emerge" data-delay="0.5">vs.</div>
  <div>
    <div class="fig-frame" style="height:315px;position:relative" data-animate="scale-fade-in" data-delay="0.5">
      <div class="fig-lbl">Control Tank</div>
      <img src="{I['ctrl']}" alt="Control" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
    </div>
    <div class="fig-cap" data-animate="text-emerge" data-delay="0.85">Normal (non-neoplastic) clam added — uninfected baseline</div>
  </div>
</div>''',title='Second Round — Exposure vs. Control'))

# SLIDE 18 – Timepoints (4 images)
slides.append(mkslide(18,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;padding:1% 5% 0;margin-top:0.5%">
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.3">
    <div class="fig-lbl">Normal</div>
    <img src="{I['nrm']}" alt="Normal" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.45">
    <div class="fig-lbl">Neoplastic</div>
    <img src="{I['exp']}" alt="Neoplastic" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.6">
    <div class="fig-lbl">5-Day Exposure</div>
    <img src="{I['exp']}" alt="5-Day Exposure" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-frame" style="position:relative" data-animate="scale-fade-in" data-delay="0.75">
    <div class="fig-lbl">12-Day Exposure</div>
    <img src="{I['exp']}" alt="12-Day Exposure" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
</div>''',title='Four Sampling Conditions'))

# SLIDE 19 – Why scRNA-seq
slides.append(mkslide(19,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:1% 5% 0;margin-top:2%">
  {acard('<div class="card-head">Cell-level resolution</div><div class="card-body">Single-cell RNA sequencing captures the <em>individual transcriptome</em> of each cell — enabling classification at the resolution where neoplasia manifests.</div>',0.4,AC['III'])}
  {acard('<div class="card-head">Expression-based classification</div><div class="card-body">Each cell can be assigned to a class (neoplastic vs. normal) based on its gene expression profile — creating a labeled dataset for machine learning.</div>',0.6,AC['III'])}
</div>
<div style="padding:0 5%;margin-top:8px" data-animate="text-emerge" data-delay="0.8">
  <div style="display:flex;gap:10px;flex-wrap:wrap">
    {pill('61,658 labeled hemocyte transcriptomes','mint')}
    {pill('99,969 total cells including genotype','blue')}
    {pill('13,974 cells · 5-day post-exposure pool','lavender')}
  </div>
</div>''',title='Why Single-Cell Sequencing?'))

# SLIDE 20 – Bridge to ML (merged 22+23)
slides.append(mkslide(20,f'''
<div class="layout-d" style="gap:14px">
  <div style="font-size:1em;color:#5a8099;max-width:60%;line-height:1.6" data-animate="text-emerge" data-delay="0.2">We have single-cell RNA sequencing data from both trials. What is the next step in our analysis?</div>
  <div style="font-size:2.6em;font-weight:600;color:#2D2D2D" data-animate="stat-reveal" data-delay="0.65">Machine Learning</div>
</div>'''))

# SLIDE 21 – ML Defined
slides.append(mkslide(21,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:1% 5% 0;margin-top:2%">
  {card('<div class="card-head">What it is</div><div class="card-body">Machine learning is when a computer learns patterns from data so it can make predictions or decisions <em>without being told every rule explicitly</em>.</div>',0.4)}
  {card('<div class="card-head">What it asks</div><div class="card-body">Which genes — in combination — provide the best separation of two classes in high-dimensional multivariate space? <span style="font-size:0.85em;color:#5a8099">(Pedregosa et al., 2011; Alquicira-Hernandez et al., 2019)</span></div>',0.6)}
</div>''',title='Machine Learning'))

# SLIDE 22 – Model Selection Context
slides.append(mkslide(22,f'''
<div style="padding:1% 5% 0;margin-top:1%">
  {card('<div class="card-head">The classification task</div><div class="card-body">We need a model that can classify <strong>confirmed neoplastic</strong> and <strong>confirmed normal</strong> hemocytes — trained on Trial 1 confirmed cells and validated on held-out Trial 2 data.<br><br>We evaluated multiple model families, requiring high-dimensional support, interpretability, and generalization.</div>',0.4)}
</div>''',title='Classifying Confirmed Neoplastic and Normal Cells'))

# SLIDE 23 – Why SVM
slides.append(mkslide(23,f'''
<div style="display:grid;grid-template-columns:48% 1fr;gap:20px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i15','SVM Concept','The SVM finds the hyperplane that maximizes the margin between two classes. Support vectors are the critical boundary points.',0.3,'380px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:14px;margin-top:4px">
    {acard('<div class="card-head">Built for high-dimensional data</div><div class="card-body">SVM is better suited than tree-based methods for high-dimensional, low-sample biological data where interpretability and generalization are critical.</div>',0.45,AC['III'])}
    {acard('<div class="card-head">Linear interpretability</div><div class="card-body">Linear SVM weight vectors directly report feature (gene) importance — each coefficient is a biomarker candidate score.</div>',0.65,AC['III'])}
  </div>
</div>''',title='Support Vector Machine (SVM)'))

# SLIDE 24 – Framework
slides.append(mkslide(24,f'''
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:1% 5% 0;margin-top:2%">
  {acard('<div style="font-size:1.3em;font-weight:600;margin-bottom:6px;color:#2D2D2D">01</div><div class="card-head">70 / 30 Split</div><div class="card-body">70% of confirmed hemocytes held for testing. Model trained on the remaining 30% — prevents overfitting.</div>',0.4,AC['III'])}
  {acard('<div style="font-size:1.3em;font-weight:600;margin-bottom:6px;color:#2D2D2D">02</div><div class="card-head">Three HVG Configurations</div><div class="card-body">Models run across 3,000 HVG · 5,000 HVG · all genes — ensuring robustness across feature-set choices.</div>',0.55,AC['III'])}
  {acard('<div style="font-size:1.3em;font-weight:600;margin-bottom:6px;color:#2D2D2D">03</div><div class="card-head">5-Fold Cross-Validation</div><div class="card-body">Grid search over C ∈ {{0.1…10}} × PCA components ∈ {{10…100}} within training split only.</div>',0.7,AC['III'])}
</div>''',title='Model Framework: 70/30 Split'))

# SLIDE 25 – SVM Pipeline Animation
slides.append(mkslide(25,f'''
<div id="svm-widget" style="display:flex;flex-direction:column;gap:6px;padding:0 3% 0;margin-top:0.5%;height:calc(100% - 36px)">
  <div id="svm-prog-wrap" style="height:4px;background:rgba(152,255,152,0.2);border-radius:2px;overflow:hidden;flex-shrink:0">
    <div id="svm-prog" style="height:100%;width:0%;background:#98FF98;transition:width 0.5s ease"></div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 210px;gap:14px;flex:1;min-height:0">
  <div style="display:flex;flex-direction:column;gap:6px;min-height:0">
    <svg id="svm-svg" viewBox="0 0 300 240" preserveAspectRatio="xMidYMid meet" style="width:100%;flex:1;min-height:0;border:0.5px solid rgba(175,238,238,0.4);border-radius:8px;background:#fafeff">
      <!-- Axis labels -->
      <text id="svm-xlab" x="150" y="235" text-anchor="middle" font-size="9" fill="#5a8099">Raw Counts</text>
      <text id="svm-ylab" x="8" y="125" text-anchor="middle" font-size="9" fill="#5a8099" transform="rotate(-90,8,125)">Expression</text>
      <!-- Zone backgrounds (hidden until step 4) -->
      <rect id="neo-zone" x="0" y="0" width="148" height="230" fill="#E6E6FA" opacity="0" rx="6"/>
      <rect id="norm-zone" x="152" y="0" width="148" height="230" fill="#AFEEEE" opacity="0" rx="6"/>
      <!-- Zone labels -->
      <text id="neo-zone-lbl" x="74" y="20" text-anchor="middle" font-size="9" fill="#7F77DD" opacity="0" font-weight="600">Neoplastic</text>
      <text id="norm-zone-lbl" x="226" y="20" text-anchor="middle" font-size="9" fill="#185FA5" opacity="0" font-weight="600">Normal</text>
      <!-- HVG annotation (step 3) -->
      <text id="hvg-ann" x="150" y="245" text-anchor="middle" font-size="8" fill="#3C3489" opacity="0">HVG 3,000 / 5,000 / All Genes</text>
      <!-- Scanning line (step 5) -->
      <line id="scan-line" x1="80" y1="15" x2="80" y2="225" stroke="#E6E6FA" stroke-width="2" stroke-dasharray="4,3" opacity="0"/>
      <!-- Decision boundary (step 6) -->
      <line id="dec-boundary" x1="148" y1="15" x2="148" y2="225" stroke="#98FF98" stroke-width="2.5" opacity="0" stroke-dasharray="400" stroke-dashoffset="400"/>
      <!-- Margin lines (step 6) -->
      <line id="margin-l" x1="112" y1="15" x2="112" y2="225" stroke="#98FF98" stroke-width="1" stroke-dasharray="5,4" opacity="0"/>
      <line id="margin-r" x1="192" y1="15" x2="192" y2="225" stroke="#98FF98" stroke-width="1" stroke-dasharray="5,4" opacity="0"/>
      <!-- Margin arrow (step 6) -->
      <g id="margin-arrow" opacity="0">
        <line x1="112" y1="115" x2="192" y2="115" stroke="#98FF98" stroke-width="1.5" marker-start="url(#ah)" marker-end="url(#ah)"/>
        <text x="152" y="110" text-anchor="middle" font-size="8" fill="#98FF98" font-weight="600">max margin</text>
        <defs><marker id="ah" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#98FF98"/></marker></defs>
      </g>
      <!-- AUC Badge (step 6) -->
      <g id="auc-badge" opacity="0" transform="translate(222,185)">
        <rect x="0" y="0" width="68" height="36" rx="6" fill="rgba(240,248,255,0.95)" stroke="#AFEEEE" stroke-width="0.8"/>
        <text x="34" y="13" text-anchor="middle" font-size="8" fill="#5a8099">AUC</text>
        <text x="34" y="29" text-anchor="middle" font-size="13" fill="#2D2D2D" font-weight="600">0.9985</text>
      </g>
      <!-- Support vector rings (step 6) -->
      <circle id="sv1" cx="108" cy="138" r="10" fill="none" stroke="#7F77DD" stroke-width="1.8" opacity="0"/>
      <circle id="sv2" cx="95" cy="122" r="10" fill="none" stroke="#7F77DD" stroke-width="1.8" opacity="0"/>
      <circle id="sv3" cx="190" cy="85" r="10" fill="none" stroke="#185FA5" stroke-width="1.8" opacity="0"/>
      <!-- Support vector label -->
      <text id="sv-lbl" x="152" y="225" text-anchor="middle" font-size="8" fill="#5a8099" opacity="0">support vectors define the margin</text>
      <!-- NEO POINTS (15) -->
      <g id="np0" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np1" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np2" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np3" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np4" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np5" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np6" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np7" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np8" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np9" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np10" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np11" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np12" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np13" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <g id="np14" style="transition:transform 1.2s ease"><circle r="5.5" fill="#E6E6FA" stroke="#7F77DD" stroke-width="1.3"/></g>
      <!-- NORMAL POINTS (15) -->
      <g id="mp0" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp1" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp2" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp3" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp4" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp5" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp6" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp7" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp8" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp9" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp10" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp11" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp12" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp13" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
      <g id="mp14" style="transition:transform 1.2s ease"><circle r="5.5" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.3"/></g>
    </svg>
    <div id="svm-caption" style="font-size:0.6em;color:#5a8099;font-style:italic;line-height:1.4;flex-shrink:0">CPM normalization applied — counts scaled to counts-per-million per cell</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:8px;overflow:hidden">
    <div id="svm-steps" style="display:flex;flex-direction:column;gap:5px;flex:1">
      <div class="svm-step future" id="ss0"><div class="svm-step-num">1</div><div><div class="svm-step-title">CPM Normalization</div><div class="svm-step-sub">Scale raw counts to library size</div></div></div>
      <div class="svm-step future" id="ss1"><div class="svm-step-num">2</div><div><div class="svm-step-title">Log Transform</div><div class="svm-step-sub">log₂(CPM+1) — variance stabilization</div></div></div>
      <div class="svm-step future" id="ss2"><div class="svm-step-num">3</div><div><div class="svm-step-title">HVG Selection</div><div class="svm-step-sub">Seurat v3 · 3K / 5K / all genes</div></div></div>
      <div class="svm-step future" id="ss3"><div class="svm-step-num">4</div><div><div class="svm-step-title">Scaling + PCA</div><div class="svm-step-sub">Fit on training data only — no leakage</div></div></div>
      <div class="svm-step future" id="ss4"><div class="svm-step-num">5</div><div><div class="svm-step-title">Grid Search</div><div class="svm-step-sub">C × PCA components · 5-fold CV</div></div></div>
      <div class="svm-step future" id="ss5"><div class="svm-step-num">6</div><div><div class="svm-step-title">Max-Margin Boundary</div><div class="svm-step-sub">AUC = 0.9985 on held-out test</div></div></div>
    </div>
    <div id="c-pills-wrap" style="display:none;padding:8px;background:rgba(230,230,250,0.1);border-radius:8px">
      <div style="font-size:0.6em;color:#5a8099;margin-bottom:4px;font-weight:600">C values tested:</div>
      <div style="display:flex;gap:4px;flex-wrap:wrap" id="c-pills">
        <span class="c-pill" data-c="0.1">0.1</span><span class="c-pill" data-c="0.5">0.5</span>
        <span class="c-pill" data-c="1">1</span><span class="c-pill" data-c="2">2</span>
        <span class="c-pill" data-c="5">5</span><span class="c-pill" data-c="10">10</span>
      </div>
      <div style="font-size:0.6em;color:#5a8099;margin:6px 0 4px;font-weight:600">PCA components:</div>
      <div style="display:flex;gap:4px;flex-wrap:wrap" id="pca-pills">
        <span class="pca-pill" data-pca="10">10</span><span class="pca-pill" data-pca="20">20</span>
        <span class="pca-pill" data-pca="30">30</span><span class="pca-pill" data-pca="40">40</span>
        <span class="pca-pill" data-pca="50">50</span><span class="pca-pill" data-pca="75">75</span>
        <span class="pca-pill" data-pca="100">100</span>
      </div>
    </div>
  </div>
  </div>
</div>''',title='What the Classifier Is Actually Doing'))

# SLIDE 26 – Gold Standard Results (merged 30+31)
slides.append(mkslide(26,f'''
<div style="display:grid;grid-template-columns:52% 1fr;gap:20px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i13','ROC Curve','Gold-Standard 70/30 Model · HVG 5,000 · Bal. Acc. = 0.986',0.3,'380px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:14px;margin-top:4px">
    {stcard('0.9985','Area Under the Curve (AUC) — near-perfect separation of neoplastic from normal hemocytes',0.5)}
    {stcard('0.986','Balanced accuracy — equal performance across both classes',0.65)}
    {acard('<div class="card-head">18,491 hemocytes</div><div class="card-body">Evaluated on a held-out 30% test split of confirmed neoplastic and normal cells; 5,000 highly variable genes; linear SVM kernel.</div>',0.8,AC['IV'])}
  </div>
</div>''',title='Gold Standard Model — 70/30 Split, 5,000 HVG'))

# SLIDE 27 – Feature Coefficients
slides.append(mkslide(27,f'''
<div style="display:grid;grid-template-columns:48% 1fr;gap:20px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i13','ROC Curve (reference)','The same model whose coefficients will now be used for biomarker discovery',0.3,'340px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:14px;margin-top:4px">
    {acard('<div class="card-head">What the model gives us next</div><div class="card-body">A linear SVM weight vector assigns a coefficient to <em>every gene</em>. Genes with the largest absolute coefficients are the strongest discriminators between neoplastic and normal states.</div>',0.45,AC['IV'])}
    {acard('<div class="card-head">406 biomarker candidates</div><div class="card-body">Feature importance extracted across all three HVG configurations — 46 genes appearing in all three configurations became the core candidate list.</div>',0.65,AC['IV'])}
  </div>
</div>''',title='Gold Standard Model — Feature Importance'))

# SLIDE 28 – Bridge: Test Biological Relevance
slides.append(mkslide(28,f'''
<div class="layout-d" style="gap:14px">
  <div style="font-size:1.3em;color:#5a8099;max-width:60%;line-height:1.6" data-animate="text-emerge" data-delay="0.2">Are the genes the model thinks are important…</div>
  <div style="font-size:1.8em;font-weight:600;color:#2D2D2D;max-width:65%;line-height:1.3" data-animate="stat-reveal" data-delay="0.6">actually biologically meaningful — or are they just mathematical artifacts?</div>
</div>'''))

# SLIDE 29 – Robustness Filter
slides.append(mkslide(29,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:1% 5% 0;margin-top:2%">
  {card('<div class="card-head">Feature importance defined</div><div class="card-body">Feature importance was extracted from linear SVM weight vectors for <em>each</em> of the three HVG configurations — measuring how much each gene contributes to classification.</div>',0.4)}
  {acard('<div class="card-head">The robustness filter</div><div class="card-body">A single model may identify features discriminative under its specific configuration but unreliable across others — a recognized vulnerability in single-cell biomarker studies (Squair et al., 2021). Only genes ranked highly across <em>all three configurations</em> were retained.</div>',0.6,AC['IV'])}
</div>''',title='Biomarker Discovery — The Robustness Filter'))

# SLIDE 30 – Top 20 Biomarkers
slides.append(mkslide(30,f'''
<div style="display:grid;grid-template-columns:55% 1fr;gap:16px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i9','Top 20 Biomarkers','Absolute SVM coefficient magnitude · Gold-Standard 70/30 Model · HVG 5,000',0.3,'400px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:8px;margin-top:4px">
    <div style="font-size:0.7em;font-weight:600;color:#5a8099;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:2px" data-animate="text-emerge" data-delay="0.35">Cancer Hallmarks Mapped</div>
    {acard('<div class="card-head" style="font-size:0.82em">Immune Evasion</div><div class="card-body" style="font-size:0.75em">Non-self hemocytes escape host immune recognition — a hallmark of transmissible cancers.</div>',0.45,AC['IV'])}
    {acard('<div class="card-head" style="font-size:0.82em">Cell Migration</div><div class="card-body" style="font-size:0.75em">Neoplastic cells acquire motility, enabling horizontal spread between animals via seawater.</div>',0.55,AC['IV'])}
    {acard('<div class="card-head" style="font-size:0.82em">Apoptosis Inhibition</div><div class="card-body" style="font-size:0.75em">BTN cells suppress programmed cell death pathways, sustaining clonal proliferation.</div>',0.65,AC['IV'])}
    {acard('<div class="card-head" style="font-size:0.82em">Autophagy Upregulation</div><div class="card-body" style="font-size:0.75em">Increased autophagy provides energy and metabolic recycling for rapid tumor growth.</div>',0.75,AC['IV'])}
    {acard('<div class="card-head" style="font-size:0.82em">Warburg Effect</div><div class="card-body" style="font-size:0.75em">Shift to aerobic glycolysis — a metabolic reprogramming signature shared across cancer types.</div>',0.85,AC['IV'])}
  </div>
</div>
<div style="padding:0 4%;margin-top:4px" data-animate="text-emerge" data-delay="0.9">
  {pill('top-ranked: Beta-hexosaminidase','lavender')}
</div>''',title='Top 20 Gold-Standard Biomarkers'))

# SLIDE 31 – Validation + Next (merged 36+37)
slides.append(mkslide(31,f'''
<div class="layout-d" style="gap:18px">
  <div style="font-size:1.6em;font-weight:600;color:#2D2D2D;max-width:60%;line-height:1.3" data-animate="stat-reveal" data-delay="0.3">Model features map onto known cancer hallmarks.</div>
  <div style="font-size:0.95em;color:#5a8099;max-width:55%" data-animate="text-emerge" data-delay="0.6">Our model is not finding random statistical artifacts — it is recovering biologically coherent signals.</div>
  <div style="font-size:1em;color:#2D2D2D;max-width:60%;line-height:1.5;border-left:3px solid {AC["IV"]};padding-left:14px" data-animate="text-emerge" data-delay="0.8">Next question: how many of these genes do we actually <em>need</em> to classify a cell as neoplastic?</div>
</div>'''))

# SLIDE 32 – Complexity Analysis
slides.append(mkslide(32,f'''
<div style="display:grid;grid-template-columns:56% 1fr;gap:18px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i10','Complexity Analysis','AUC · Balanced Accuracy · Brier Score vs. number of top-ranked genes (Gold-Standard 70/30 model)',0.3,'380px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
    {acard('<div class="card-head">AUC</div><div class="card-body">Higher = better. Near 1.0 = excellent class separation. Near 0.5 = random guessing.</div>',0.45,AC['IV'])}
    {acard('<div class="card-head">Balanced Accuracy</div><div class="card-body">Equal weight to both classes — prevents a majority-class classifier from appearing strong.</div>',0.6,AC['IV'])}
    {acard('<div class="card-head">Brier Score</div><div class="card-body">Lower = better probability calibration. Mean squared error between predicted probability and true label.</div>',0.75,AC['IV'])}
  </div>
</div>''',title='Parsimonious Models and Complexity Analysis'))

# SLIDE 33 – Summary
slides.append(mkslide(33,f'''
<div style="display:grid;grid-template-columns:55% 1fr;gap:18px;padding:1% 4% 0;margin-top:0.5%">
  <svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;border:1px solid rgba(175,238,238,.4);border-radius:10px;background:#fafeff" data-animate="scale-fade-in" data-delay="0.3">
    <!-- Axes -->
    <line x1="45" y1="20" x2="45" y2="165" stroke="#AFEEEE" stroke-width="1"/>
    <line x1="45" y1="165" x2="300" y2="165" stroke="#AFEEEE" stroke-width="1"/>
    <!-- Y axis label -->
    <text x="12" y="95" text-anchor="middle" font-size="9" fill="#5a8099" transform="rotate(-90,12,95)" font-family="-apple-system,sans-serif">AUC</text>
    <!-- X axis label -->
    <text x="172" y="182" text-anchor="middle" font-size="9" fill="#5a8099" font-family="-apple-system,sans-serif">Number of top-ranked genes</text>
    <!-- X axis ticks -->
    <text x="65" y="175" text-anchor="middle" font-size="8" fill="#5a8099" font-family="-apple-system,sans-serif">1</text>
    <text x="100" y="175" text-anchor="middle" font-size="8" fill="#5a8099" font-family="-apple-system,sans-serif">3</text>
    <text x="135" y="175" text-anchor="middle" font-size="8" fill="#5a8099" font-family="-apple-system,sans-serif">5</text>
    <text x="170" y="175" text-anchor="middle" font-size="8" fill="#5a8099" font-family="-apple-system,sans-serif">7</text>
    <text x="205" y="175" text-anchor="middle" font-size="8" fill="#5a8099" font-family="-apple-system,sans-serif">10</text>
    <text x="255" y="175" text-anchor="middle" font-size="8" fill="#5a8099" font-family="-apple-system,sans-serif">20</text>
    <!-- Gridlines -->
    <line x1="45" y1="130" x2="295" y2="130" stroke="#AFEEEE" stroke-width="0.5" stroke-dasharray="3,3"/>
    <line x1="45" y1="95" x2="295" y2="95" stroke="#AFEEEE" stroke-width="0.5" stroke-dasharray="3,3"/>
    <line x1="45" y1="60" x2="295" y2="60" stroke="#AFEEEE" stroke-width="0.5" stroke-dasharray="3,3"/>
    <!-- AUC curve -->
    <polyline points="65,148 100,100 135,52 170,36 205,32 255,30 290,30" fill="none" stroke="#AFEEEE" stroke-width="2.5" stroke-linejoin="round"/>
    <!-- Plateau zone shading -->
    <rect x="160" y="25" width="135" height="145" fill="rgba(152,255,152,0.12)" rx="4"/>
    <line x1="160" y1="25" x2="160" y2="165" stroke="#98FF98" stroke-width="1.5" stroke-dasharray="4,3"/>
    <!-- Plateau label -->
    <text x="227" y="45" text-anchor="middle" font-size="9" fill="#27500A" font-weight="600" font-family="-apple-system,sans-serif">Plateau region</text>
    <text x="227" y="57" text-anchor="middle" font-size="8.5" fill="#27500A" font-family="-apple-system,sans-serif">7–10 genes sufficient</text>
    <!-- AUC value -->
    <text x="275" y="25" text-anchor="middle" font-size="9" fill="#27500A" font-weight="600" font-family="-apple-system,sans-serif">0.9985</text>
    <!-- Dots at plateau -->
    <circle cx="170" cy="36" r="4" fill="#98FF98" stroke="#27500A" stroke-width="1.5"/>
    <circle cx="205" cy="32" r="4" fill="#98FF98" stroke="#27500A" stroke-width="1.5"/>
  </svg>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
    {stcard('7–10','Gene plateau — most diagnostic signal captured by this compact biomarker set',0.45)}
    {acard('<div class="card-head">Implication</div><div class="card-body">A parsimonious diagnostic panel of fewer than 10 genes may be sufficient for practical BTN detection — reducing cost and complexity.</div>',0.65,AC['IV'])}
    {card('<div class="card-head">Performance rises with gene count</div><div class="card-body">AUC and balanced accuracy increase as top-ranked genes are added; Brier score falls as the model becomes more reliable.</div>',0.8)}
  </div>
</div>''',title='Performance Plateau at 7–10 Genes'))

# SLIDE 34 – Bridge: Are These Genes Biologically Real?
slides.append(mkslide(34,f'''
<div class="layout-d" style="gap:18px">
  <div style="font-size:0.9em;color:#5a8099;text-transform:uppercase;letter-spacing:0.12em;font-weight:600" data-animate="title-fade" data-delay="0.2">The next question</div>
  <div style="font-size:1.75em;font-weight:600;color:#2D2D2D;max-width:62%;line-height:1.35;text-align:center" data-animate="stat-reveal" data-delay="0.4">We know <em>how many</em> genes are needed. But are the genes the model chose actually biologically meaningful?</div>
  <div style="width:48px;height:2px;background:{AC["IV"]};margin:0 auto" data-animate="text-emerge" data-delay="0.65"></div>
  <div style="font-size:1em;color:#5a8099;max-width:56%;text-align:center;line-height:1.7" data-animate="text-emerge" data-delay="0.8">To test this, we compared the ML feature importance rankings against an independent differential expression analysis — two completely separate methods asking the same biological question.</div>
</div>'''))

# SLIDE 35 – ML–DE Convergence (merged 40+41)
slides.append(mkslide(35,f'''
<div style="display:grid;grid-template-columns:55% 1fr;gap:18px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i12','ML vs. DE Convergence','Absolute SVM coefficient vs. log₂ fold-change (Neoplastic/Normal). Red = Top 20 gold-standard; Blue = in all 3 configs; Gray = other candidates.',0.3,'380px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
    <div style="font-size:0.7em;font-weight:600;color:#5a8099;letter-spacing:0.06em;text-transform:uppercase" data-animate="text-emerge" data-delay="0.35">Concordance confirmed</div>
    {stcard('18 / 20','Top ML biomarkers also differentially expressed between neoplastic and normal pools',0.5)}
    {acard('<div class="card-head">What this means</div><div class="card-body">ML feature importance and differential expression converge on the same biological signal — validating the candidate biomarker list through two independent analytical lenses.</div>',0.8,AC['IV'])}
  </div>
</div>''',title='Convergence of ML Feature Importance and Differential Expression'))

# SLIDE 35 – Overall Summary
slides.append(mkslide(35,f'''
<div class="layout-d" style="gap:16px">
  <div style="font-size:1.8em;font-weight:600;color:#2D2D2D;max-width:60%;line-height:1.3" data-animate="stat-reveal" data-delay="0.3">A high-performing SVM classifier and a validated biomarker list.</div>
  <div style="font-size:1em;color:#5a8099;max-width:55%;line-height:1.6" data-animate="text-emerge" data-delay="0.6">Now: can this model detect BTN-like transcriptomics in animals that were <em>never used in training</em>?</div>
  <div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:4px" data-animate="text-emerge" data-delay="0.8">
    {pill('AUC = 0.9985','mint')} {pill('406 biomarker candidates','blue')}
  </div>
</div>'''))

# SLIDE 36 – Contextual Reminder
slides.append(mkslide(36,f'''
<div class="layout-d" style="gap:16px">
  <div style="font-size:0.9em;color:#5a8099;text-transform:uppercase;letter-spacing:0.12em;font-weight:600" data-animate="text-emerge" data-delay="0.2">Critical context</div>
  <div style="font-size:1.7em;font-weight:600;color:{AC["V"]};max-width:65%;line-height:1.3" data-animate="stat-reveal" data-delay="0.45">Our model was NOT trained on 5-day or 12-day samples.</div>
  <div style="font-size:1em;color:#5a8099;max-width:55%;line-height:1.6" data-animate="text-emerge" data-delay="0.75">These animals were exposed but showed no histological signs of neoplasia at time of sampling. We are applying a trained classifier to entirely novel data.</div>
</div>'''))

# SLIDE 37 – Pre-Symptomatic Methodology
slides.append(mkslide(37,f'''
<div style="display:flex;flex-direction:column;gap:14px;padding:1% 5% 0;margin-top:1%">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
    {acard('<div class="card-head">The goal</div><div class="card-body">Detect neoplastic-like transcriptomics at early timepoints where conventional histology <em>cannot</em> yet detect disease — presymptomatic classification.</div>',0.4,AC['V'])}
    {acard('<div class="card-head">The method</div><div class="card-body">Apply the trained model — using 406 biomarkers from the gold-standard SVM — to classify each cell from the 5-day and 12-day post-exposure pools.</div>',0.6,AC['V'])}
  </div>
  <svg viewBox="0 0 700 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;border:1px solid rgba(175,238,238,.3);border-radius:10px;background:#fafeff" data-animate="scale-fade-in" data-delay="0.8">
    <line x1="50" y1="68" x2="660" y2="68" stroke="#AFEEEE" stroke-width="2"/>
    <polygon points="655,62 668,68 655,74" fill="#AFEEEE"/>
    <!-- Day 0 -->
    <circle cx="80" cy="68" r="10" fill="#AFEEEE" stroke="#185FA5" stroke-width="1.5"/>
    <text x="80" y="48" text-anchor="middle" font-size="10" font-weight="600" fill="#2D2D2D" font-family="-apple-system,sans-serif">Day 0</text>
    <text x="80" y="36" text-anchor="middle" font-size="9" fill="#5a8099" font-family="-apple-system,sans-serif">BTN exposure</text>
    <text x="80" y="92" text-anchor="middle" font-size="8.5" fill="#5a8099" font-family="-apple-system,sans-serif">Source clam introduced</text>
    <!-- Day 5 -->
    <circle cx="230" cy="68" r="10" fill="#98FF98" stroke="#27500A" stroke-width="2"/>
    <text x="230" y="48" text-anchor="middle" font-size="10" font-weight="600" fill="#27500A" font-family="-apple-system,sans-serif">Day 5</text>
    <text x="230" y="36" text-anchor="middle" font-size="9" fill="#27500A" font-weight="600" font-family="-apple-system,sans-serif">ML detects 7%</text>
    <text x="230" y="92" text-anchor="middle" font-size="8.5" fill="#5a8099" font-family="-apple-system,sans-serif">Hemocyte sample collected</text>
    <!-- Day 12 -->
    <circle cx="390" cy="68" r="10" fill="#98FF98" stroke="#27500A" stroke-width="2"/>
    <text x="390" y="48" text-anchor="middle" font-size="10" font-weight="600" fill="#27500A" font-family="-apple-system,sans-serif">Day 12</text>
    <text x="390" y="36" text-anchor="middle" font-size="9" fill="#27500A" font-weight="600" font-family="-apple-system,sans-serif">ML detects 6%</text>
    <text x="390" y="92" text-anchor="middle" font-size="8.5" fill="#5a8099" font-family="-apple-system,sans-serif">Hemocyte sample collected</text>
    <!-- Presymptomatic bracket -->
    <rect x="158" y="108" width="314" height="15" rx="4" fill="rgba(152,255,152,0.15)" stroke="#98FF98" stroke-width="1"/>
    <text x="315" y="119" text-anchor="middle" font-size="8.5" fill="#27500A" font-weight="600" font-family="-apple-system,sans-serif">Presymptomatic window — no histological signs of BTN</text>
    <!-- Histology node -->
    <circle cx="540" cy="68" r="10" fill="rgba(224,85,85,0.2)" stroke="#E05555" stroke-width="1.5"/>
    <text x="540" y="48" text-anchor="middle" font-size="10" font-weight="600" fill="#791F1F" font-family="-apple-system,sans-serif">Weeks later</text>
    <text x="540" y="36" text-anchor="middle" font-size="9" fill="#791F1F" font-family="-apple-system,sans-serif">Histology detects</text>
    <text x="540" y="92" text-anchor="middle" font-size="8.5" fill="#5a8099" font-family="-apple-system,sans-serif">Visible neoplasia confirmed</text>
  </svg>
</div>''',title='Pre-Symptomatic Detection at 5 and 12 Days'))

# SLIDE 38 – Pre-Symptomatic Results (merged 45+46)
slides.append(mkslide(38,f'''
<div style="display:grid;grid-template-columns:55% 1fr;gap:18px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i8','Probability Distribution','Neoplastic probability scores for all four conditions. Dashed line = 0.5 classification threshold.',0.3,'370px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
    {stcard('7%','Of 5-day post-exposure cells predicted neoplastic — before histological signs appear',0.5)}
    {stcard('6%','Of 12-day post-exposure cells predicted neoplastic — later presymptomatic timepoint',0.65)}
    {acard('<div class="card-head">Presymptomatic signal detected</div><div class="card-body">The model was never trained on 5-day or 12-day samples. These transcriptional signatures emerge spontaneously from the trained classifier — confirming early biological change.</div>',0.8,AC['V'])}
  </div>
</div>''',title='Pre-Symptomatic Detection — Results'))

# SLIDE 39 – Genotyping Introduction (merged 47+48)
slides.append(mkslide(39,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:1% 5% 0;margin-top:1%">
  {card('<div class="card-head">The question</div><div class="card-body">Can we detect <em>foreign host genomes</em> — a key biological trait of BTN — in the neoplastic pools? If so, do those foreign-genotype cells agree with our ML predictions?</div>',0.4)}
  {acard('<div class="card-head">The hypothesis</div><div class="card-body">Neoplastic pools contained four host animals plus the invading BTN cancer cells. A fifth, foreign genotype should appear — corresponding to the transmissible cancer lineage.</div>',0.6,AC['V'])}
</div>''',title='Genotyping — An Independent Validation'))

# SLIDE 40 – Genotyping PCA (merged 49+50)
slides.append(mkslide(40,f'''
<div style="display:grid;grid-template-rows:1fr auto;padding:1% 5% 0;gap:8px;height:100%">
  <div class="fig-frame" style="flex:1;min-height:0;position:relative" data-animate="scale-fade-in" data-delay="0.3">
    <div class="fig-lbl">Genotype-Level PCA</div>
    <img src="{I['i21']}" alt="Genotype PCA" style="width:100%;height:100%;object-fit:contain" onerror="imgErr(this)">
  </div>
  <div class="fig-cap" data-animate="text-emerge" data-delay="0.75">Genotype-Level PCA (≥1,000 cells per genotype) · 23 genotypes · point size proportional to cell count · PC1 = 7.3% variance, PC2 = 6.0%</div>
  <div style="display:flex;gap:8px;flex-wrap:wrap" data-animate="text-emerge" data-delay="0.9">
    {pill('Neoplastic pool','coral')} {pill('Normal pool','blue')} {pill('5-Day exposure','mint')} {pill('12-Day exposure','lavender')}
  </div>
</div>''',title='A Fifth Genotype Emerges'))

# SLIDE 41 – Bridge: Genotype Validation Question
slides.append(mkslide(41,f'''
<div class="layout-d" style="gap:20px">
  <div style="font-size:1.05em;font-weight:600;color:{AC["V"]};letter-spacing:0.06em;text-transform:uppercase" data-animate="title-fade" data-delay="0.25">One lineage identified</div>
  <div style="font-size:1.7em;font-weight:600;color:#2D2D2D;max-width:65%;line-height:1.35;text-align:center" data-animate="stat-reveal" data-delay="0.4">A single transmissible BTN lineage appears to underlie the neoplastic pool.</div>
  <div style="width:48px;height:2px;background:{AC["V"]};margin:0 auto" data-animate="text-emerge" data-delay="0.65"></div>
  <div style="font-size:1em;color:#5a8099;max-width:58%;text-align:center;line-height:1.7" data-animate="text-emerge" data-delay="0.8">Can we use the host genotype assignments to independently validate the ML classifier — and confirm that the model agrees on which cells are neoplastic versus normal?</div>
</div>'''))

# SLIDE 42 – Concordance (merged 51+52)
slides.append(mkslide(42,f'''
<div style="display:grid;grid-template-columns:58% 1fr;gap:18px;padding:1% 4% 0;margin-top:0.5%">
  <div>
    {figbox('i20','Classifier Agreement','Per-Genotype ML Classification (28 Genotypes) — % cells classified as neoplastic by SVM, grouped by pool type.',0.3,'370px')}
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
    <div style="font-size:0.65em;font-weight:600;color:{AC["V"]};text-transform:uppercase;letter-spacing:0.1em" data-animate="text-emerge" data-delay="0.35">And it does!</div>
    {stcard('98.7%','Overall agreement between SVM classifications and genotype-based pool assignments',0.5)}
    {stcard('97.3%','Mean neoplastic SVM classification across 10 neoplastic genotypes',0.65)}
    {acard('<div class="card-head">1.9% normal misclassification</div><div class="card-body">Only 1.9% of cells in 8 normal genotype clusters were misclassified as neoplastic — confirming near-perfect specificity.</div>',0.8,AC['V'])}
  </div>
</div>''',title='Classifier and Genotype Concordance'))

# SLIDE 43 – Summary of Key Findings
slides.append(mkslide(43,f'''
<div style="display:flex;flex-direction:column;gap:12px;padding:1% 5% 0;margin-top:0.5%">
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
    {stcard('0.9985','AUC — near-perfect separation of neoplastic from normal hemocytes on held-out test data',0.35)}
    {stcard('0.986','Balanced accuracy — equal performance across both classes in 70/30 split',0.45)}
    {stcard('20','Gold-standard biomarkers — top genes by SVM coefficient magnitude across all configurations',0.55)}
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
    {acard('<div class="card-head">Biological validation</div><div class="card-body"><strong>18 of 20</strong> top ML biomarkers are also differentially expressed — confirming biological ground truth through two independent analytical lenses.</div>',0.65,AC['VI'])}
    {acard('<div class="card-head">Presymptomatic detection</div><div class="card-body"><strong>7%</strong> of 5-day post-exposure cells and <strong>6%</strong> of 12-day cells predicted neoplastic — before any histological evidence of disease. Model never trained on these samples.</div>',0.75,AC['VI'])}
  </div>
  <div style="padding:0" data-animate="text-emerge" data-delay="0.9">
    <div style="background:rgba(152,255,152,0.1);border-left:3px solid #98FF98;border-radius:0 8px 8px 0;padding:8px 14px;font-size:0.82em;color:#2D2D2D;line-height:1.5">
      <strong>Bottom line:</strong> A parsimonious panel of fewer than 10 genes — identified by machine learning — is sufficient for near-perfect BTN classification, with presymptomatic signal emerging before symptoms are histologically detectable.
    </div>
  </div>
</div>''',title='Summary of Key Findings'))

# SLIDE 44 – Limitations
slides.append(mkslide(44,f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:1% 5% 0;margin-top:1%">
  {acard('<div class="card-head">Single BTN lineage</div><div class="card-body">Training data represents one BTN lineage from one laboratory exposure experiment. Generalizability across the 8+ known independent BTN lineages in bivalves is not yet established.</div>',0.4,AC['V'])}
  {acard('<div class="card-head">Unconfirmed cell-level labels</div><div class="card-body">The 5-day and 12-day post-exposure pools lack confirmed single-cell neoplastic labels — predicted proportions (7%, 6%) are SVM estimates, not ground truth.</div>',0.55,AC['V'])}
  {acard('<div class="card-head">Reference genome incompleteness</div><div class="card-body">3 of the top 20 biomarkers remain unannotated due to gaps in the <em>M. mercenaria</em> reference — limiting full biological characterization of the panel.</div>',0.7,AC['V'])}
  {acard('<div class="card-head">Diagnostic transferability</div><div class="card-body">Field application requires further validation across wild populations, seasonal variation, and other environmental stressors that may alter hemocyte transcriptomes independently of BTN.</div>',0.85,AC['V'])}
</div>''',title='Limitations'))

# SLIDE 46 – Acknowledgments / Thank You
slides.append(mkslide(45,f'''
<div style="display:flex;flex-direction:column;gap:14px;padding:1% 5% 0;margin-top:0.5%">
  <div style="text-align:center;font-size:1.8em;font-weight:600;color:#2D2D2D" data-animate="stat-reveal" data-delay="0.2">Thank You</div>
  <div style="width:50px;height:2px;background:#98FF98;margin:0 auto" data-animate="text-emerge" data-delay="0.35"></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px" data-animate="text-emerge" data-delay="0.5">
    {card('<div class="card-head" style="color:#412402">Major Professor</div><div class="card-body"><strong>Dr. Marta Gomez-Chiarri</strong><br>University of Rhode Island<br>Mentorship, direction, and support throughout this work.</div>',0,'card card-amber')}
    {card('<div class="card-head" style="color:#412402">Thesis Committee</div><div class="card-body"><strong>Dr. Nic Fisk</strong><br><strong>Dr. Thomas Delomas</strong><br><strong>Dr. Hollie Putnam</strong></div>',0,'card card-amber')}
    {card('<div class="card-head" style="color:#412402">Data & Collaboration</div><div class="card-body">Samson et al. 2025 for experimental data<br>URI Coastal Resources Center<br>National Sea Grant Program</div>',0,'card card-amber')}
  </div>
  <div style="text-align:center;font-size:0.82em;color:#5a8099;margin-top:4px" data-animate="text-emerge" data-delay="0.7">University of Rhode Island · Biological Environmental Sciences · 2025</div>
</div>''',title='Acknowledgments'))

print(f"Generated {len(slides)} slides.")

# Save slides for assembly
import pickle
with open('/tmp/slides.pkl','wb') as f:
    pickle.dump(slides, f)
with open('/tmp/imgs.pkl','wb') as f:
    pickle.dump(I, f)
print("Slides saved.")