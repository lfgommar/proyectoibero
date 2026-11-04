# Audio

| Ruta | Contenido |
|---|---|
| `vo/VO01.wav` … `vo/VO06.wav` | Locución en español de México, **una línea por archivo**. El texto exacto, la dirección y el hueco de cada línea están en [`../01_guion/guion_tecnico.md`](../01_guion/guion_tecnico.md#locución--español-de-méxico). |
| `musica.wav` | Música instrumental de 35 s o más, con licencia para publicidad (brief en el guion técnico). |
| `sfx/foto_roce.wav`, `lapiz_papel.wav`, `impresora.wav`, `encaje_pieza.wav`, `caja_abre.wav`, `papel_seda.wav`, `caja_mesa.wav` | Efectos sutiles; los tiempos están en `05_montaje/timeline.json`. |

También sirven `.flac`, `.aiff`, `.mp3` y `.m4a`. El montaje coloca cada archivo en su tiempo, atenúa la música bajo la voz, normaliza a −14 LUFS y avisa si alguna locución no cabe en su hueco. Si falta algún archivo, se monta sin él y lo indica en `09_salida/informe_qc.txt`.

**Estado:** pendiente. No se ha generado locución, música ni efectos.
