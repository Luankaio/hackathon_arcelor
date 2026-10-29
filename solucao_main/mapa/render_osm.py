"""Renderiza a geometria OSM da CSP (ArcelorMittal Pecém) em SVG simples.
Uso: python3 -I render_osm.py <entrada.json> <saida.svg> [zonas]
"""
import json
import math
import sys

src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src))
els = data["elements"]

plant = next(e for e in els if e["type"] == "way" and e["id"] == 299910787)
lats = [p["lat"] for p in plant["geometry"]]
lons = [p["lon"] for p in plant["geometry"]]
pad = 0.002
min_lat, max_lat = min(lats) - pad, max(lats) + pad
min_lon, max_lon = min(lons) - pad, max(lons) + pad
lat0 = (min_lat + max_lat) / 2
kx = 111320 * math.cos(math.radians(lat0))  # metros por grau de longitude
ky = 110540                                  # metros por grau de latitude
W_m = (max_lon - min_lon) * kx
H_m = (max_lat - min_lat) * ky
W = 1400
S = W / W_m
H = int(H_m * S)


def xy(p):
    return ((p["lon"] - min_lon) * kx * S, (max_lat - p["lat"]) * ky * S)


def path(geom, close):
    pts = [xy(p) for p in geom]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return d + (" Z" if close else "")


out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H + 60}" viewBox="0 0 {W} {H + 60}" font-family="Arial, sans-serif">',
       f'<rect width="{W}" height="{H + 60}" fill="#f4f1ea"/>']
NAMES = {"Blast Furnace 1": "Alto-Forno 1", "Subestação UTE CSP": "Subestação UTE CSP", "Subestação Pecém": "Subestação Pecém (Enel)",
         "Correia Transportadora Fechada - tubular": "Correia tubular (carvão, vem do porto)", "Portaria ZPE": "Portaria ZPE"}


def label(x, y, text, color, size=13):
    text = NAMES.get(text, text)
    w = len(text) * size * 0.58 + 10
    return (f'<rect x="{x - w / 2:.0f}" y="{y - size:.0f}" width="{w:.0f}" height="{size + 8}" rx="4" fill="#ffffff" fill-opacity="0.9" stroke="{color}" stroke-width="1"/>'
            f'<text x="{x:.0f}" y="{y + 2:.0f}" font-size="{size}" font-weight="bold" fill="{color}" text-anchor="middle">{text}</text>')


ZONES = len(sys.argv) > 3
layers = {"plant": [], "road": [], "rail": [], "bldg": [], "conv": [], "sub": [], "pts": [], "lbl": []}

for e in els:
    t = e.get("tags", {})
    if e["type"] == "way" and "geometry" in e:
        g = e["geometry"]
        if e["id"] == 299910787:
            layers["plant"].append(f'<path d="{path(g, True)}" fill="#e9e4d8" stroke="#8a8270" stroke-width="2" stroke-dasharray="8 5"/>')
        elif "building" in t:
            fill = "#c96f3b" if t.get("name") == "Blast Furnace 1" else "#9aa3ad"
            layers["bldg"].append(f'<path d="{path(g, True)}" fill="{fill}" stroke="#4b5560" stroke-width="0.8"/>')
        elif t.get("power") == "substation":
            layers["sub"].append(f'<path d="{path(g, True)}" fill="#f2d25c" stroke="#8a7413" stroke-width="1"/>')
        elif t.get("man_made") == "goods_conveyor":
            layers["conv"].append(f'<path d="{path(g, False)}" fill="none" stroke="#2f7d4f" stroke-width="3"/>')
        elif "railway" in t:
            layers["rail"].append(f'<path d="{path(g, False)}" fill="none" stroke="#555" stroke-width="1.6" stroke-dasharray="6 3"/>')
        elif "highway" in t:
            wdt = 3.5 if t["highway"] in ("tertiary", "unclassified") else 2
            layers["road"].append(f'<path d="{path(g, False)}" fill="none" stroke="#ffffff" stroke-width="{wdt + 1.5}"/><path d="{path(g, False)}" fill="none" stroke="#c9c2b2" stroke-width="{wdt}"/>')
        name = t.get("name")
        if name and e["id"] != 299910787 and ("building" in t or "power" in t or t.get("man_made") == "goods_conveyor"):
            cx = sum(xy(p)[0] for p in g) / len(g)
            cy = sum(xy(p)[1] for p in g) / len(g)
            layers["lbl"].append(label(cx, cy - 12, name, "#222"))
    elif e["type"] == "node":
        x, y = xy(e)
        if t.get("barrier") == "gate":
            layers["pts"].append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#e0662a" stroke="#fff" stroke-width="2"/>')
            layers["lbl"].append(label(x + 45, y - 12, "Portaria", "#e0662a"))
        elif t.get("man_made") == "chimney":
            layers["pts"].append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#333"/>')

# áreas inferidas (pixels do desenho 1400 px de largura); só na versão com zonas
zones = [
    ("Pátio de Matérias-Primas", 105, 198, 313, 396),
    ("Sinterização", 110, 600, 200, 160),
    ("Coqueria", 345, 745, 110, 170),
    ("Alto-Forno", 190, 1040, 230, 150),
    ("Aciaria + Lingotamento", 140, 1320, 300, 200),
    ("Termelétrica / Utilidades", 590, 985, 140, 130),
    ("Pátio de Placas", 520, 1430, 120, 160),
]
if ZONES:
    for n, x, y, w, h in zones:
        layers["lbl"].insert(0, f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="#e0662a" stroke-width="3" stroke-dasharray="12 7"/>')
        layers["lbl"].append(label(x + w / 2, y + 22, n + " *", "#b24a12", 14))

for k in ("plant", "road", "rail", "conv", "bldg", "sub", "pts", "lbl"):
    out += layers[k]

# escala de 500 m
bar = 500 * S
out.append(f'<line x1="30" y1="{H + 30}" x2="{30 + bar:.0f}" y2="{H + 30}" stroke="#222" stroke-width="4"/>')
out.append(f'<text x="30" y="{H + 50}" font-size="13">500 m</text>')
out.append(f'<text x="{W - 20}" y="{H + 50}" font-size="12" text-anchor="end" fill="#555">CSP / ArcelorMittal Pecém · dados © OpenStreetMap contributors (ODbL) · cinza: prédios · laranja: Alto-Forno 1 · amarelo: subestação · verde: correia · tracejado: ferrovia' + (' · * área inferida, verificar' if ZONES else '') + '</text>')
out.append('</svg>')
open(dst, "w").write("\n".join(out))
print(f"{dst}: {W}x{H + 60}px, área {W_m:.0f} x {H_m:.0f} m")
