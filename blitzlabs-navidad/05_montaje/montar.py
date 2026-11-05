#!/usr/bin/env python3
"""Monta el anuncio BlitzLabs (35 s, 1080x1920) a partir de timeline.json.

Para cada plano busca, en este orden:
  1. 07_clips/<ID>.mp4|.mov|.webm   clip animado (Higgsfield)  -> se usa tal cual
  2. 07_clips/<ID>.png|.jpg|.webp   fotograma clave aún sin animar -> acercamiento lento
  3. nada                           -> placa "PENDIENTE" (animatic)

Después añade disolvencias, gradación de recuerdo, textos, subtítulos,
pantalla final con el logo original, locución, música con atenuación bajo
la voz (sidechain), efectos y normalización de sonoridad.

Si falta algún plano, la salida se marca como ANIMATIC (con código de tiempo)
y no sustituye al anuncio final.

Uso:
  python3 montar.py            # monta con lo que exista
  python3 montar.py --borrador # codificación rápida para revisar
"""
import argparse
import json
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
TL = json.loads((AQUI / "timeline.json").read_text(encoding="utf-8"))
W, H, FPS, DUR = TL["ancho"], TL["alto"], TL["fps"], TL["duracion"]
TOTAL_FOTOGRAMAS = round(DUR * FPS)
BUILD = AQUI / "build"
CLIPS = RAIZ / "07_clips"
GRAF = RAIZ / "03_graficos"
SALIDA = RAIZ / "09_salida"
FUENTES = Path("/usr/share/fonts/opentype/inter")

EXT_VIDEO = (".mp4", ".mov", ".webm", ".mkv")
EXT_IMAGEN = (".png", ".jpg", ".jpeg", ".webp")
EXT_AUDIO = (".wav", ".flac", ".aiff", ".mp3", ".m4a")

GRADOS = {
    "presente": "",
    # Recuerdo: más cálido, contraste y saturación suaves, leve difusión, viñeta y grano.
    "recuerdo": ("colorbalance=rs=0.05:gs=0.01:bs=-0.06:rm=0.03:bm=-0.04,"
                 "eq=contrast=0.90:saturation=0.82:gamma=1.04,"
                 "gblur=sigma=0.7,vignette=angle=PI/4.5,noise=alls=5:allf=t"),
}

avisos: list[str] = []


def fotogramas(seg: float) -> int:
    return round(seg * FPS)


def ejecutar(cmd: list[str]) -> None:
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *cmd])
    if r.returncode:
        sys.exit(f"ffmpeg falló ({r.returncode}).")


def duracion_medio(ruta: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(ruta)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def buscar(base: Path, nombre: str, extensiones) -> Path | None:
    for ext in extensiones:
        p = base / f"{nombre}{ext}"
        if p.exists():
            return p
    return None


# ----------------------------------------------------------------- placas
def placa(plano: dict, ruta: Path) -> None:
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    calido = plano["grado"] == "recuerdo"
    for y in range(H):
        t = y / H
        base = (38, 27, 18) if calido else (30, 24, 20)
        d.line([(0, y), (W, y)], fill=tuple(int(c * (0.75 + 0.5 * t)) for c in base))
    f = lambda n, s: ImageFont.truetype(str(FUENTES / n), s)
    crema, tenue = (255, 246, 232), (200, 188, 172)
    dur = plano["fin"] - plano["inicio"]
    rango = f"{plano['inicio']:05.2f} – {plano['fin']:05.2f} s   ·   {dur:.1f} s".replace(".", ",")
    if plano["id"] == TL["planos"][-1]["id"]:
        # Plano de producto: placa compacta en la franja central que deja libre la pantalla final.
        d.rounded_rectangle((300, 870, W - 300, 1230), radius=36, outline=(90, 74, 60), width=3)
        d.text((W / 2, 990), plano["id"], font=f("InterDisplay-SemiBold.otf", 96), fill=crema, anchor="ms")
        d.text((W / 2, 1050), rango, font=f("Inter-Medium.otf", 30), fill=tenue, anchor="ms")
        d.text((W / 2, 1110), "figura impresa aquí", font=f("Inter-Regular.otf", 34), fill=crema, anchor="ms")
        d.text((W / 2, 1180), "PENDIENTE", font=f("Inter-SemiBold.otf", 32), fill=(214, 150, 60), anchor="ms")
        img.save(ruta)
        return
    d.rounded_rectangle((90, 600, W - 90, 1250), radius=36, outline=(90, 74, 60), width=3)
    d.text((W / 2, 730), f"PLANO {plano['id']}", font=f("InterDisplay-SemiBold.otf", 104),
           fill=crema, anchor="ms")
    d.text((W / 2, 800), rango, font=f("Inter-Medium.otf", 38), fill=tenue, anchor="ms")
    y = 890
    for linea in textwrap.wrap(plano["titulo"], 30):
        d.text((W / 2, y), linea, font=f("Inter-Regular.otf", 44), fill=crema, anchor="ms")
        y += 60
    d.text((W / 2, y + 30), "Refs: " + " · ".join(plano["refs"]), font=f("Inter-Regular.otf", 32),
           fill=tenue, anchor="ms")
    etiqueta = "PENDIENTE · generar en Higgsfield"
    fe = f("Inter-SemiBold.otf", 34)
    ancho = fe.getlength(etiqueta) + 56
    d.rounded_rectangle((W / 2 - ancho / 2, 1150, W / 2 + ancho / 2, 1212), radius=31, fill=(214, 150, 60))
    d.text((W / 2, 1193), etiqueta, font=fe, fill=(30, 20, 10), anchor="ms")
    img.save(ruta)


# ----------------------------------------------------------------- segmentos
def asas(plano: dict) -> tuple[int, int]:
    """Fotogramas extra al inicio/fin del plano para las disolvencias."""
    entrada = salida = 0
    for t in TL["transiciones"]:
        mitad = fotogramas(t["duracion"]) // 2
        if abs(t["en"] - plano["inicio"]) < 1e-6:
            entrada = mitad
        if abs(t["en"] - plano["fin"]) < 1e-6:
            salida = mitad
    return entrada, salida


def segmento(plano: dict, crf: str, preset: str) -> tuple[Path, str]:
    a_in, a_out = asas(plano)
    n = fotogramas(plano["fin"]) - fotogramas(plano["inicio"]) + a_in + a_out
    destino = BUILD / f"seg_{plano['id']}.mp4"
    grado = GRADOS[plano.get("grado", "presente")]
    cola = (f",{grado}" if grado else "") + ",format=yuv420p"
    codif = ["-an", "-frames:v", str(n), "-c:v", "libx264", "-preset", preset, "-crf", crf,
             "-pix_fmt", "yuv420p", "-r", str(FPS), str(destino)]

    clip = buscar(CLIPS, plano["id"], EXT_VIDEO)
    imagen = buscar(CLIPS, plano["id"], EXT_IMAGEN)
    if clip:
        inicio = plano.get("entrada", 0.0) - a_in / FPS
        if inicio < 0:
            avisos.append(f"{plano['id']}: el punto de entrada no deja asa para la disolvencia; se adelanta a 0.")
            inicio = 0.0
        vel = plano.get("velocidad", 1.0)
        necesario = inicio + n / FPS * vel
        disponible = duracion_medio(clip)
        if disponible + 1e-3 < necesario:
            avisos.append(f"{plano['id']}: el clip dura {disponible:.2f} s y se necesitan {necesario:.2f} s; "
                          "se congela el último fotograma.")
        vf = (f"setpts=(PTS-STARTPTS)/{vel},"
              f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},"
              f"fps={FPS},setsar=1,tpad=stop_mode=clone:stop_duration=10{cola}")
        ejecutar(["-ss", f"{inicio:.3f}", "-i", str(clip), "-vf", vf, *codif])
        return destino, "clip"
    if imagen:
        zoom = plano.get("acercamiento", 0.05)
        vf = (f"scale={2 * W}:{2 * H}:force_original_aspect_ratio=increase:flags=lanczos,crop={2 * W}:{2 * H},"
              f"zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
              f"setsar=1{cola}")
        ejecutar(["-i", str(imagen), "-vf", vf, *codif])
        return destino, "fotograma clave"
    ruta_placa = BUILD / f"placa_{plano['id']}.png"
    placa(plano, ruta_placa)
    ejecutar(["-loop", "1", "-framerate", str(FPS), "-i", str(ruta_placa),
              "-vf", "setsar=1,format=yuv420p", *codif])
    return destino, "placa"


# ----------------------------------------------------------------- grafo final
def grafo_video(segmentos: list[Path], animatic: bool) -> tuple[list[str], list[str], str]:
    entradas: list[str] = []
    filtros: list[str] = []
    for s in segmentos:
        entradas += ["-i", str(s)]

    # Bloques separados por disolvencias.
    cortes = {round(t["en"], 3): t for t in TL["transiciones"]}
    bloques: list[list[int]] = [[]]
    trans_bloques = []
    for i, p in enumerate(TL["planos"]):
        if i and round(p["inicio"], 3) in cortes:
            bloques.append([])
            trans_bloques.append(cortes[round(p["inicio"], 3)])
        bloques[-1].append(i)

    longitudes = []
    for b, idx in enumerate(bloques):
        n = 0
        for i in idx:
            a_in, a_out = asas(TL["planos"][i])
            p = TL["planos"][i]
            n += fotogramas(p["fin"]) - fotogramas(p["inicio"]) + a_in + a_out
        longitudes.append(n / FPS)
        pads = "".join(f"[{i}:v]" for i in idx)
        filtros.append(f"{pads}concat=n={len(idx)}:v=1:a=0,settb=AVTB,fps={FPS}[b{b}]")

    actual, acumulado = "b0", longitudes[0]
    for k, t in enumerate(trans_bloques, 1):
        d = fotogramas(t["duracion"]) / FPS
        filtros.append(f"[{actual}][b{k}]xfade=transition=fade:duration={d:.4f}:offset={acumulado - d:.4f}[x{k}]")
        actual, acumulado = f"x{k}", acumulado + longitudes[k] - d

    # Capas gráficas (PNG a pantalla completa).
    capas = []
    for t in TL["textos"]:
        capas.append((t["id"], t["inicio"], t["fin"], 0.45, 0))
    for s in TL["subtitulos"]:
        if s.get("quemado") is not False:
            capas.append((s["id"], s["inicio"], s["fin"], 0.15, 0))
    for c in TL["pantalla_final"]["capas"]:
        capas.append((c["id"], c["inicio"], DUR + 0.5, c["fundido"], c.get("subida", 0)))

    n_ent = len(segmentos)
    for k, (nombre, ini, fin, fundido, subida) in enumerate(capas):
        png = GRAF / f"{nombre}.png"
        dur = fin - ini
        entradas += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.3f}", "-i", str(png)]
        fades = f"fade=t=in:st=0:d={fundido}:alpha=1"
        if fin < DUR:
            fades += f",fade=t=out:st={dur - fundido:.3f}:d={fundido}:alpha=1"
        filtros.append(f"[{n_ent + k}:v]format=rgba,{fades},setpts=PTS-STARTPTS+{ini}/TB[g{k}]")
        y = f"'{subida}*pow(max(0,1-(t-{ini})/{fundido}),2)'" if subida else "0"
        filtros.append(f"[{actual}][g{k}]overlay=x=0:y={y}:eval=frame:eof_action=pass[v{k}]")
        actual = f"v{k}"

    if animatic:
        fuente = FUENTES / "Inter-Medium.otf"
        filtros.append(
            f"[{actual}]drawtext=fontfile={fuente}:text='%{{pts\\:hms}}':x=48:y=150:fontsize=30:"
            f"fontcolor=white@0.85:box=1:boxcolor=black@0.45:boxborderw=12,"
            f"drawtext=fontfile={fuente}:text='ANIMATIC · sin material generado':x=w-tw-48:y=150:"
            f"fontsize=30:fontcolor=white@0.85:box=1:boxcolor=0xB4501E@0.75:boxborderw=12[vfin]")
    else:
        filtros.append(f"[{actual}]null[vfin]")
    filtros.append(f"[vfin]trim=end_frame={TOTAL_FOTOGRAMAS},format=yuv420p[vout]")
    return entradas, filtros, n_ent + len(capas)


def grafo_audio(indice_inicial: int) -> tuple[list[str], list[str], list[str]]:
    a = TL["audio"]
    entradas, filtros, presentes = [], [], []
    i = indice_inicial
    fmt = "aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo"

    voces = []
    for v in TL["locucion"]:
        ruta = buscar(RAIZ / "08_audio" / "vo", v["id"], EXT_AUDIO)
        if not ruta:
            avisos.append(f"Falta locución {v['id']} (08_audio/vo/{v['id']}.wav): «{v['texto']}»")
            continue
        largo, hueco = duracion_medio(ruta), v["fin"] - v["inicio"]
        if largo > hueco + 0.35:
            avisos.append(f"{v['id']} dura {largo:.2f} s; su hueco es {hueco:.2f} s. Ajusta ritmo o tiempos.")
        ms = int(v["inicio"] * 1000)
        entradas += ["-i", str(ruta)]
        filtros.append(f"[{i}:a]{fmt},volume={a['locucion_ganancia_db']}dB,adelay={ms}|{ms}[vo{len(voces)}]")
        voces.append(f"[vo{len(voces)}]")
        i += 1
    if voces:
        # La llave del compresor se rellena hasta el final: si no, sidechaincompress
        # termina con la última frase y corta la música antes de la marca.
        filtros.append(f"{''.join(voces)}amix=inputs={len(voces)}:normalize=0,asplit=2[voz][llave0]")
        filtros.append(f"[llave0]apad=whole_dur={DUR}[llave]")
        presentes.append("[voz]")

    m = a["musica"]
    ruta = buscar(RAIZ / "08_audio", Path(m["archivo"]).stem, EXT_AUDIO)
    if ruta:
        entradas += ["-i", str(ruta)]
        f_out = m["fundido_salida"]
        filtros.append(f"[{i}:a]{fmt},volume={m['ganancia_db']}dB,atrim=0:{DUR},"
                       f"afade=t=out:st={DUR - f_out}:d={f_out}[mus]")
        if voces:
            filtros.append("[mus][llave]sidechaincompress=threshold=0.035:ratio=5:attack=15:"
                           "release=450:makeup=1[musd]")
            presentes.append("[musd]")
        else:
            presentes.append("[mus]")
        i += 1
    else:
        avisos.append("Falta música (08_audio/musica.wav).")
        if voces:
            filtros.append("[llave]anullsink")

    sfx = []
    for e in a["efectos"]:
        ruta = buscar(RAIZ / "08_audio" / "sfx", Path(e["archivo"]).stem, EXT_AUDIO)
        if not ruta:
            avisos.append(f"Falta efecto {e['archivo']}.")
            continue
        ms = int(e["inicio"] * 1000)
        entradas += ["-i", str(ruta)]
        filtros.append(f"[{i}:a]{fmt},volume={e['ganancia_db']}dB,adelay={ms}|{ms}[sfx{len(sfx)}]")
        sfx.append(f"[sfx{len(sfx)}]")
        i += 1
    presentes += sfx

    if presentes:
        mezcla = (f"{''.join(presentes)}amix=inputs={len(presentes)}:normalize=0," if len(presentes) > 1
                  else f"{presentes[0]}anull,")
        filtros.append(f"{mezcla}apad=whole_dur={DUR},atrim=0:{DUR}[premezcla]")
    return entradas, filtros, presentes


def mezclar_audio() -> tuple[Path | None, list[str]]:
    """Mezcla el audio a WAV y lo normaliza en dos pasadas (medición + corrección lineal)."""
    entradas, filtros, presentes = grafo_audio(0)
    if not presentes:
        return None, presentes
    a = TL["audio"]
    premezcla, final = BUILD / "premezcla.wav", BUILD / "mezcla.wav"
    grafo = BUILD / "grafo_audio.txt"
    grafo.write_text(";\n".join(filtros), encoding="utf-8")
    ejecutar([*entradas, "-filter_complex_script", str(grafo), "-map", "[premezcla]",
              "-c:a", "pcm_s24le", "-ar", "48000", str(premezcla)])
    objetivo = f"I={a['sonoridad_lufs']}:TP={a['pico_real_dbtp']}:LRA=11"
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(premezcla), "-af",
                        f"loudnorm={objetivo}:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    medido = (f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
              f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    ejecutar(["-i", str(premezcla), "-af", f"loudnorm={objetivo}:{medido},aresample=48000",
              "-c:a", "pcm_s24le", "-t", f"{DUR}", str(final)])
    return final, presentes


# ----------------------------------------------------------------- control de calidad
def hoja_contactos(video: Path, destino: Path) -> None:
    miniaturas = []
    for p in TL["planos"]:
        t = (p["inicio"] + p["fin"]) / 2
        tmp = BUILD / f"qc_{p['id']}.png"
        ejecutar(["-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-vf", "scale=270:480", str(tmp)])
        miniaturas.append((p["id"], tmp))
    col, fila = 6, -(-len(miniaturas) // 6)
    hoja = Image.new("RGB", (col * 280 + 10, fila * 530 + 10), (18, 14, 11))
    d = ImageDraw.Draw(hoja)
    f = ImageFont.truetype(str(FUENTES / "Inter-SemiBold.otf"), 24)
    for k, (pid, ruta) in enumerate(miniaturas):
        x, y = 10 + (k % col) * 280, 10 + (k // col) * 530
        hoja.paste(Image.open(ruta), (x, y))
        d.text((x + 4, y + 488), pid, font=f, fill=(255, 246, 232))
    hoja.save(destino, quality=90)


def informe(final: Path, origenes: dict, presentes: list[str]) -> str:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate:format=duration",
                        "-of", "json", str(final)], capture_output=True, text=True)
    info = json.loads(r.stdout)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    au = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"]["duration"])
    lineas = [
        f"Archivo: {final.relative_to(RAIZ)}",
        f"Video: {v['codec_name']} {v['width']}x{v['height']} @ {v['r_frame_rate']}  "
        f"{'OK' if (v['width'], v['height']) == (W, H) else 'REVISAR'}",
        f"Audio: {au['codec_name']} {au['sample_rate']} Hz" if au else "Audio: ninguno",
        f"Duración: {dur:.3f} s  {'OK' if abs(dur - DUR) < 0.05 else 'REVISAR'}",
        f"Pistas de audio mezcladas: {len(presentes)} {'(silencio)' if not presentes else ''}",
        "",
        "Origen de cada plano:",
    ]
    lineas += [f"  {pid:<5} {tipo}" for pid, tipo in origenes.items()]
    if avisos:
        lineas += ["", "Avisos:"] + [f"  - {a}" for a in avisos]
    return "\n".join(lineas)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--borrador", action="store_true", help="codificación rápida")
    args = ap.parse_args()
    crf_seg, preset = ("20", "veryfast") if args.borrador else ("14", "medium")

    BUILD.mkdir(exist_ok=True)
    SALIDA.mkdir(exist_ok=True)
    if not (GRAF / "EC1_logo.png").exists():
        sys.path.insert(0, str(AQUI))
        import graficos
        graficos.main()

    origenes, segmentos = {}, []
    for p in TL["planos"]:
        ruta, tipo = segmento(p, crf_seg, preset)
        origenes[p["id"]] = tipo
        segmentos.append(ruta)
        print(f"  {p['id']:<5} {tipo}")

    # ANIMATIC: falta material (placas). VERSION_REDUCIDA: todo es material generado,
    # pero algún plano es un fotograma clave con acercamiento en lugar de un clip.
    animatic = any(t == "placa" for t in origenes.values())
    reducida = not animatic and any(t != "clip" for t in origenes.values())
    ent_v, fil_v, siguiente = grafo_video(segmentos, animatic)
    mezcla, presentes = mezclar_audio()
    if mezcla:
        ent_a, mapa_audio = ["-i", str(mezcla)], f"{siguiente}:a"
    else:
        ent_a, mapa_audio = ["-f", "lavfi", "-t", f"{DUR}", "-i", "anullsrc=r=48000:cl=stereo"], f"{siguiente}:a"

    final = RAIZ / TL["salida"]
    if animatic:
        final = SALIDA / ("ANIMATIC_" + final.name)
    elif reducida:
        final = SALIDA / ("VERSION_REDUCIDA_" + final.name)
    grafo = BUILD / "grafo.txt"
    grafo.write_text(";\n".join(fil_v), encoding="utf-8")
    ejecutar([*ent_v, *ent_a, "-filter_complex_script", str(grafo),
              "-map", "[vout]", "-map", mapa_audio,
              "-c:v", "libx264", "-preset", "veryfast" if args.borrador else "slow",
              "-crf", "20" if args.borrador else "18", "-profile:v", "high", "-level", "4.2",
              "-pix_fmt", "yuv420p", "-r", str(FPS),
              "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
              "-t", f"{DUR}", "-movflags", "+faststart", str(final)])

    hoja_contactos(final, SALIDA / "hoja_de_contactos.jpg")
    ejecutar(["-ss", f"{DUR - 0.4}", "-i", str(final), "-frames:v", "1",
              str(SALIDA / "fotograma_pantalla_final.png")])
    texto = informe(final, origenes, presentes)
    (SALIDA / "informe_qc.txt").write_text(texto + "\n", encoding="utf-8")
    print("\n" + texto)


if __name__ == "__main__":
    main()
