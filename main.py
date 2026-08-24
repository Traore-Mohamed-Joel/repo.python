

# afficher_informations_personne
# Paramètres : nom, age
def afficher_informations_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print(f"Vous vous appelez {nom}, vous avez {age}" )
    print("Vous vous appelez %s , vous avez %s ans" % (nom, age) )

    print("L'an prochain vous aurez " + str(age + 1) + " ans")
    print("L'an prochain vous aurez %s ans " % (age + 1 ))
    

    condition = age >= 18
    print(condition)
    if condition:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    #afficher la taille
    if not taille == 0:
        print("votre taille : " + str(taille) + " m")


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
# nom1 = demander_nom()
# nom2 = demander_nom()
# nom1 = "personne1"
# nom2 ="personne2"

# # demander l'âge
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# # afficher les résultats
# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)

NB_PERSONNES = 1

# la boucle for
for i in range (0, NB_PERSONNES):
    nom = "personne" + str(i +1)
    age = demander_age(nom)
    afficher_informations_personne(nom, age, 1.80)


print("""
vous 
    mettez
        ce que vous voulez

""")

print("toto", 20 , "ans", "taille:", 1.70)