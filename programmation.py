from spectacle import Spectacle


class Programmation:
    def __init__(self, spectacles: Spectacle):
        self.spectacles = spectacles

    def selectPrice(self, prix):
        liste = list()
        for spectacle in self.spectacles:
            if spectacle.prix <= prix:
                liste.append(spectacle)
        return liste

    def selectArtiste(self, artiste):
        liste = list()
        for spectacle in self.spectacles:
            if artiste in spectacle.artistes:
                liste.append(spectacle)
        return liste

    def selectLesArtistes(self, collectionartiste):
        for artiste in collectionartiste:
            if artiste.nom in self.spectacles.artistes:
                liste = [artiste]
        return liste

    def  saveToXML(nomdefichier):
        pass
