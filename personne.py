class Personne:
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, x):
        self.nom = x

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, x):
        self.prenom = x

    def __str__(self):
        return f'Nom : {self.nom} \n Prénom : {self.prenom}'
