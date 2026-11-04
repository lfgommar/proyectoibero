# BlitzLabs · Navidad — Guion técnico (35 s, 9:16)

**Concepto:** «De tu imaginación a sus manos.»
**Emoción central:** «Papá todavía se acuerda».
**Mensaje de producto:** BlitzLabs fabrica una pieza nueva a partir de un recuerdo, mediante impresión 3D. La figura recreada se reconoce como la bailarina original, pero se ve claramente impresa en 3D: plástico mate, piezas de colores ensambladas y líneas de capa visibles.

Fuente de verdad de tiempos: [`05_montaje/timeline.json`](../05_montaje/timeline.json). Si cambias un tiempo aquí, cámbialo también allí.

---

## Línea de tiempo

| Plano | Tiempo (s) | Dur. | Imagen (una acción principal por clip) | Texto en edición | Locución |
|---|---|---|---|---|---|
| **S01A** | 0,0–2,6 | 2,6 | Primerísimo plano: manos de la hija adulta sostienen la foto antigua (el padre joven entrega la bailarina a la niña). El pulgar acaricia el borde. | «Hay regalos que nunca se olvidan.» (0,6–4,6) | VO01 0,5–3,8 |
| **S01B** | 2,6–5,0 | 2,4 | Cambio de foco de la foto a su rostro adulto con lentes; mirada nostálgica. | ↑ | ↑ |
| ⟶ | 5,0 | 0,6 | *Disolvencia de entrada al recuerdo* | | |
| **S02A** | 5,0–7,4 | 2,4 | Recuerdo: la niña de 6 años observa la bailarina intacta con ilusión. | — | VO02 5,6–9,2 |
| **S02B** | 7,4–10,0 | 2,6 | Detalle: la bailarina sobre la mesa con el brazo roto a un lado. Al fondo, el padre joven pone la mano en el hombro de la niña. Sin mostrar el accidente. | — | ↑ |
| ⟶ | 10,0 | 0,6 | *Disolvencia de salida del recuerdo* | | |
| **S03A** | 10,0–12,8 | 2,8 | Presente: el padre mira la foto junto al boceto; su gesto pasa de la nostalgia a una determinación tranquila. | «Algunos recuerdos merecen volver.» (10,8–14,7) | VO03 10,5–14,2 |
| **S03B** | 12,8–15,0 | 2,2 | Inserto: un hilo sutil de luz dorada recorre el contorno del boceto. | ↑ | ↑ |
| **S04A** | 15,0–17,4 | 2,4 | Detalle: la boquilla de una impresora FDM imprime una pieza turquesa del tutú (a medio hacer). | «Recreado con impresión 3D.» (15,6–19,7) | VO04 15,4–19,3 |
| **S04B** | 17,4–20,0 | 2,6 | Manos del fabricante colocan el moño blanco y revisan la figura terminada sobre su base marfil. | ↑ | ↑ |
| **S05** | 20,0–25,0 | 5,0 | Junto al árbol, el padre acerca la caja abierta (bailarina en papel de seda); ella empieza a reconocerla. Acercamiento lento hacia su rostro. | — | *(silencio: papel y música)* |
| **S06A** | 25,0–27,6 | 2,6 | Ella mira la muñeca y luego a su padre; sonrisa contenida, ojos húmedos. | — | VO05 25,3–29,8 |
| **S06B** | 27,6–30,0 | 2,4 | Abrazo natural; la caja queda apoyada con seguridad sobre la mesa. | — | ↑ |
| ⟶ | 30,0 | 0,4 | *Disolvencia suave* | | |
| **S07** | 30,0–35,0 | 5,0 | Bailarina impresa sobre la mesa junto a su caja; padre e hija desenfocados al fondo, cerca del árbol. Acercamiento muy suave y final estable. | Pantalla final (30,2–35,0) | VO06 30,8–33,9 |

**Pantalla final (sobre S07):** se ve completa desde 31,8 s, es decir, **3,2 s legible** como mínimo; el lema está completo desde 31,2 s.
- Logo original de BlitzLabs sobre una insignia blanca circular (mismo blanco que su fondo original; el diseño no se toca) + nombre «BlitzLabs».
- Texto principal: **«De tu imaginación a sus manos.»**
- Texto de acción: **«Cuéntanos tu idea. Escríbenos «REGALO».»** («REGALO» en una pastilla con el rojo del logo).
- Texto secundario: **«WhatsApp · Instagram»**. No se incluyen números, usuarios ni datos de contacto.

**Subtítulos:** se queman VO01–VO05, en una caja translúcida dentro del área segura. VO06 no se quema, porque el lema de la pantalla final ya lo dice, pero sí está en el `.srt` para las plataformas.

**Área segura 9:16:** los textos quedan entre y = 250 y y = 1500 px, y entre x = 120 y x = 940 px. Así no los tapan la interfaz superior, la descripción inferior ni el riel de botones de Reels o TikTok. El script lo comprueba automáticamente.

---

## Locución — español de México

**Tono:** cálido, cercano, como alguien que cuenta una historia familiar. Nada de tono de oferta, nada de «voz de anuncio». Volumen íntimo, cerca del micrófono, sin aire de narrador épico.
**Pronunciación:** *BlitzLabs* se dice «BLITS-labs», en dos sílabas, con acento en la primera.
**Entrega:** una toma por línea, con 0,3 s de aire antes y después. WAV 48 kHz / 24 bit, mono o estéreo, nombradas `VO01.wav` … `VO06.wav` en `08_audio/vo/`. El script las coloca en su tiempo y avisa si alguna no cabe en su hueco.

| ID | Texto exacto | Hueco | Dirección |
|---|---|---|---|
| VO01 | Cuando era pequeña, le regaló una bailarina. | 3,3 s | Evocador, sonrisa en la voz. Pausa mínima tras «pequeña». |
| VO02 | Se rompió. *(pausa 0,4 s)* Y nunca encontraron otra igual. | 3,6 s | Más bajo, sin dramatizar. La pausa es importante. |
| VO03 | Esta Navidad, papá decidió recuperar ese recuerdo. | 3,7 s | Sube un poco la energía en «decidió»: determinación tranquila. |
| VO04 | En BlitzLabs, lo convertimos en un regalo personalizado. | 3,9 s | Cercano, orgulloso del oficio, sin vender. |
| VO05 | Porque recordar lo que ama… *(pausa 0,4 s)* también es una forma de decir ‘te quiero’. | 4,5 s | El momento más íntimo. Casi susurrado en «te quiero». |
| VO06 | BlitzLabs. *(pausa 0,3 s)* De tu imaginación a sus manos. | 3,1 s | Firma serena; cierre descendente, sin subir el volumen. |

---

## Música (instrumental, con licencia para publicidad)

35 s, alrededor de 68–72 BPM, en tonalidad mayor y cálida. Piano cálido, cuerdas suaves y campanas o celesta navideñas discretas. Entrega: `08_audio/musica.wav`, de 35 s o más (el script la recorta y hace un fundido final de 0,7 s).

| Tramo | Momento | Qué hace la música |
|---|---|---|
| 0–10 s | Recuerdo | Piano solo, notas espaciadas, íntimo. Un toque de celesta al entrar al recuerdo (5 s). |
| 10–20 s | Intención y fabricación | Entra un colchón de cuerdas suaves; un pulso ligero de piano acompaña a la impresora. |
| 20–25 s | Entrega (sin voz) | La música pasa al frente, con un crecimiento contenido. Deja espacio al papel de seda. |
| 25–30 s | Reconocimiento | Clímax emocional: las cuerdas se abren y el piano sube una octava. |
| 30–35 s | Marca | Resolución delicada en la tónica, con campanas discretas y una nota final que se deja sonar. |

La mezcla la deja siempre por debajo de la voz: ganancia base de −15 dB y atenuación automática mientras suena la locución. La sonoridad final es de −14 LUFS integrados, con picos reales ≤ −1 dBTP.

## Efectos de sonido (sutiles)

| Archivo (`08_audio/sfx/`) | Inicio | Descripción |
|---|---|---|
| `foto_roce.wav` | 1,2 s | Pulgar que roza el borde de una foto de papel brillante. |
| `lapiz_papel.wav` | 11,0 s | Roce leve de papel y lápiz sobre la mesa. |
| `impresora.wav` | 15,0 s | Impresora FDM: motores paso a paso suaves y ventilador (unos 5 s). |
| `encaje_pieza.wav` | 18,6 s | «Clic» pequeño de una pieza plástica que encaja. |
| `caja_abre.wav` | 20,2 s | Tapa de caja de cartón que se separa. |
| `papel_seda.wav` | 21,0 s | Papel de seda que se aparta con cuidado (unos 3 s). |
| `caja_mesa.wav` | 27,9 s | Caja apoyada suavemente sobre una mesa de madera. |

Los personajes no hablan a cámara. Se descarta el audio que generen los modelos de video.
