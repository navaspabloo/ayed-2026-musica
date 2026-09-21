from src.config import TEMA

from src.dominio.datos import crear_catalogo, buscar_cancion_id



TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def listar_catalogo(catalogo):
    for c in catalogo:
        print(c)

'''
def listar_catalogo():
    print("id,titulo,artista,album,genero,anio,duracion_seg")
    for c in canciones:
        print(str(c["id"])+"," + c["titulo"]+"," + c["artista"]+"," + c["album"]+"," + c["genero"]+"," + str(c["anio"]) +","+ str(c["duracion_seg"]))
'''

def iterar_recursivo(catalogo):
    id = int(input("id de la cancion: "))

    cancion = buscar_cancion_id(catalogo, id)
    if cancion is None:
        print("No se encontró la canción")
        return

    if not cancion.versiones:
        print("Esta cancón no tiene hijas derivadas")
    else:
        cancion.listar_versiones_hijas()

def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    catalogo = crear_catalogo()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")

        elif opcion == "1":
                listar_catalogo(catalogo)
        elif opcion == "5":
                iterar_recursivo(catalogo)
        elif opcion in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
                
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
