#!/usr/bin/env python3
"""Genera los gráficos de edición del anuncio (PNG 1080x1920 con transparencia).

Salidas:
  03_graficos/T1..T3.png           textos añadidos en edición
  03_graficos/SUB01..SUB06.png     subtítulos quemados
  03_graficos/EC0..EC4_*.png       capas de la pantalla final (velo, logo, lema, acción, secundario)
  03_graficos/guia_area_segura.png guía de revisión (no va en el video)
  04_subtitulos/BlitzLabs_Navidad_es-MX.srt

Todo se lee de timeline.json. Tipografía: Inter / Inter Display (licencia OFL,
apta para publicidad). Para cambiarla, edita FUENTES.

Uso: python3 graficos.py
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
TL = json.loads((Path(__file__).parent / "timeline.json").read_text(encoding="utf-8"))
W, H = TL["ancho"], TL["alto"]
DIR_G = RAIZ / "03_graficos"
DIR_S = RAIZ / "04_subtitulos"
LOGO = RAIZ / "02_marca" / "logo_blitzlabs_transparente.png"

FUENTES = Path("/usr/share/fonts/opentype/inter")
F = {
    "titulo": FUENTES / "InterDisplay-Medium.otf",
    "lema": FUENTES / "InterDisplay-SemiBold.otf",
    "sub": FUENTES / "Inter-SemiBold.otf",
    "accion": FUENTES / "Inter-Medium.otf",
    "clave": FUENTES / "Inter-Bold.otf",
    "secundario": FUENTES / "Inter-Regular.otf",
    "marca": FUENTES / "Inter-SemiBold.otf",
}

CREMA = (255, 246, 232)
SOMBRA = (20, 13, 8)
ROJO_MARCA = (250, 40, 27)    # muestreado del logo original
BLANCO = (255, 255, 255)

# Área segura para 9:16 (Reels / TikTok / Shorts): evita la interfaz superior,
# la franja inferior de descripción y el riel derecho de botones.
SEGURA = {"arriba": 250, "abajo": H - 420, "izq": 120, "der": W - 140}


def fuente(clave: str, tam: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(F[clave]), tam)


def lienzo() -> Image.Image:
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def ancho_texto(f: ImageFont.FreeTypeFont, texto: str, tracking: float = 0) -> float:
    return f.getlength(texto) + tracking * max(len(texto) - 1, 0)


def dibujar_linea(d: ImageDraw.ImageDraw, x_centro: float, y: float, texto: str,
                  f: ImageFont.FreeTypeFont, color, tracking: float = 0) -> None:
    """Línea centrada en x_centro; y es la línea base."""
    if not tracking:
        d.text((x_centro, y), texto, font=f, fill=color, anchor="ms")
        return
    x = x_centro - ancho_texto(f, texto, tracking) / 2
    for ch in texto:
        d.text((x, y), ch, font=f, fill=color, anchor="ls")
        x += f.getlength(ch) + tracking


def con_sombra(capa: Image.Image, suave: int = 12, opac: float = 0.55,
               dura: int = 3, opac_dura: float = 0.35) -> Image.Image:
    """Añade una sombra suave cálida detrás de lo dibujado en `capa`."""
    alfa = capa.getchannel("A")
    out = lienzo()
    for radio, op in ((suave, opac), (dura, opac_dura)):
        s = Image.new("RGBA", (W, H), SOMBRA + (0,))
        s.putalpha(alfa.filter(ImageFilter.GaussianBlur(radio)).point(lambda v, o=op: int(v * o)))
        out.alpha_composite(s)
    out.alpha_composite(capa)
    return out


def bloque_texto(texto: str, f: ImageFont.FreeTypeFont, y_base_1: float,
                 interlinea: float, color=CREMA, tracking: float = 0) -> Image.Image:
    capa = lienzo()
    d = ImageDraw.Draw(capa)
    for i, linea in enumerate(texto.split("\n")):
        dibujar_linea(d, W / 2, y_base_1 + i * interlinea, linea, f, color, tracking)
    return capa


def comprobar_area(img: Image.Image, nombre: str) -> None:
    caja = img.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
    if not caja:
        return
    x0, y0, x1, y1 = caja
    ok = (x0 >= SEGURA["izq"] and x1 <= SEGURA["der"]
          and y0 >= SEGURA["arriba"] and y1 <= SEGURA["abajo"])
    estado = "OK " if ok else "REVISAR"
    print(f"  [{estado}] {nombre:<18} caja=({x0},{y0})-({x1},{y1})")


# ---------------------------------------------------------------- textos
def textos() -> None:
    f = fuente("titulo", 68)
    for t in TL["textos"]:
        img = con_sombra(bloque_texto(t["texto"], f, y_base_1=372, interlinea=84))
        img.save(DIR_G / f"{t['id']}.png", optimize=True)
        comprobar_area(img, t["id"])


# ---------------------------------------------------------------- subtítulos
def subtitulos() -> None:
    f = fuente("sub", 46)
    interlinea = 60
    base_ultima = 1440  # línea base de la última línea
    for s in TL["subtitulos"]:
        if s.get("quemado") is False:
            continue
        lineas = s["texto"].split("\n")
        y1 = base_ultima - (len(lineas) - 1) * interlinea
        ancho = max(ancho_texto(f, ln) for ln in lineas)
        asc, desc = f.getmetrics()
        pad_x, pad_y = 30, 20
        caja = (W / 2 - ancho / 2 - pad_x, y1 - asc - pad_y + 6,
                W / 2 + ancho / 2 + pad_x, base_ultima + desc + pad_y - 6)
        img = lienzo()
        fondo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(fondo).rounded_rectangle(caja, radius=24, fill=(16, 11, 8, 112))
        img.alpha_composite(fondo)
        texto = bloque_texto(s["texto"], f, y1, interlinea, color=(255, 250, 243))
        img.alpha_composite(con_sombra(texto, suave=6, opac=0.35, dura=2, opac_dura=0.25))
        img.save(DIR_G / f"{s['id']}.png", optimize=True)
        comprobar_area(img, s["id"])


def srt() -> None:
    def tc(seg: float) -> str:
        ms = int(round(seg * 1000))
        h, ms = divmod(ms, 3_600_000)
        m, ms = divmod(ms, 60_000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    bloques = []
    for i, s in enumerate(TL["subtitulos"], 1):
        bloques.append(f"{i}\n{tc(s['inicio'])} --> {tc(s['fin'])}\n{s['texto']}\n")
    (DIR_S / "BlitzLabs_Navidad_es-MX.srt").write_text("\n".join(bloques), encoding="utf-8")


# ---------------------------------------------------------------- pantalla final
def velo() -> Image.Image:
    """Degradado cálido arriba y abajo; el centro (la figura) queda limpio."""
    alfa = Image.new("L", (1, H))
    for y in range(H):
        if y < 1000:
            v = 0.66 * (1 - y / 1000) ** 1.6
        elif y > 1100:
            v = 0.72 * ((y - 1100) / (H - 1100)) ** 1.3
        else:
            v = 0.0
        alfa.putpixel((0, y), int(v * 255))
    img = Image.new("RGBA", (W, H), SOMBRA + (255,))
    img.putalpha(alfa.resize((W, H)))
    return img


def capa_logo(cfg: dict) -> Image.Image:
    img = lienzo()
    cx, cy, r = W / 2, 430, 128
    # Sombra de la insignia
    sombra = lienzo()
    ImageDraw.Draw(sombra).ellipse((cx - r, cy - r + 10, cx + r, cy + r + 10), fill=SOMBRA + (150,))
    img.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(16)))
    # Insignia blanca: mismo fondo blanco del logo original, para conservar su contraste.
    ImageDraw.Draw(img).ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLANCO + (255,))
    # Logo original, escalado de forma uniforme (proporciones intactas).
    logo = Image.open(LOGO).convert("RGBA")
    alto_logo = 178
    esc = alto_logo / logo.height
    logo = logo.resize((round(logo.width * esc), alto_logo), Image.LANCZOS)
    img.alpha_composite(logo, (round(cx - logo.width / 2 + 4), round(cy - logo.height / 2 + 4)))
    if cfg.get("nombre_marca"):
        marca = bloque_texto(cfg["nombre_marca"], fuente("marca", 40), y_base_1=cy + r + 66,
                             interlinea=0, tracking=1.5)
        img.alpha_composite(con_sombra(marca, suave=8, opac=0.45))
    return img


def capa_lema(cfg: dict) -> Image.Image:
    return con_sombra(bloque_texto(cfg["lema"], fuente("lema", 80), y_base_1=736, interlinea=92))


def capa_accion(cfg: dict) -> Image.Image:
    img = lienzo()
    f1 = fuente("accion", 46)
    t1 = bloque_texto(cfg["accion_1"], f1, y_base_1=1302, interlinea=0)
    img.alpha_composite(con_sombra(t1, suave=8, opac=0.5))

    f2, fk = fuente("accion", 46), fuente("clave", 46)
    antes, clave, despues = cfg["accion_2_antes"], cfg["accion_2_clave"], cfg["accion_2_despues"]
    pad_x = 22
    w_antes, w_clave, w_desp = f2.getlength(antes), fk.getlength(clave), f2.getlength(despues)
    total = w_antes + w_clave + 2 * pad_x + w_desp
    x = W / 2 - total / 2
    base = 1384
    texto = lienzo()
    d = ImageDraw.Draw(texto)
    d.text((x, base), antes, font=f2, fill=CREMA, anchor="ls")
    img.alpha_composite(con_sombra(texto, suave=8, opac=0.5))

    asc, desc = fk.getmetrics()
    x_p = x + w_antes
    pastilla = (x_p, base - asc + 2, x_p + w_clave + 2 * pad_x, base + desc + 4)
    sombra = lienzo()
    ImageDraw.Draw(sombra).rounded_rectangle(pastilla, radius=18, fill=SOMBRA + (120,))
    img.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(8)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(pastilla, radius=18, fill=ROJO_MARCA + (255,))
    d.text((x_p + pad_x, base), clave, font=fk, fill=BLANCO, anchor="ls")

    resto = lienzo()
    ImageDraw.Draw(resto).text((x_p + w_clave + 2 * pad_x, base), despues, font=f2, fill=CREMA, anchor="ls")
    img.alpha_composite(con_sombra(resto, suave=8, opac=0.5))
    return img


def capa_secundario(cfg: dict) -> Image.Image:
    t = bloque_texto(cfg["secundario"], fuente("secundario", 36), y_base_1=1472, interlinea=0,
                     color=CREMA + (225,), tracking=0.6)
    return con_sombra(t, suave=8, opac=0.5)


def pantalla_final() -> None:
    cfg = TL["pantalla_final"]
    capas = {
        "EC0_velo": velo(),
        "EC1_logo": capa_logo(cfg),
        "EC2_lema": capa_lema(cfg),
        "EC3_accion": capa_accion(cfg),
        "EC4_secundario": capa_secundario(cfg),
    }
    for nombre, img in capas.items():
        img.save(DIR_G / f"{nombre}.png", optimize=True)
        if nombre != "EC0_velo":
            comprobar_area(img, nombre)


def guia_area_segura() -> None:
    img = lienzo()
    d = ImageDraw.Draw(img)
    gris = (255, 255, 255, 70)
    d.rectangle((0, 0, W, SEGURA["arriba"]), fill=(255, 0, 0, 40))
    d.rectangle((0, SEGURA["abajo"], W, H), fill=(255, 0, 0, 40))
    d.rectangle((SEGURA["der"], 0, W, H), fill=(255, 0, 0, 25))
    d.rectangle((SEGURA["izq"], SEGURA["arriba"], SEGURA["der"], SEGURA["abajo"]), outline=gris, width=3)
    d.text((W / 2, SEGURA["arriba"] - 30), "zona de interfaz", font=fuente("secundario", 28),
           fill=(255, 255, 255, 140), anchor="ms")
    d.text((W / 2, SEGURA["abajo"] + 50), "zona de interfaz / descripción", font=fuente("secundario", 28),
           fill=(255, 255, 255, 140), anchor="ms")
    img.save(DIR_G / "guia_area_segura.png", optimize=True)


def main() -> None:
    DIR_G.mkdir(exist_ok=True)
    DIR_S.mkdir(exist_ok=True)
    print("Comprobación de área segura:")
    textos()
    subtitulos()
    pantalla_final()
    guia_area_segura()
    srt()
    print("Gráficos en 03_graficos/  ·  subtítulos en 04_subtitulos/")


if __name__ == "__main__":
    main()
