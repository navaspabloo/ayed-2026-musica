from src.dominio.cancion import Cancion


def crear_catalogo():
    c1 = Cancion(1, "De Música Ligera", "Soda Stereo", "Canción Animal", "Rock Nacional", 1990, 118)
    c2 = Cancion(2, "Muchacha (Ojos de Papel)", "Almendra", "Almendra", "Rock Nacional", 1969, 162)
    c3 = Cancion(3, "Ji Ji Ji", "Patricio Rey y sus Redonditos de Ricota", "Oktubre", "Rock Nacional", 1986, 299)
    c4 = Cancion(4, "Mil Horas", "Los Abuelos de la Nada", "Vasos y Besos", "Rock Nacional", 1983, 189)
    c5 = Cancion(5, "Persiana Americana", "Soda Stereo", "Signos", "Rock Nacional", 1986, 321)
    c6 = Cancion(6, "De Música Ligera (Unplugged)", "Soda Stereo", "Comfort y Música Para Volar", "Rock Nacional", 1996, 221)
    c7 = Cancion(7, "De Música Ligera (Remix)", "Soda Stereo", "Remixes", "Rock Nacional", 1998, 230)

    c1.agregar_version(c6)
    c6.agregar_version(c7)

    return [c1, c2, c3, c4, c5, c6, c7]


def buscar_cancion_id(catalogo, cancion_id):
    for cancion in catalogo:
        if cancion.id == cancion_id:
            return cancion
    return None