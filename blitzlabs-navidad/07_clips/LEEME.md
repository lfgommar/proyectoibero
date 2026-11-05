# Clips de video

Descarga aquí cada clip animado con **el nombre exacto del plano**. El montaje los detecta solo.

| Archivo | Plano | Se usa (s) | Generar |
|---|---|---|---|
| `S01A.mp4` | La foto en sus manos | 2,6 | 5 s |
| `S01B.mp4` | Su rostro | 2,4 (+0,3 de asa) | 5 s |
| `S02A.mp4` | Recuerdo: la ilusión | 2,4 (+0,3) | 5 s |
| `S02B.mp4` | Lo que se perdió | 2,6 (+0,3) | 5 s |
| `S03A.mp4` | La intención del padre | 2,8 (+0,3) | 5 s |
| `S03B.mp4` | El hilo de luz dorada | 2,2 | 5 s |
| `S04A.mp4` | La impresora | 2,4 | 5 s |
| `S04B.mp4` | Ensamblado y revisión | 2,6 | 5 s |
| `S05.mp4` | La entrega | 5,0 | 5–6 s |
| `S06A.mp4` | El reconocimiento | 2,6 | 5 s |
| `S06B.mp4` | El abrazo | 2,4 (+0,2) | 5 s |
| `S07.mp4` | Producto y marca | 5,0 (+0,2) | 6 s si es posible |

- También sirven `.mov`, `.webm` y `.mkv`. Puede ser cualquier resolución: el script recorta al centro para llenar 1080 × 1920. Si el clip no es 9:16, revisa el encuadre.
- Si un plano solo tiene fotograma clave, guárdalo como `<ID>.png` o `.jpg`: el montaje lo anima con un acercamiento lento para previsualizar.
- Para elegir desde qué segundo del clip empieza el plano, cambia `"entrada"` en `05_montaje/timeline.json` (por defecto 0,3–0,5 s, para saltar los primeros fotogramas, que suelen ser inestables). También puedes ralentizar un plano con `"velocidad": 0.85`.

**Estado (versión reducida):** los 12 fotogramas clave están generados (`<ID>.jpg`). Hay 3 clips animados: `S05.mp4`, `S06A.mp4` y `S07.mp4`, de Cinema Studio Video v2 a 716 × 1284 y 24 fps; el montaje los escala a 1080 × 1920. En cuanto agregues el `.mp4` de cualquier otro plano, el montaje lo usa en lugar del fotograma.
