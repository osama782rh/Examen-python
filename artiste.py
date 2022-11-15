from personne import Personne


class Artiste(Personne):
    def __init__(self, nom: str, prenom, nom_scene: str):
        super().__init__(nom, prenom)
        self.nom_scene = nom_scene

    def get_nomscene(self):
        return self.nomscene

    def set_nomscene(self, x):
        self.nom_scene = x

    def __str__(self):
        return f'Nom : {self.nom} \n Prénom : {self.prenom} Nom scène : {self.nom_scene}'