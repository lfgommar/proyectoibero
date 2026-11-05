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
| **Referencias** (5 base: padre, hija, bailarina original, bailarina impresa, foto antigua) | ✅ Generadas en Higgsfield · `06_referencias/` |
| **Fotogramas clave** de los 12 planos | ✅ Generados en Higgsfield · `07_clips/<ID>.jpg` |
| **Clips animados** | 🟡 3 de 12 (S05, S06A, S07) · `07_clips/<ID>.mp4` |
| **Locución** es-MX (6 líneas) | 🟡 Generada (voz «Marisol»); falta confirmar el acento · `08_audio/vo/` |
| **Música** instrumental 36 s | ✅ Generada (ElevenLabs Music v2) · `08_audio/musica.wav` |
| **Efectos de sonido** | 🟡 4 de 7 · `08_audio/sfx/` |
| **MP4 versión reducida** | ✅ `09_salida/VERSION_REDUCIDA_BlitzLabs_Navidad_35s_1080x1920.mp4` |
| **MP4 final** `09_salida/BlitzLabs_Navidad_35s_1080x1920.mp4` | ⛔ Requiere los 12 clips animados |

La versión reducida se hizo con los 60 créditos del plan gratuito. Los 9 planos sin clip se animan en el montaje con un acercamiento lento sobre el fotograma clave. Los modelos, créditos, IDs de trabajo y avisos de calidad están en [`01_guion/registro_generacion.md`](01_guion/registro_generacion.md).

## Para terminar

1. La CLI de Higgsfield (`npm install -g @higgsfield/cli`, después `higgsfield auth login`) es la que genera. El conector MCP solo consulta. En una nube de Claude Code, la red del entorno debe permitir los dominios de Higgsfield y `d8j0ntlcm91z4.cloudfront.net`, que es de donde se descargan los resultados.
2. Anima los planos que faltan a partir de sus fotogramas clave (`07_clips/<ID>.jpg`), con los prompts de movimiento de `01_guion/prompts_higgsfield.md`. En el plan gratuito, Cinema Studio Video v2 funciona; Seedance 2.0 requiere el plan Basic.
3. Escucha la locución y, si el acento no es de México, vuelve a generarla o grábala. Agrega los 3 efectos que faltan en `08_audio/sfx/` (los nombres están en `08_audio/LEEME.md`).
4. Ejecuta el montaje:
   ```bash
   python3 blitzlabs-navidad/05_montaje/montar.py
   ```
   Requiere `ffmpeg` y Python 3 con Pillow. Para una revisión rápida, añade `--borrador`.
5. Revisa `09_salida/hoja_de_contactos.jpg`, `09_salida/informe_qc.txt` y `01_guion/control_calidad.md`. Si falta material (placas «PENDIENTE»), la salida se llama `ANIMATIC_…`. Si todo está generado pero algún plano es un fotograma fijo, se llama `VERSION_REDUCIDA_…`. Cuando están los 12 clips, sale `BlitzLabs_Navidad_35s_1080x1920.mp4`.
6. **Antes de usarlo en publicidad:** BlitzLabs debe validar que la recreación mostrada se puede fabricar tal cual. No se publica nada automáticamente.

### Prompt para la sesión nueva

> Continúa la producción del anuncio en `blitzlabs-navidad/` con la CLI de Higgsfield. Lee `01_guion/registro_generacion.md`: anima los planos que todavía no tienen `.mp4` en `07_clips/`, a partir de sus fotogramas clave `<ID>.jpg` y con los prompts de movimiento de `01_guion/prompts_higgsfield.md`. Antes de gastar créditos, muéstrame el costo. Revisa cada clip con `01_guion/control_calidad.md` y regenera lo que falle. Genera los 3 efectos que faltan, vuelve a ejecutar `05_montaje/montar.py` y entrégame el MP4. No publiques nada.

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
