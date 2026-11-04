#!/usr/bin/env python3
"""Recorta el fondo blanco del logo de BlitzLabs sin alterar su diseño.

- Solo se vuelve transparente el fondo conectado con los bordes de la imagen
  (relleno por inundación), de modo que el brillo blanco del ojo se conserva.
- Los píxeles interiores no se modifican: colores y proporciones idénticos.
- En el borde antialiasado se aplica "color a alfa" contra el blanco del fondo
  para que el contorno quede limpio sobre cualquier color.
- El recorte final solo elimina margen vacío; no se reescala.

Uso: python3 preparar_logo.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "02_marca" / "logo_blitzlabs_original.jpg"
DESTINO = RAIZ / "02_marca" / "logo_blitzlabs_transparente.png"

UMBRAL_FONDO = 240  # canal mínimo para considerar un píxel "blanco de fondo"
BANDA_BORDE = 3     # píxeles de transición tratados con color a alfa
MARGEN = 16         # margen transparente alrededor del recorte


def relleno_fondo(claro: np.ndarray) -> np.ndarray:
    """Devuelve la máscara de píxeles claros conectados con el borde (BFS)."""
    alto, ancho = claro.shape
    fondo = np.zeros_like(claro, dtype=bool)
    pila = [(y, x) for x in range(ancho) for y in (0, alto - 1) if claro[y, x]]
    pila += [(y, x) for y in range(alto) for x in (0, ancho - 1) if claro[y, x]]
    for y, x in pila:
        fondo[y, x] = True
    while pila:
        y, x = pila.pop()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < alto and 0 <= nx < ancho and claro[ny, nx] and not fondo[ny, nx]:
                fondo[ny, nx] = True
                pila.append((ny, nx))
    return fondo


def main() -> None:
    rgb = np.asarray(Image.open(ORIGEN).convert("RGB")).astype(np.float64)
    claro = (rgb >= UMBRAL_FONDO).all(axis=2)
    fondo = relleno_fondo(claro)

    # Blanco de referencia: mediana del fondo real (≈ 253-254).
    blanco = np.median(rgb[fondo], axis=0)

    # Banda de transición: píxeles no-fondo a <= BANDA_BORDE px del fondo.
    masc_fondo = Image.fromarray((fondo * 255).astype(np.uint8))
    dilatada = np.asarray(masc_fondo.filter(ImageFilter.MaxFilter(2 * BANDA_BORDE + 1))) > 0
    banda = dilatada & ~fondo

    alfa = np.ones(rgb.shape[:2])
    alfa[fondo] = 0.0

    # Color a alfa (GIMP) en la banda: alfa = max_c (b_c - p_c) / b_c
    p = rgb[banda]
    a = np.clip(((blanco - p) / blanco).max(axis=1), 0.0, 1.0)
    salida = rgb.copy()
    with np.errstate(divide="ignore", invalid="ignore"):
        color = np.where(a[:, None] > 0, (p - blanco) / a[:, None] + blanco, p)
    salida[banda] = np.clip(color, 0, 255)
    alfa[banda] = a

    rgba = np.dstack([salida, alfa * 255]).round().astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")

    caja = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    x0, y0, x1, y1 = caja
    x0, y0 = max(0, x0 - MARGEN), max(0, y0 - MARGEN)
    x1, y1 = min(img.width, x1 + MARGEN), min(img.height, y1 + MARGEN)
    img.crop((x0, y0, x1, y1)).save(DESTINO, optimize=True)

    # Verificación: los píxeles interiores no cambian.
    interior = ~dilatada
    cambio = np.abs(salida[interior] - rgb[interior]).max() if interior.any() else 0
    print(f"Logo transparente: {DESTINO.relative_to(RAIZ)}  ({x1 - x0}x{y1 - y0} px)")
    print(f"Blanco de fondo detectado: {blanco.round(1).tolist()}  |  cambio máximo interior: {cambio}")


if __name__ == "__main__":
    main()
