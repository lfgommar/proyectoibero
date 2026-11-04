# BlitzLabs · Anuncio navideño «De tu imaginación a sus manos» (35 s, 9:16)

Paquete de producción del anuncio. Incluye guion, prompts para Higgsfield, marca, gráficos, subtítulos y un montaje automático que produce el MP4 final en cuanto existan los clips y el audio.

## Estado

| Fase | Estado |
|---|---|
| Guion técnico, tiempos, locución y brief de audio | ✅ `01_guion/guion_tecnico.md` |
| Prompts de referencias maestras y de los 12 planos | ✅ `01_guion/prompts_higgsfield.md` |
| Lista de control de calidad | ✅ `01_guion/control_calidad.md` |
| Logo original (copia idéntica) + versión con fondo transparente (píxeles interiores sin cambios) | ✅ `02_marca/` |
| Textos de edición, subtítulos quemados y pantalla final (PNG 1080 × 1920) | ✅ `03_graficos/` |
| Subtítulos `.srt` (es-MX) | ✅ `04_subtitulos/` |
| Montaje automático: cortes, disolvencias, gradación de recuerdo, gráficos, mezcla con atenuación y −14 LUFS, control de calidad | ✅ `05_montaje/montar.py` (probado con medios sintéticos) |
| Animatic de tiempos y maquetación (placas «PENDIENTE», sin material generado) | ✅ `09_salida/ANIMATIC_BlitzLabs_Navidad_35s_1080x1920.mp4` |
| **Referencias maestras** (10 + 4 locaciones) | ⛔ Pendiente: requiere Higgsfield |
| **Fotogramas clave** de los 12 planos | ⛔ Pendiente: requiere Higgsfield |
| **Clips animados** de los 12 planos | ⛔ Pendiente: requiere Higgsfield |
| **Locución** es-MX (6 líneas) | ⛔ Pendiente |
| **Música** con licencia publicitaria (35 s) | ⛔ Pendiente |
| **Efectos de sonido** (7) | ⛔ Pendiente |
| **MP4 final** `09_salida/BlitzLabs_Navidad_35s_1080x1920.mp4` | ⛔ Se genera al ejecutar el montaje con todo lo anterior |

En la sesión donde se preparó este paquete, Higgsfield no estaba conectado como herramienta MCP. Por eso **no se generó ninguna imagen, ningún video ni ningún audio**. El animatic usa placas de texto y lleva la marca «ANIMATIC · sin material generado».

## Para terminar

1. Conecta Higgsfield en <https://claude.ai/customize/connectors> y abre una **sesión nueva**. Los conectores se cargan al iniciar la sesión.
2. Genera las referencias maestras (`06_referencias/`), luego los fotogramas clave y los clips (`07_clips/`), en el orden que indica `01_guion/prompts_higgsfield.md`.
3. Graba o genera la locución, consigue la música con licencia y los efectos, y guárdalos en `08_audio/` con los nombres de `08_audio/LEEME.md`.
4. Ejecuta el montaje:
   ```bash
   python3 blitzlabs-navidad/05_montaje/montar.py
   ```
   Requiere `ffmpeg` y Python 3 con Pillow. Para una revisión rápida, añade `--borrador`.
5. Revisa `09_salida/hoja_de_contactos.jpg`, `09_salida/informe_qc.txt` y `01_guion/control_calidad.md`. Mientras falte algún plano, la salida se llama `ANIMATIC_…`; cuando están los 12, sale `BlitzLabs_Navidad_35s_1080x1920.mp4`.
6. **Antes de usarlo en publicidad:** BlitzLabs debe validar que la recreación mostrada se puede fabricar tal cual. No se publica nada automáticamente.

### Prompt para la sesión nueva

> Continúa la producción del anuncio en `blitzlabs-navidad/` usando las herramientas de Higgsfield por MCP. Sigue `01_guion/prompts_higgsfield.md`: primero las referencias maestras (guárdalas en `06_referencias/` y muéstramelas para aprobarlas), después los fotogramas clave y los clips de los 12 planos en `07_clips/`, con sus nombres exactos. Revisa cada resultado con `01_guion/control_calidad.md` y regenera lo que falle. Si Higgsfield tiene voz o música, genera `08_audio/` según `01_guion/guion_tecnico.md`; si no, dímelo. Luego ejecuta `05_montaje/montar.py` y entrégame el MP4 final y los clips originales. No publiques nada.

## Cambiar algo

- **Tiempos, textos, subtítulos o niveles de audio:** edita `05_montaje/timeline.json`, ejecuta `python3 05_montaje/graficos.py` y vuelve a montar.
- **Tipografía o colores:** usa las constantes al inicio de `05_montaje/graficos.py`. La fuente es Inter, con licencia OFL, apta para publicidad.
- **Logo:** `05_montaje/preparar_logo.py` vuelve a generar la versión transparente a partir del original.

## Decisiones tomadas (ajustables)

- **Lateralidad de la pose:** el brazo **derecho** de la figura es el que se eleva. Es el que se rompe en el recuerdo.
- **Rasgos fijados para la consistencia:** el padre va sin barba; padre e hija tienen ojos avellana; la hija lleva lentes de armazón fino dorado; la niña usa un pasador azul pálido y un cárdigan crema, que rima con el suéter de la hija adulta.
- **Rostro de la figura impresa:** se describe con ojos y labios pintados a mano tras la impresión. Hay que confirmarlo con BlitzLabs en la validación del producto.
- **Logo en la pantalla final:** va sobre una insignia blanca circular para conservar su contraste original sobre el video. Debajo se añade el nombre «BlitzLabs» como texto aparte, que se puede quitar dejando `nombre_marca` vacío en `timeline.json`.
- **«WhatsApp · Instagram»** va solo como texto, sin íconos de terceros ni datos de contacto.
