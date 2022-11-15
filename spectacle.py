class Spectacle:
    def __init__(self, titre: str, date, prix: float, nb_places: int, artistes):
        self.titre = titre
        self.date = date
        self.prix = prix
        self.nb_places = nb_places
        self.artistes = artistes

    def get_titre(self):
        return self.titre

    def set_titre(self, x):
        self.titre = x

    def get_date(self):
        return self.date

    def set_date(self, x):
        self.date = x

    def get_prix(self):
        return self.prix

    def set_prix(self, x):
        self.prix = x

    def get_nb_places(self):
        return self.nb_places

    def set_nb_places(self, x):
        self.nb_places = x

    def nbArtistes(self):
        return  len(self.artistes)

    def asArtisteCommun(self, spectacle2):
        for spectacle in range(spectacle2):
            return True if self.spectacle == spectacle2[spectacle] else False



