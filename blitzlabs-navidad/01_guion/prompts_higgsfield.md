# Prompts de producción para Higgsfield

Estos prompts están listos para pegar. Van en inglés porque los modelos de imagen y video responden mejor en ese idioma; las notas de dirección están en español.

**Orden de trabajo (no te lo saltes):**
1. **Referencias maestras**: personajes, muñecas, objetos y locaciones. Apruébalas antes de seguir.
2. **Fotogramas clave**: un fotograma por plano, generado con sus referencias adjuntas.
3. **Animación**: de imagen a video, a partir de cada fotograma clave aprobado, con una sola acción por clip.
4. Descarga y renombra los archivos según la tabla de cada apartado y ejecuta `python3 05_montaje/montar.py`.

**Reglas generales:**
- Formato **9:16** en todo y la máxima resolución disponible. Genera **5 s** por clip; el montaje usa unos 2,5 s y guarda el resto como asas para las disolvencias.
- **Silencia o descarta el audio** de los clips generados. El sonido se mezcla aparte.
- **Nunca pidas el logo, textos ni subtítulos al generador.** Todo eso se añade en el montaje.
- Adjunta siempre las referencias indicadas en «Refs». Si la herramienta permite entrenar o fijar un personaje (ID de personaje), crea uno para el padre y otro para la hija, a partir de las variaciones aprobadas de REF-01 y REF-03.
- Si un clip deforma manos, rostro u objeto, **vuelve a generarlo**; no lo arregles en el montaje.

---

## 0 · Bloques reutilizables

Copia el bloque completo, tal cual, en cada prompt donde aparezca su etiqueta. Repetir siempre el mismo texto es lo que mantiene la consistencia.

**[STYLE]**
> Cinematic photorealism, intimate Christmas atmosphere, cozy family home, warm practical light around 2700–3000 K, Christmas tree softly out of focus in the background, natural wood, deep green and cream tones, natural skin texture with pores and fine lines, gentle shallow depth of field, 35 mm film look with subtle grain, vertical 9:16 composition. No text, no letters, no logos, no watermark, no captions.

**[NEGATIVE]** (en el campo negativo, si existe; si no, al final como «Avoid: …»)
> text, letters, logo, watermark, subtitles, extra fingers, fused or deformed hands, face morphing, identity drift, age drift, glasses disappearing or changing, figurine changing pose, figurine limbs moving, extra limbs on the figurine, cartoon, anime, 3D render look, plastic skin, oversaturated colors, heavy lens flare, sparkles, glitter particles, fast or dramatic camera moves, whip pans, flicker

**[FATHER-47]**
> a 47-year-old Caucasian man, medium build, relaxed and kind facial features, short brown hair with some gray at the temples, clean-shaven, hazel-brown eyes, warm natural expression, real skin with fine lines around the eyes; wearing a plain dark forest-green crew-neck knit sweater, simple and neat clothes, no jewelry, no watch; an ordinary real person, not a fashion model

**[FATHER-30]**
> the same man seventeen years younger, about 30 years old: identical face shape, nose, eyebrows, ears and hazel-brown eyes; fuller short brown hair with no gray, slightly fuller cheeks, clean-shaven; wearing a rust-brown knit sweater over a light shirt, late-2000s casual style

**[DAUGHTER-23]**
> a 23-year-old Caucasian woman, shoulder-length brown hair with soft natural waves, thin gold-tone metal-frame glasses with rounded-rectangular clear lenses, hazel-brown eyes, natural features, minimal makeup, wearing a cream cable-knit crew-neck sweater; restrained, authentic expressiveness

**[DAUGHTER-6]**
> the same girl at six years old: brown hair of the same shade, chin-to-shoulder length, with a small pale-blue hair clip; hazel-brown eyes; soft round child face with a clearly recognizable family resemblance (same nose, eyebrows and smile as the adult daughter); no glasses; wearing a cream knit cardigan over a pale pink top

**[BALLERINA-ORIGINAL]**
> a decorative ballerina figurine about 18 cm tall (roughly the length of an adult hand) standing on a round ivory base; stylized ballerina with a delicate doll face, fair skin, painted eyes with tiny painted lashes, soft pink lips; blonde hair gathered in an updo with small curls and tiny very-pale-blue ornaments; turquoise bodice; short, wide, airy tutu in layered turquoise and light-blue tulle with a small white bow at the front of the waist; turquoise ballet slippers. Fixed pose: right arm raised in a rounded curve above the head, left arm extended to the side and slightly downward, left leg straight as the supporting leg, right leg crossed in front with the toe resting on the base; the figure is permanently attached to its base. Satin-finish surfaces with a soft sheen; the tutu is real textile tulle.

**[BALLERINA-PRINTED]**
> a faithful recreation of that same ballerina figurine — identical pose, proportions, face and color palette, about 18 cm tall on a round ivory base — manufactured by FDM 3D printing in matte PLA/PETG and assembled from separate colored parts: ivory base; light-peach matte body and face; blonde-yellow hair piece with small curls and tiny very-pale-blue ornaments; turquoise bodice; the tutu interpreted as rigid layered plastic ruffles in turquoise and light blue whose sculpted relief evokes the folds of tulle; a small separate white bow at the waist; turquoise slippers. Eyes, lashes and lips finely hand-painted after printing. Matte surfaces, fine horizontal layer lines (about 0.1 mm) visible in close-ups, subtle seams where parts join. Not porcelain, not real fabric, not glossy injection-molded plastic.

**[GIFT-BOX]**
> an open square gift box about 25 × 25 × 25 cm in cream kraft cardboard, lid set aside, deep-green satin ribbon, filled with soft white tissue paper; no logos, no text

---

## 1 · Referencias maestras

Genera primero la «imagen héroe» de cada referencia. Después, con esa imagen como referencia, genera las variaciones de la columna «Variaciones». Guarda las aprobadas en `06_referencias/` con el nombre indicado.

| ID | Archivo | Variaciones necesarias |
|---|---|---|
| REF-01 | `REF-01_padre_47_*.png` | frente, 3/4, perfil, medio cuerpo, manos en primer plano |
| REF-02 | `REF-02_padre_30_*.png` | frente, 3/4, medio cuerpo |
| REF-03 | `REF-03_hija_23_*.png` | frente, 3/4, perfil, medio cuerpo, manos |
| REF-04 | `REF-04_hija_6_*.png` | frente, 3/4, medio cuerpo |
| REF-05 | `REF-05_bailarina_original_*.png` | frente, 3/4 izq., 3/4 der., espalda, macro del rostro, macro del tutú |
| REF-06 | `REF-06_bailarina_impresa_*.png` | las mismas vistas que REF-05 + macro de las líneas de capa |
| REF-07 | `REF-07_bailarina_rota.png` | una vista |
| REF-08 | `REF-08_foto_antigua.png` | contenido de la foto (plano) + la foto como objeto físico |
| REF-09 | `REF-09_boceto.png` | una vista cenital |
| REF-10 | `REF-10_caja_regalo.png` | vacía + con la bailarina impresa en papel de seda |
| LOC-01…04 | `LOC-0X_*.png` | una vista amplia + una vista en el eje de cada plano |

**REF-01 · Padre, 47 años** — imagen héroe
> Photorealistic portrait, vertical 9:16, head and shoulders, neutral warm interior background slightly out of focus, soft window light from the left. [FATHER-47]. He looks at the camera with a calm, warm, natural expression. [STYLE]

Variaciones (con REF-01 adjunta):
> Same man, same sweater, same lighting — {three-quarter view facing left | full profile facing left | waist-up seated at a wooden table | close-up of both hands resting on a wooden table, natural male hands with clean short nails}. Keep identity exactly.

**REF-02 · Padre, unos 30 años** (con REF-01 adjunta)
> Photorealistic portrait, vertical 9:16, head and shoulders, warm living-room light. [FATHER-30]. Keep the identity of the reference person exactly, only younger. [STYLE]

**REF-03 · Hija, 23 años** — imagen héroe
> Photorealistic portrait, vertical 9:16, head and shoulders, warm interior background slightly out of focus, soft window light. [DAUGHTER-23]. Gentle, natural expression, looking slightly off camera. [STYLE]

Variaciones (con REF-03 adjunta): las mismas que el padre, con manos femeninas naturales que sostienen una hoja de papel.

**REF-04 · Hija, 6 años** (con REF-03 y REF-01 adjuntas)
> Photorealistic portrait, vertical 9:16, a child sitting on a rug in a warm living room. [DAUGHTER-6]. She is the adult woman in the reference as a child, with a visible family resemblance to the man in the second reference. Natural, joyful expression. [STYLE]

**REF-05 · Bailarina original** — imagen héroe
> Studio product photograph, vertical 9:16, front view, the whole figurine in frame on a seamless warm-gray background, soft key light and gentle rim light. [BALLERINA-ORIGINAL]. Sharp focus across the whole figure. No text.

Variaciones (con REF-05 adjunta):
> The exact same figurine, identical pose and colors, {three-quarter left view | three-quarter right view | back view | macro of the face and hair | macro of the tulle tutu and white bow}.

**REF-06 · Bailarina recreada por BlitzLabs** (con REF-05 adjunta)
> Studio product photograph, vertical 9:16, front view, whole figurine in frame on a seamless warm-gray background, soft key light. [BALLERINA-PRINTED]. It must be instantly recognizable as the figurine in the reference image, but clearly a 3D-printed matte plastic object. Sharp focus. No text.

Variaciones: las mismas que REF-05, más:
> Extreme macro of the printed tutu ruffles and bodice showing fine horizontal layer lines and a subtle seam between the turquoise and light-blue parts, matte PLA texture.

**REF-07 · Bailarina original rota** (edición de REF-05)
> The exact same original figurine standing on its ivory base on a warm wooden table; its raised right arm has broken off cleanly at the shoulder and lies on the table beside the base; everything else intact; no shards, no glue, no dust. Soft warm nostalgic light, vertical 9:16.

**REF-08 · Fotografía antigua** (con REF-02, REF-04, REF-05 y LOC-02 adjuntas)

Contenido de la foto:
> An amateur family snapshot from around 2009, vertical: by a Christmas tree in a living room, [FATHER-30] kneels and hands [BALLERINA-ORIGINAL] to [DAUGHTER-6], who looks at it with delight; the figurine is clearly visible in the center between them. Slightly faded warm colors, soft focus, mild compact-camera grain, small flash falloff.

La foto como objeto:
> The same image as a physical 10 × 15 cm glossy photo print, slightly faded, with gentle corner wear, photographed on a wooden table in warm light; the printed image must match the reference exactly.

**REF-09 · Boceto** (con REF-05 adjunta)
> Top-down view of an open cream sketchbook page on a wooden table: a pencil and fine-liner sketch of the ballerina figurine from the reference, in the exact pose, front view, light construction lines, a small side view of the round base, a few arrows and only the handwritten measurement "18 cm"; a few soft turquoise colored-pencil touches on the tutu. Warm desk-lamp light, vertical 9:16.

**REF-10 · Caja de regalo** (con REF-06 adjunta para la segunda versión)
> Product photograph on a wooden table, vertical 9:16: [GIFT-BOX]. {empty | with the 3D-printed ballerina from the reference nestled upright in the tissue paper, front view}. [STYLE]

**LOC-01 · Sala, presente**
> Cozy family living room at night, vertical 9:16: Christmas tree with warm white lights softly out of focus, wooden floor and furniture, a low wooden side table next to a cream sofa with a deep-green throw and cushions, warm table lamp, a few understated ornaments in gold, deep green and cream; lived-in but tidy; no screens, no text, no brands. Empty of people. [STYLE]

**LOC-02 · Sala, recuerdo (unos 17 años antes)** (con LOC-01 adjunta)
> The same family living room seventeen years earlier, around 2009: similar layout, older beige fabric sofa, a different patterned rug, Christmas tree with warm late-2000s lights, some wrapping paper on the floor; warm nostalgic evening light, slight haze. Empty of people. [STYLE]

**LOC-03 · Mesa de trabajo del padre** (con LOC-01 adjunta)
> A wooden worktable in a corner of the same family home at night, vertical 9:16: warm desk lamp, an open sketchbook, a pencil, a ceramic mug; Christmas tree lights as faint bokeh in the far background. Empty of people. [STYLE]

**LOC-04 · Taller de BlitzLabs**
> A small, clean, real 3D-printing workshop, vertical 9:16: wooden workbench, pegboard with neatly hung hand tools, two unbranded desktop FDM 3D printers that are mechanically coherent (open-frame design, visible gantry, belts, hotend with cooling fan, textured PEI build plate), filament spools in turquoise, light blue, ivory, blonde-yellow and skin tone, a cutting mat, calipers, flush cutters, tweezers, small sanding sticks; soft daylight from a window plus a warm task lamp; no logos, no text, no screens showing text. Empty of people. Cinematic photorealism, natural colors, gentle depth of field.

---

## 2 · Planos: fotograma clave y animación

Para cada plano: genera el **fotograma clave** con las refs adjuntas, apruébalo según `control_calidad.md` y anímalo con el **prompt de movimiento**. Descarga el video como `07_clips/<ID>.mp4`. Si quieres previsualizar antes de animar, guarda también el fotograma como `07_clips/<ID>.png`: el montaje lo usa con un acercamiento lento hasta que exista el `.mp4`.

### S01A · 0,0–2,6 s · La foto en sus manos
Refs: REF-03 (manos), REF-08 (objeto), LOC-01
**Fotograma clave**
> Extreme close-up, vertical 9:16. The hands of [DAUGHTER-23] — cream cable-knit sleeve cuffs visible — hold the old glossy photo print from the reference at chest height; the photo fills the center of the frame and its content is clearly readable: the young father handing the ballerina figurine to the little girl by a Christmas tree. Her right thumb rests on the edge of the photo. Warm lamplight, Christmas tree bokeh behind. [STYLE]

**Movimiento**
> Her thumb slowly and gently strokes along the edge of the photo once. The hands otherwise stay steady. Locked-off camera with a barely perceptible drift. The photo content remains unchanged and undistorted. No other movement.

Si la imagen dentro de la foto se deforma, sustitúyela en el fotograma clave con edición por referencia (REF-08) antes de animar.

### S01B · 2,6–5,0 s · Su rostro
Refs: REF-03, REF-08, LOC-01
**Fotograma clave**
> Close-up, vertical 9:16. [DAUGHTER-23] looks down at the old photo she holds near the bottom of the frame; the photo edge is in the soft-focus foreground; her face with the thin gold-frame glasses is in the upper half of the frame. Warm lamplight on her face, tree bokeh. [STYLE]

**Movimiento**
> Slow rack focus from the photo in the foreground to her face. She keeps looking at the photo with a soft, nostalgic half-smile and blinks once. Static camera. Glasses stay identical.

### S02A · 5,0–7,4 s · Recuerdo: la ilusión
Refs: REF-04, REF-05, LOC-02
**Fotograma clave**
> Medium close-up, vertical 9:16, a warm memory. [DAUGHTER-6] sits on the rug by the Christmas tree in the living room from the reference, holding [BALLERINA-ORIGINAL] in both hands at eye level, looking at it with wide-eyed delight; wrapping paper around her. Soft warm nostalgic light, slight bloom. [STYLE]

**Movimiento**
> The girl slowly brings the figurine a little closer and her smile grows. Small natural movements only. Very slow push-in. The figurine is a rigid solid object: its arms, legs and tutu never move or change.

### S02B · 7,4–10,0 s · Lo que se perdió
Refs: REF-07, REF-02, REF-04, LOC-02
**Fotograma clave**
> Detail shot, vertical 9:16, a warm memory. In the sharp foreground, lower half of the frame: the broken original figurine from the reference standing on its ivory base on a wooden table, its raised arm lying beside the base. In the soft-focus background, upper half: [DAUGHTER-6] standing by the table looking down, sad, and [FATHER-30] standing beside her. [STYLE]

**Movimiento**
> In the background, the young father gently places his hand on the girl's shoulder to comfort her. The foreground figurine and the broken arm stay perfectly still and sharp. Static camera.

No muestres cómo se rompe.

### S03A · 10,0–12,8 s · La intención del padre
Refs: REF-01, REF-08, REF-09, LOC-03
**Fotograma clave**
> Medium close-up, vertical 9:16. [FATHER-47] sits at the wooden worktable at night, looking down at the old photo from the reference, which lies next to the open sketchbook with the ballerina sketch; warm desk lamp light on his face; nostalgic expression. [STYLE]

**Movimiento**
> His nostalgic expression slowly turns into calm, quiet determination: he exhales softly, his jaw settles and a faint resolute smile appears as he lifts his gaze slightly. Minimal movement. Static camera.

### S03B · 12,8–15,0 s · El hilo de luz dorada
Refs: REF-09, REF-08, LOC-03
**Fotograma clave**
> Top-down insert, vertical 9:16: the pencil sketch of the ballerina from the reference on cream paper on the wooden worktable; the corner of the old photo visible at the edge of the frame; warm lamplight. [STYLE]

**Movimiento**
> A delicate, thin thread of warm golden light slowly traces the outline of the sketched ballerina from the base upward, leaving a faint glow that softly fades. Subtle and elegant: no sparkles, no particle bursts. The paper and drawing stay otherwise unchanged. Static camera.

### S04A · 15,0–17,4 s · La impresora
Refs: REF-06 (macro del tutú), LOC-04
**Fotograma clave**
> Macro close-up, vertical 9:16, in the workshop from the reference: the nozzle of a desktop FDM 3D printer (hotend with cooling fan) depositing turquoise matte PLA onto a partially printed part — a single layered ruffle segment of the ballerina's tutu, about 40 % complete — on a textured PEI build plate; fine layer lines visible; no complete figurine on the bed. Soft daylight plus warm lamp, shallow depth of field. Cinematic photorealism, no text, no logos.

**Movimiento**
> The print head moves smoothly back and forth along the edge of the part, extruding a thin turquoise line; the part grows by a barely perceptible layer. Mechanically coherent, steady motion; no morphing; no complete figure appearing. Static camera or a very slow lateral slide.

### S04B · 17,4–20,0 s · Ensamblado y revisión
Refs: REF-06, LOC-04
**Fotograma clave**
> Close-up, vertical 9:16, workshop bench: the hands and forearms of a maker (dark-gray work apron, sleeves rolled up, face not visible) — one hand holds the small white printed bow with fine tweezers just above the waist of the nearly finished [BALLERINA-PRINTED], which stands on its ivory base on a cutting mat; calipers and a few spare printed parts nearby. Warm task lamp. Cinematic photorealism, no text, no logos.

**Movimiento**
> The maker carefully places the small white bow onto the figurine's waist, then the hand withdraws. The figurine stays rigid; its pose, colors and matte printed finish stay identical. Static camera.

Alternativa, si el moño se deforma: las manos giran un cuarto de vuelta la base para revisar la figura terminada.

### S05 · 20,0–25,0 s · La entrega
Refs: REF-01, REF-03, REF-06, REF-10 (con la bailarina), LOC-01
**Fotograma clave**
> Medium shot, vertical 9:16, living room by the Christmas tree. [DAUGHTER-23] sits on the cream sofa; [FATHER-47] leans in from the right, holding the open gift box from the reference toward her at chest height; inside, nestled in white tissue paper, the 3D-printed ballerina from the reference is visible from the front. She looks down at the box. [STYLE]

**Movimiento**
> The father slowly brings the open box a little closer to her; the tissue paper moves slightly. She looks at the figurine and begins to recognize it: her breath pauses and her eyes widen slightly. Slow, gentle dolly-in toward her face. The figurine stays identical and rigid in the box.

### S06A · 25,0–27,6 s · El reconocimiento
Refs: REF-03, REF-01, REF-06, LOC-01
**Fotograma clave**
> Close-up, vertical 9:16. [DAUGHTER-23] looks down at the 3D-printed ballerina in the open box at the bottom edge of the frame; her father is out of focus at the right edge. Warm light, tree bokeh. [STYLE]

**Movimiento**
> She lifts her gaze from the figurine to her father and smiles with contained emotion; her eyes are slightly moist; no tears running. Static camera with a gentle drift.

### S06B · 27,6–30,0 s · El abrazo
Refs: REF-01, REF-03, REF-10, LOC-01
**Fotograma clave**
> Medium shot, vertical 9:16, living room by the tree. [FATHER-47] and [DAUGHTER-23] share a natural, warm hug; her face is visible over his shoulder, eyes closed, gently smiling; the open gift box with the figurine rests securely on the low wooden side table in the foreground left. [STYLE]

**Movimiento**
> They hold the hug; her hand gently tightens on his back; a slight sway. The box stays perfectly still and secure on the table. Static camera.

Empieza el clip ya en el abrazo; no pidas el movimiento de acercarse.

### S07 · 30,0–35,0 s · Producto y marca
Refs: REF-06, REF-10, REF-01, REF-03, LOC-01
**Fotograma clave**
> Product shot, vertical 9:16: the 3D-printed ballerina from the reference stands on the low wooden side table in a front three-quarter view, beside the open gift box with tissue paper. The figurine is centered horizontally and occupies the band between about 45 % and 65 % of the frame height. In the background, softly out of focus near the Christmas tree, the father and daughter stand together (recognizable by the dark-green and cream sweaters). The upper 40 % of the frame (tree bokeh) and the lower 30 % (table surface) stay visually calm and uncluttered. [STYLE]

**Movimiento**
> Very slow, smooth push-in toward the figurine; the couple in the background moves only subtly; the last second is completely still. The figurine remains identical.

La parte superior y la inferior del cuadro deben quedar limpias, porque ahí van el logo, el lema y la llamada a la acción.
