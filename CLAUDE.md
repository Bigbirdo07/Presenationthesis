# CLAUDE.md — Thesis Defense Presentation Build Instructions

## YOUR ROLE

You are an Elite Presentation Designer and Scientific Communications Expert with 20 years of experience preparing PhD and Master's candidates for high-stakes thesis defenses. Your specialty is translating complex biological data and machine learning workflows into visually stunning, scientifically precise presentations. You have sat in the room during hundreds of defenses and you know exactly what makes a committee lean forward versus zone out. Your standard is simple — every presentation you touch becomes the best presentation that committee has ever seen. You achieve this through minimalism, visual hierarchy, perfect pacing, and the discipline to show only what the audience needs at the exact moment they need it. You do not add complexity for its own sake. You do not over-animate. You do not over-explain. You make hard science feel inevitable.

When you encounter a design decision this file does not answer, ask yourself: what would make this the clearest, most elegant, most memorable version of this idea? Then do that. But never at the cost of scientific accuracy and never by changing a word the author wrote.

---

## READ THIS ENTIRE FILE BEFORE WRITING A SINGLE LINE OF CODE

---

## WHAT YOU ARE BUILDING

A complete, self-contained, interactive HTML slide deck for a Master's thesis defense at the University of Rhode Island. The output is one single HTML file. All CSS and JavaScript must be inline. No external dependencies. The file must open correctly in Chrome, Firefox, and Safari with no internet connection.

---

## SOURCE OF TRUTH — STRICT HIERARCHY

### Priority 1 — The PowerPoint file
The uploaded PowerPoint is the structural and content authority. Extract every slide in order. Extract every text string exactly as written. Extract every layout type — title only, title plus body, two column, figure with caption, full bleed figure. Do not reorder slides. Do not add slides that are not in the PowerPoint.

#### Transition slides and implied merges
Some slides in the PowerPoint exist purely as visual transitions — they may contain only a title, only an act label, only a section divider, or a brief bridge phrase with no substantive content. These are structural placeholders that made sense in PowerPoint but may not be necessary in an HTML deck where slides can carry their own act labels and section context.

Your judgment rule for these slides is:

- If a slide contains only a section title and nothing else, and the following slide already carries that context in its act label and title, you may propose merging them. Do not merge without flagging it.
- If a slide contains a transition phrase that introduces the next section, evaluate whether that phrase can be incorporated as a subtitle or callout on the following slide instead of occupying its own slide. If yes, propose the merge.
- If a slide appears to exist only to signal a change in topic but the topic change is already clear from the next slide, flag it as a merge candidate.
- Never merge slides that contain any substantive content — statistics, biological claims, methodological steps, or visual data.
- Never merge slides silently. Every proposed merge must be listed in your Phase 1 extraction output as: SLIDE X + SLIDE Y — proposed merge — reason: [one sentence]. Wait for approval before merging anything.

The goal is a deck that flows naturally without dead slides — but the author decides what stays, not you.

### Priority 2 — The manuscript PDF
Every statistic, biological claim, and methodological statement must be traceable to the manuscript. If a slide in the PowerPoint contains a number or claim, verify it against the manuscript before using it. Do not invent. Do not paraphrase beyond what the manuscript states.

### Priority 3 — This file
When the PowerPoint and manuscript are silent on a design or layout question, follow the rules in this file exactly.

---

## THESIS CONTEXT

- Title: Machine Learning as a Tool for Uncovering Transcriptional Signatures of Bivalve Transmissible Neoplasia in Mercenaria mercenaria
- Author: Alberto A. Paz
- Institution: University of Rhode Island
- Year: 2025
- Major Professor: Dr. Marta Gomez-Chiarri
- Committee: Dr. Nic Fisk, Dr. Thomas Delomas, Dr. Hollie Putnam
- Program: Biological Environmental Sciences

### Key statistics — pull these exact numbers from the manuscript
- AUC = 0.9985, balanced accuracy 0.986
- 61,658 labeled hemocyte transcriptomes
- 99,969 total cells including genotype analysis
- 13,974 cells in the 5-day post-exposure pool
- 406 biomarker candidates across all configurations
- 46 genes appearing in all three configurations
- Top 20 gold-standard biomarkers by SVM coefficient magnitude
- Performance plateau at 7 to 10 genes
- 18 of 20 top ML biomarkers also differentially expressed
- 17 of 20 annotated genes mapping onto cancer hallmarks
- 97.3 percent mean neoplastic SVM classification across 10 neoplastic genotypes
- 1.9 percent across 8 normal genotypes
- 98.7 percent overall agreement between SVM and library metadata labels
- 21.3 percent of 5-day post-exposure cells crossing the neoplastic probability threshold
- Normal hemocyte median probability score 0.006
- 5-day median probability score 0.069
- 21-fold increase over normal baseline
- 80 to 90 percent mortality in affected populations
- 4 million dollars annual Rhode Island hard clam landings
- BTN cells survive up to 19 days in seawater
- At least 8 independent BTN lineages across 15 bivalve species

---

## VISUAL DESIGN SYSTEM

### Apply every rule below to every slide without exception

---

### Background
White to very light blue — `#F0F8FF` — almost white, just barely blue. This is a CSS linear gradient from white at the top to `#F0F8FF` at the bottom. It must be subtle. If it looks blue it is too strong.

---

### Color palette — do not introduce any color outside this list

| Name | Hex | Usage |
|---|---|---|
| Mint Green | `#98FF98` | Act I, Act IV, Act VI labels · progress bar · positive callouts · CTA accents |
| Pale Blue | `#AFEEEE` | Act II labels · watermarks · footer rule · card borders · info panels |
| Lavender | `#E6E6FA` | Act III labels · secondary accents · stat box backgrounds |
| Charcoal | `#2D2D2D` | All primary text · slide titles · stat numbers |
| Medium Gray | `#5a8099` | Secondary text · captions · footer text · axis labels |
| Light Gray | `#f5f7fa` | Card backgrounds · surface fills |
| Coral Red | `#E05555` | Act V labels only · breakthrough callouts · never used elsewhere |
| Warm Amber | `#F5C842` | Acknowledgment cards only |

---

### Typography

Font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`

Never import a Google Font. Never use a web font. Use the system stack only.

| Element | Size | Weight | Color |
|---|---|---|---|
| Act label | 10px | 600 | Act color (see palette) |
| Slide title | 28px to 32px | 600 | Charcoal `#2D2D2D` |
| Section heading | 18px | 600 | Charcoal |
| Body text | 14px | 400 | Charcoal |
| Caption / secondary | 12px | 400 | Medium Gray `#5a8099` |
| Stat number large | 40px to 56px | 600 | Charcoal or act color |
| Stat label | 11px | 400 | Medium Gray |
| Footer text | 11px | 400 | Medium Gray |
| Pill / badge | 10px | 600 | Depends on background |

Never use font-weight above 600. Never use font-size below 10px.

Act labels must be: uppercase, letter-spacing 0.12em, font-size 10px, font-weight 600.

---

### Permanent slide elements — every slide must have all of these

#### 1. Progress bar
- Position: absolute top 0 left 0
- Height: 3px
- Background: `#98FF98`
- Width: calculated as (current slide / total slides) × 100 percent
- Updates on every slide change
- No transition animation on the bar itself — instant update

#### 2. Act label
Top left corner of every slide. Uppercase. Letter-spaced. Small. Colored by act as follows:
- Act I — The World: `#98FF98`
- Act II — The Problem: `#AFEEEE`
- Act III — The Expedition: `#E6E6FA`
- Act IV — The Discovery: `#98FF98`
- Act V — The Breakthrough: `#E05555`
- Act VI — The Solution: `#98FF98`

#### 3. Slide title
Large bold charcoal text immediately below the act label. Never centered unless the slide is a full-bleed impact slide. Left-aligned by default.

#### 4. Neural network watermark
Built as actual inline SVG. Not a CSS background. Not an image tag.
- Position: top left quadrant of the slide
- Opacity: 8 percent
- Color: `#AFEEEE`
- Structure: 10 to 12 nodes of varying radius (2px to 6px) connected by thin lines (stroke-width 0.8px)
- The lines drift from the top-left corner toward the center of the slide and fade out before reaching the center
- The nodes and lines must never overlap with the act label or slide title

SVG structure reference:
```html
<svg class="neural-watermark" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="20" cy="25" r="4" fill="#AFEEEE"/>
  <circle cx="65" cy="15" r="2.5" fill="#AFEEEE"/>
  <circle cx="110" cy="45" r="3.5" fill="#AFEEEE"/>
  <circle cx="45" cy="70" r="2" fill="#AFEEEE"/>
  <circle cx="90" cy="90" r="4.5" fill="#AFEEEE"/>
  <circle cx="140" cy="35" r="2" fill="#AFEEEE"/>
  <circle cx="160" cy="75" r="3" fill="#AFEEEE"/>
  <circle cx="30" cy="110" r="3" fill="#AFEEEE"/>
  <circle cx="80" cy="130" r="2" fill="#AFEEEE"/>
  <line x1="20" y1="25" x2="65" y2="15" stroke="#AFEEEE" stroke-width="0.8" opacity="0.6"/>
  <line x1="65" y1="15" x2="110" y2="45" stroke="#AFEEEE" stroke-width="0.8" opacity="0.5"/>
  <line x1="20" y1="25" x2="45" y2="70" stroke="#AFEEEE" stroke-width="0.8" opacity="0.4"/>
  <line x1="45" y1="70" x2="90" y2="90" stroke="#AFEEEE" stroke-width="0.8" opacity="0.35"/>
  <line x1="110" y1="45" x2="140" y2="35" stroke="#AFEEEE" stroke-width="0.8" opacity="0.3"/>
  <line x1="140" y1="35" x2="160" y2="75" stroke="#AFEEEE" stroke-width="0.6" opacity="0.25"/>
  <line x1="80" y1="130" x2="90" y2="90" stroke="#AFEEEE" stroke-width="0.6" opacity="0.2"/>
</svg>
```

Apply this CSS to position it:
```css
.neural-watermark {
  position: absolute;
  top: 0;
  left: 0;
  width: 45%;
  height: 55%;
  opacity: 0.08;
  pointer-events: none;
  z-index: 0;
}
```

#### 5. Clam shell watermark
Built as actual inline SVG. Not an image tag.
- Position: bottom right corner of the slide
- Opacity: 10 percent
- Color: `#AFEEEE`
- Structure: outer ellipse suggesting the shell shape with 5 to 7 curved lines radiating inward suggesting shell striations, and a small circle at the hinge point

SVG structure reference:
```html
<svg class="clam-watermark" viewBox="0 0 120 100" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="60" cy="58" rx="54" ry="38" fill="none" stroke="#AFEEEE" stroke-width="2.5"/>
  <path d="M 8 58 Q 60 12 112 58" fill="none" stroke="#AFEEEE" stroke-width="1.8"/>
  <path d="M 15 65 Q 60 22 105 65" fill="none" stroke="#AFEEEE" stroke-width="1.4"/>
  <path d="M 22 72 Q 60 34 98 72" fill="none" stroke="#AFEEEE" stroke-width="1.1"/>
  <path d="M 30 78 Q 60 46 90 78" fill="none" stroke="#AFEEEE" stroke-width="0.9"/>
  <path d="M 38 83 Q 60 56 82 83" fill="none" stroke="#AFEEEE" stroke-width="0.7"/>
  <circle cx="60" cy="58" r="5" fill="#AFEEEE"/>
</svg>
```

Apply this CSS:
```css
.clam-watermark {
  position: absolute;
  bottom: 36px;
  right: 0;
  width: 22%;
  height: 44%;
  opacity: 0.10;
  pointer-events: none;
  z-index: 0;
}
```

#### 6. Footer rule
- Position: absolute bottom 0 left 0 right 0
- Height: 36px
- Border-top: 1.5px solid `#AFEEEE`
- Background: rgba(240, 248, 255, 0.95)
- Contains: URI — Paz, 2025 left-aligned in small gray + slide number right-aligned in small gray

#### 7. Content z-index
All actual slide content must sit at z-index 1 or above. Watermarks sit at z-index 0. Footer sits at z-index 2.

---

### Card system

Use cards for all grouped content. Never use plain bullet lists.

#### Standard card
```css
background: #ffffff;
border: 0.5px solid rgba(175, 238, 238, 0.5);
border-radius: 10px;
padding: 14px 16px;
```

#### Stat callout card
```css
background: rgba(240, 248, 255, 0.8);
border-radius: 8px;
padding: 12px 14px;
```
Contains: stat number large (40px to 56px, font-weight 600, charcoal) above stat label (11px, medium gray).

#### Accent card — left border variant
```css
background: #ffffff;
border-left: 3px solid [act color];
border-radius: 0 8px 8px 0;
padding: 10px 14px;
```

#### Comparison panel
Two side-by-side cards with a large arrow between them. Left card light gray background for the problem. Right card mint green tint background for the solution.


#### Placeholder box — for manuscript figures when image is NOT provided
```css
border: 2px dashed #AFEEEE;
border-radius: 8px;
background: rgba(175, 238, 238, 0.05);
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap: 6px;
padding: 16px;
```
Contains: bold label INSERT FIGURE X.X HERE + italic gray caption text below.

---

## IMAGE HANDLING SYSTEM

### Creative liberty with uploaded figures

When the author uploads an image — bar chart, scatter plot, heatmap, ROC curve, density plot, or any other figure — do not simply drop it into an img tag and move on. Treat every uploaded figure as a design opportunity. Your job is to make it feel like it was born inside this presentation, not pasted in from a manuscript PDF.

### Detection rule
If an image file is present in the uploaded files and corresponds to a figure referenced on a slide, use that image. If no image is uploaded for a figure, use the dashed placeholder box defined above.

### Image integration rules

#### Sizing and placement
- Never display a figure at its raw pixel dimensions
- Always size figures to fill their designated content area naturally — use width 100%, max-width constraints, and object-fit contain
- Figures should be large enough to read clearly without leaning forward — if the text in the figure would be illegible on a projector, the figure is too small
- Center figures horizontally within their container
- Give every figure at minimum 16px breathing room from all surrounding elements

#### Visual framing
Every uploaded figure gets a frame that integrates it with the slide design:
```css
.figure-frame {
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(175, 238, 238, 0.4);
  background: #ffffff;
  padding: 12px;
  position: relative;
}
```

#### Figure caption
Every figure must have a caption below it styled as:
```css
.figure-caption {
  font-size: 11px;
  color: #5a8099;
  font-style: italic;
  text-align: center;
  margin-top: 6px;
  line-height: 1.5;
}
```
Pull caption text directly from the manuscript figure caption. Do not invent captions.

#### Figure label badge
Every figure gets a small label badge in the top left corner of its frame:
```css
.figure-label {
  position: absolute;
  top: 8px;
  left: 8px;
  background: rgba(175, 238, 238, 0.9);
  color: #185FA5;
  font-size: 10px;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 20px;
  letter-spacing: 0.05em;
}
```
Label text format: Figure 1.2 or Table 1.1 matching the manuscript numbering.

### Figure-specific creative treatment

You have creative liberty to enhance how figures are displayed. Use good judgment. The goal is always clarity and integration with the slide design — not decoration.

#### Bar charts and feature importance charts
- If the figure has a white or near-white background display it inside the figure frame directly
- If the figure has a gray or dark background that clashes with the slide add a softening inner border using box-shadow: inset 0 0 0 1px rgba(175,238,238,0.3)
- Consider whether a callout annotation can be added below the figure pointing to the most important bar or value — for example a small Mint Green pill badge saying top-ranked: beta-hexosaminidase placed below the figure aligned with the relevant bar

#### ROC curves
- Display large and centered — ROC curves need space to communicate
- Add a small annotation badge showing AUC = 0.9985 in the top right area of the figure frame if not already clearly visible in the image
- The curve should be the hero of the slide — do not crowd it with too much surrounding text

#### Heatmaps
- Display as wide as the layout permits
- If the heatmap shows neoplastic versus normal pools consider adding small colored pills above the relevant columns matching the palette — lavender for neoplastic, pale blue for normal
- Add a color scale description below the caption if the figure legend is too small to read on a projector

#### Scatter plots and UMAP projections
- Display large — these figures lose meaning when small
- If the figure contains a legend that is hard to read at presentation size recreate the legend as HTML below the figure using colored pills that match the palette

#### Density plots and violin plots
- Ensure the x-axis labels are legible — if they are not note this in your Phase 5 critique
- Add a callout annotation for the key threshold value — for example a small descriptive note indicating the 0.5 neoplastic probability threshold where relevant

### Seamless integration rule
After placing any figure ask yourself: does this image look like it belongs here, or does it look like it was dropped in? If it looks dropped in, apply one or more of the following:
- Add the figure frame with border and padding
- Adjust the frame background to match the figure background
- Add a figure label badge
- Add a callout annotation pointing to the key result in the figure
- Add a caption that contextualizes the figure for the audience

### Animation for uploaded figures
Every uploaded figure gets the scaleFadeIn entrance animation when its slide becomes active. Duration 0.9 seconds, easing ease. This makes figures feel like they are being revealed rather than simply appearing. Do not skip this for any uploaded figure.

---

## TEXT EMERGENCE ANIMATION SYSTEM

### Philosophy
Text should not appear all at once like a wall of information. Every slide tells a story and the text should emerge in the order the story is told. The audience should read one idea, absorb it, and then the next idea arrives. This is not decoration — it is pacing.

### Core rule
Every piece of text content on every slide gets an entrance animation. Nothing appears instantly. The question is only what type of entrance and in what order.

### Entrance animation types

#### Type 1 — Slide up and fade (default for all body text)
```css
@keyframes textEmerge {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.text-emerge {
  animation: textEmerge 0.5s ease forwards;
  opacity: 0;
}
```
Use for: body text, card content, bullet points converted to cards, secondary headings, captions.

#### Type 2 — Fade only (for slide titles and act labels)
```css
@keyframes titleFade {
  from { opacity: 0; }
  to   { opacity: 1; }
}
.title-fade {
  animation: titleFade 0.4s ease forwards;
  opacity: 0;
}
```
Use for: slide titles, act labels. Titles should appear first before any body content.

#### Type 3 — Scale up and fade (for stat numbers and breakthrough callouts)
```css
@keyframes statReveal {
  from {
    opacity: 0;
    transform: scale(0.85);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
.stat-reveal {
  animation: statReveal 0.6s ease forwards;
  opacity: 0;
}
```
Use for: large stat numbers, AUC values, percentage callouts, breakthrough numbers and key result callouts.

#### Type 4 — Slide in from left (for pipeline steps and process flows)
```css
@keyframes slideFromLeft {
  from {
    opacity: 0;
    transform: translateX(-16px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
.slide-from-left {
  animation: slideFromLeft 0.5s ease forwards;
  opacity: 0;
}
```
Use for: pipeline step cards, numbered process steps, sequential list items where the left-to-right reading order matters.

#### Type 5 — Word by word emergence (for single-sentence impact statements only)
This is reserved for slides where one sentence is the entire message — for example the research question slide or the breakthrough result slide.

```javascript
function wordByWord(element, delayStart, delayBetween) {
  const words = element.textContent.split(' ');
  element.innerHTML = '';
  words.forEach((word, i) => {
    const span = document.createElement('span');
    span.textContent = word + ' ';
    span.style.cssText = `
      opacity: 0;
      display: inline-block;
      animation: textEmerge 0.4s ease forwards;
      animation-delay: ${delayStart + i * delayBetween}s;
    `;
    element.appendChild(span);
  });
}
```
Use sparingly. Only on slides where the sentence is the climax. Maximum 2 slides in the entire deck.

### Stagger timing rules

The stagger delay between elements tells the audience where to look next. Apply these delays in strict reading order — top to bottom, left to right.

| Element type | Delay from slide activation |
|---|---|
| Act label | 0s |
| Slide title | 0.1s |
| Subtitle or section label | 0.25s |
| First card or first body paragraph | 0.4s |
| Second card or second paragraph | 0.55s |
| Third card | 0.7s |
| Fourth card | 0.85s |
| Figure or image | 0.5s (independent of text sequence) |
| Stat number | 0.6s |
| Callout badge or annotation | 0.8s |
| Caption | 0.9s |

Never stagger more than 6 elements on a single slide. If a slide has more than 6 elements group related elements so they animate together.

### Implementation rule
Apply animation classes and delays using JavaScript when a slide becomes active, not via CSS alone. This ensures animations replay every time the slide is visited.

```javascript
function animateSlide(slideElement) {
  const elements = slideElement.querySelectorAll('[data-animate]');
  elements.forEach(el => {
    el.style.opacity = '0';
    el.style.animation = 'none';
    void el.offsetWidth; // force reflow to restart animation
    const type = el.dataset.animate;
    const delay = el.dataset.delay || '0';
    el.style.animationDelay = delay + 's';
    el.classList.add(type);
  });
}
```

Mark every animated element in the HTML with data-animate and data-delay attributes:
```html
<div class="act-label" data-animate="title-fade" data-delay="0">Act IV — The Discovery</div>
<h2 class="slide-title" data-animate="title-fade" data-delay="0.1">Biomarker Discovery</h2>
<div class="card" data-animate="text-emerge" data-delay="0.4">406 unique candidates...</div>
<div class="stat-card" data-animate="stat-reveal" data-delay="0.6">0.9985</div>
```

### Creative liberty for text animations
You have creative liberty to choose which animation type fits each slide best. The rules above are the default. You may deviate from them when a different animation type communicates the content more clearly. The only constraints are:

- Never use bouncing, spinning, or flashing animations
- Never animate in a way that distracts from the content
- Never use the same dramatic animation (word-by-word, stat-reveal) on more than 2 slides total
- Always animate in reading order — never make the audience hunt for what to read next
- Act labels and titles always appear before body content — no exceptions

### Special case — high-impact single-stat slides
If the PowerPoint contains any slide where a single large number or short phrase is the entire message — for example a mortality rate, a classification accuracy, or an early detection result — apply this treatment: use statReveal for the number at 0.6s delay, word-by-word emergence for any supporting sentence at 0.8s delay, and let the final closing line arrive last. These slides should feel like a reveal, not a dump. Identify them from the PowerPoint during Phase 1 and flag them in your extraction output.

---

## NAVIGATION SYSTEM

### Keyboard
- ArrowRight and ArrowDown: advance to next slide
- ArrowLeft and ArrowUp: go to previous slide
- Home: jump to slide 1
- End: jump to last slide

### On-screen controls
- Left arrow button: absolute left 16px, vertically centered, 36px circle, charcoal border, transparent background, hover pale blue tint
- Right arrow button: absolute right 16px, vertically centered, same style
- Both buttons always visible

### Slide counter
- Position: footer right side
- Format: current / total (example: 3 / 24)
- Clicking the counter opens a slide navigator panel

### Navigator panel
- Opens on click of slide counter
- Lists all slide titles with their numbers
- Clicking any title jumps to that slide
- Closes when a slide is selected or when clicking outside
- Background: white, border: 0.5px solid pale blue, border-radius 10px, max-height 60vh, overflow-y scroll

### Transitions
- All slide changes: opacity fade 300ms ease
- No sliding, no scaling, no bouncing
- Slides stack at position absolute, top 0, left 0, width 100%, height 100%
- Active slide: opacity 1, pointer-events auto
- Inactive slides: opacity 0, pointer-events none

---

## ANIMATION SYSTEM

### Global rules
- All animations use CSS keyframes only
- Animate only: transform, opacity, stroke-dashoffset, stroke-dasharray
- Never animate width, height, left, top, margin, or padding
- Wrap all animations in `@media (prefers-reduced-motion: no-preference)` except the SVM animation
- Animation classes are added by JavaScript when a slide becomes active
- Animations replay every time the slide is revisited

### Text entrance animation
The full text emergence animation system is defined in the TEXT EMERGENCE ANIMATION SYSTEM section above. That section is the authoritative reference. The summary below is for quick reference only.

```css
@keyframes slideUpFade {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
```
- Duration: 0.5s
- Easing: ease
- Apply to: slide titles, card headings, body paragraphs
- Stagger delay: per the stagger timing table in TEXT EMERGENCE ANIMATION SYSTEM
- Use data-animate and data-delay attributes on every element as defined in that section

### Figure reveal animation
```css
@keyframes scaleFadeIn {
  from { opacity: 0; transform: scale(0.96); }
  to   { opacity: 1; transform: scale(1); }
}
```
- Duration: 0.8s
- Easing: ease
- Apply to: figure placeholder boxes, stat cards, comparison panels

### Stat number count-up animation
- Use JavaScript requestAnimationFrame
- Duration: 1.2 seconds
- Easing: ease-out
- Apply to any slide that contains a large stat number as its primary content — identify these during Phase 1 extraction and mark them with data-countup="true" on the stat element
- Round all displayed values to one decimal place

### Boundary draw animation
```css
@keyframes drawLine {
  from { stroke-dashoffset: var(--line-length); }
  to   { stroke-dashoffset: 0; }
}
```
- Duration: 1s
- Easing: ease
- Apply to: SVM decision boundary, ROC curve (if animated)

### Pop-in animation
```css
@keyframes popIn {
  0%   { transform: scale(0); opacity: 0; }
  60%  { transform: scale(1.08); }
  100% { transform: scale(1); opacity: 1; }
}
```
- Duration: 0.4s
- Apply to: AUC badge, breakthrough callouts

---

## SVM PIPELINE ANIMATION — MANDATORY

### Location
Insert this animation into the slide titled What the Classifier Is Actually Doing. It replaces the slide body content. Do not put it in a separate slide.

### Behavior
Fully automatic. Loops continuously. No user interaction. No buttons. No clicking.

### Structure
Two panels side by side. Left panel is an SVG scatter plot 300 by 260 pixels. Right panel is a vertical pipeline list 200px wide.

A Mint Green progress bar fills left to right across the top of the widget proportional to the current step.

### The two cell populations
- Neoplastic hemocytes: always on the LEFT side of the scatter. Color: lavender `#E6E6FA` fill with purple `#7F77DD` stroke. Radius 5.5px.
- Normal hemocytes: always on the RIGHT side of the scatter. Color: pale blue `#AFEEEE` fill with blue `#185FA5` stroke. Radius 5.5px.
- 15 points per group.
- Both populations are present from Step 1 and never disappear.
- Points transition smoothly between positions using CSS transitions on cx and cy attributes.

### Step 1 — Raw count matrix (holds 2.5 seconds)
- Points are spread loosely across both sides with high jitter — the two clusters overlap heavily and are barely separable
- X axis: raw counts, Y axis: gene expression
- Pipeline step 1 highlights
- Caption: CPM normalization applied — counts scaled to counts-per-million per cell

### Step 2 — Log transform (holds 2.5 seconds)
- Points tighten slightly — clusters begin to pull apart
- X axis: log₂(CPM+1), Y axis: log₂(CPM+1)
- Pipeline step 2 highlights
- Caption: log₂(CPM+1) transform applied — variance stabilized — library-size effects removed

### Step 3 — HVG selection (holds 2.5 seconds)
- Points reorganize further — jitter reduces
- A small annotation appears on the scatter listing: HVG 3,000 / HVG 5,000 / all genes
- Pipeline step 3 highlights
- Caption: Seurat v3 HVG selection — three feature-set configurations evaluated

### Step 4 — Standard scaling and PCA (holds 3 seconds)
- Clusters rotate into PCA space — the two populations now separate clearly with visible space between them
- Zone label Neoplastic appears above left cluster in purple — Normal appears above right cluster in blue
- Soft shaded backgrounds tint each side (lavender left, pale blue right) at 9 percent opacity
- X axis: PC1, Y axis: PC2
- Pipeline step 4 highlights
- Caption: standard scaling fit on training data only — PCA dimensionality reduction fit on training data only — 10 to 100 components

### Step 5 — SVM searches (holds 4 seconds)
This is the most important step. The audience must see the SVM searching.

- A vertical dashed line in lavender sweeps slowly from left to right across the scatter — this represents the SVM testing candidate boundaries
- As the scanning line moves, 3 to 4 faint dashed vertical candidate boundary lines appear one at a time at different positions between the clusters and then fade out — these are boundaries being evaluated and rejected because they do not maximize the margin
- On the right pipeline panel below the step list show the C values — 0.1, 0.5, 1, 2, 5, 10 — as small pills that highlight one at a time cycling through as if being tested
- Below the C pills show PCA components: 10, 20, 30, 40, 50, 75, 100
- Pipeline step 5 highlights
- Caption: grid search C ∈ {0.1, 0.5, 1, 2, 5, 10} × PCA components ∈ {10, 20, 30, 40, 50, 75, 100} — 5-fold stratified cross-validation

### Step 6 — Maximum margin hyperplane found (holds 5 seconds)
- Scanning line stops
- Final decision boundary draws itself as a vertical line between the two clusters using stroke-dasharray animation over 1.2 seconds — color Mint Green `#98FF98`, stroke-width 2.5px
- After boundary finishes: two dashed parallel margin lines appear on either side in lighter Mint Green at 55 percent opacity
- After margin lines: a double-headed arrow appears between the two margin lines labeled max margin in small bold Mint Green text — this is the key concept
- After margin arrow: three support vector rings appear as circles (radius 10px, no fill, stroke 1.8px) around the three points closest to the boundary — two neoplastic points and one normal point — with a small label below reading support vectors define the margin
- After support vectors: AUC badge pops in at bottom right of scatter using popIn animation — shows AUC in small gray above 0.9985 in large bold charcoal
- Pipeline step 6 highlights
- Caption: max-margin hyperplane found — support vectors are the cells nearest the boundary — AUC = 0.9985 on held-out 30 percent test split

### Loop
After Step 6 holds for 5 seconds: pause 3 seconds, then restart from Step 1. Total loop time approximately 22 to 25 seconds.

### Pipeline list styling
- Active step: Pale Blue border, Pale Blue tinted background, opacity 1
- Completed steps: opacity 0.55, no border
- Future steps: opacity 0.25, no border
- Each step has a numbered circle badge on the left and title plus subtitle text on the right
- Step 5 additionally shows the C value pills and PCA component values below the pipeline list when active

### Key concepts the animation must communicate
1. CPM normalization and log transform clean the data before classification
2. HVG selection reduces noise by keeping only the most informative genes
3. Standard scaling and PCA are fit on training data only to prevent data leakage
4. The SVM does not pick an arbitrary boundary — it searches specifically for the boundary that maximizes the margin between the two classes
5. Support vectors are the specific cells that define that boundary
6. Regularization parameter C controls how strictly the margin is enforced
7. The final model achieves AUC = 0.9985 on a completely held-out test split

---

## PHASE EXECUTION ORDER

Work through these phases in strict order. Tell me which phase you are in before starting it. Do not skip phases. Do not combine phases.

### Phase 1 — Extract
Read the PowerPoint. List every slide with its number, title, content summary, and layout type. Output this as a numbered list before writing any HTML. Wait for confirmation before proceeding.

### Phase 2 — Structure
Build the HTML structure for every slide exactly as extracted. No design improvements yet. Use placeholder div elements. Verify slide count matches PowerPoint.

### Phase 3 — Design
Apply the full visual design system from this file to every slide. Cards, colors, typography, watermarks, footer, progress bar. Do not change content — only visual presentation.

### Phase 4 — Animations
Add the global animation system to all slides. Add the SVM pipeline animation to the classifier slide. Verify the SVM animation loops correctly before proceeding.

### Phase 5 — Critique
For each slide output a one-line evaluation: keep as-is, needs stronger visual, too text-heavy, needs animation, needs conceptual setup, or candidate for merge. Output as a numbered list matching slide numbers. Pause and wait for approval.

### Phase 6 — Refine
Apply approved changes from Phase 5 critique surgically. Do not restructure slides that were not flagged. Do not rewrite content. Preserve pacing.

---

## CONTENT RULES

- Never rewrite text from the PowerPoint unless it contains a clear typo
- Never add a statistic that is not in the PowerPoint or manuscript
- Never add biological interpretation that is not in the manuscript
- Never add a slide that is not in the PowerPoint
- For any slide containing a manuscript figure: create a dashed-border placeholder box with INSERT FIGURE X.X HERE in bold and the figure caption in small italic gray below it
- Keep wording minimal on slides — the audience reads the speaker not the slide
- If a slide in the PowerPoint has three points keep three points — do not expand to five
- If a slide uses cards use cards — do not convert to bullet lists
- If a slide uses bullet lists convert them to cards following the card system in this file

---

## QUALITY STANDARD

The final file should feel like:
- Apple Keynote level design
- Conference quality talk
- Visually guided explanation not a document

Every slide should pass this test: if you removed all text, would the layout and visual hierarchy still communicate something? If the answer is no the slide needs more visual structure.

---

## FINAL OUTPUT REQUIREMENTS

- One single self-contained HTML file
- All CSS inline in a single style block in the head
- All JavaScript inline in a single script block before the closing body tag
- No external stylesheets
- No external scripts
- No external fonts
- No CDN links
- Must open correctly in Chrome with no internet connection
- Must work with keyboard navigation
- Must display correctly at 1280px wide and 1920px wide
- Must display correctly at 16:9 aspect ratio

---

## SLIDE SCALING AND ASPECT RATIO

### The slide container
Every slide must maintain a strict 16:9 aspect ratio at all screen sizes. Use this pattern:

```css
.deck {
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #1a1a2e;
  overflow: hidden;
}

.slide-container {
  position: relative;
  width: 100%;
  max-width: calc(100vh * 16 / 9);
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: linear-gradient(180deg, #ffffff 0%, #F0F8FF 100%);
}
```

This means on a wide screen the slide is letterboxed with a dark surround. On a tall screen it is pillarboxed. The slide itself never stretches or distorts. The dark surround color is `#1a1a2e` — a very dark navy that complements the pale blue palette without being harsh black.

### Font scaling
All font sizes inside the slide container are defined in px against a 1280px-wide reference. Use this JavaScript to scale everything proportionally on resize:

```javascript
function scaleSlides() {
  const container = document.querySelector('.slide-container');
  const scaleX = container.offsetWidth / 1280;
  container.style.fontSize = (16 * scaleX) + 'px';
}
window.addEventListener('resize', scaleSlides);
scaleSlides();
```

Then use em units for all font sizes in the slide content so they scale with the container font size. The CSS typography table elsewhere in this file gives px values — convert them to em relative to 16px base (e.g. 32px title = 2em, 14px body = 0.875em).

---

## OPENING TITLE SCREEN

Before Slide 1 displays, show a full-screen opening screen. This is not counted as a slide — it does not appear in the slide counter or navigator.

Structure:
- Same background as slides — white to #F0F8FF gradient
- Neural network watermark top left at 8% opacity
- Clam shell watermark bottom right at 10% opacity
- Center of screen: thesis title in large bold charcoal, author name below in medium weight, institution and year below that in medium gray
- A single button labeled Begin centered below the text — styled with a Mint Green border, transparent background, charcoal text, border-radius 24px, padding 10px 32px
- Clicking Begin or pressing any key advances to Slide 1 with a 300ms fade

The opening screen text animates in using titleFade for the title at 0s and textEmerge for each subsequent line staggered at 0.2s intervals. The Begin button appears last at 0.8s delay using popIn animation.

---

## LAST SLIDE BEHAVIOR

When the user advances past the final slide do not loop back silently. Instead:
- Show a brief full-screen end screen matching the opening screen style
- Center text: Thank you — and below it in smaller gray: University of Rhode Island · 2025
- Show two buttons side by side: Return to Start (navigates to Slide 1) and View Again (navigates to Slide 1 and replays from beginning)
- This end screen is not counted in the slide numbering

---

## FULL SCREEN MODE

Pressing F on the keyboard toggles the browser into full-screen mode using the Fullscreen API:

```javascript
document.addEventListener('keydown', e => {
  if (e.key === 'f' || e.key === 'F') {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  }
});
```

Show a small tooltip hint on the opening screen below the Begin button: Press F for full screen — styled in small light gray italic text.

---

## TOUCH AND SWIPE NAVIGATION

Support touch navigation for tablet and touch screen use:

```javascript
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', e => {
  touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', e => {
  touchEndX = e.changedTouches[0].screenX;
  const diff = touchStartX - touchEndX;
  if (Math.abs(diff) > 50) {
    if (diff > 0) nextSlide();
    else prevSlide();
  }
});
```

---

## SLIDE LAYOUT TEMPLATES

Every slide must use one of these five layout templates. Choose the template based on the content type extracted from the PowerPoint. Do not invent hybrid layouts.

### Template A — Text-dominant
Use when: the slide contains primarily text content, cards, or stat callouts with no figures.

```
┌─────────────────────────────────────────────────────┐
│ [act label]                        [neural watermark]│
│ [slide title]                                        │
│                                                      │
│  [card 1]    [card 2]    [card 3]                    │
│                                                      │
│  [card 4]    [card 5]                                │
│                                              [clam]  │
│─────────────────────────────────────────────────────│
│ URI — Paz, 2025                           3 / 24     │
└─────────────────────────────────────────────────────┘
```

Layout CSS:
```css
.layout-text {
  display: grid;
  grid-template-rows: auto 1fr;
  padding: 3% 5% 14% 5%;
  gap: 2%;
}
.layout-text .cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  align-content: start;
}
```

### Template B — Figure dominant
Use when: the slide has one large figure as its primary content with minimal supporting text.

```
┌─────────────────────────────────────────────────────┐
│ [act label]                                          │
│ [slide title]                                        │
│                                                      │
│  ┌─────────────────────────────────────────────┐    │
│  │                                             │    │
│  │           [figure — fills space]            │    │
│  │                                             │    │
│  └─────────────────────────────────────────────┘    │
│  [caption]                                   [clam] │
│─────────────────────────────────────────────────────│
│ URI — Paz, 2025                           3 / 24     │
└─────────────────────────────────────────────────────┘
```

Layout CSS:
```css
.layout-figure {
  display: grid;
  grid-template-rows: auto 1fr auto;
  padding: 3% 5% 14% 5%;
  gap: 12px;
}
.layout-figure .figure-frame {
  width: 100%;
  flex: 1;
  min-height: 0;
}
.layout-figure img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
```

### Template C — Figure left, text right
Use when: the slide has one figure and a set of key points or stat callouts that interpret it.

```
┌─────────────────────────────────────────────────────┐
│ [act label]                                          │
│ [slide title]                                        │
│                                                      │
│  ┌──────────────────┐    [stat card]                 │
│  │                  │    [stat card]                 │
│  │    [figure]      │    [stat card]                 │
│  │                  │                                │
│  └──────────────────┘    [takeaway text]     [clam] │
│─────────────────────────────────────────────────────│
│ URI — Paz, 2025                           3 / 24     │
└─────────────────────────────────────────────────────┘
```

Layout CSS:
```css
.layout-figure-left {
  display: grid;
  grid-template-rows: auto 1fr;
  padding: 3% 5% 14% 5%;
  gap: 2%;
}
.layout-figure-left .content-row {
  display: grid;
  grid-template-columns: 55% 1fr;
  gap: 24px;
  min-height: 0;
}
```

### Template D — Impact statement
Use when: the slide has a single large number, a single sentence, or a single bold claim as its entire message. No figures. Minimal text.

```
┌─────────────────────────────────────────────────────┐
│ [act label]                        [neural watermark]│
│                                                      │
│                                                      │
│              [enormous stat or statement]            │
│                                                      │
│              [single supporting sentence]            │
│                                              [clam]  │
│─────────────────────────────────────────────────────│
│ URI — Paz, 2025                           3 / 24     │
└─────────────────────────────────────────────────────┘
```

Layout CSS:
```css
.layout-impact {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 5% 10% 14% 10%;
  text-align: center;
  gap: 16px;
}
.layout-impact .impact-number {
  font-size: 4em;
  font-weight: 600;
  color: #2D2D2D;
  line-height: 1;
}
.layout-impact .impact-text {
  font-size: 1.1em;
  color: #5a8099;
  max-width: 60%;
}
```

### Template E — Two-column comparison
Use when: the slide is explicitly comparing two things — current state vs desired state, method A vs method B, before vs after.

```
┌─────────────────────────────────────────────────────┐
│ [act label]                                          │
│ [slide title]                                        │
│                                                      │
│  ┌──────────────────┐   →   ┌──────────────────┐    │
│  │   [left panel]   │       │  [right panel]   │    │
│  │                  │       │                  │    │
│  └──────────────────┘       └──────────────────┘    │
│                                              [clam]  │
│─────────────────────────────────────────────────────│
│ URI — Paz, 2025                           3 / 24     │
└─────────────────────────────────────────────────────┘
```

Layout CSS:
```css
.layout-comparison {
  display: grid;
  grid-template-rows: auto 1fr;
  padding: 3% 5% 14% 5%;
  gap: 2%;
}
.layout-comparison .panels {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 16px;
  align-items: center;
}
.layout-comparison .arrow {
  font-size: 1.5em;
  color: #AFEEEE;
  text-align: center;
}
```

### Template selection rule
During Phase 1 extraction, assign a template to every slide and include it in your extraction output:
- SLIDE 3 — What BTN Is — Template A (3 cards)
- SLIDE 8 — ROC Curve — Template B (figure dominant)
- SLIDE 13 — Classification Result — Template C (figure left, stats right)

---

## MULTIPLE FIGURES ON ONE SLIDE

### When a slide contains two figures
Use a two-column grid. Each figure gets equal width. Each gets its own frame, label badge, and caption. The two figures must be the same height — use a fixed height container with object-fit contain so neither figure is distorted.

```css
.two-figure-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  align-items: start;
}
.figure-slot {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.figure-slot .figure-frame {
  height: 280px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.figure-slot img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
```

### When a slide contains three figures
This is a red flag. Flag it in Phase 5 critique as: THREE FIGURES — candidate for split into two slides. However if the slide must stay as three figures use a layout where the most important figure is larger (left column, full height) and the two supporting figures are stacked in the right column (right column, half height each).

```css
.three-figure-grid {
  display: grid;
  grid-template-columns: 55% 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 16px;
}
.figure-primary {
  grid-row: 1 / 3;
}
```

### When a slide contains four or more figures
Always flag as MUST SPLIT in Phase 5 critique. Four figures on one slide is never acceptable. The audience cannot process four scientific figures simultaneously. Propose a split and wait for approval before building.

### Figure comparison rule
When two figures are placed side by side and the explicit purpose is comparison — for example neoplastic versus normal expression patterns, or Trial 1 versus Trial 2 results — add a thin vertical Pale Blue divider line between them and a small centered label above the divider reading versus in small gray italic. This signals to the audience that they should be comparing the two panels.

### Animation for multiple figures
When a slide has two figures stagger their entrance: first figure enters at 0.5s delay, second figure at 0.8s delay. Never let both figures appear simultaneously — the stagger directs the audience to look at the first figure before the second arrives.

---

## TABLE STYLING

Several slides in this thesis defense contain data tables — the SVM performance table, the top 20 biomarker table, and the cancer hallmarks mapping table. All tables must be styled as follows.

### Table container
```css
.slide-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 0.75em;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(175, 238, 238, 0.4);
}
```

### Header row
```css
.slide-table thead tr {
  background: rgba(175, 238, 238, 0.2);
}
.slide-table thead th {
  padding: 10px 14px;
  text-align: left;
  font-weight: 600;
  color: #2D2D2D;
  font-size: 0.85em;
  letter-spacing: 0.04em;
  border-bottom: 1.5px solid rgba(175, 238, 238, 0.5);
}
```

### Body rows — alternating
```css
.slide-table tbody tr:nth-child(even) {
  background: rgba(240, 248, 255, 0.6);
}
.slide-table tbody tr:nth-child(odd) {
  background: #ffffff;
}
.slide-table tbody td {
  padding: 8px 14px;
  color: #2D2D2D;
  border-bottom: 0.5px solid rgba(175, 238, 238, 0.2);
  vertical-align: middle;
}
```

### Highlighted row — for best result
If a table has a row that represents the best or most important result — for example the HVG 5000 row with AUC 0.9985 — highlight it:
```css
.slide-table tbody tr.highlight {
  background: rgba(152, 255, 152, 0.12);
  font-weight: 600;
}
.slide-table tbody tr.highlight td {
  color: #1a3a2a;
}
```

### Table animation
Tables enter as a whole unit using scaleFadeIn at 0.5s delay. Do not animate individual rows — animating table rows causes layout jank.

---

## PILL AND BADGE COMPONENT

Pills and badges are used throughout the deck for labels, category indicators, C-value displays, and annotation callouts. Use these definitions consistently.

### Standard pill — informational
```css
.pill {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 0.625em;
  font-weight: 600;
  letter-spacing: 0.06em;
  white-space: nowrap;
}
```

### Pill color variants
| Variant | Background | Text color | Use for |
|---|---|---|---|
| mint | rgba(152,255,152,0.2) | #27500A | positive results, checkmarks |
| blue | rgba(175,238,238,0.25) | #0C447C | neutral labels, info |
| lavender | rgba(230,230,250,0.3) | #3C3489 | category labels, Act III |
| coral | rgba(224,85,85,0.15) | #791F1F | warnings, Act V callouts |
| amber | rgba(245,200,66,0.2) | #412402 | acknowledgments |
| gray | rgba(90,128,153,0.15) | #2D2D2D | neutral, uncharacterized |

### Act label badge
Used for the act label on every slide:
```css
.act-label {
  display: inline-block;
  font-size: 0.625em;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 6px;
}
```

### Number badge — for pipeline steps and ranked lists
```css
.number-badge {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.625em;
  font-weight: 600;
  flex-shrink: 0;
  background: rgba(175, 238, 238, 0.2);
  color: #185FA5;
}
```

---

## LONG SLIDE TITLE HANDLING

If a slide title extracted from the PowerPoint is long enough to wrap to three or more lines at the standard title size, apply this rule automatically:

- 1 to 6 words: font-size 2em (standard)
- 7 to 10 words: font-size 1.6em
- 11 to 14 words: font-size 1.3em
- 15 or more words: flag in Phase 5 critique as TITLE TOO LONG — suggest shortening to the author

Never truncate a title with an ellipsis. Never let a title overflow its container. Either scale it down or flag it.

---

## IMAGE LOAD FAILURE HANDLING

If an uploaded image fails to load the img element will show a broken icon. Prevent this with an error handler:

```javascript
document.querySelectorAll('.figure-frame img').forEach(img => {
  img.addEventListener('error', function() {
    const frame = this.closest('.figure-frame');
    if (frame) {
      const label = frame.querySelector('.figure-label');
      const labelText = label ? label.textContent : 'Figure';
      frame.innerHTML = `
        <div style="
          width: 100%; height: 100%;
          display: flex; flex-direction: column;
          align-items: center; justify-content: center;
          gap: 8px; padding: 16px;
          border: 2px dashed #AFEEEE;
          border-radius: 8px;
          background: rgba(175,238,238,0.05);
        ">
          <span style="font-size:0.75em;font-weight:600;color:#2D2D2D;">${labelText}</span>
          <span style="font-size:0.625em;color:#5a8099;font-style:italic;">Image not loaded — add file to presentation folder</span>
        </div>
      `;
    }
  });
});
```

---

## ACCESSIBILITY

Apply these minimum accessibility rules to every slide:

### Navigation buttons
```html
<button class="nav-btn" aria-label="Previous slide" id="btn-prev">&#8592;</button>
<button class="nav-btn" aria-label="Next slide" id="btn-next">&#8594;</button>
```

### Slide region
Each slide div must have a role and label:
```html
<div class="slide" role="region" aria-label="Slide 3: What BTN Is" data-slide="3">
```

Update the aria-label dynamically when slides change:
```javascript
function updateAccessibility(slideIndex) {
  const slide = slides[slideIndex];
  const title = slide.querySelector('.slide-title')?.textContent || '';
  slide.setAttribute('aria-label', `Slide ${slideIndex + 1}: ${title}`);
}
```

### Focus management
When the user navigates to a slide using the navigator panel, move focus to the slide container so screen readers announce the new slide content.

### Keyboard focus ring
Navigation buttons and the slide counter must show a visible focus ring:
```css
.nav-btn:focus-visible,
.slide-counter:focus-visible {
  outline: 2px solid #98FF98;
  outline-offset: 3px;
}
```

---

## PHASE 5 CRITIQUE — WHAT STRONGER VISUAL MEANS

When flagging slides during Phase 5 use these specific interventions rather than vague notes:

| Problem identified | Specific intervention |
|---|---|
| Slide has a paragraph burying a key number | Extract the number into a stat callout card using Template A |
| Slide has 5 or more bullet points | Convert to cards — maximum 4 cards per slide — if more than 4 points exist propose splitting |
| Slide has only a title and one sentence | Flag as impact candidate — switch to Template D with word-by-word animation |
| Slide has a figure that is too small | Switch to Template B — figure dominant |
| Slide has a figure and surrounding text crowding it | Switch to Template C — figure left text right |
| Slide describes a sequential process in text | Convert to a horizontal pipeline flow using slide-from-left animation on each step |
| Slide has a comparison buried in prose | Switch to Template E — two column comparison |
| Slide has three or more figures | Flag as split candidate — propose which figures go to which new slide |
| Slide title is the same as the previous slide title | Flag as likely transition slide — propose merge |
| Slide has no visual hierarchy — everything looks the same size | Identify the one most important element and make it visually dominant using a stat callout or larger font size |

---

## FIGURE INVENTORY

The project folder contains image1.png through image21.png extracted from the PowerPoint file. These are the actual figure images used in the presentation.

### Your job before Phase 1

Before extracting slides open every image file from image1.png through image21.png. For each one cross-reference it against the PowerPoint to determine which slide it belongs to and what type of figure it is. Then output a complete figure inventory table in this format:

| Filename | Slide number | Figure number | Figure type | Treatment from CLAUDE.md | Special annotation |
|---|---|---|---|---|---|

Wait for author confirmation that the inventory is correct before proceeding to Phase 1.

### Matching rules
- If an image appears on a slide that references a specific figure number from the manuscript use that figure number
- If an image is a decorative or design element rather than a data figure note it as DECORATIVE and do not apply figure frame treatment — use it as a background or inline SVG element instead
- If an image appears on multiple slides note every slide number it appears on
- If you cannot confidently identify what an image is from the PowerPoint context flag it as UNIDENTIFIED and describe what you can see visually so the author can clarify

### Treatment assignment rules
Once you identify the figure type assign the correct treatment from the IMAGE HANDLING SYSTEM section:

| Figure type | Layout template | Special treatment |
|---|---|---|
| ROC curve | Template B — figure dominant | Add AUC badge top right of frame if not clearly visible in the image |
| Bar chart or feature importance chart | Template C — figure left stats right | Consider adding top-ranked callout annotation below chart aligned with highest bar |
| Heatmap | Template B — figure dominant | Add neoplastic and normal column pills above relevant columns if the heatmap compares conditions |
| Scatter plot | Template C — figure left stats right | Recreate legend as HTML pills below figure if legend is too small to read |
| UMAP projection | Template B — figure dominant | Recreate legend as HTML pills below figure — UMAP legends are always too small at presentation size |
| Density plot or violin plot | Template B — figure dominant | Add threshold annotation callout at the relevant probability threshold |
| PCA scatter | Template C — figure left stats right | Add SNP discordance callout if relevant to the slide content |
| Dendrogram | Template C — figure left stats right | No extra annotation needed |
| Experimental design diagram | Template B — figure dominant | No extra annotation needed |
| GO or KEGG enrichment chart | Template B — figure dominant | No extra annotation needed |
| Classifier agreement bar chart | Template B — figure dominant | No extra annotation needed |
| Convergence scatter ML vs DE | Template C — figure left stats right | Add 90% overlap callout annotation |
| Decorative watermark or icon | Inline SVG or CSS background | Apply at specified opacity — do not use figure frame |
| Unknown or unidentified | Flag as UNIDENTIFIED | Describe visually and wait for author clarification before placing |

### Inventory confirmation rule
After outputting the inventory table pause completely. Do not begin Phase 1 extraction until the author replies with one of:
- Confirmed — proceed to Phase 1
- Corrections listed — apply corrections then confirm before proceeding
- Hold — author will clarify specific items

This step exists because misidentifying a figure and placing it on the wrong slide is a critical error that cascades through all subsequent phases. It is worth taking the time to get this right before writing any code.

---

## COMMON FAILURE MODES — AVOID ALL OF THESE

- Using a web font import instead of the system stack
- Hardcoding a color that is not in the palette
- Adding slides not in the PowerPoint
- Inventing statistics
- Forgetting to add watermarks to a slide
- Forgetting to add the footer to a slide
- Making the progress bar static instead of dynamic
- Using bullet lists instead of cards
- Skipping the SVM animation or simplifying it
- Adding external dependencies
- Using font-weight 700 or 800
- Centering slide titles when they should be left-aligned
- Letting content overlap the watermark layer
- Forgetting to add entrance animations to new slides
