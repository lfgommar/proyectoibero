# Registro de generación en Higgsfield (5 de noviembre de 2026)

Versión **reducida**, con los 60 créditos del plan gratuito. Todo el material visual y sonoro es generado. Hay 3 planos animados y los otros 9 son fotogramas clave a los que el montaje aplica un acercamiento lento.

Herramienta: la CLI de Higgsfield (`@higgsfield/cli` 1.2.2). El conector MCP de Higgsfield solo permite consultar (saldo, modelos, historial) y no genera.

## Créditos

| Concepto | Modelo | Cantidad | Créditos |
|---|---|---|---|
| Referencias y fotogramas clave (9:16, 2k) | Nano Banana Pro | 17 imágenes | 34 |
| Clips animados (720p, sin audio) | Cinema Studio Video v2 (`std`, género `intimate`) | S06A 4 s · S05 6 s · S07 6 s | 16 |
| Locución es-MX | Text to Speech V2 (`elevenlabs`, voz preset «Marisol») | 6 líneas | ≈ 1,2 |
| Música instrumental 36 s | ElevenLabs Music v2 | 1 | 2,31 |
| Efectos de sonido | Mirelo Text to Audio | 4 (9 s en total) | 2,25 |
| **Total** | | | **≈ 55,8** (quedan 4,24) |

Modelos que **no** están disponibles en el plan gratuito: Seedance 2.0 / 2.0 Mini (`job_minimum_basic_plan_required`). El plan gratuito permite **un solo video a la vez**.

## Estrategia de consistencia

En lugar de las 14 referencias con todas sus variaciones (que no cabían en el presupuesto), se generaron 5 referencias base, y algunos fotogramas clave sirven de referencia para los siguientes:

- REF-01 (padre), REF-03 (hija) y REF-05 (bailarina original), sin referencias.
- REF-06 (bailarina impresa) ← REF-05.
- S02A (niña con la bailarina) ← REF-03 + REF-01 + REF-05. **Funciona como referencia de la niña.**
- REF-08 (foto antigua) ← S02A + REF-01 + REF-05. **Funciona como referencia del padre joven.**
- S05 (entrega) ← REF-01 + REF-03 + REF-06. **Funciona como referencia de la sala del presente** para S06A, S06B y S07.
- S03B (boceto) ← S03A + REF-05.

Las referencias se pasaron por ID de trabajo de Higgsfield, sin volver a subir los archivos.

## Archivos e IDs de trabajo

Las imágenes se guardaron en JPEG de calidad 93 para que el repositorio no pese tanto. Los PNG originales (1536 × 2752) se pueden volver a descargar desde Higgsfield con estos IDs (`higgsfield generate get <id>`).

| Archivo | ID de trabajo | Refs usadas |
|---|---|---|
| `06_referencias/REF-01_padre_47_frente.jpg` | `2ce1f422-2907-44ea-b0d5-aa82d2b851a5` | — |
| `06_referencias/REF-03_hija_23_frente.jpg` | `32280802-33bc-459f-bad8-ce75f273d38a` | — |
| `06_referencias/REF-05_bailarina_original_frente.jpg` | `e0aa6ca5-a374-4888-90d7-07934bd01914` | — |
| `06_referencias/REF-06_bailarina_impresa_frente.jpg` | `c5d9f703-af2e-4e33-afe9-fcd5657c4786` | REF-05 |
| `06_referencias/REF-08_foto_antigua_contenido.jpg` | `7eb69275-955b-4c5a-a4c3-7abe4a0e41ad` | S02A, REF-01, REF-05 |
| `07_clips/S01A.jpg` | `13326172-7c3d-4595-bb2e-b42381b04858` | REF-03, REF-08 |
| `07_clips/S01B.jpg` | `1e1469b5-63d9-42f9-943e-9202ff2e09c2` | REF-03, REF-08 |
| `07_clips/S02A.jpg` | `9b449350-d5da-4d70-b0bc-3b59a50261fb` | REF-03, REF-01, REF-05 |
| `07_clips/S02B.jpg` | `a201a721-10ae-4115-abc0-077a31cfdb09` | REF-05, REF-08 |
| `07_clips/S03A.jpg` | `3b68865c-de66-4c89-a90c-1f5816761019` | REF-01, REF-08, REF-05 |
| `07_clips/S03B.jpg` | `63877bdf-7f32-4945-8ecb-f613cc253bb0` | S03A, REF-05 |
| `07_clips/S04A.jpg` | `53c55a80-b587-47ad-b5e9-18865a4cd370` | REF-06 · **recortado al 84 % centrado** para quitar un texto grabado en la cama de impresión |
| `07_clips/S04B.jpg` | `4df26c3e-d442-4567-ad32-4d875af10ec4` | REF-06 |
| `07_clips/S05.jpg` | `925931ca-bb68-468f-ad09-282752ff03cc` | REF-01, REF-03, REF-06 |
| `07_clips/S06A.jpg` | `34ba89e6-8b6f-4a8a-b3df-763e13a22f35` | REF-03, REF-01, REF-06, S05 |
| `07_clips/S06B.jpg` | `1bbdad11-c564-41d6-addb-a044c79c45e4` | REF-01, REF-03, S05 |
| `07_clips/S07.jpg` | `b1247ede-daff-43a2-8c6e-697e18ca4aac` | REF-06, S05 |
| `07_clips/S05.mp4` (6 s, 716 × 1284, 24 fps) | `12f4ea24-f1c4-4162-ae9a-7767dbe3c7f5` | fotograma S05 |
| `07_clips/S06A.mp4` (4 s) | `2eba1b22-11a3-4279-8d6c-a7cb3d42cc4a` | fotograma S06A |
| `07_clips/S07.mp4` (6 s) | `e6a8a52e-baba-498f-8654-e5f094d2bc51` | fotograma S07 |

Los prompts siguen `prompts_higgsfield.md` con sus bloques reutilizables y la cláusula «Avoid: …» al final. Se adaptaron para nombrar cada referencia por su orden («the man from the first reference image…»).

## Control de calidad (resumen)

- ✅ Identidades estables entre planos: el padre con suéter verde y canas, la hija con lentes dorados y suéter crema, y la niña con pasador azul pálido y cárdigan crema.
- ✅ Bailarina original con el brazo derecho elevado y tutú de tul; en S02B el brazo roto es el elevado y está junto a la base.
- ✅ Bailarina impresa en plástico mate, con el tutú en volantes rígidos turquesa y azul claro, reconocible como la original.
- ✅ Impresora coherente: la pieza turquesa del tutú va a medio imprimir y no hay figura completa bajo la boquilla.
- ✅ Clips: la bailarina no se deforma y no hay cambios de identidad.
- ⚠️ S07: el acercamiento del clip es más marcado de lo pedido. Se compensó con `"velocidad": 0.6` en `timeline.json`.
- ⚠️ S06A: hacia el final del clip aparecen reflejos verdosos en los lentes.
- ⚠️ La voz «Marisol» no tiene metadatos de idioma ni de acento. **Hay que escuchar y confirmar que suena a español de México.** Volver a generar una línea cuesta unos 0,2 créditos.

## Ajustes al montaje

- `montar.py`: el letrero «ANIMATIC · sin material generado» y el código de tiempo solo aparecen si falta material (placas). Si todo es material generado pero hay fotogramas fijos, la salida se llama `09_salida/VERSION_REDUCIDA_…mp4`.
- `graficos.py`: los títulos T1–T3 llevan un halo oscuro difuso para leerse sobre fondos claros (el papel del boceto en S03B), y el velo inferior de la pantalla final oscurece más para que la llamada a la acción se lea sobre la figura.
- VO06 se aceleró un 3 % (`atempo=1.03`) para que entre en su hueco de 3,1 s.

## Pendiente para la versión completa

- Animar los 9 planos restantes: S01A, S01B, S02A, S02B, S03A, S03B, S04A, S04B y S06B. Con Cinema Studio Video v2 cuestan unos 4 créditos por clip de 4 s, unos 36 créditos en total. Para S02A, S02B, S03A y S01B, que llevan disolvencia o asa, conviene generar 5 s.
- Efectos que faltan: `lapiz_papel.wav`, `encaje_pieza.wav` y `caja_mesa.wav` (≈ 0,25 créditos por segundo con Mirelo).
- Confirmar las condiciones de uso comercial del contenido generado con el plan gratuito de Higgsfield antes de pautar el anuncio.
- Validación de producto por BlitzLabs (ver `control_calidad.md`).
