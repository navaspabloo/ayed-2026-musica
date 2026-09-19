class Cancion:
    def __init__(self, _id, _titulo, _artista, _album, _genero, _year, _duracion):
        self.id = _id
        self.titulo = _titulo
        self.artista = _artista
        self.album = _album
        self.genero = _genero
        self.year = _year
        self.duracion = _duracion

        def __str__(self):
            return f" {self.id} - {self.titulo} - {self.artista} - {self.album} - {self.genero} - {self.year} - {self.duracion}" 