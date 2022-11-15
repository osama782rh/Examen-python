from personne import Personne
from compte import Compte
from programmation import Programmation
from utilisateur import Utilisateur
from artiste import Artiste
from spectacle import Spectacle


def creePersonne():
    nom = input('Saisir le nom du personnage que vous voulez créer : ')
    prenom = input('Saisir le prénom du personnage que vous voulez créer : ')
    return Personne(nom, prenom)


def creeCompte():
    login = input('Saisir le login : ')
    mdp = input('Saisir le mdp : ')
    return Compte(login, mdp)


def creeUtilisateur():
    return Utilisateur(creePersonne(), creeCompte())


def creeArtistes():
    nom_scene = input('Saisir le nom de la scène de votre artiste : ')
    nom = input("nom : ")
    prenom = input(" prenom : ")
    return Artiste(Personne(nom, prenom), nom_scene)


def afficher_personne():
    for k, personne in enumerate(liste_pers, 1):
        print(f'{k} : {personne.__str__()}')


choix = ""
while choix != "Q" or choix != "q":
    print('Création d\'un personnage.........1')
    print('Création d\'un compte.............2')
    print('Création d\'un utilisatuer........3')
    print('Création d\'artistes..............4')
    choix = input("Votre choix ..............:")

    if choix == '1':
        personne = creePersonne()
        liste_pers = [personne]
        aff = input("Voulez vous afficher la liste de personne ? : ")
        if aff == 'y':
            afficher_personne()

    elif choix == '2':
        compte = creeCompte()
        liste_compte = [compte]

    elif choix == '3':
        utlisateur = creeUtilisateur()

    elif choix == '4':
        '''
        artiste = creeArtistes()
        list_artistes = [artiste]
        for artiste in list_artistes:
            print(artiste)
        '''
        res = input("Voulez vous envoyer une liste d'artistes et les comparer aux existants ? : ")
        if res == 'y':
            les_spectacles = ['Bercy', 'Bébé', '15/11/2000', float('20.3'), int(20), Artiste('Toto', 'Grande', 'CASA')]
            specta = ['Bercy', 'Bébé', '15/11/2000', float('20.3'), int(20), Artiste('Titi', 'Petit', 'rabat')]
            specta2 = ['Bercy', 'Bébé', '15/11/2000', float('20.3'), int(20), Artiste('paris', 'paris', 'Paris')]
            les_spectacles.append(specta)
            les_spectacles.append(specta2)
            collec = ['Bercy', 'Bébé', '15/11/2000', float('20.3'), int(20), Artiste('paris', 'paris', 'Paris')]
            programmation = Programmation(les_spectacles)
            programmation.selectLesArtistes(collec)


