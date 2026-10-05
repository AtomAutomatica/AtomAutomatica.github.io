"""
Shareable PDF report + phone infographic, written in Riven's voice.

Writes share/report.html and share/infographic.html; render_share.js turns them
into share/two_calendars_report.pdf and share/two_calendars_infographic.png.
Calendar arithmetic has no year 0 (BCE year Y -> 1 - Y).
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "share"
OUT.mkdir(exist_ok=True)
FONTS = (HERE / "fonts").as_uri()


def bce(y):
    return 1 - y


def gap(a, b):
    return abs(b - a)


def n(x):
    return f"{x:,}"


FONT_CSS = f"""
@font-face{{font-family:Inter;src:url({FONTS}/Inter-Regular.ttf);font-weight:400}}
@font-face{{font-family:Inter;src:url({FONTS}/Inter-Italic.ttf);font-weight:400;font-style:italic}}
@font-face{{font-family:Inter;src:url({FONTS}/Inter-Medium.ttf);font-weight:500}}
@font-face{{font-family:Inter;src:url({FONTS}/Inter-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:Inter;src:url({FONTS}/Inter-Bold.ttf);font-weight:700}}
@font-face{{font-family:Mono;src:url({FONTS}/JetBrainsMono-Regular.ttf);font-weight:400}}
@font-face{{font-family:Mono;src:url({FONTS}/JetBrainsMono-Italic.ttf);font-weight:400;font-style:italic}}
@font-face{{font-family:Mono;src:url({FONTS}/JetBrainsMono-Medium.ttf);font-weight:500}}
@font-face{{font-family:Mono;src:url({FONTS}/JetBrainsMono-Bold.ttf);font-weight:700}}
"""

# ------------------------------------------------------------------ data
# (subject, kind, accepted marks, accepted text, proposed marks, proposed text, move text, move_mid)
# marks: list of (t0, t1, style) with style in epoch|span|build|art|event
S = [
    ("Pharaonic Egypt", "era vs era",
     [(bce(3100), bce(30), "epoch")], "c. 3100–30 BCE",
     [(1001, 1600, "epoch")], "11th–16th c. CE", "no single offset", None),
    ("Great Pyramid", "builder’s reign vs build era",
     [(bce(2589), bce(2566), "span")], "Khufu, c. 2589–2566 BCE",
     [(1301, 1600, "build")], "14th–16th c. CE",
     f"+{n(gap(bce(2566), 1301))} to +{n(gap(bce(2589), 1600))}", 4027),
    ("Senenmut ceiling", "artwork vs sky reading",
     [(bce(1473), bce(1458), "build")], "c. 1473–1458 BCE",
     [(1007, 1007, "art")], "1007 CE",
     f"+{n(gap(bce(1458), 1007))} to +{n(gap(bce(1473), 1007))}", 2472),
    ("Seti I", "reign vs two zodiac readings",
     [(bce(1294), bce(1279), "span")], "c. 1294–1279 BCE",
     [(969, 969, "art"), (1206, 1206, "art")], "969 or 1206 CE",
     f"+{n(gap(bce(1279), 969))}…+{n(gap(bce(1294), 1206))}", 2373),
    ("Round Dendera zodiac", "carved sky vs reading",
     [(bce(50), bce(50), "art")], "50 BCE",
     [(1185, 1185, "art")], "20 Mar 1185 CE",
     f"+{n(gap(bce(50), 1185))}", 1234),
    ("Classical Greece", "era vs era",
     [(bce(480), bce(323), "epoch")], "c. 480–323 BCE",
     [(1001, 1600, "epoch")], "11th–16th c. CE", "no single offset", None),
    ("Parthenon", "build vs build",
     [(bce(447), bce(432), "build")], "447–432 BCE",
     [(1351, 1400, "build")], "late 14th c. CE", "≈ +1,800", 1800),
    ("Peloponnesian War", "war vs war",
     [(bce(431), bce(404), "span")], "431–404 BCE",
     [(1374, 1387, "span")], "1374–1387 CE",
     f"+{n(gap(bce(404), 1387))} to +{n(gap(bce(431), 1374))}", 1797),
    ("Rome: Sulla → Caracalla", "dynasty vs prototype",
     [(bce(82), 217, "span")], "82 BCE – 217 CE",
     [(962, 1254, "span")], "962/965–1254 CE",
     f"+{n(gap(217, 1254))} to +{n(gap(bce(82), 965))}", 1041),
    ("Crucifixion", "event vs revised proposal",
     [(30, 30, "event"), (33, 33, "event")], "30 or 33 CE",
     [(1152, 1152, "eventopen"), (1185, 1185, "event")], "1185 CE (birth 1152)",
     f"+{n(gap(33, 1185))} to +{n(gap(30, 1185))}", 1153),
]
mids = sorted(m for *_, m in S if m)
median = (mids[len(mids) // 2 - 1] + mids[len(mids) // 2]) / 2   # 8 values

EX = [
    ("1", "Second Roman Empire 82 BC–217 AD", "Third Roman Empire 270–526", "≈333 · caption ≈330–360", "split"),
    ("2", "Israel kings 922–724 BC", "Third Roman Empire 300–476", "≈1,300 (“sum of ≈1000 and 300”)", "ok"),
    ("3", "Judah kings 928–587 BC", "Eastern Roman Empire 300–552", "none printed", "none"),
    ("4", "Popes 140–314", "Popes 324–532", "none printed", "none"),
    ("5", "Carolingians 681–887 (captions: 888)", "Eastern Roman Empire 324–527", "≈360 · mean 359.6", "split"),
    ("6", "Holy Roman Empire 983–1266", "Roman Empire 270–553", "≈720 = 1053 − 333 · mean 723", "ok"),
    ("7", "Holy Roman Empire 911–1254", "Habsburgs 1273–1637", "≈362 · ≈360 · mean 373", "split"),
    ("8", "Holy Roman Empire 936–1273", "Second Roman Empire 82 BC–217 AD", "≈1,053 · mean 1,039", "ok"),
    ("9", "Judah kings 928–587 BC", "Holy Roman Empire 911–1307", "≈1,830 · 1,839 (math: 1,838)", "split"),
    ("10", "Israel kings 922–724 BC", "Roman coronations 920–1170", "≈1,840 · “920 + 922 = 1842”", "split"),
    ("11", "Russian czar-khans 1276–1600", "Habsburgs 1273–1600", "0 — “no shift”", "ok"),
    ("12", "Armenian Catholicoses (from 970)", "Holy Roman Empire + Judah", "60 (math: 59) · 1,839", "split"),
    ("13", "Byzantium I 527–829", "Byzantium II 829–1204", "≈340", "ok"),
    ("14", "Byzantium II 867–1143", "Byzantium III 1204–1453", "≈330 (Byz II range ≠ Ex. 13)", "split"),
    ("15", "Russia 945–1174", "Russia 1363–1598", "410", "ok"),
    ("16", "“Ancient” Greece 510–300 BC", "Medieval Greece 1250–1460", "≈1,810", "ok"),
    ("17", "England 640–1330", "Byzantium 380–1453", "text 210–270 · fig. ≈275 / ≈120", "split"),
    ("18", "Greek kings · Lacedaemon", "Byzantium · Mistras", "none printed (fig. typo “330-397”)", "none"),
    ("19", "Regal Rome of Livy", "Third Roman Empire 300–552", "≈1,050", "ok"),
    ("20", "Regal Rome of Livy", "Holy Roman Empire + Byzantium", "none printed", "none"),
]
n_none = sum(1 for e in EX if e[4] == "none")
n_split = sum(1 for e in EX if e[4] == "split")

# ------------------------------------------------------------------ svg helpers
def strip_svg(marks_a, marks_p, w, h, c_acc, c_prop, ink, rule, bg, tick_col, ticks=True, fs=10):
    """One subject on the full 3100 BCE → 2026 CE axis."""
    X0, X1 = bce(3150), 2080
    sx = lambda t: 4 + (t - X0) / (X1 - X0) * (w - 8)
    ya, yp = h * 0.32, h * 0.72
    out = [f'<svg viewBox="0 0 {w} {h}" width="100%" style="display:block">']
    for t in (bce(3000), bce(2000), bce(1000), 1000, 2000):
        out.append(f'<line x1="{sx(t):.1f}" x2="{sx(t):.1f}" y1="2" y2="{h-2}" stroke="{rule}" stroke-width="1"/>')
    out.append(f'<line x1="{sx(0.5):.1f}" x2="{sx(0.5):.1f}" y1="2" y2="{h-2}" stroke="{tick_col}" '
               f'stroke-width="1" stroke-dasharray="2 2"/>')
    out.append(f'<line x1="{sx(2026):.1f}" x2="{sx(2026):.1f}" y1="0" y2="{h}" stroke="#e5343b" stroke-width="2"/>')

    def draw(marks, y, c):
        for t0, t1, st in marks:
            x0, x1 = sx(t0), sx(t1)
            if st == "epoch":
                out.append(f'<rect x="{x0:.1f}" y="{y-6:.1f}" width="{x1-x0:.1f}" height="12" fill="{c}" '
                           f'fill-opacity=".22" stroke="{c}" stroke-dasharray="4 2"/>')
            elif st in ("span", "build"):
                ww = max(x1 - x0, 4)
                if st == "build":
                    out.append(f'<rect x="{x0:.1f}" y="{y-5:.1f}" width="{ww:.1f}" height="10" fill="url(#h{c[1:]})" '
                               f'stroke="{c}" stroke-width="1.2"/>')
                else:
                    out.append(f'<rect x="{x0:.1f}" y="{y-5:.1f}" width="{ww:.1f}" height="10" fill="{c}"/>')
            elif st == "art":
                out.append(f'<rect x="{x0-5:.1f}" y="{y-5:.1f}" width="10" height="10" fill="{c}" '
                           f'transform="rotate(45 {x0:.1f} {y:.1f})" stroke="{bg}" stroke-width="1"/>')
            elif st == "event":
                out.append(f'<circle cx="{x0:.1f}" cy="{y:.1f}" r="5" fill="{c}" stroke="{bg}" stroke-width="1"/>')
            elif st == "eventopen":
                out.append(f'<circle cx="{x0:.1f}" cy="{y:.1f}" r="4.3" fill="{bg}" stroke="{c}" stroke-width="2"/>')

    # connector
    a_mid = sum((m[0] + m[1]) / 2 for m in marks_a) / len(marks_a)
    p_mid = sum((m[0] + m[1]) / 2 for m in marks_p) / len(marks_p)
    out.append(f'<path d="M{sx(a_mid):.1f},{ya+6:.1f} C{sx(a_mid):.1f},{(ya+yp)/2:.1f} {sx(p_mid):.1f},{(ya+yp)/2:.1f} '
               f'{sx(p_mid):.1f},{yp-7:.1f}" fill="none" stroke="{tick_col}" stroke-width="1.2" stroke-dasharray="3 2"/>')
    draw(marks_a, ya, c_acc)
    draw(marks_p, yp, c_prop)
    out.append("</svg>")
    defs = (f'<svg width="0" height="0" style="position:absolute"><defs>'
            f'<pattern id="h{c_acc[1:]}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<rect width="5" height="5" fill="{c_acc}"/><line x1="0" y1="0" x2="0" y2="5" stroke="{bg}" stroke-width="2"/></pattern>'
            f'<pattern id="h{c_prop[1:]}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<rect width="5" height="5" fill="{c_prop}"/><line x1="0" y1="0" x2="0" y2="5" stroke="{bg}" stroke-width="2"/></pattern>'
            f'</defs></svg>')
    return defs + "".join(out)


def axis_svg(w, h, col, fs):
    X0, X1 = bce(3150), 2080
    sx = lambda t: 4 + (t - X0) / (X1 - X0) * (w - 8)
    lab = [(bce(3100), "3100 BCE"), (bce(2000), "2000 BCE"), (bce(1000), "1000 BCE"), (0.5, "1 BCE|1 CE"),
           (1000, "1000 CE"), (2026, "NOW")]
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" style="display:block">']
    for t, l in lab:
        anchor = "end" if l == "NOW" else ("start" if l == "3100 BCE" else "middle")
        c = "#e5343b" if l == "NOW" else col
        s.append(f'<text x="{sx(t):.1f}" y="{h-4}" fill="{c}" font-family="Mono" font-size="{fs}" '
                 f'text-anchor="{anchor}">{l}</text>')
    s.append("</svg>")
    return "".join(s)


def fan_svg(w, h, ink, dim, prop, rule, fs=12, bg="#fff"):
    """Three alternative offsets from one origin."""
    L, R = 40, w - 170
    sx = lambda v: R - v / 1950 * (R - L)
    rows = [(333, 360, "I", "333 / 360", "Roman–Byzantine"), (1053, 1053, "II", "1,053", "Roman"),
            (1778, 1810, "III", "1,778–1,810", "Graeco-Biblical")]
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" style="display:block">']
    top, step = 52, (h - 96) / 3
    s.append(f'<line x1="{R}" x2="{R}" y1="{top-14}" y2="{h-38}" stroke="{prop}" stroke-width="3"/>')
    s.append(f'<text x="{R+10}" y="{top-26}" fill="{prop}" font-family="Mono" font-size="{fs}" font-weight="700">SAME ORIGIN</text>')
    s.append(f'<text x="{R+10}" y="{top-10}" fill="{dim}" font-family="Mono" font-size="{fs-2}">medieval original</text>')
    for k, (lo, hi, num, val, name) in enumerate(rows):
        y = top + 18 + k * step
        x_lo, x_hi = sx(lo), sx(hi)
        s.append(f'<line x1="{R}" x2="{x_lo+8:.1f}" y1="{y:.1f}" y2="{y:.1f}" stroke="{prop}" stroke-width="2.4"/>')
        s.append(f'<path d="M{x_lo+1:.1f},{y:.1f} l10,-6 l0,12 z" fill="{prop}"/>')
        s.append(f'<rect x="{x_hi:.1f}" y="{y-8:.1f}" width="{max(x_lo-x_hi,6):.1f}" height="16" fill="{prop}"/>')
        tx, anc = (x_hi - 12, "end") if k == 0 else (x_lo + 22, "start")
        ty1, ty2 = (y - 2, y + 16) if k == 0 else (y - 9, y + 19)
        s.append(f'<text x="{tx:.1f}" y="{ty1:.1f}" fill="{ink}" font-family="Mono" font-size="{fs+1}" font-weight="700" '
                 f'text-anchor="{anc}">{num} · −{val} yrs</text>')
        s.append(f'<text x="{tx:.1f}" y="{ty2:.1f}" fill="{dim}" font-family="Mono" font-size="{fs-1}" '
                 f'text-anchor="{anc}">{name} shift</text>')
    yb = h - 30
    s.append(f'<line x1="{L}" x2="{R}" y1="{yb}" y2="{yb}" stroke="{dim}" stroke-width="1"/>')
    for v in (0, 500, 1000, 1500):
        s.append(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="{yb}" y2="{yb+5}" stroke="{dim}"/>')
        s.append(f'<text x="{sx(v):.1f}" y="{yb+18}" fill="{dim}" font-family="Mono" font-size="{fs-2}" '
                 f'text-anchor="middle">{"0" if v == 0 else "−" + n(v)}</text>')
    s.append("</svg>")
    return "".join(s)


# ================================================================== REPORT (PDF)
P = dict(bg="#ffffff", ink="#1c1b19", mute="#6b6862", rule="#d9d6cf", acc="#1f5fbf", prop="#c2560e",
         band="#f5f4f0", head="#faf9f6")

rows_html = []
for subj, kind, ma, ta, mp, tp, mv, _ in S:
    rows_html.append(f"""
<tr><td><b>{subj}</b><div class="k">{kind}</div></td>
<td class="a">{ta}</td><td class="p">{tp}</td><td class="mv">{mv}</td>
<td class="sv">{strip_svg(ma, mp, 300, 30, P['acc'], P['prop'], P['ink'], P['rule'], P['bg'], P['mute'])}</td></tr>""")

ex_html = []
for num, a, b, sh, flag in EX:
    tag = {"none": '<span class="tag none">NO OFFSET</span>', "split": '<span class="tag split">DISAGREES</span>',
           "ok": ""}[flag]
    ex_html.append(f"<tr><td class='num'>{num}</td><td>{a}</td><td>{b}</td><td class='sh'>{sh}</td><td>{tag}</td></tr>")

report = f"""<!doctype html><html><head><meta charset="utf-8"><title>Two Calendars — Riven read</title>
<style>
{FONT_CSS}
@page{{size:Letter;margin:0.55in 0.6in 0.6in}}
:root{{--bg:{P['bg']};--ink:{P['ink']};--mute:{P['mute']};--rule:{P['rule']};--acc:{P['acc']};--prop:{P['prop']};
--band:{P['band']};--head:{P['head']}}}
html{{background:var(--bg)}}
body{{margin:0;color:var(--ink);font:9.8pt/1.5 Inter,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.mono,h1,h2,.stamp,table.t th,.k,.num,.sh,.mv,.tag,.strip .l,.strip .v,.lede{{font-family:Mono,monospace}}
h1{{font-size:21pt;line-height:1.05;letter-spacing:.01em;text-transform:uppercase;margin:0 0 6px}}
h1 small{{display:block;font-size:8pt;letter-spacing:.18em;color:var(--mute);margin-top:8px;font-weight:400}}
.lede{{border-top:1px solid var(--rule);padding-top:8px;margin-top:10px;font-size:9pt;font-style:italic;color:var(--mute)}}
h2{{font-size:8.6pt;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin:22px 0 8px;
  border-bottom:1px solid var(--rule);padding-bottom:5px;font-weight:500;break-after:avoid}}
p{{margin:7px 0;max-width:6.9in}}
strong{{color:var(--prop);font-weight:600}}
.b{{color:var(--acc);font-weight:600}} .o{{color:var(--prop);font-weight:600}}
.strip{{display:grid;grid-template-columns:repeat(5,1fr);border:1px solid var(--rule);margin:14px 0 4px}}
.strip div{{padding:9px 10px;border-right:1px solid var(--rule)}} .strip div:last-child{{border-right:0}}
.strip .l{{font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}}
.strip .v{{font-size:15pt;font-weight:700;margin-top:3px;line-height:1}}
table.t{{width:100%;border-collapse:collapse;font-size:8.6pt;border:1px solid var(--rule);margin:8px 0}}
table.t th{{text-align:left;background:var(--head);color:var(--mute);font-weight:500;letter-spacing:.08em;
  text-transform:uppercase;font-size:6.6pt;padding:6px 7px;border-bottom:1px solid var(--rule)}}
table.t td{{padding:3px 7px;border-bottom:1px solid var(--rule);vertical-align:middle}}
table.t tbody tr:nth-child(even) td{{background:var(--band)}}
table.t tr{{break-inside:avoid}}
.k{{font-size:6.6pt;color:var(--mute);letter-spacing:.04em}}
td.a{{color:var(--acc);font-weight:600}} td.p{{color:var(--prop);font-weight:600}}
td.mv,td.sh{{font-size:8pt;white-space:nowrap}} td.sv{{width:2.1in}}
td.num{{font-weight:700;color:var(--prop);width:16px}}
.tag{{font-size:6.2pt;letter-spacing:.1em;padding:2px 5px;border:1px solid;white-space:nowrap}}
.tag.none{{color:var(--mute)}} .tag.split{{color:#b0302a}}
ol,ul{{padding-left:18px;margin:6px 0;max-width:6.9in}} li{{margin:4px 0}}
.leg{{font-family:Mono;font-size:7.4pt;color:var(--mute);display:flex;gap:16px;flex-wrap:wrap;margin:6px 0 2px}}
.leg i{{display:inline-block;width:12px;height:8px;margin-right:5px;vertical-align:middle}}
.fan{{border:1px solid var(--rule);background:var(--head);padding:10px 12px;margin:8px 0}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.stamp{{color:var(--mute);font-size:7.6pt;letter-spacing:.08em;text-transform:uppercase;margin-top:18px;
  border-top:1px solid var(--rule);padding-top:8px}}
.pb{{break-before:page}}
.src{{font-size:7.6pt;color:var(--mute);line-height:1.5}} .src b{{color:var(--ink);font-weight:600}}
img.poster{{width:100%;border:1px solid var(--rule);display:block;margin-top:8px}}
</style></head><body>

<h1>Two calendars, one past<small>Accepted chronology vs. the Fomenko–Nosovsky “New Chronology” · a Riven read</small></h1>
<p class="lede">Written 10/5/2026. Every number is from the authors’ own PDFs or a museum, university or antiquities page.
Where their printed numbers disagree with each other, both are shown. The page beats the summary.</p>

<div class="strip">
<div><div class="l">Subjects</div><div class="v">10</div></div>
<div><div class="l">Median move</div><div class="v">≈{n(int(round(median, -2)))}y</div></div>
<div><div class="l">Shift families</div><div class="v">3</div></div>
<div><div class="l">Ch.6 examples</div><div class="v">20</div></div>
<div><div class="l">No offset printed</div><div class="v">{n_none}/20</div></div>
</div>

<h2>1. The short version</h2>
<p>Fomenko and Nosovsky say most of “ancient” history is medieval history copied backward. I put ten of their cases on one axis, 3100 BCE to 2026 CE. <span class="b">Blue</span> is the accepted date. <span class="o">Orange</span> is theirs. Every gap is counted without a year 0.</p>
<p>Eight of the ten have a number. Their median move is <strong>about {n(int(round(median, -2)))} years later</strong>. The biggest is the Great Pyramid: Khufu’s reign, c. 2589–2566 BCE, moved into a 14th–16th-century build era. That is +3,866 to +4,188 years. The smallest is Rome, Sulla to Caracalla, moved onto the Holy Roman Empire: +1,037 to +1,046 years. Egypt and Classical Greece don’t get a number. They are placed as whole eras inside the 11th–16th centuries.</p>

<table class="t"><thead><tr><th>Subject</th><th>Accepted</th><th>Proposed</th><th>Move (yrs)</th><th>3100 BCE → now</th></tr></thead>
<tbody>{''.join(rows_html)}</tbody></table>
<div class="leg"><span><i style="background:{P['acc']}"></i>accepted</span><span><i style="background:{P['prop']}"></i>proposed</span>
<span>▭ dashed = era · ▬ bar = reign/war · ▨ hatched = construction · ◆ = date read from art · ● = one-year event</span></div>

<h2>2. What kind of date it is</h2>
<p>The two columns don’t always measure the same thing, and the chart keeps them apart.</p>
<ul>
<li><b>A zodiac reading is a date, not a reign.</b> Seti I’s 969 and 1206 CE are two answers to one horoscope. Neither is a period he ruled.</li>
<li><b>A reign isn’t a build date.</b> Khufu’s reign is set against their era for <i>large pyramids</i>, 14th–16th c. Chron4 ch.20 also says “X–XI century the earliest,” with some “as late as the XVII.”</li>
<li><b>An era isn’t a shift.</b> Egypt, c. 3100–30 BCE, is about 3,070 years long. They fit it inside about 600, so there is no single offset.</li>
<li><b>The crucifixion date moved twice.</b> Chron4 ch.20 says 1095. Their later revision (Tsar of the Slavs, 2004) says birth 1152 and crucifixion 1185. This sheet uses the revision and flags the older one.</li>
</ul>

<h2>3. How the shifts work</h2>
<p>There are three offset families. Each one is a <strong>different distance from the same origin</strong>. You don’t add them. Chron1 ch.6 §7 says it plainly: “All the three shifts are counted off the same point.”</p>
<div class="fan">{fan_svg(640, 270, P['ink'], P['mute'], P['prop'], P['rule'], 12, P['head'])}</div>
<div class="two">
<p><b>Right:</b> copy = original − 333/360, <i>or</i> − 1,053, <i>or</i> − 1,778…1,810. Chron2 ch.3 names them the Roman–Byzantine, Roman and Graeco-Biblical shifts.</p>
<p><b>Wrong:</b> 333 + 1,053 + 1,778 = 3,164. Nobody proposes that number. There is also <b>no universal 600-year correction</b> anywhere in the sources.</p>
</div>
<p class="src">Gaps measured between two copies, not from the origin, can equal a difference or a sum. Fig. 6.20 labels Example 6 “720 = 1053 – 333.” Table 2 calls Example 2’s ≈1,300 “the sum of two basic shifts.”</p>

<h2>4. The 20 duplicate dynasties, as printed</h2>
<p>These are Chron1 ch.6, Examples 1–20. Shifts are copied from the text, tables, captions and figure notes. {n_split} examples print numbers that disagree with each other. {n_none} print no fixed offset at all.</p>
<table class="t"><thead><tr><th>#</th><th>Dynasty a</th><th>Dynasty b</th><th>Shift as printed</th><th></th></tr></thead>
<tbody>{''.join(ex_html)}</tbody></table>

<h2>5. Where the pages disagree with themselves</h2>
<ol>
<li>Ex. 1: the text says ≈333 and the caption says ≈330–360.</li>
<li>Ex. 7 has three numbers for one pair: ≈362 in the text, ≈360 in the captions, and a mean reign-end shift of 373.</li>
<li>Ex. 9: “911 AD = 928 BC … 1839.” Counted without a year 0, that is 1,838. Fig. 6.26 says ≈1,830.</li>
<li>Ex. 12: “970 AD = 911 AD … 60 year shift.” The difference is 59.</li>
<li>Ex. 17: the text gives 210–270 forward. Fig. 6.47 prints ≈275.</li>
<li>Parthenon: “447 b.c. … shift of 1810 years … 1363 a.d.” With no year 0, the arithmetic gives 1364.</li>
<li>Ex. 5 ends in 887 in the text and 888 in the captions. Byzantium II is 829–1204 in Ex. 13 and 867–1143 in Ex. 14.</li>
<li>Fig. 6.50 prints one Spartan reign as “330-397” BC.</li>
<li>No offset is printed for Examples 3, 4, 18 and 20.</li>
</ol>

<h2>6. What this sheet is not</h2>
<ul>
<li>It is not a redated list of every pharaoh. Egypt is shown as one era.</li>
<li>It applies no universal correction. None exists in the sources.</li>
<li>It doesn’t endorse the claim. Historians, Egyptologists and astronomers reject the New Chronology. This sheet only reports it accurately.</li>
</ul>

<h2>Sources</h2>
<div class="two src">
<div><b>Proposed — Fomenko &amp; Nosovsky, <i>History: Fiction or Science?</i></b><br>
Chron1 ch.6, pp. 256–325: Examples 1–20, Tables 1–11, Figs 6.11–6.57, §7.<br>
Chron2 ch.3 §§14–15: the 1374–1387 war, the Parthenon, the shift families.<br>
Chron3 ch.19: zodiac datings (Dendera 1185, Seti I 969/1206, Senenmut 1007).<br>
Chron4 ch.20: Egypt after 900 AD, pyramids XIV–XVI c., crucifixion 1095.<br>
<i>Tsar of the Slavs</i> (2004): birth 1152, crucifixion 1185.<br>
chronologia.org/en</div>
<div><b>Accepted</b><br>
The Met: Egyptian chronology; Classical Greece ca. 480–323 B.C.; Senenmut ceiling (TT353).<br>
Harvard Giza Project: Khufu, builder of the Great Pyramid.<br>
Egyptian Ministry of Tourism &amp; Antiquities: Tomb of Sety I (KV17).<br>
Louvre D 38: Dendera zodiac (Cauville &amp; Aubourg, mid-50 BC sky).<br>
Columbia Art Humanities: Parthenon 447–432 BC.<br>
Britannica / Cambridge: Peloponnesian War 431–404 BC; Sulla 82 BC; Caracalla d. 217.<br>
B. Ehrman (UNC): crucifixion 30 or 33 CE.</div>
</div>

<p class="stamp">Riven · pass over Chron1 ch.6, Chron2 ch.3, Chron3 ch.19, Chron4 ch.20 · every figure checked against the printed page · page wins over summary</p>
<div class="pb"></div>
<h2>Appendix — the full timeline</h2>
<img class="poster" src="../poster_part1_rot.png" style="height:8.3in;width:auto;margin:8px auto 0">
<p class="src">Rotated to fit the page. The full poster, including the 20-example panel, is in fomenko_new_chronology_timeline.pdf.</p>

</body></html>"""
(OUT / "report.html").write_text(report, encoding="utf-8")

# ================================================================== INFOGRAPHIC (phone, dark)
D = dict(bg="#000000", ink="#ffffff", dim="#8a8a91", dimmer="#55555d", rule="#1f1f26", acc="#4d8dff",
         prop="#ff9f1c")
ig_rows = []
for subj, kind, ma, ta, mp, tp, mv, _ in S:
    ig_rows.append(f"""
<div class="row"><div class="hd"><b>{subj}</b><span class="mv">{mv}{'' if mv.startswith('no') else ' yrs'}</span></div>
{strip_svg(ma, mp, 960, 54, D['acc'], D['prop'], D['ink'], D['rule'], D['bg'], D['dimmer'])}
<div class="ft"><span class="a">{ta}</span><span class="p">{tp}</span></div></div>""")

info = f"""<!doctype html><html><head><meta charset="utf-8"><title>Two Calendars</title>
<style>
{FONT_CSS}
*{{box-sizing:border-box}}
html,body{{margin:0;background:{D['bg']};color:{D['ink']}}}
body{{width:1080px;padding:64px 60px 54px;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased}}
.mono,.eyebrow,.stat .l,.stat .v,.mv,.ft,.sec,.foot,.big{{font-family:Mono,monospace}}
.eyebrow{{font-size:17px;letter-spacing:.2em;color:{D['dimmer']};text-transform:uppercase}}
h1{{font-size:96px;line-height:.92;letter-spacing:-.035em;margin:14px 0 18px;font-weight:700}}
h1 em{{font-style:normal;color:{D['prop']}}}
.dek{{font-size:27px;line-height:1.4;color:{D['dim']};margin:0 0 30px;max-width:900px}}
.dek b{{color:{D['ink']};font-weight:600}} .dek b.ac,.ac{{color:{D['acc']}}} .dek b.pr,.pr{{color:{D['prop']}}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:{D['rule']};border-block:1px solid {D['rule']}}}
.stat{{background:{D['bg']};padding:20px 16px}}
.stat .l{{font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:{D['dimmer']}}}
.stat .v{{font-size:52px;font-weight:700;letter-spacing:-.03em;margin-top:8px;line-height:1}}
.sec{{font-size:17px;letter-spacing:.16em;text-transform:uppercase;color:{D['dim']};margin:44px 0 6px;
  padding-bottom:10px;border-bottom:1px solid {D['rule']}}}
.row{{padding:14px 0 12px;border-bottom:1px solid {D['rule']}}}
.hd{{display:flex;justify-content:space-between;align-items:baseline}}
.hd b{{font-size:27px;font-weight:600;letter-spacing:-.01em}}
.mv{{font-size:21px;color:{D['dim']}}}
.ft{{display:flex;justify-content:space-between;font-size:19px;margin-top:2px}}
.ft .a{{color:{D['acc']}}} .ft .p{{color:{D['prop']}}}
.axis{{margin-top:6px}}
.law{{display:grid;grid-template-columns:auto 1fr;gap:10px 18px;margin-top:20px;font-size:26px;line-height:1.35}}
.law .n{{font-family:Mono;color:{D['prop']};font-weight:700}}
.law .t b{{font-weight:600}} .law .t span{{color:{D['dim']}}}
.foot{{margin-top:44px;padding-top:16px;border-top:1px solid {D['rule']};font-size:14.5px;line-height:1.75;color:{D['dimmer']}}}
.foot b{{color:{D['dim']};font-weight:500}}
</style></head><body>
<div class="eyebrow">Riven · one axis · 3100 BCE → 2026 CE · no year 0</div>
<h1>Two calendars,<br><em>one past.</em></h1>
<p class="dek">The accepted dates in <b class="ac">blue</b>. Fomenko &amp; Nosovsky’s “New Chronology” in <b class="pr">orange</b>.
Their claim: ancient history is medieval history copied backward. <b>Every number is from their own PDFs or a museum page.</b></p>

<div class="stats">
<div class="stat"><div class="l">Median move</div><div class="v pr">≈{n(int(round(median, -2)))}y</div></div>
<div class="stat"><div class="l">Biggest</div><div class="v">+4,188</div></div>
<div class="stat"><div class="l">Smallest</div><div class="v">+1,037</div></div>
</div>

<div class="sec">Ten cases · blue = accepted · orange = proposed</div>
{''.join(ig_rows)}
<div class="axis">{axis_svg(960, 26, D['dimmer'], 15)}</div>
<div class="mono" style="font-size:15px;color:{D['dimmer']};margin-top:8px">▭ era · ▬ reign/war · ▨ construction · ◆ date read from art · ● event · red line = today</div>

<div class="sec">Three shifts · one origin · never added</div>
{fan_svg(960, 300, D['ink'], D['dim'], D['prop'], D['rule'], 17, D['bg'])}

<div class="sec">Read it right</div>
<div class="law">
<div class="n">01</div><div class="t"><b>A zodiac reading is a date, not a reign.</b> <span>Seti I: 969 <i>or</i> 1206, two answers to one sky.</span></div>
<div class="n">02</div><div class="t"><b>The shifts don’t stack.</b> <span>333 + 1,053 + 1,778 is nobody’s number. There is no 600-year rule.</span></div>
<div class="n">03</div><div class="t"><b>Their own pages disagree.</b> <span>{n_split} of 20 dynasty examples print conflicting shifts. {n_none} print none.</span></div>
<div class="n">04</div><div class="t"><b>It’s a proposal.</b> <span>Historians, Egyptologists and astronomers reject it.</span></div>
</div>

<div class="foot"><b>Proposed:</b> Fomenko &amp; Nosovsky, <i>History: Fiction or Science?</i> Chron1 ch.6 · Chron2 ch.3 · Chron3 ch.19 · Chron4 ch.20; <i>Tsar of the Slavs</i> (2004) · chronologia.org/en<br>
<b>Accepted:</b> The Met · Harvard Giza Project · Egyptian Ministry of Tourism &amp; Antiquities · Louvre D 38 · Columbia · Britannica · Cambridge · UNC<br>
Gaps counted without a year 0 · compiled 10/2026 · page wins over summary</div>
</body></html>"""
(OUT / "infographic.html").write_text(info, encoding="utf-8")
print("median move:", median, "| none:", n_none, "| split:", n_split)
