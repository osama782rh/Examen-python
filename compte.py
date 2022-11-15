class Compte:
    def __init__(self, login: str, mdp: str):
        self.login = login
        self.mdp = mdp

    def get_login(self):
        return self.login

    def set_login(self, x):
        self.login = x

    def get_mdp(self):
        return self.mdp

    def set_mdp(self, x):
        self.mdp = x

    def login(self):
        resultat = False
        monfichier = open('file.csv', 'r')
        f = monfichier.readline()
        if self.login and self.mdp in f:
            resultat = True
        return resultat
