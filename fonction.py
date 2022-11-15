from personne import  Personne


class Fonction(Personne):
    def __init__(self, nom, prenom, fonction):
        super().__init__(nom, prenom)
        self.fonction = fonction

    def get_fonction(self):
        return self.fonction

    def set_fonction(self, x):
        self.fonction = x
