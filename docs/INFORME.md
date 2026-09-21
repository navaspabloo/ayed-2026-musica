# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Música
- Por qué lo eligieron (5–8 líneas): Un integrante lo sugirió como primera opción y como a todos nos gusta la música, quedo seleccionado.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: listar_versiones_hijas(nivel) 
- Caso base: si la lista versiones esta vacía => retorna None 
- Caso recursivo: para cada canción en lista versiones la imprime llamando listar_versiones_hija(nivel + 1) 
- Traza de un ejemplo real del dataset: 

Datos:
- id 1 De Música Ligera → versiones: [id 6 Unplugged]
- id 6 Unplugged → versiones: [id 7 Remix]
- id 7 Remix → versiones: []

Inicia programa

1. llama a listar_versiones_hijas(), id 1, nivel=1
   - lista versiones no está vacía, no es caso base
   - le paso id 1
   - imprime: " 6 - De Música Ligera (Unplugged) - Soda Stereo  - Comfort y Música Para Volar - Rock Nacional - 1996 - 221"
   - llama nuevamente a listar_versiones_hijas(2)
    - lista versiones no está vacía
   - toma id 7
   - imprime: "7 - De Música Ligera (Remix) - Soda Stereo - Remixes - Rock Nacional - 1998 - 230"
   - llama nuevamente listar_versiones_hijas(3), nivel 3
    - lista versiones está vacía, es caso base
    - `return`
    - vuelve a la llamada 2
    - La llamada 2 no tiene más hijas, vuelve a la llamada 1
    - La llamada 1 no tiene más hijas
    - Termina llamada recursiva

Salida en consola:

    id de la cancion: 1
        6 - De Música Ligera (Unplugged) - Soda Stereo - Comfort y Música Para Volar - Rock Nacional - 1996 - 221
            7 - De Música Ligera (Remix) - Soda Stereo - Remixes - Rock Nacional - 1998 - 230

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
