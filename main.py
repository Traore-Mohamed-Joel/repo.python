# afficher_informations_personne
# Paramètres : nom, age
def afficher_informations_personne(nom, age):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans")

    condition = age >= 18
    print(condition)
    if condition:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0

    while age_int == 0:
        age_str = input(nom_personne + ", quel est votre âge ? ")

        try:
            age_int = int(age_str)
        except:
            print("ERREUR : Vous devez rentrer un nombre pour l'âge")

    return age_int


# demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# demander l'âge
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)