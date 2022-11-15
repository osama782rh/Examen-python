from personne import Personne
from compte import Compte


class Utilisateur(Personne):
    def __init__(self, nom, prenom, son_compte: Compte):
        super().__init__(nom, prenom)
        self.son_compte = son_compte

    def get_son_compte(self):
        return self.son_compte

    def set_son_compte(self, x):
        self.son_compte = x
