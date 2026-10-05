"""
Accepted chronology vs. Fomenko & Nosovsky's New Chronology — poster renderer.

Outputs (same folder):
  fomenko_new_chronology_timeline.png   (200 dpi, 7200 × 9800 px)
  fomenko_new_chronology_timeline.pdf   (vector, printable)

Calendar handling: no year 0. Internally a BCE year Y is mapped to the
astronomical value 1 - Y (1 BCE -> 0, 50 BCE -> -49); CE years are unchanged.
All tick labels are written as "BCE"/"CE", so "0" is never displayed.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch
from matplotlib.transforms import blended_transform_factory
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
FONT_DIR = HERE / "fonts"
for f in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(f))
plt.rcParams["font.family"] = "Inter"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["hatch.linewidth"] = 1.6

# ---------------------------------------------------------------- palette
BLUE = "#1F5FBF"       # accepted chronology
BLUE_T = "#DCE7F7"
BLUE_D = "#143F80"
ORANGE = "#E07000"     # Fomenko / Nosovsky proposal
ORANGE_T = "#FCE3C6"
ORANGE_D = "#9A4A00"
INK = "#1B2230"
MUTED = "#5A6372"
FAINT = "#9AA2AE"
GRID = "#E3E6EB"
PAPER = "#FFFFFF"
BAND = "#F6F7F9"


def bce(y):
    """BCE year -> astronomical axis value (no year zero)."""
    return 1 - y


def ce(y):
    return y


def gap(t1, t2):
    """Elapsed calendar years between two astronomical values."""
    return abs(t2 - t1)


# ---------------------------------------------------------------- figure
FIG_W, FIG_H = 36.0, 49.0
fig = plt.figure(figsize=(FIG_W, FIG_H), facecolor=PAPER)


def ax_in(x, y_top, w, h, **kw):
    """Axes placed in inches, y measured from the top of the page."""
    return fig.add_axes([x / FIG_W, 1 - (y_top + h) / FIG_H, w / FIG_W, h / FIG_H], **kw)


def ftext(x, y_top, s, **kw):
    """Figure text placed in inches from the top-left corner."""
    kw.setdefault("color", INK)
    return fig.text(x / FIG_W, 1 - y_top / FIG_H, s, **kw)


# ================================================================ HEADER
LM = 0.9   # left margin (in)
ftext(LM, 0.95, "Two calendars for the same past", fontsize=60, fontweight="bold", va="top")
ftext(LM, 2.05,
      "Accepted historical chronology compared with the “New Chronology” proposed by "
      "A. T. Fomenko and G. V. Nosovsky", fontsize=25, color=MUTED, va="top")
ftext(LM, 2.6,
      "One continuous calendar axis, c. 3100 BCE → 2026 CE. The calendar has no year 0: 1 BCE is followed "
      "directly by 1 CE. Orange marks show the authors’ proposal as they publish it; they are not accepted findings.",
      fontsize=16, color=MUTED, va="top")

# ---- legend (marks encode the KIND of date, colour encodes WHOSE date)
LEG_Y = 3.35
lx = LM
ftext(lx, LEG_Y, "COLOUR", fontsize=12, fontweight="bold", color=FAINT, va="top")
leg = ax_in(lx, LEG_Y + 0.3, 33.5, 0.9)
leg.set_xlim(0, 33.5)
leg.set_ylim(0, 0.9)
leg.axis("off")


def leg_swatch(x, color, label):
    leg.add_patch(Rectangle((x, 0.35), 0.55, 0.28, color=color, lw=0))
    leg.text(x + 0.7, 0.49, label, fontsize=15, va="center", fontweight="semibold", color=INK)


leg_swatch(0.0, BLUE, "Accepted historical dates")
leg_swatch(4.4, ORANGE, "Fomenko & Nosovsky’s proposed dates")
leg.text(10.0, 1.15, "MARK = KIND OF DATE", fontsize=12, fontweight="bold", color=FAINT, va="top")

kx = 10.0
# broad epoch
leg.add_patch(Rectangle((kx, 0.28), 1.1, 0.42, facecolor="#E9ECF0", edgecolor=MUTED, lw=1.4, ls=(0, (4, 2))))
leg.text(kx + 1.25, 0.49, "Broad historical epoch", fontsize=14, va="center")
kx += 4.6
leg.add_patch(Rectangle((kx, 0.36), 1.1, 0.26, facecolor=MUTED, lw=0))
leg.text(kx + 1.25, 0.49, "Reign, war or dynastic span", fontsize=14, va="center")
kx += 5.1
leg.add_patch(Rectangle((kx, 0.36), 1.1, 0.26, facecolor=MUTED, edgecolor="white", hatch="///", lw=0))
leg.text(kx + 1.25, 0.49, "Construction / making of a monument", fontsize=14, va="center")
kx += 6.3
leg.plot([kx + 0.25], [0.49], marker="D", ms=15, mfc=MUTED, mec=INK, mew=1.2)
leg.text(kx + 0.6, 0.49, "Date read from artwork (zodiac)", fontsize=14, va="center")
kx += 5.2
leg.plot([kx + 0.2], [0.49], marker="o", ms=15, mfc=MUTED, mec=INK, mew=1.2)
leg.text(kx + 0.5, 0.49, "Single-year event", fontsize=14, va="center")

ftext(LM, LEG_Y + 1.25,
      "Grey dashed arrows show the displacement from the accepted date to the proposed one. Alternative dates are drawn as "
      "separate marks joined by “or” — never merged into a span.",
      fontsize=13.5, color=MUTED, va="top")

# ================================================================ MAIN TIMELINE
GUTTER = 8.7                      # left label column (in)
PLOT_X = GUTTER + 0.2
PLOT_W = FIG_W - PLOT_X - 0.9
MAIN_TOP = 5.55
ROW_H = 1.42
rows_n = 10
MAIN_H = rows_n * ROW_H + 0.4

X0, X1 = bce(3150), ce(2090)
ax = ax_in(PLOT_X, MAIN_TOP, PLOT_W, MAIN_H)
ax.set_xlim(X0, X1)
ax.set_ylim(-rows_n - 0.12, 0.28)
ax.axis("off")
lab_tf = blended_transform_factory(fig.transFigure, ax.transData)

# scale: years per inch -> for label offsets
YPI = (X1 - X0) / PLOT_W


def yr_off(inches):
    return inches * YPI


# century grid + axis labels (top and bottom)
ticks = [(bce(y), f"{y:,} BCE") for y in (3000, 2500, 2000, 1500, 1000, 500)] + \
        [(ce(y), f"{y:,} CE") for y in (500, 1000, 1500, 2000)]
for t in range(-2999, 2001, 100):
    ax.axvline(t, color=GRID, lw=0.6, zorder=0)
for t, _ in ticks:
    ax.axvline(t, color="#CDD2D9", lw=1.1, zorder=0)

# subject bands
for i in range(rows_n):
    top = -i
    if i % 2 == 0:
        ax.add_patch(Rectangle((X0, top - 1), X1 - X0, 1, color=BAND, lw=0, zorder=-1))

# axis rulers
axt = ax_in(PLOT_X, MAIN_TOP - 0.55, PLOT_W, 0.5)
axb = ax_in(PLOT_X, MAIN_TOP + MAIN_H + 0.05, PLOT_W, 0.5)
for a, top in ((axt, True), (axb, False)):
    a.set_xlim(X0, X1)
    a.set_ylim(0, 1)
    a.axis("off")
    yline = 0.12 if top else 0.88
    a.plot([X0, X1], [yline, yline], color=INK, lw=1.4)
    for t in range(-2999, 2001, 100):
        a.plot([t, t], [yline, yline + (0.12 if top else -0.12)], color=INK, lw=0.8)
    for t, s in ticks:
        a.plot([t, t], [yline, yline + (0.25 if top else -0.25)], color=INK, lw=1.6)
        a.text(t + (yr_off(0.05) if s == "2,000 CE" else 0), 0.5 if top else 0.42, s,
               ha="right" if s == "2,000 CE" else "center", va="bottom" if top else "top",
               fontsize=15, fontweight="semibold", color=INK)

# era boundary (between 1 BCE and 1 CE)
ERA = 0.5
ax.axvline(ERA, color=INK, lw=1.4, ls=(0, (2, 2)), zorder=1)
axt.text(ERA, 0.5, "1 BCE | 1 CE", ha="center", va="bottom", fontsize=15, fontweight="bold",
         color=INK, bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=INK, lw=1.0))
axb.text(ERA, 0.42, "no year 0", ha="center", va="top", fontsize=13.5, fontstyle="italic", color=INK,
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

# present
NOW = ce(2026)
ax.axvline(NOW, color="#C0182B", lw=3.0, zorder=6)
axt.plot([NOW, NOW], [0.12, 1.75], color="#C0182B", lw=3.0, clip_on=False)
axt.text(NOW - yr_off(0.1), 1.75, "PRESENT · 2026 CE", ha="right", va="top", fontsize=15,
         fontweight="bold", color="#C0182B")
axb.plot([NOW, NOW], [0.0, 0.88], color="#C0182B", lw=3.0)

BAR_H = 0.2
EPOCH_H = 0.3
ACC_DY, PROP_DY, MID_DY = 0.24, 0.74, 0.49


def ya(i):
    return -i - ACC_DY


def yp(i):
    return -i - PROP_DY


def ym(i):
    return -i - MID_DY


# ---- mark primitives
def epoch(y, t0, t1, col, tint, lbl=None, lbl_inside=True, fs=14.5):
    ax.add_patch(Rectangle((t0, y - EPOCH_H / 2), t1 - t0, EPOCH_H, facecolor=tint,
                           edgecolor=col, lw=1.8, ls=(0, (5, 2.5)), zorder=3))
    if lbl and lbl_inside:
        ax.text(t0 + yr_off(0.15), y, lbl, va="center", ha="left", fontsize=fs, color=INK,
                fontweight="semibold", zorder=5)


def span(y, t0, t1, col, hatch=None):
    ax.add_patch(Rectangle((t0, y - BAR_H / 2), max(t1 - t0, yr_off(0.07)), BAR_H,
                           facecolor=col, edgecolor="white" if hatch else col, hatch=hatch,
                           lw=0 if not hatch else 0, zorder=4))
    if hatch:  # crisp outline around hatched bars
        ax.add_patch(Rectangle((t0, y - BAR_H / 2), max(t1 - t0, yr_off(0.07)), BAR_H,
                               facecolor="none", edgecolor=col, lw=1.4, zorder=4.5))


def diamond(y, t, col):
    ax.plot([t], [y], marker="D", ms=17, mfc=col, mec=INK, mew=1.3, zorder=7)


def dot(y, t, col):
    ax.plot([t], [y], marker="o", ms=17, mfc=col, mec=INK, mew=1.3, zorder=7)


def label(y, t, s, ha="left", col=INK, fs=14.5, weight="normal", dy=0.0, style="normal", **kw):
    if dy:
        kw.setdefault("bbox", dict(boxstyle="square,pad=0.08", fc="white", ec="none", alpha=0.85))
    return ax.text(t, y + dy, s, ha=ha, va="center", fontsize=fs, color=col, fontweight=weight,
                   fontstyle=style, zorder=8, **kw)


def displacement(i, ta, tp, text, text_t=None, shift_y=0.0):
    """Elbow connector: accepted mark -> mid line -> proposed mark."""
    y0, y1, y_mid = ya(i) - 0.12, yp(i) + 0.13, ym(i) + shift_y
    ax.plot([ta, ta], [y0, y_mid], color=FAINT, lw=1.6, ls=(0, (3, 2)), zorder=2)
    ax.plot([ta, tp], [y_mid, y_mid], color=FAINT, lw=1.6, ls=(0, (3, 2)), zorder=2)
    ax.add_patch(FancyArrowPatch((tp, y_mid), (tp, y1), arrowstyle="-|>", mutation_scale=18,
                                 color=FAINT, lw=1.6, zorder=2))
    if text:
        tt = text_t if text_t is not None else (ta + tp) / 2
        ax.text(tt, y_mid, text, ha="center", va="center", fontsize=13.5, color=MUTED,
                fontweight="semibold", zorder=6,
                bbox=dict(boxstyle="round,pad=0.28", fc="white", ec=GRID, lw=1))


def row_header(i, title, kind):
    xg = LM / FIG_W
    ax.text(xg, -i - 0.2, title, transform=lab_tf, fontsize=20, fontweight="bold", va="center",
            color=INK)
    ax.text(xg, -i - 0.47, kind, transform=lab_tf, fontsize=12, va="center", color=MUTED,
            fontweight="semibold")
    xr = (GUTTER - 0.1) / FIG_W
    ax.text(xr, ya(i), "ACCEPTED HISTORICAL DATES", transform=lab_tf, ha="right", va="center",
            fontsize=12.5, fontweight="bold", color=BLUE)
    ax.text(xr, yp(i), "FOMENKO’S PROPOSED DATES", transform=lab_tf, ha="right", va="center",
            fontsize=12.5, fontweight="bold", color=ORANGE)
    # thin coloured track guides
    ax.plot([X0, X1], [ya(i), ya(i)], color=BLUE, lw=0.6, alpha=0.25, zorder=1)
    ax.plot([X0, X1], [yp(i), yp(i)], color=ORANGE, lw=0.6, alpha=0.25, zorder=1)


def fmt(n):
    return f"{n:,}"


# ------------------------------------------------------------ 1 Pharaonic Egypt
i = 0
row_header(i, "Pharaonic Egypt", "BROAD EPOCH  vs.  BROAD EPOCH")
epoch(ya(i), bce(3100), bce(30), BLUE, BLUE_T,
      "Pharaonic Egypt · c. 3100–30 BCE  (1st Dynasty → end of Ptolemaic rule)")
epoch(yp(i), ce(1001), ce(1600), ORANGE, ORANGE_T)
label(yp(i), ce(1001) - yr_off(0.15), "Broad placement: 11th–16th c. CE", ha="right", weight="semibold")
label(yp(i), ce(1001) - yr_off(0.15), "Chron3 ch.19 · Chron4 ch.20: all of “ancient” Egypt postdates 900 CE",
      ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, bce(1565), ce(1300), "a c. 3,070-year epoch placed inside c. 600 years — no single fixed offset",
             text_t=bce(560))

# ------------------------------------------------------------ 2 Great Pyramid
i = 1
row_header(i, "Great Pyramid of Giza", "REIGN OF ITS BUILDER  vs.  PROPOSED CONSTRUCTION ERA")
span(ya(i), bce(2589), bce(2566), BLUE)
label(ya(i), bce(2566) + yr_off(0.15), "Khufu’s reign, c. 2589–2566 BCE — the Great Pyramid was built for him",
      weight="semibold")
span(yp(i), ce(1301), ce(1600), ORANGE, hatch="///")
label(yp(i), ce(1301) - yr_off(0.15), "Proposed era of the large pyramids: 14th–16th c. CE", ha="right",
      weight="semibold")
label(yp(i), ce(1301) - yr_off(0.15),
      "Chron4 ch.20 also: pyramids “X–XI c. the earliest”, some “as late as the XVII c.”",
      ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, bce(2577), ce(1450),
             f"≈ +{fmt(gap(bce(2566), ce(1301)))} to +{fmt(gap(bce(2589), ce(1600)))} years",
             text_t=bce(1200))

# ------------------------------------------------------------ 3 Senenmut ceiling
i = 2
row_header(i, "Senenmut astronomical ceiling", "MAKING OF ARTWORK  vs.  DATE READ FROM ITS SKY")
span(ya(i), bce(1473), bce(1458), BLUE, hatch="///")
label(ya(i), bce(1458) + yr_off(0.17),
      "Tomb TT353, Deir el-Bahri — made in Hatshepsut’s reign, c. 1473–1458 BCE", weight="semibold")
diamond(yp(i), ce(1007), ORANGE)
label(yp(i), ce(1007) + yr_off(0.17), "1007 CE", weight="bold", col=ORANGE_D)
label(yp(i), ce(1007) - yr_off(0.17), "Their astronomical reading of the ceiling (14–16 June) — a date, not a reign",
      ha="right", fs=13)
displacement(i, bce(1465), ce(1007),
             f"+{fmt(gap(bce(1458), ce(1007)))} to +{fmt(gap(bce(1473), ce(1007)))} years", text_t=bce(250))

# ------------------------------------------------------------ 4 Seti I
i = 3
row_header(i, "Seti I", "REIGN  vs.  TWO ALTERNATIVE ZODIAC READINGS")
span(ya(i), bce(1294), bce(1279), BLUE)
label(ya(i), bce(1279) + yr_off(0.17),
      "Seti I reigned c. 1294–1279 BCE (19th Dynasty; tomb KV17 has the astronomical ceiling)",
      weight="semibold")
diamond(yp(i), ce(969), ORANGE)
diamond(yp(i), ce(1206), ORANGE)
label(yp(i), (ce(969) + ce(1206)) / 2, "or", ha="center", weight="bold", col=ORANGE_D, fs=15)
label(yp(i), ce(969) - yr_off(0.17), "969 CE (14–16 Aug)", ha="right", weight="bold", col=ORANGE_D)
label(yp(i), ce(1206) + yr_off(0.17), "1206 CE (5–7 Aug)", weight="bold", col=ORANGE_D)
label(yp(i), ce(969) - yr_off(0.17), "alternative solutions for the zodiac — not a reign",
      ha="right", fs=12, col=MUTED, dy=-0.2)
d1 = f"+{fmt(gap(bce(1279), ce(969)))}–{fmt(gap(bce(1294), ce(969)))}"
d2 = f"+{fmt(gap(bce(1279), ce(1206)))}–{fmt(gap(bce(1294), ce(1206)))} years"
displacement(i, bce(1286), ce(969), None)
displacement(i, bce(1286), ce(1206), f"{d1}  or  {d2}", text_t=bce(170))

# ------------------------------------------------------------ 5 Round Dendera zodiac
i = 4
row_header(i, "Round zodiac of Dendera", "DATE OF CARVED SKY  vs.  DATE READ FROM IT")
diamond(ya(i), bce(50), BLUE)
label(ya(i), bce(50) + yr_off(0.17),
      "50 BCE — sky configuration of mid-50 BCE; carved c. 50 BCE (Louvre, D 38)", weight="semibold")
diamond(yp(i), ce(1185), ORANGE)
label(yp(i), ce(1185) + yr_off(0.17), "1185 CE", weight="bold", col=ORANGE_D)
label(yp(i), ce(1185) - yr_off(0.17), "Their reading: morning of 20 March 1185 CE", ha="right", fs=13)
displacement(i, bce(50), ce(1185), f"+{fmt(gap(bce(50), ce(1185)))} years", text_t=ce(560))

# ------------------------------------------------------------ 6 Classical Greece
i = 5
row_header(i, "Classical Greece", "BROAD EPOCH  vs.  BROAD EPOCH")
epoch(ya(i), bce(480), bce(323), BLUE, BLUE_T)
label(ya(i), bce(480) - yr_off(0.15), "Classical period, c. 480–323 BCE", ha="right", weight="semibold")
epoch(yp(i), ce(1001), ce(1600), ORANGE, ORANGE_T)
label(yp(i), ce(1001) - yr_off(0.15), "Broad placement: medieval Greece of the 11th–16th c. CE (Chron2 ch.3)",
      ha="right", weight="semibold")
label(yp(i), ce(1001) - yr_off(0.15),
      "Their tightest Greek parallel: 510–300 BCE ↔ 1250–1460 CE, ≈1,810 yrs (Chron1 ch.6, Ex. 16)",
      ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, bce(400), ce(1300), "no single fixed offset", text_t=ce(560))

# ------------------------------------------------------------ 7 Parthenon
i = 6
row_header(i, "Parthenon, Athens", "CONSTRUCTION  vs.  PROPOSED CONSTRUCTION")
span(ya(i), bce(447), bce(432), BLUE, hatch="///")
label(ya(i), bce(447) - yr_off(0.15), "Built 447–432 BCE", ha="right", weight="semibold")
span(yp(i), ce(1351), ce(1400), ORANGE, hatch="///")
ax.plot([ce(1363), ce(1363)], [yp(i) - 0.17, yp(i) + 0.17], color=ORANGE_D, lw=2.4, zorder=6)
label(yp(i), ce(1351) - yr_off(0.15), "Proposed: second half of the 14th c. CE (under Nerio Acciaioli)",
      ha="right", weight="semibold")
label(yp(i), ce(1351) - yr_off(0.15),
      "Chron2 ch.3 §15: “447 b.c. … shift of 1810 years … 1363 a.d.” (as printed; no-year-0 count gives 1364)",
      ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, bce(440), ce(1375), f"≈ +1,800 years (their ≈1,810-year shift)", text_t=ce(560))

# ------------------------------------------------------------ 8 Peloponnesian War
i = 7
row_header(i, "Peloponnesian War", "WAR  vs.  CLAIMED MEDIEVAL ORIGINAL")
span(ya(i), bce(431), bce(404), BLUE)
label(ya(i), bce(431) - yr_off(0.15), "431–404 BCE (27 years)", ha="right", weight="semibold")
span(yp(i), ce(1374), ce(1387), ORANGE)
label(yp(i), ce(1374) - yr_off(0.15), "Claimed original: war in Greece of 1374–1387 CE (13 years)", ha="right",
      weight="semibold")
label(yp(i), ce(1374) - yr_off(0.15), "Chron2 ch.3 §14", ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, bce(418), ce(1380),
             f"+{fmt(gap(bce(431), ce(1374)))} (start) / +{fmt(gap(bce(404), ce(1387)))} (end) years",
             text_t=ce(560))

# ------------------------------------------------------------ 9 Roman sequence
i = 8
row_header(i, "Rome: Sulla → Caracalla", "DYNASTIC SEQUENCE  vs.  CLAIMED PROTOTYPE")
span(ya(i), bce(82), ce(217), BLUE)
label(ya(i), ce(217) + yr_off(0.15),
      "82 BCE – 217 CE: Sulla’s dictatorship to Caracalla’s death (F&N’s “Second Roman Empire”)",
      weight="semibold")
span(yp(i), ce(962), ce(1254), ORANGE)
ax.plot([ce(965), ce(965)], [yp(i) - 0.17, yp(i) + 0.17], color=ORANGE_D, lw=2.2, zorder=6)
ax.plot([ce(962), ce(962)], [yp(i) - 0.17, yp(i) + 0.17], color=ORANGE_D, lw=2.2, zorder=6)
label(yp(i), ce(962) - yr_off(0.15), "Claimed prototype: Holy Roman Empire, 962 or 965 → 1254 CE", ha="right",
      weight="semibold")
label(yp(i), ce(962) - yr_off(0.15), "≈1,053-year shift · Chron1 ch.6, Ex. 8 (printed span there: 936–1273)",
      ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, ce(60), ce(1100),
             f"+{fmt(gap(bce(82), ce(962)))}/{fmt(gap(bce(82), ce(965)))} (start) · "
             f"+{fmt(gap(ce(217), ce(1254)))} (end) years", text_t=ce(580))

# ------------------------------------------------------------ 10 Crucifixion
i = 9
row_header(i, "Jesus: crucifixion", "SINGLE-YEAR EVENT  vs.  REVISED PROPOSAL")
for _t in (30, 33):
    ax.plot([ce(_t)], [ya(i)], marker="o", ms=12, mfc=BLUE, mec=INK, mew=1.3, zorder=7)
label(ya(i), ce(33) + yr_off(0.2), "Crucifixion: 30 CE  or  33 CE (the two conventional dates)",
      weight="semibold")
ax.plot([ce(1152), ce(1185)], [yp(i), yp(i)], color=ORANGE, lw=2.0, ls=(0, (2, 1.5)), zorder=5)
ax.plot([ce(1152)], [yp(i)], marker="o", ms=12, mfc="white", mec=ORANGE, mew=2.6, zorder=7)
ax.plot([ce(1185)], [yp(i)], marker="o", ms=12, mfc=ORANGE, mec=INK, mew=1.3, zorder=7)
label(yp(i), ce(1185) + yr_off(0.2), "crucifixion 1185 CE", weight="bold", col=ORANGE_D)
label(yp(i), ce(1152) - yr_off(0.2), "birth 1152 CE (open circle) ·", ha="right", weight="semibold")
label(yp(i), ce(1152) - yr_off(0.2),
      "Revised proposal (Nosovsky & Fomenko, 2004). Chron4 ch.20 still gives their earlier XI-c. version (Crucifixion 1095)",
      ha="right", fs=12, col=MUTED, dy=-0.2)
displacement(i, ce(31), ce(1185),
             f"+{fmt(gap(ce(33), ce(1185)))} to +{fmt(gap(ce(30), ce(1185)))} years", text_t=ce(560),
             shift_y=0.0)

# row separators
for k in range(rows_n + 1):
    ax.plot([X0, X1], [-k, -k], color="#D5D9DF", lw=1.0, zorder=1)
    fig.add_artist(Line2D([LM / FIG_W, PLOT_X / FIG_W],
                          [1 - (MAIN_TOP + (k + 0.28) * MAIN_H / (rows_n + 0.4)) / FIG_H] * 2,
                          color="#D5D9DF", lw=1.0))

# ================================================================ SECTION A: OFFSET FAMILIES
SEC_A = MAIN_TOP + MAIN_H + 1.25
ftext(LM, SEC_A, "How the proposed shifts work", fontsize=34, fontweight="bold", va="top")
ftext(LM, SEC_A + 0.62,
      "Three principal duplicate-offset families. Each one is an alternative distance measured from the SAME "
      "medieval original — they are not consecutive amounts to be added together.",
      fontsize=17, color=MUTED, va="top")

A_TOP = SEC_A + 1.35
A_H = 5.6
axA = ax_in(LM, A_TOP, 22.6, A_H)
axA.set_xlim(-2050, 260)
axA.set_ylim(0, 5.6)
axA.axis("off")

# ruler: years earlier than the original
ry = 0.55
axA.plot([-1950, 0], [ry, ry], color=INK, lw=1.3)
for v in range(0, 1951, 100):
    axA.plot([-v, -v], [ry, ry + (0.18 if v % 500 == 0 else 0.09)], color=INK, lw=1.0)
for v in (0, 500, 1000, 1500):
    axA.text(-v, ry - 0.12, "0" if v == 0 else f"−{v:,}", ha="center", va="top", fontsize=13,
             color=INK, fontweight="semibold")
axA.text(-1950, ry - 0.48, "years earlier than the medieval original  (an offset scale, not a calendar)",
         fontsize=13, color=MUTED, va="top", fontstyle="italic")

# common origin: one vertical line every arrow starts from
lane_top, lane_bot = 4.75, 1.05
axA.plot([0, 0], [ry, lane_top + 0.1], color=ORANGE_D, lw=3.0, zorder=6)
axA.text(25, lane_top + 0.32, "SAME ORIGIN", ha="left", va="center", fontsize=15, fontweight="bold",
         color=ORANGE_D)
axA.text(25, lane_top + 0.02, "the medieval\noriginal epoch", ha="left", va="top", fontsize=12.5,
         color=ORANGE_D, linespacing=1.3)

fams = [
    (333, 360, 4.1, "FAMILY I · ≈333 or 360 years",
     "“Roman–Byzantine” shift\nEx. 1 ≈333 · Ex. 5 ≈360 · Ex. 7 ≈360/362\nEx. 13–14 ≈340 / ≈330", "left"),
    (1053, 1053, 2.75, "FAMILY II · ≈1,053 years  (also “1000 or 1053”, ≈1,050)",
     "“Roman” shift · Ex. 8 ≈1,053 · Ex. 19 ≈1,050 · Sulla→Caracalla ↔ 962/965–1254", "right"),
    (1778, 1810, 1.4, "FAMILY III · ≈1,778 / 1,780 / 1,800 / 1,810 years",
     "“Graeco-Biblical” shift · Ex. 16 ≈1,810 · Parthenon · Peloponnesian War", "right"),
]
for lo, hi, yy, title, sub, side in fams:
    w = max(hi - lo, 14)
    axA.add_patch(Rectangle((-hi, yy - 0.17), w, 0.34, fc=ORANGE, ec=ORANGE_D, lw=1.2, zorder=4))
    for v in {lo, hi}:
        axA.plot([-v, -v], [ry, yy - 0.17], color=ORANGE, lw=1.0, ls=(0, (2, 3)), alpha=0.7)
    axA.add_patch(FancyArrowPatch((0, yy), (-lo + 2, yy), arrowstyle="-|>", mutation_scale=26,
                                  color=ORANGE_D, lw=2.4, zorder=5))
    if side == "left":
        tx = -hi - 30
        axA.text(tx, yy + 0.05, title, ha="right", va="bottom", fontsize=15.5, fontweight="bold",
                 color=ORANGE_D)
        axA.text(tx, yy - 0.05, sub, ha="right", va="top", fontsize=12.5, color=INK, linespacing=1.3)
    else:
        tx = -lo + 40
        axA.text(tx, yy + 0.1, title, ha="left", va="bottom", fontsize=15.5, fontweight="bold",
                 color=ORANGE_D)
        axA.text(tx, yy - 0.1, sub, ha="left", va="top", fontsize=12.5, color=INK)
# FAMILY I title would collide with arrows -> it is placed right-aligned left of its bar, fine.

# right-hand explanation box
axB = ax_in(LM + 23.2, A_TOP, FIG_W - LM - 23.2 - 0.9, A_H)
axB.set_xlim(0, 1)
axB.set_ylim(0, 1)
axB.axis("off")
axB.add_patch(FancyBboxPatch((0.0, 0.0), 1.0, 1.0, boxstyle="round,pad=0,rounding_size=0.03",
                             fc="#F7F8FA", ec="#D5D9DF", lw=1.2, transform=axB.transAxes))
bx = 0.05
axB.text(bx, 0.93, "Read the shifts as alternatives", fontsize=18, fontweight="bold", va="top")
axB.text(bx, 0.83,
         "Chron1 ch.6 §7: chronicles S2, S3, S4 are copies of S1 shifted\n"
         "“by 333, 1053, and 1778 years accordingly … All the three\n"
         "shifts are counted off the same point.”",
         fontsize=13.5, va="top", color=INK, linespacing=1.45)
axB.text(bx, 0.555, "✓", fontsize=22, color="#1E7B45", fontweight="bold", va="top")
axB.text(bx + 0.06, 0.55,
         "copy = original − 333/360   or   original − 1,053\n"
         "or   original − 1,778…1,810",
         fontsize=14, va="top", color=INK, fontweight="semibold", linespacing=1.4)
axB.text(bx, 0.36, "✗", fontsize=22, color="#C0182B", fontweight="bold", va="top")
axB.text(bx + 0.06, 0.355,
         "333 + 1,053 + 1,778 = 3,164 — not a shift they propose.\n"
         "There is also no universal 600-year correction.",
         fontsize=14, va="top", color=INK, linespacing=1.4)
axB.text(bx, 0.17,
         "Gaps between two copies (rather than from the origin) can equal\n"
         "differences or sums: Fig. 6.20 labels Ex. 6 “720 = 1053 – 333”;\n"
         "Table 2 calls Ex. 2’s ≈1,300 “the sum of two basic shifts”.",
         fontsize=12.5, va="top", color=MUTED, linespacing=1.4)

# ================================================================ SECTION B: 20 EXAMPLES
SEC_B = A_TOP + A_H + 0.85
ftext(LM, SEC_B, "The 20 duplicate-dynasty examples of Chron1, chapter 6", fontsize=34, fontweight="bold",
      va="top")
ftext(LM, SEC_B + 0.62,
      "Shifts are reproduced exactly as printed (text, tables, figure captions and figure annotations). "
      "Disagreements between printed values, and examples with no fixed offset, are kept as they are. "
      "All bar dates below are the conventional dates the authors cite for each dynasty.",
      fontsize=15.5, color=MUTED, va="top")

T_TOP = SEC_B + 1.35
ROW = 0.62
cols = dict(num=LM, figs=LM + 0.65, a=LM + 2.35, b=LM + 8.55, mini=LM + 14.75, shift=LM + 22.35,
            note=LM + 26.55)
MINI_W = 7.2
END_X = FIG_W - 0.9

hdr_y = T_TOP
for k, s in (("num", "#"), ("figs", "FIGURES"), ("a", "DYNASTY / EPOCH  a  (as printed)"),
             ("b", "DYNASTY / EPOCH  b  (as printed)"),
             ("mini", "CONVENTIONAL DATES  (1300 BCE → 1700 CE)"), ("shift", "SHIFT AS PRINTED"),
             ("note", "NOTES · inconsistencies / missing offsets")):
    ftext(cols[k], hdr_y, s, fontsize=12, fontweight="bold", color=MUTED, va="top")
fig.add_artist(Line2D([LM / FIG_W, END_X / FIG_W], [1 - (hdr_y + 0.32) / FIG_H] * 2, color=INK, lw=1.4))

ex = [
    ("1", "6.11–6.12a", "Second Roman Empire (Sulla → Caracalla), 82 BC–217 AD",
     "Third Roman Empire (Aurelian → Theodoric), 270–526 AD",
     [(bce(82), ce(217), "a"), (ce(270), ce(526), "b")], "≈333 (text, Table 1)\n≈330–360 (Fig. 6.12 caption)",
     "Text and caption give different values."),
    ("2", "6.13–6.14", "Kings of Israel (Bible), 922–724 BC", "Third Roman Empire jet, 300–476 AD",
     [(bce(922), bce(724), "a"), (ce(300), ce(476), "b")], "≈1,300 (Table 2)",
     "Not a basic value: Table 2 calls it the sum of ≈1000 and ≈300."),
    ("3", "6.13, 6.15", "Kings of Judah (Bible), 928–587 BC", "Eastern Roman Empire jet, 300–552 AD",
     [(bce(928), bce(587), "a"), (ce(300), ce(552), "b")], "— none printed",
     "No fixed offset in text, table or captions."),
    ("4", "6.16", "Popes of Rome, 140–314 AD", "Popes of Rome, 324–532 AD",
     [(ce(140), ce(314), "a"), (ce(324), ce(532), "b")], "— none printed",
     "No offset given; text says it conforms to Ex. 1."),
    ("5", "6.17–6.18", "Carolingian Empire, 681–887 AD (captions: 681–888)",
     "Eastern Roman Empire jet, 324–527 AD",
     [(ce(681), ce(887), "a"), (ce(324), ce(527), "b")], "≈360 (Fig. 6.18)\nmean reign shift 359.6 (fig.)",
     "End year printed as 887 (text) and 888 (captions)."),
    ("6", "6.19–6.20", "Holy Roman Empire, 983–1266 AD", "Roman Empire jet, 270–553 AD",
     [(ce(983), ce(1266), "a"), (ce(270), ce(553), "b")], "≈720 (text, Fig. 6.20)\nmean 723 (fig.)",
     "Fig. 6.20: “720 = 1053 – 333” — a gap between two copies."),
    ("7", "6.21–6.22", "Holy Roman Empire, 911–1254 AD", "Habsburg empire, 1273–1637 AD",
     [(ce(911), ce(1254), "a"), (ce(1273), ce(1637), "b")],
     "≈362 (text) · ≈360 (captions)\nmean reign-end 373 (fig.)", "Three different printed values for one pair."),
    ("8", "6.23–6.24", "Holy Roman Empire, 936–1273 AD", "Second Roman Empire, 82 BC–217 AD",
     [(ce(936), ce(1273), "a"), (bce(82), ce(217), "b")], "≈1,053 (Fig. 6.24)\nmean reign-end 1,039 (fig.)",
     "Per-ruler differences in Fig. 6.24 run 1,015–1,057."),
    ("9", "6.25–6.26", "Kings of Judah (Bible), 928–587 BC", "Holy Roman Empire (German reigns), 911–1307 AD",
     [(bce(928), bce(587), "a"), (ce(911), ce(1307), "b")], "≈1,830 (Fig. 6.26)\n1,839 (Fig. 6.31)",
     "“911 AD = 928 BC” is 1,838 yrs counted without a year 0."),
    ("10", "6.27–6.28", "Kings of Israel (Bible), 922–724 BC", "Roman coronations of German emperors, 920–1170 AD",
     [(bce(922), bce(724), "a"), (ce(920), ce(1170), "b")], "≈1,840 (Fig. 6.28)\n“920 + 922 = 1842” (fig.)",
     "Figure counts from a table “year zero” of 920 BC."),
    ("11", "6.29–6.30", "Russian czar-khans, 1276–1600 AD", "Habsburg empire, 1273–1600 AD",
     [(ce(1276), ce(1600), "a"), (ce(1273), ce(1600), "b")], "0 — “no chronological shift”",
     "Same-period identification (details in Chron7)."),
    ("12", "6.31", "Armenian Catholicoses (Fig. 6.31: from 970 AD)",
     "Holy Roman Empire X–XIII c. (from 911) + kings of Judah",
     [(ce(970), ce(970), "pa"), (ce(911), ce(911), "pb"), (bce(928), bce(928), "pb")],
     "60 and 1,839 (Fig. 6.31 only)", "“970 AD = 911 AD … 60 year shift” (arithmetic: 59)."),
    ("13", "6.32", "First Byzantine Empire, 527–829 AD", "Second Byzantine Empire, 829–1204 AD",
     [(ce(527), ce(829), "a"), (ce(829), ce(1204), "b")], "≈340 (Figs 6.32, 6.34–6.36)", ""),
    ("14", "6.33–6.36", "Second Byzantine Empire, 867–1143 AD", "Third Byzantine Empire, 1204–1453 AD",
     [(ce(867), ce(1143), "a"), (ce(1204), ce(1453), "b")], "≈330 (Figs 6.33–6.36)",
     "Byzantium II is 829–1204 in Ex. 13 but 867–1143 here."),
    ("15", "6.37–6.39", "Russian history, 945–1174 AD", "Russian history, 1363–1598 AD",
     [(ce(945), ce(1174), "a"), (ce(1363), ce(1598), "b")], "410 (Figs 6.37–6.39)", ""),
    ("16", "6.40–6.41", "“Ancient” Greece, 510–300 BC", "Medieval Greece, 1250–1460 AD",
     [(bce(510), bce(300), "a"), (ce(1250), ce(1460), "b")], "≈1,810 (Figs 6.40–6.41)", ""),
    ("17", "6.42–6.48", "England, 640–1330 AD", "Byzantium, 380–1453 AD",
     [(ce(640), ce(1330), "a"), (ce(380), ce(1453), "b")],
     "text: 210–270 fwd, 100–120 back\nFigs 6.47 / 6.48: ≈275 / ≈120",
     "Fig. 6.47’s ≈275 lies outside the text’s 210–270."),
    ("18", "6.49–6.50", "Greek kings 1182–1070 BC; Lacedaemon 491–330 BC",
     "Byzantium 1341–1453 AD; despots of Mistras 1348–1460",
     [(bce(1182), bce(1070), "a"), (bce(491), bce(330), "a"), (ce(1341), ce(1453), "b"),
      (ce(1348), ce(1460), "b")], "— none printed",
     "Reign matches only (equal 112-yr spans). Fig. 6.50 prints one reign as “330-397” BC."),
    ("19", "6.51–6.52", "Regal Rome of Livy (7 kings)", "Third Roman Empire jet, 300–552 AD",
     [(bce(753), bce(509), "c"), (ce(300), ce(552), "b")], "≈1,050 (Fig. 6.52)",
     "c = 10⁻⁴. Ch. 6 prints no BC dates; dashed bar = conventional 753–509 BC."),
    ("20", "6.52a", "Regal Rome of Livy", "Holy Roman Empire + Byzantium (both X–XIII c.)",
     [(bce(753), bce(509), "c"), (ce(901), ce(1300), "b")], "— none printed",
     "Figure aligns Livy’s years-from-Rome’s-founding with years AD."),
]

MX0, MX1 = bce(1300), ce(1700)


def mini_x(t):
    return cols["mini"] + (t - MX0) / (MX1 - MX0) * MINI_W


for r, (num, figs, a_txt, b_txt, bars, shift, note) in enumerate(ex):
    y = T_TOP + 0.5 + r * ROW
    if r % 2 == 0:
        fig.add_artist(Rectangle((LM / FIG_W, 1 - (y + ROW - 0.08) / FIG_H), (END_X - LM) / FIG_W, ROW / FIG_H,
                                 transform=fig.transFigure, color=BAND, lw=0, zorder=-5))
    yc = y + ROW / 2 - 0.08
    ftext(cols["num"], yc, num, fontsize=17, fontweight="bold", va="center", color=ORANGE_D)
    ftext(cols["figs"], yc, figs, fontsize=12, va="center", color=MUTED)
    ftext(cols["a"], yc, "a ", fontsize=12.5, va="center", fontweight="bold", color=BLUE_D)
    ftext(cols["a"] + 0.25, yc, a_txt, fontsize=12.5, va="center", wrap=False)
    ftext(cols["b"], yc, "b ", fontsize=12.5, va="center", fontweight="bold", color=BLUE)
    ftext(cols["b"] + 0.25, yc, b_txt, fontsize=12.5, va="center")
    ftext(cols["shift"], yc, shift, fontsize=12.5, va="center", fontweight="semibold",
          color=ORANGE_D if not shift.startswith("—") else MUTED, linespacing=1.25)
    ftext(cols["note"], yc, note, fontsize=12, va="center", color=MUTED, linespacing=1.25)

    # mini timeline
    mt = ax_in(cols["mini"], y + 0.02, MINI_W, ROW - 0.12)
    mt.set_xlim(MX0, MX1)
    mt.set_ylim(0, 1)
    mt.axis("off")
    mt.axvline(ERA, color=INK, lw=0.8, ls=(0, (2, 2)))
    for t in (bce(1000), bce(500), ce(500), ce(1000), ce(1500)):
        mt.axvline(t, color=GRID, lw=0.8, zorder=0)
    a_starts, b_starts = [], []
    for t0, t1, kind in bars:
        if kind in ("a", "b", "c"):
            yy = 0.68 if kind in ("a", "c") else 0.3
            col = BLUE_D if kind in ("a", "c") else BLUE
            if kind == "c":
                mt.add_patch(Rectangle((t0, yy - 0.14), t1 - t0, 0.28, fc="white", ec=BLUE_D, lw=1.3,
                                       ls=(0, (3, 2))))
            else:
                mt.add_patch(Rectangle((t0, yy - 0.14), max(t1 - t0, 8), 0.28, fc=col, lw=0))
            (a_starts if kind in ("a", "c") else b_starts).append(t0)
        else:  # point markers for Ex. 12
            yy = 0.68 if kind == "pa" else 0.3
            mt.plot([t0], [yy], marker="|", ms=14, mew=3, color=BLUE_D if kind == "pa" else BLUE)
            (a_starts if kind == "pa" else b_starts).append(t0)
    # orange identification connectors (start ↔ start), no implied direction
    for sa in a_starts:
        for sb in b_starts:
            if abs(sa - sb) < 1 and False:
                continue
            mt.plot([sa, sb], [0.54, 0.44], color=ORANGE, lw=1.6, alpha=0.9)

# mini-axis labels under the table
yl = T_TOP + 0.5 + len(ex) * ROW + 0.05
for t, s in ((bce(1000), "1000 BCE"), (bce(500), "500 BCE"), (ERA, "1 BCE|1 CE"), (ce(500), "500"),
             (ce(1000), "1000"), (ce(1500), "1500 CE")):
    ftext(mini_x(t), yl, s, fontsize=10.5, ha="center", va="top", color=MUTED)
ftext(cols["mini"], yl + 0.32,
      "dark blue = a · mid blue = b · dashed = date not printed in ch.6 · orange line = the authors’ claimed identification",
      fontsize=10.5, va="top", color=MUTED)

# ================================================================ FOOTER
FOOT = yl + 0.95
fig.add_artist(Line2D([LM / FIG_W, END_X / FIG_W], [1 - FOOT / FIG_H] * 2, color=INK, lw=1.2))
ftext(LM, FOOT + 0.22, "SOURCES", fontsize=13, fontweight="bold", va="top")
src_left = (
    "Proposed (primary) — A. T. Fomenko & G. V. Nosovsky, History: Fiction or Science? (chronologia.org/en):\n"
    "• Chron1 ch.6, pp. 256–289 and 290–325 — 20 duplicate-dynasty examples, Tables 1–11, Figs 6.11–6.57, "
    "§7 (“shifts … counted off the same point”)\n"
    "   chronologia.org/en/chronologia1/1N06-EN-256-289.pdf · …/1N06-EN-290-325.pdf\n"
    "• Chron3 ch.19 — zodiac datings: Round Dendera 20 Mar 1185; Seti I 969 or 1206; Senenmut 1007; "
    "Egypt in the XI–XVI c.   chronologia.org/en/chronologia3/3N19-EN.pdf\n"
    "• Chron4 ch.20 — Egypt after 900 AD; large pyramids XIV–XVI c.; earlier Crucifixion version (1095)   "
    "chronologia.org/en/chronologia4/4N20-EN.pdf\n"
    "• Chron2 ch.3 §§14–15 — war of 1374–1387 as the Peloponnesian War; Parthenon, “447 b.c. + 1810 → 1363 a.d.”; "
    "shift families 333/360, 1000/1053, 1778/1780/1800/1810\n"
    "   chronologia.org/en/chronologia2/2N031a-EN.pdf · …/2n031-EN.pdf\n"
    "• Birth 1152 / Crucifixion 1185: G. V. Nosovsky & A. T. Fomenko, Царь Славян (Tsar of the Slavs), 2004 — "
    "the authors’ revised dating, reported on chronologia.org."
)
src_right = (
    "Accepted dates — museum, university and antiquities-authority references:\n"
    "• The Met, Heilbrunn Timeline of Art History: Egyptian chronology (Early Dynastic c. 3100 BC → Ptolemaic end 30 BC); "
    "“The Art of Classical Greece (ca. 480–323 B.C.)”\n"
    "• The Met, “Astronomical Ceiling”, tomb of Senenmut (TT353), acc. 544566 — reign of Hatshepsut   metmuseum.org/art/collection/search/544566\n"
    "• Harvard University, Giza Project (giza.fas.harvard.edu) — Khufu, 4th Dynasty, builder of the Great Pyramid; reign c. 2589–2566 BC\n"
    "• Egyptian Ministry of Tourism & Antiquities, “Tomb of Sety I (KV17)”   egymonuments.gov.eg — Seti I c. 1294–1279 BC\n"
    "• Musée du Louvre, Zodiac of Dendera, inv. D 38 (c. 50 BC); S. Cauville & É. Aubourg (IFAO): sky of 15 June–15 Aug 50 BC\n"
    "• Parthenon 447–432 BC (Iktinos & Kallikrates): Acropolis Museum / Hellenic Ministry of Culture; Columbia Univ. Art Humanities\n"
    "• Peloponnesian War 431–404 BC; Sulla dictator 82 BC; Caracalla d. 217 AD — Encyclopaedia Britannica; P. Cartledge (Cambridge)\n"
    "• Crucifixion 30 or 33 CE (Passover Fridays under Pilate, 26–36 CE): standard scholarly range, e.g. B. Ehrman (UNC)"
)
ftext(LM, FOOT + 0.6, src_left, fontsize=11.2, va="top", color=INK, linespacing=1.5)
ftext(LM + 17.6, FOOT + 0.6, src_right, fontsize=11.2, va="top", color=INK, linespacing=1.5)
ftext(LM, FOOT + 3.85,
      "This chart presents the New Chronology as the authors’ proposal, quoting their own figures. It is not a complete "
      "redated succession of every pharaoh, and it applies no universal correction (there is no single 600-year offset).\n"
      "Mainstream historians, Egyptologists and astronomers reject the New Chronology. Calendar years shown without year 0; "
      "displacements are counted accordingly (e.g. 50 BCE → 1185 CE = 1,234 years). Compiled October 2026.",
      fontsize=11.5, va="top", color=MUTED, wrap=True)

out = HERE / "fomenko_new_chronology_timeline"
fig.savefig(f"{out}.png", dpi=int(__import__("os").environ.get("DPI", "200")), facecolor=PAPER)
fig.savefig(f"{out}.pdf", facecolor=PAPER)
print("wrote", out)
