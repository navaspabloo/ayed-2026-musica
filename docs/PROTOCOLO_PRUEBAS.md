# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | Se imprimieron las 7 canciones con sus sub-canciones |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | No se encontró la canción |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa | No corrido |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) | Esta cancón no tiene hijas derivadas |  |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | No corrido |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | No corrido |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | No corrido |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | No corrido |  |

