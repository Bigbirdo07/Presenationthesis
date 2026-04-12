import pickle

with open('/tmp/slides.pkl','rb') as f:
    slides = pickle.load(f)

TOTAL = len(slides)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
body{background:#1a1a2e}

/* Opening / End screens */
#opening,#end-screen{position:fixed;inset:0;background:linear-gradient(180deg,#fff 0%,#F0F8FF 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:1000;gap:0}
#end-screen{display:none}
.open-title{font-size:2em;font-weight:600;color:#2D2D2D;max-width:600px;text-align:center;line-height:1.3;opacity:0}
.open-sub{font-size:0.95em;color:#5a8099;opacity:0;margin-top:10px}
.open-inst{font-size:0.75em;color:#2D2D2D;opacity:0;margin-top:4px}
.begin-btn{margin-top:20px;background:transparent;border:2px solid #98FF98;color:#2D2D2D;border-radius:24px;padding:10px 32px;font-size:1em;cursor:pointer;font-family:inherit;opacity:0;transition:background 200ms}
.begin-btn:hover{background:rgba(152,255,152,0.12)}
.begin-btn:focus-visible{outline:2px solid #98FF98;outline-offset:3px}
.hint-text{font-size:0.7em;color:#aaa;font-style:italic;margin-top:10px;opacity:0}

/* Deck */
.deck{width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}

/* Slide container */
.slide-container{position:relative;width:100%;max-width:calc(100vh * 16 / 9);aspect-ratio:16/9;overflow:hidden;background:linear-gradient(180deg,#fff 0%,#F0F8FF 100%)}

/* Progress bar */
.progress-bar{position:absolute;top:0;left:0;height:3px;background:#98FF98;z-index:10;pointer-events:none}

/* Slides */
.slide{position:absolute;top:0;left:0;width:100%;height:100%;opacity:0;pointer-events:none;transition:opacity 300ms ease}
.slide.active{opacity:1;pointer-events:auto}

/* Watermarks */
.neural-wm{position:absolute;top:0;left:0;width:45%;height:55%;opacity:.08;pointer-events:none;z-index:0}
.clam-wm{position:absolute;bottom:36px;right:0;width:22%;height:44%;opacity:.10;pointer-events:none;z-index:0}

/* Slide inner */
.slide-inner{position:absolute;top:0;left:0;width:100%;height:100%;z-index:1;padding:2% 3.5% 6% 3.5%}

/* Footer */
.footer{position:absolute;bottom:0;left:0;right:0;height:36px;border-top:1.5px solid #AFEEEE;background:rgba(240,248,255,.95);display:flex;align-items:center;justify-content:space-between;padding:0 20px;z-index:2}
.fbrand{font-size:.6875em;color:#5a8099}
.fcounter{font-size:.6875em;color:#5a8099;background:none;border:none;cursor:pointer;padding:0}
.fcounter:focus-visible{outline:2px solid #98FF98;outline-offset:3px}

/* Act label */
.act-lbl{font-size:.625em;font-weight:600;letter-spacing:.12em;text-transform:uppercase;margin-bottom:6px;opacity:0}

/* Slide title */
.slide-title{font-size:2.1em;font-weight:600;color:#2D2D2D;line-height:1.2;margin-bottom:10px;opacity:0}
.slide-title.sm{font-size:1.7em}
.slide-title.xs{font-size:1.35em}

/* Text sizes */
.card-head{font-size:1em;font-weight:600;color:#2D2D2D;margin-bottom:6px}
.card-body{font-size:.875em;color:#2D2D2D;line-height:1.6}

/* Cards */
.card{background:#fff;border:.5px solid rgba(175,238,238,.5);border-radius:10px;padding:16px 18px;opacity:0}
.card-accent{background:#fff;border-left:3px solid #98FF98;border-radius:0 8px 8px 0;padding:10px 14px;opacity:0}
.stat-card{background:rgba(240,248,255,.8);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0}
.stat-num{font-size:3.4em;font-weight:600;color:#2D2D2D;line-height:1}
.stat-lbl{font-size:.65em;color:#5a8099;margin-top:5px;line-height:1.4}
.card-amber{background:rgba(245,200,66,.08);border:.5px solid rgba(245,200,66,.4)}

/* Cards grid */
.cards-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:1%}

/* Figure */
.fig-frame{border-radius:10px;overflow:hidden;border:1px solid rgba(175,238,238,.4);background:#fff;padding:10px;display:flex;align-items:center;justify-content:center}
.fig-lbl{position:absolute;top:8px;left:8px;background:rgba(175,238,238,.9);color:#185FA5;font-size:.625em;font-weight:600;padding:2px 8px;border-radius:20px;letter-spacing:.05em;z-index:2}
.fig-cap{font-size:.78em;color:#5a8099;font-style:italic;text-align:center;margin-top:6px;line-height:1.5;opacity:0}

/* Layout D */
.layout-d{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:14px;height:calc(100% - 36px)}

/* Pill */
.pill{display:inline-flex;align-items:center;padding:3px 10px;border-radius:20px;font-size:.625em;font-weight:600;letter-spacing:.06em;white-space:nowrap}
.pill-mint{background:rgba(152,255,152,.2);color:#27500A}
.pill-blue{background:rgba(175,238,238,.25);color:#0C447C}
.pill-lavender{background:rgba(230,230,250,.3);color:#3C3489}
.pill-coral{background:rgba(224,85,85,.15);color:#791F1F}
.pill-amber{background:rgba(245,200,66,.2);color:#412402}

/* Animations */
@keyframes textEmerge{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes titleFade{from{opacity:0}to{opacity:1}}
@keyframes statReveal{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:scale(1)}}
@keyframes scaleFadeIn{from{opacity:0;transform:scale(.96)}to{opacity:1;transform:scale(1)}}
@keyframes popIn{0%{transform:scale(0);opacity:0}60%{transform:scale(1.08)}100%{transform:scale(1);opacity:1}}

[data-animate]{opacity:0}
.text-emerge{animation:textEmerge .5s ease forwards}
.title-fade{animation:titleFade .4s ease forwards}
.stat-reveal{animation:statReveal .6s ease forwards}
.scale-fade-in{animation:scaleFadeIn .8s ease forwards}
.pop-in{animation:popIn .4s ease forwards}

/* Navigation */
.nav-btn{position:fixed;top:50%;transform:translateY(-50%);width:36px;height:36px;border-radius:50%;background:transparent;border:1.5px solid rgba(200,200,200,.6);color:rgba(200,200,200,.7);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:15px;z-index:100;transition:all 200ms}
.nav-btn:hover{background:rgba(175,238,238,.2);border-color:#AFEEEE;color:#AFEEEE}
.nav-btn:focus-visible{outline:2px solid #98FF98;outline-offset:3px}
#btn-prev{left:16px}
#btn-next{right:16px}

/* Navigator */
#navigator{position:fixed;bottom:50px;right:20px;background:#fff;border:.5px solid #AFEEEE;border-radius:10px;max-height:60vh;overflow-y:auto;z-index:200;display:none;min-width:280px;box-shadow:0 4px 20px rgba(0,0,0,.08)}
#navigator.open{display:block}
.nav-item{padding:8px 16px;cursor:pointer;font-size:.78em;color:#2D2D2D;border-bottom:.5px solid rgba(175,238,238,.25);display:flex;gap:10px;align-items:baseline}
.nav-item:hover{background:rgba(175,238,238,.1)}
.nav-num{color:#5a8099;min-width:22px;font-weight:600;font-size:.85em}

/* SVM Animation Widget */
.svm-step{display:flex;gap:8px;align-items:flex-start;padding:7px 10px;border-radius:8px;transition:all .3s;border:1px solid transparent}
.svm-step.future{opacity:.22}
.svm-step.done{opacity:.5}
.svm-step.active{opacity:1;background:rgba(175,238,238,.08);border-color:#AFEEEE}
.svm-step-num{width:20px;height:20px;border-radius:50%;background:rgba(175,238,238,.2);color:#185FA5;font-size:.625em;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.svm-step-title{font-size:.78em;font-weight:600;color:#2D2D2D}
.svm-step-sub{font-size:.65em;color:#5a8099;margin-top:1px;line-height:1.3}
.c-pill,.pca-pill{font-size:.6em;padding:2px 7px;border-radius:12px;background:rgba(230,230,250,.2);color:#3C3489;border:.5px solid rgba(230,230,250,.4);transition:all .25s}
.c-pill.active-pill,.pca-pill.active-pill{background:rgba(230,230,250,.7);font-weight:600;border-color:#7F77DD}

/* End screen buttons */
.end-btn{background:transparent;border:1.5px solid #AFEEEE;color:#2D2D2D;border-radius:20px;padding:8px 24px;font-size:.9em;cursor:pointer;font-family:inherit;transition:background 200ms}
.end-btn:hover{background:rgba(175,238,238,.15)}
"""

# Navigator items
nav_items_html = ''
slide_titles = [
  'Title','Opening Hook','The Study Organism','Global Significance of Bivalve Aquaculture',
  'Rhode Island Economic Stakes','The Threat Arrives','Hemic Neoplasia & BTN',
  'Why We Care','The Wellfleet Outbreak (2009)','Detection Challenge',
  'The Detection Gap','The Research Question','Flow of Today\'s Research',
  'Experimental Design','First Round Exposure','Single-Cell Experimental Design',
  'Second Round — Exposure vs. Control','Four Sampling Conditions',
  'Why Single-Cell Sequencing?','Bridge to Machine Learning','Machine Learning',
  'Classifying Confirmed Cells','Why SVM?','Model Framework: 70/30 Split',
  'What the Classifier Is Actually Doing','Gold Standard Model Results',
  'Feature Importance','Test for Biological Relevance',
  'Biomarker Discovery — Robustness Filter','Top 20 Gold-Standard Biomarkers',
  'Validation & Next Question','Parsimonious Models & Complexity',
  'Performance Plateau at 7–10 Genes','ML–DE Convergence',
  'Overall Summary','Critical Context: Not Trained on Early Timepoints',
  'Pre-Symptomatic Detection Methodology','Pre-Symptomatic Detection Results',
  'Genotyping — An Independent Validation','A Fifth Genotype Emerges',
  'Classifier and Genotype Concordance','Acknowledgments'
]
for i,t in enumerate(slide_titles):
    nav_items_html += f'<div class="nav-item" onclick="goTo({i});toggleNav()"><span class="nav-num">{i+1}</span><span>{t}</span></div>\n'

JS = r"""
// ─── State ───────────────────────────────────────────────────────────────────
var cur = -1;   // -1 means "not yet started"
const TOTAL = """ + str(TOTAL) + r""";
var svmTimer = null;
var svmTimers = [];

// ─── Slide navigation ────────────────────────────────────────────────────────
function goTo(n) {
  if (n < 0 || n >= TOTAL) return;
  if (cur >= 0) {
    const old = document.getElementById('s' + (cur+1));
    if (old) old.classList.remove('active');
  }
  cur = n;
  const el = document.getElementById('s' + (cur+1));
  if (el) el.classList.add('active');
  document.getElementById('progress-bar').style.width = ((cur+1)/TOTAL*100) + '%';
  animateSlide(el);
  if (cur === 24) {
    setTimeout(startSVM, 600);
  } else {
    stopSVM();
  }
}
function nextSlide() { if (cur < TOTAL-1) goTo(cur+1); else showEnd(); }
function prevSlide() { if (cur > 0) goTo(cur-1); }
function showEnd() {
  document.getElementById('end-screen').style.display = 'flex';
}

// ─── Animation system ────────────────────────────────────────────────────────
function animateSlide(el) {
  if (!el) return;
  const items = el.querySelectorAll('[data-animate]');
  items.forEach(function(item) {
    // 1. Remove animation classes — stops any in-progress animation
    item.classList.remove('text-emerge','title-fade','stat-reveal','scale-fade-in','pop-in');
    // 2. Clear any previously-set inline overrides (but NOT opacity — CSS [data-animate] keeps it 0)
    item.style.animation = '';
    item.style.animationDelay = '';
    // 3. Force reflow so the browser registers the class removal before re-adding
    void item.offsetWidth;
    // 4. Set delay and re-add class — animation now plays cleanly from opacity:0
    const type = item.dataset.animate;
    const delay = parseFloat(item.dataset.delay || '0');
    item.style.animationDelay = delay + 's';
    item.classList.add(type);
  });
}

// ─── Scale slides ────────────────────────────────────────────────────────────
function scaleSlides() {
  const c = document.querySelector('.slide-container');
  if (!c) return;
  const s = c.offsetWidth / 1280;
  c.style.fontSize = (16 * s) + 'px';
}
window.addEventListener('resize', scaleSlides);

// ─── Image error handler ─────────────────────────────────────────────────────
function imgErr(img) {
  const f = img.closest('.fig-frame');
  if (f) {
    const lbl = f.querySelector('.fig-lbl');
    const t = lbl ? lbl.textContent : 'Figure';
    f.innerHTML = '<div style="width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:16px;border:2px dashed #AFEEEE;border-radius:8px;background:rgba(175,238,238,.05)"><span style="font-size:.75em;font-weight:600;color:#2D2D2D">' + t + '</span><span style="font-size:.625em;color:#5a8099;font-style:italic">Image not loaded</span></div>';
  }
}

// ─── Navigator ───────────────────────────────────────────────────────────────
function toggleNav() {
  document.getElementById('navigator').classList.toggle('open');
}
document.addEventListener('click', function(e) {
  const nav = document.getElementById('navigator');
  if (!nav.contains(e.target) && !e.target.classList.contains('fcounter')) {
    nav.classList.remove('open');
  }
});

// ─── Keyboard ────────────────────────────────────────────────────────────────
document.addEventListener('keydown', function(e) {
  const op = document.getElementById('opening');
  const opVisible = op && op.style.display !== 'none';
  if (opVisible) { beginPresentation(); return; }
  if (document.getElementById('end-screen').style.display === 'flex') return;
  if (e.key==='ArrowRight'||e.key==='ArrowDown'||e.key===' ') { e.preventDefault(); nextSlide(); }
  else if (e.key==='ArrowLeft'||e.key==='ArrowUp') { e.preventDefault(); prevSlide(); }
  else if (e.key==='Home') goTo(0);
  else if (e.key==='End') goTo(TOTAL-1);
  else if (e.key==='f'||e.key==='F') {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(function(){});
    else document.exitFullscreen();
  }
});

// ─── Touch ───────────────────────────────────────────────────────────────────
var txStart = 0;
document.addEventListener('touchstart', function(e){ txStart = e.changedTouches[0].screenX; });
document.addEventListener('touchend', function(e) {
  const diff = txStart - e.changedTouches[0].screenX;
  if (Math.abs(diff) > 50) { if (diff > 0) nextSlide(); else prevSlide(); }
});

// ─── Opening screen ──────────────────────────────────────────────────────────
var _begun = false;
function beginPresentation() {
  if (_begun) return;
  _begun = true;
  const op = document.getElementById('opening');
  op.style.transition = 'opacity 300ms ease';
  op.style.opacity = '0';
  setTimeout(function(){
    op.style.display = 'none';
    scaleSlides();
    goTo(0);
  }, 320);
}

// ─── SVM Pipeline Animation ──────────────────────────────────────────────────
// Point positions [x,y] for 6 steps: neo (15 pts) and normal (15 pts)
// Step 0 = heavily overlapping; Step 5 = cleanly separated
const NEO_HOME = [
  [45,80],[72,105],[58,132],[92,90],[76,157],[95,122],
  [38,107],[108,138],[62,67],[54,177],[97,70],[40,122],
  [105,163],[65,112],[86,52]
];
const NORM_HOME = [
  [192,82],[218,64],[242,108],[197,148],[228,82],[257,128],
  [202,163],[248,68],[212,118],[187,52],[237,168],[262,93],
  [197,138],[232,78],[252,153]
];
// Jitter offsets (fixed)
const NEO_JITTER  = [[12,-15],[25,20],[-18,30],[35,-20],[8,40],[-22,15],[30,-25],[-28,18],[15,-30],[22,35],[-15,-25],[28,22],[-32,12],[18,-18],[-20,28]];
const NORM_JITTER = [[-15,20],[18,-25],[22,15],[-28,-12],[15,30],[-20,10],[28,-18],[-12,25],[20,-20],[25,15],[-18,-28],[12,22],[-25,8],[18,-22],[22,-15]];

function svmPos(step) {
  // centerShift: how much points shift toward boundary (x=148) in early steps
  const shifts = [0.50, 0.34, 0.18, 0.05, 0.04, 0.03];
  const jMults  = [3.2,  2.2,  1.4,  0.6,  0.5,  0.5];
  const s = shifts[step], j = jMults[step];
  return {
    neo: NEO_HOME.map(function([x,y],i){
      return [x + (148-x)*s + NEO_JITTER[i][0]*j, y + NEO_JITTER[i][1]*j];
    }),
    norm: NORM_HOME.map(function([x,y],i){
      return [x + (148-x)*s + NORM_JITTER[i][0]*j, y + NORM_JITTER[i][1]*j];
    })
  };
}

function setPoints(step) {
  const pos = svmPos(step);
  for (let i=0;i<15;i++) {
    const np = document.getElementById('np'+i);
    const mp = document.getElementById('mp'+i);
    if (np) np.style.transform = 'translate('+pos.neo[i][0]+'px,'+pos.neo[i][1]+'px)';
    if (mp) mp.style.transform = 'translate('+pos.norm[i][0]+'px,'+pos.norm[i][1]+'px)';
  }
}

function setSVMStep(step) {
  // Update pipeline list
  for (let i=0;i<6;i++) {
    const el = document.getElementById('ss'+i);
    if (!el) continue;
    el.className = 'svm-step ' + (i < step ? 'done' : i === step ? 'active' : 'future');
  }
  // Update progress bar
  const prog = document.getElementById('svm-prog');
  if (prog) prog.style.width = ((step+1)/6*100)+'%';
  // Captions
  const captions = [
    'CPM normalization applied — counts scaled to counts-per-million per cell',
    'log₂(CPM+1) transform — variance stabilized; library-size effects removed',
    'Seurat v3 HVG selection — three feature-set configurations evaluated',
    'Standard scaling fit on training data only — PCA dimensionality reduction; 10–100 components',
    'Grid search C ∈ {0.1,0.5,1,2,5,10} × PCA components ∈ {10,20,30,40,50,75,100} — 5-fold stratified cross-validation',
    'Max-margin hyperplane found — support vectors are the cells nearest the boundary — AUC = 0.9985'
  ];
  const capEl = document.getElementById('svm-caption');
  if (capEl) capEl.textContent = captions[step];
  // Axis labels
  const xlabs = ['Raw Counts','log₂(CPM+1)','log₂(CPM+1)','PC1','PC1','PC1'];
  const ylabs = ['Expression','log₂(CPM+1)','log₂(CPM+1)','PC2','PC2','PC2'];
  const xl = document.getElementById('svm-xlab');
  const yl = document.getElementById('svm-ylab');
  if (xl) xl.textContent = xlabs[step];
  if (yl) yl.textContent = ylabs[step];
  // Zone backgrounds (step 4+)
  const nz = document.getElementById('neo-zone');
  const mz = document.getElementById('norm-zone');
  const nzl = document.getElementById('neo-zone-lbl');
  const mzl = document.getElementById('norm-zone-lbl');
  const zoneOp = step >= 3 ? '0.06' : '0';
  const lblOp  = step >= 3 ? '1' : '0';
  if (nz) nz.setAttribute('opacity', zoneOp);
  if (mz) mz.setAttribute('opacity', zoneOp);
  if (nzl) nzl.setAttribute('opacity', lblOp);
  if (mzl) mzl.setAttribute('opacity', lblOp);
  // HVG annotation (step 3)
  const hvg = document.getElementById('hvg-ann');
  if (hvg) hvg.setAttribute('opacity', step === 2 ? '1' : '0');
  // C-value / PCA pills (step 5)
  const cpw = document.getElementById('c-pills-wrap');
  if (cpw) cpw.style.display = step === 4 ? 'block' : 'none';
  // Decision boundary + margin + support vectors (step 6)
  const showBound = step === 5;
  const scanLine = document.getElementById('scan-line');
  const decBound = document.getElementById('dec-boundary');
  const ml = document.getElementById('margin-l');
  const mr = document.getElementById('margin-r');
  const ma = document.getElementById('margin-arrow');
  const ab = document.getElementById('auc-badge');
  const sv1 = document.getElementById('sv1');
  const sv2 = document.getElementById('sv2');
  const sv3 = document.getElementById('sv3');
  const svLbl = document.getElementById('sv-lbl');
  if (step === 4) {
    // scanning line visible
    if (scanLine) { scanLine.setAttribute('opacity','1'); }
  } else {
    if (scanLine) { scanLine.setAttribute('opacity','0'); }
  }
  if (showBound) {
    if (decBound) { decBound.setAttribute('opacity','1'); decBound.style.strokeDashoffset='400'; setTimeout(function(){ decBound.style.transition='stroke-dashoffset 1.2s ease'; decBound.style.strokeDashoffset='0'; },50); }
    setTimeout(function(){
      if (ml) ml.setAttribute('opacity','0.55');
      if (mr) mr.setAttribute('opacity','0.55');
    }, 1400);
    setTimeout(function(){
      if (ma) ma.setAttribute('opacity','1');
    }, 2000);
    setTimeout(function(){
      if (sv1) sv1.setAttribute('opacity','1');
      if (sv2) sv2.setAttribute('opacity','1');
      if (sv3) sv3.setAttribute('opacity','1');
      if (svLbl) svLbl.setAttribute('opacity','1');
    }, 2600);
    setTimeout(function(){
      if (ab) { ab.setAttribute('opacity','0'); ab.style.transition='opacity .4s ease'; ab.setAttribute('opacity','1'); }
    }, 3200);
  } else {
    if (decBound) { decBound.setAttribute('opacity','0'); decBound.style.strokeDashoffset='400'; decBound.style.transition='none'; }
    if (ml) ml.setAttribute('opacity','0');
    if (mr) mr.setAttribute('opacity','0');
    if (ma) ma.setAttribute('opacity','0');
    if (ab) ab.setAttribute('opacity','0');
    if (sv1) sv1.setAttribute('opacity','0');
    if (sv2) sv2.setAttribute('opacity','0');
    if (sv3) sv3.setAttribute('opacity','0');
    if (svLbl) svLbl.setAttribute('opacity','0');
  }
}

var svmStep = 0;
var scanInterval = null;
var cInterval = null;

function stopSVM() {
  svmTimers.forEach(clearTimeout);
  svmTimers = [];
  if (scanInterval) clearInterval(scanInterval);
  if (cInterval) clearInterval(cInterval);
  scanInterval = null; cInterval = null;
}

function runSVMStep(step) {
  if (step >= 6) {
    // pause then restart
    const t = setTimeout(function(){ runSVMStep(0); }, 3000);
    svmTimers.push(t);
    return;
  }
  setSVMStep(step);
  setPoints(step);
  // Scanning line animation in step 4
  if (step === 4) {
    let sx = 100;
    scanInterval = setInterval(function(){
      sx += 2.5;
      const sl = document.getElementById('scan-line');
      if (sl) { sl.setAttribute('x1',sx); sl.setAttribute('x2',sx); }
      if (sx >= 200) { clearInterval(scanInterval); scanInterval = null; }
    }, 35);
    // Cycle C values
    let ci = 0, pi = 0;
    const cpills = document.querySelectorAll('.c-pill');
    const ppills = document.querySelectorAll('.pca-pill');
    cInterval = setInterval(function(){
      cpills.forEach(function(p,i){ p.classList.toggle('active-pill', i===ci%cpills.length); });
      ppills.forEach(function(p,i){ p.classList.toggle('active-pill', i===pi%ppills.length); });
      ci++; pi++;
    }, 380);
  } else {
    if (scanInterval) { clearInterval(scanInterval); scanInterval = null; }
    if (cInterval) { clearInterval(cInterval); cInterval = null; }
  }
  const durations = [2500, 2500, 2500, 3000, 4000, 5000];
  const t = setTimeout(function(){ runSVMStep(step+1); }, durations[step]);
  svmTimers.push(t);
}

function startSVM() {
  stopSVM();
  // Init all points at step 0 position instantly (no transition)
  document.querySelectorAll('#svm-svg g[id^="np"],#svm-svg g[id^="mp"]').forEach(function(g){
    g.style.transition = 'none';
  });
  const pos0 = svmPos(0);
  for (let i=0;i<15;i++){
    const np=document.getElementById('np'+i); const mp=document.getElementById('mp'+i);
    if(np) np.style.transform='translate('+pos0.neo[i][0]+'px,'+pos0.neo[i][1]+'px)';
    if(mp) mp.style.transform='translate('+pos0.norm[i][0]+'px,'+pos0.norm[i][1]+'px)';
  }
  // re-enable transitions after first frame
  setTimeout(function(){
    document.querySelectorAll('#svm-svg g[id^="np"],#svm-svg g[id^="mp"]').forEach(function(g){
      g.style.transition='transform 1.2s ease';
    });
    runSVMStep(0);
  }, 80);
}

// ─── Init ────────────────────────────────────────────────────────────────────
window.addEventListener('load', function() {
  scaleSlides();
  // Animate opening screen elements
  function fadeIn(sel, delay) {
    setTimeout(function(){ const el=document.querySelector(sel); if(el){el.style.transition='opacity .5s ease'; el.style.opacity='1';} }, delay);
  }
  fadeIn('.open-title',200);
  fadeIn('.open-sub',500);
  fadeIn('.open-inst',700);
  fadeIn('.begin-btn',900);
  fadeIn('.hint-text',1100);
  // Set initial progress
  document.getElementById('progress-bar').style.width = (1/TOTAL*100)+'%';
});
"""

OPENING = """
<div id="opening">
  <svg class="neural-wm" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <circle cx="20" cy="25" r="4" fill="#AFEEEE"/><circle cx="65" cy="15" r="2.5" fill="#AFEEEE"/>
    <circle cx="110" cy="45" r="3.5" fill="#AFEEEE"/><circle cx="45" cy="70" r="2" fill="#AFEEEE"/>
    <circle cx="90" cy="90" r="4.5" fill="#AFEEEE"/><circle cx="140" cy="35" r="2" fill="#AFEEEE"/>
    <line x1="20" y1="25" x2="65" y2="15" stroke="#AFEEEE" stroke-width="0.8" opacity="0.6"/>
    <line x1="65" y1="15" x2="110" y2="45" stroke="#AFEEEE" stroke-width="0.8" opacity="0.5"/>
    <line x1="45" y1="70" x2="90" y2="90" stroke="#AFEEEE" stroke-width="0.8" opacity="0.4"/>
    <line x1="140" y1="35" x2="160" y2="75" stroke="#AFEEEE" stroke-width="0.6" opacity="0.3"/>
  </svg>
  <svg class="clam-wm" viewBox="0 0 120 100" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="60" cy="58" rx="54" ry="38" fill="none" stroke="#AFEEEE" stroke-width="2.5"/>
    <path d="M 8 58 Q 60 12 112 58" fill="none" stroke="#AFEEEE" stroke-width="1.8"/>
    <path d="M 22 72 Q 60 34 98 72" fill="none" stroke="#AFEEEE" stroke-width="1.1"/>
    <circle cx="60" cy="58" r="5" fill="#AFEEEE"/>
  </svg>
  <div style="text-align:center;z-index:1;padding:20px">
    <div style="font-size:0.8em;font-weight:600;color:#5a8099;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:16px;opacity:0" class="open-sub">Master of Science Thesis · University of Rhode Island · 2025</div>
    <div class="open-title">Machine Learning as a Tool for Uncovering Transcriptional Signatures of Bivalve Transmissible Neoplasia in <em>Mercenaria mercenaria</em></div>
    <div style="opacity:0;margin-top:14px;font-size:1em;color:#2D2D2D" class="open-inst">Alberto A. Paz</div>
    <button class="begin-btn" onclick="beginPresentation()">Begin</button>
    <div class="hint-text">Press F for full screen</div>
  </div>
</div>
"""

END_SCREEN = """
<div id="end-screen">
  <div style="text-align:center;z-index:1">
    <div style="font-size:2.5em;font-weight:600;color:#2D2D2D;margin-bottom:12px">Thank you</div>
    <div style="font-size:1em;color:#5a8099;margin-bottom:28px">University of Rhode Island · 2025</div>
    <div style="display:flex;gap:16px;justify-content:center">
      <button class="end-btn" onclick="document.getElementById('end-screen').style.display='none';goTo(0)">Return to Start</button>
      <button class="end-btn" onclick="document.getElementById('end-screen').style.display='none';goTo(0)">View Again</button>
    </div>
  </div>
</div>
"""

NAVIGATOR = f"""
<div id="navigator">
  {nav_items_html}
</div>
"""

ALL_SLIDES = '\n'.join(slides)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Paz 2025 — BTN Thesis Defense</title>
<style>{CSS}</style>
</head>
<body>
{OPENING}
<div class="deck" id="deck">
  <div class="slide-container" id="slide-container">
    <div class="progress-bar" id="progress-bar" style="width:{100/TOTAL:.2f}%"></div>
    {ALL_SLIDES}
  </div>
  <button class="nav-btn" id="btn-prev" aria-label="Previous slide" onclick="prevSlide()">&#8592;</button>
  <button class="nav-btn" id="btn-next" aria-label="Next slide" onclick="nextSlide()">&#8594;</button>
  {NAVIGATOR}
</div>
{END_SCREEN}
<script>{JS}</script>
</body>
</html>"""

OUT = '/Users/albertopaz/Masterthesis/Claudemasterthesis/presentation.html'
with open(OUT,'w',encoding='utf-8') as f:
    f.write(HTML)

size_mb = len(HTML.encode('utf-8')) / 1_000_000
print(f"Written: {OUT}")
print(f"File size: {size_mb:.1f} MB")
print(f"Slides: {len(slides)}")
