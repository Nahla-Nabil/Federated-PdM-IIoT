"""Shared SVG style helpers for the README graphics (navy / cyan design system).

Imported by build_readme_assets.py. Standard library only.
"""
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs" / "assets"

# ---------------------------------------------------------------- design tokens
BG0, BG, PANEL, PANEL2, STROKE = "#060E22", "#0B1733", "#10204A", "#152A5C", "#25407A"
TEXT, TEXT2, MUTED = "#EAF2FF", "#A9B8D6", "#7186AE"
CYAN, BLUE, AMBER = "#22D3EE", "#5B7CFA", "#F5B342"
FED, CEN, ISO, ISO2 = "#13A6C2", "#5B7CFA", "#3E4F78", "#56688F"   # validated chart series
FONT = "'Segoe UI', 'Inter', 'Helvetica Neue', Arial, sans-serif"
MONO = "'Cascadia Code', 'SFMono-Regular', Consolas, monospace"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, size=20, fill=TEXT, weight=400, anchor="start", ls=0, family=FONT, italic=False, op=1):
    st = ' font-style="italic"' if italic else ""
    o = f' opacity="{op}"' if op != 1 else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{l}{st}{o}>{esc(s)}</text>')


def r(x, y, w, h, rx=14, fill=PANEL, stroke=None, sw=1.5, op=1, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{d}{o}/>'


def line(x1, y1, x2, y2, stroke=STROKE, sw=2, dash=None, marker=None, op=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{d}{m}{o}/>'


def path(d, stroke=STROKE, sw=2, fill="none", dash=None, marker=None, op=1):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    o = f' opacity="{op}"' if op != 1 else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round"{da}{m}{o}/>'


def defs():
    return f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{BG0}"/><stop offset="0.55" stop-color="{BG}"/><stop offset="1" stop-color="#0E2250"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.28"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowb" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{BLUE}" stop-opacity="0.30"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="0.035" stroke-width="1"/>
  </pattern>
  <marker id="ac" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="{CYAN}"/></marker>
  <marker id="ab" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="{BLUE}"/></marker>
  <marker id="am" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker>
  <marker id="aa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="{AMBER}"/></marker>
  <marker id="abig" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="18" markerHeight="18" markerUnits="userSpaceOnUse" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="{BLUE}"/></marker>
  <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="#FF7A7A"/></marker>
</defs>"""


def svg(w, h, body, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t d">\n<title id="t">{esc(title)}</title>\n<desc id="d">{esc(desc)}</desc>\n'
            f'{defs()}\n{r(0, 0, w, h, 24, "url(#bg)")}\n{r(0, 0, w, h, 24, "url(#grid)")}\n{body}\n</svg>\n')


# ---------------------------------------------------------------- icons
def cloud(cx, cy, s=1.0, fill=PANEL2, stroke=CYAN, sw=2.5):
    d = (f"M{cx-46*s} {cy+22*s} h{92*s} a{24*s} {24*s} 0 0 0 {2*s} {-48*s} "
         f"a{34*s} {34*s} 0 0 0 {-64*s} {-10*s} a{24*s} {24*s} 0 0 0 {-30*s} {58*s} z")
    return path(d, stroke=stroke, sw=sw, fill=fill)


def gear(cx, cy, rad, stroke=CYAN, fill="none", sw=2.2, teeth=8):
    pts = []
    for i in range(teeth * 4):
        a = 2 * math.pi * i / (teeth * 4)
        rr = rad if (i % 4) in (0, 1) else rad * 0.78
        pts.append(f"{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{rad*0.32:.1f}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>')


def chip(cx, cy, s=26, stroke=CYAN, fill=PANEL2):
    out = [r(cx - s, cy - s, 2*s, 2*s, 6, fill, stroke, 2.2), r(cx - s*0.5, cy - s*0.5, s, s, 3, "none", stroke, 1.6)]
    for k in (-0.5, 0, 0.5):
        for (x1, y1, x2, y2) in ((cx + k*s, cy - s, cx + k*s, cy - s*1.35), (cx + k*s, cy + s, cx + k*s, cy + s*1.35),
                                 (cx - s, cy + k*s, cx - s*1.35, cy + k*s), (cx + s, cy + k*s, cx + s*1.35, cy + k*s)):
            out.append(line(x1, y1, x2, y2, stroke, 1.8))
    return "".join(out)


def motor(cx, cy, s=1.0, stroke=TEXT2):
    return "".join([
        r(cx - 34*s, cy - 20*s, 52*s, 40*s, 8*s, PANEL2, stroke, 2),
        line(cx - 24*s, cy - 20*s, cx - 24*s, cy + 20*s, stroke, 1.4, op=0.6),
        line(cx - 12*s, cy - 20*s, cx - 12*s, cy + 20*s, stroke, 1.4, op=0.6),
        line(cx, cy - 20*s, cx, cy + 20*s, stroke, 1.4, op=0.6),
        r(cx + 18*s, cy - 6*s, 18*s, 12*s, 3, PANEL2, stroke, 2),
        r(cx - 40*s, cy + 22*s, 64*s, 7*s, 3, stroke, None, op=0.7)])


def wave(x, y, w, amp, stroke=CYAN, sw=2.2, n=3, op=1):
    seg = w / (n * 2)
    d = f"M{x} {y}"
    for i in range(n * 2):
        sgn = -1 if i % 2 == 0 else 1
        d += f" q{seg/2} {sgn*amp*2} {seg} 0"
    return path(d, stroke=stroke, sw=sw, op=op)


def lock(cx, cy, s=1.0, stroke=CYAN):
    return (r(cx - 11*s, cy - 2*s, 22*s, 17*s, 3, "none", stroke, 2) +
            path(f"M{cx-6*s} {cy-2*s} v{-6*s} a{6*s} {6*s} 0 0 1 {12*s} 0 v{6*s}", stroke=stroke, sw=2))


def db(cx, cy, s=1.0, stroke=CYAN, fill=PANEL2):
    w, h = 26*s, 30*s
    return (path(f"M{cx-w} {cy-h/2} v{h} a{w} {8*s} 0 0 0 {2*w} 0 v{-h}", stroke=stroke, sw=2, fill=fill) +
            f'<ellipse cx="{cx}" cy="{cy-h/2}" rx="{w}" ry="{8*s}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>' +
            path(f"M{cx-w} {cy} a{w} {8*s} 0 0 0 {2*w} 0", stroke=stroke, sw=1.5, op=0.7))


def bars_icon(cx, cy, s=1.0, stroke=CYAN):
    return "".join(r(cx + (i - 1.5) * 12*s - 4*s, cy + 16*s - hh*s, 8*s, hh*s, 2, stroke) for i, hh in enumerate((12, 22, 16, 30)))


def magnifier(cx, cy, s=1.0, stroke=CYAN):
    return (f'<circle cx="{cx-4*s}" cy="{cy-4*s}" r="{13*s}" fill="none" stroke="{stroke}" stroke-width="2.4"/>' +
            line(cx + 5*s, cy + 5*s, cx + 16*s, cy + 16*s, stroke, 3))


def shield(cx, cy, s=1.0, stroke=CYAN):
    return path(f"M{cx} {cy-20*s} l{17*s} {6*s} v{10*s} c0 {12*s} {-8*s} {20*s} {-17*s} {24*s} "
                f"c{-9*s} {-4*s} {-17*s} {-12*s} {-17*s} {-24*s} v{-10*s} z", stroke=stroke, sw=2.2)


def pill(x, y, s, fill=PANEL2, color=CYAN, size=15, pad=14, stroke=None):
    w = len(s) * size * 0.58 + 2 * pad
    return r(x, y, w, size * 2, size, fill, stroke or color, 1.2) + t(x + w/2, y + size*1.36, s, size, color, 600, "middle", 0.5), w


# ---------------------------------------------------------------- A. banner
def banner():
    W, H = 1600, 520
    b = [f'<circle cx="1240" cy="190" r="300" fill="url(#glow)"/>', f'<circle cx="300" cy="520" r="360" fill="url(#glowb)"/>']
    b.append(t(80, 112, "FEDERATED LEARNING  ·  INDUSTRIAL IoT  ·  EXPLAINABLE AI", 19, CYAN, 600, ls=2.5))
    b.append(t(78, 196, "Hybrid Edge–Cloud", 70, TEXT, 700))
    b.append(t(78, 276, "Federated Learning", 70, TEXT, 700))
    b.append(t(80, 330, "Predictive Maintenance for Industrial IoT", 32, CYAN, 500))
    b.append(line(80, 372, 140, 372, STROKE, 2))
    b.append(t(80, 418, "Nahla Nabil Skaik", 30, TEXT, 600))
    b.append(t(80, 454, "First Author  ·  Principal Project Developer", 19, TEXT2))
    b.append(t(80, 484, "Arab Open University – Bahrain", 19, MUTED))
    # illustration: cloud aggregator over four edge sites
    cx, cy = 1235, 128
    b.append(r(cx - 120, cy - 70, 240, 140, 70, "none", CYAN, 1, op=0.15))
    b.append(cloud(cx, cy, 1.45))
    b.append(t(cx, cy + 14, "Σ nₖ/N · fₖ", 20, TEXT, 600, "middle", family=MONO))
    xs = [960, 1145, 1330, 1515]
    for i, x in enumerate(xs):
        y = 384
        b.append(path(f"M{x} {y-64} C {x} {y-150}, {cx + (x-cx)*0.35} {cy+110}, {cx + (x-cx)*0.25} {cy+46}",
                      stroke=CYAN, sw=2, dash="2 9", op=0.85))
        mx, my = (x + cx + (x-cx)*0.35) / 2, (y - 150 + cy + 110) / 2 + 30
        b.append(r(mx - 15, my - 11, 30, 22, 5, PANEL2, CYAN, 1.5) + gear(mx, my, 7, CYAN, sw=1.4, teeth=6))
        b.append(r(x - 78, y - 62, 156, 150, 18, PANEL, STROKE, 1.5))
        b.append(chip(x, y - 22, 17))
        b.append(motor(x - 4, y + 40, 0.85))
        b.append(wave(x + 30, y + 40, 34, 4, CYAN, 1.6, 2, 0.9))
        b.append(lock(x + 54, y - 38, 0.65, TEXT2))
        b.append(t(x, y + 112, f"Edge site {i+1}", 16, TEXT2, 600, "middle"))
    return svg(W, H, "\n".join(b), "Hybrid Edge–Cloud Federated Learning — Predictive Maintenance for Industrial IoT",
               "Project banner: four edge sites with local models send model updates, not raw data, to a cloud aggregator. Author: Nahla Nabil Skaik.")


# ---------------------------------------------------------------- K. publication
def publication():
    W, H = 1200, 250
    b = [r(32, 28, 1136, 194, 20, PANEL, STROKE, 1.2)]
    b.append(r(64, 64, 96, 122, 10, PANEL2, CYAN, 1.5))
    for k in range(5): b.append(line(82, 92 + k * 16, 142 - (k % 2) * 18, 92 + k * 16, TEXT2, 3, op=0.6))
    b.append(t(196, 82, "PEER-REVIEWED PUBLICATION  ·  IEEE XPLORE", 14, CYAN, 700, ls=2))
    b.append(t(196, 122, "Hybrid Edge-Cloud Federated Learning Framework", 27, TEXT, 700))
    b.append(t(196, 156, "for Predictive Maintenance in Industrial IoT", 27, TEXT, 700))
    b.append(t(196, 194, "N. N. Skaik (first author), H. A. Razzaqi  ·  Arab Open University, Bahrain  ·  IEEE document 11430844", 16, TEXT2))
    b.append(r(990, 104, 146, 44, 22, CYAN) + t(1063, 132, "Read paper →", 16, BG0, 700, "middle"))
    return svg(W, H, "\n".join(b), "IEEE Xplore publication",
               "Hybrid Edge-Cloud Federated Learning Framework for Predictive Maintenance in Industrial IoT, by N. N. Skaik and H. A. Razzaqi, IEEE Xplore document 11430844.")


# ---------------------------------------------------------------- L. author
def author():
    W, H = 1200, 240
    b = [r(32, 24, 1136, 192, 20, PANEL, STROKE, 1.2)]
    b.append(f'<circle cx="134" cy="120" r="64" fill="{PANEL2}" stroke="{CYAN}" stroke-width="2"/>')
    b.append(t(134, 138, "NS", 46, CYAN, 700, "middle"))
    b.append(t(232, 92, "Nahla Nabil Skaik", 32, TEXT, 700))
    b.append(t(232, 128, "First Author  ·  Principal Project Developer", 19, CYAN, 600))
    b.append(t(232, 160, "AI Researcher  ·  Arab Open University – Bahrain", 17, TEXT2))
    b.append(t(232, 190, "Implemented the framework, ran the experiments and maintains this repository.", 15, MUTED))
    return svg(W, H, "\n".join(b), "Project developer: Nahla Nabil Skaik",
               "Nahla Nabil Skaik, first author, principal researcher and project developer, Arab Open University – Bahrain.")


