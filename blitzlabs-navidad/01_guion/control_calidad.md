# Control de calidad

Revisa cada referencia, cada fotograma clave y cada clip **antes** de aceptarlo. Si algo falla, se vuelve a generar. Tras el montaje, revisa `09_salida/hoja_de_contactos.jpg`, con un fotograma por plano en una sola imagen, e `09_salida/informe_qc.txt`.

## Personajes

| Revisión | Padre 47 | Padre 30 | Hija 23 | Hija 6 |
|---|---|---|---|---|
| Mismo rostro en todos los planos (nariz, cejas, ojos avellana) | ☐ | ☐ | ☐ | ☐ |
| Edad creíble y estable dentro del clip | ☐ | ☐ | ☐ | ☐ |
| Cabello: castaño con canas / castaño sin canas / castaño a los hombros / castaño con pasador azul pálido | ☐ | ☐ | ☐ | ☐ |
| Vestuario: suéter verde oscuro / suéter marrón óxido / suéter crema de punto trenzado / cárdigan crema | ☐ | ☐ | ☐ | ☐ |
| Lentes de armazón fino dorado siempre presentes e idénticos | — | — | ☐ | (sin lentes) ☐ |
| Parecido familiar reconocible entre niña, hija adulta y padre | ☐ | ☐ | ☐ | ☐ |
| Manos: cinco dedos, sin fusiones, con un agarre creíble | ☐ | ☐ | ☐ | ☐ |
| Aspecto de persona real, no de modelo publicitario | ☐ | ☐ | ☐ | ☐ |

## Bailarina

| Revisión | Original (S01, S02) | Impresa (S04B–S07) |
|---|---|---|
| Pose fija: brazo derecho curvado sobre la cabeza, izquierdo hacia el lado y ligeramente abajo, pierna derecha cruzada delante | ☐ | ☐ |
| Los brazos, las piernas y el tutú **no se mueven** en ningún clip | ☐ | ☐ |
| Paleta: corpiño turquesa, tutú turquesa y azul claro, moño blanco, zapatillas turquesa, cabello rubio con adornos azul muy claro | ☐ | ☐ |
| Base circular marfil unida a la figura | ☐ | ☐ |
| Escala de unos 18 cm (aprox. el largo de una mano adulta) | ☐ | ☐ |
| Acabado: satinado con tutú textil | ☐ | — |
| Acabado: plástico mate, piezas ensambladas, líneas de capa en los acercamientos, tutú de volúmenes plásticos rígidos | — | ☐ |
| No parece porcelana, tela real ni plástico brillante inyectado | — | ☐ |
| El mismo rostro, las mismas proporciones y los mismos colores en todas sus apariciones | ☐ | ☐ |
| S02B: el brazo roto es el brazo elevado y está junto a la base, sin fragmentos | ☐ | — |

## Fabricación (S04A–S04B)

- ☐ La impresora es coherente: pórtico, correas, hotend con ventilador y cama texturizada.
- ☐ La pieza crece capa a capa. **No aparece una figura completa bajo la boquilla.**
- ☐ La pieza que se imprime es turquesa y corresponde a una parte del tutú.
- ☐ Las manos del fabricante son creíbles y su gesto es de cuidado; no se ve su rostro.
- ☐ No hay logos de marcas de impresoras ni textos en pantalla.

## Dirección visual

- ☐ Luz cálida, árbol desenfocado, madera, verde profundo y crema.
- ☐ El hilo de luz dorada (S03B) es sutil: no hay chispas ni explosiones de partículas.
- ☐ Ningún movimiento de cámara es espectacular. Solo hay acercamientos lentos, cambios de foco y derivas mínimas.
- ☐ Los recuerdos (S02A–S02B) se distinguen del presente por la gradación, aplicada automáticamente en el montaje.
- ☐ Ningún clip trae texto, logotipos o marcas de agua generados.

## Montaje y entrega

- ☐ Duración de 35,0 s, 1080 × 1920, 30 fps, H.264 + AAC (el script lo comprueba).
- ☐ Todos los textos quedan dentro del área segura (`03_graficos/guia_area_segura.png`).
- ☐ La pantalla final se lee completa durante al menos 3 s (desde 31,8 s).
- ☐ El logo es el original, sin deformar ni recolorear (`02_marca/`).
- ☐ No hay números, usuarios, precios, disponibilidad ni promesas de entrega.
- ☐ La locución entra en sus huecos; el informe avisa si alguna línea se pasa.
- ☐ La música siempre queda por debajo de la voz, sin cortes, y resuelve con la marca.
- ☐ Sonoridad de −14 LUFS y picos reales de −1 dBTP o menos.
- ☐ El archivo final **no** lleva el prefijo `ANIMATIC_`: los 12 planos son clips reales.

## Antes de usar el video en publicidad

- ☐ **Validación de producto:** BlitzLabs confirma que la recreación mostrada se puede fabricar tal como se ve: piezas de colores ensambladas, tutú en volúmenes plásticos y rasgos pintados a mano tras la impresión. Si algo no es fabricable, ajusta REF-06 y regenera S04B–S07.
- ☐ Se confirman las licencias publicitarias de la música, la voz y los efectos.
- ☐ Se revisan las condiciones de uso comercial del contenido generado en Higgsfield según tu plan.
