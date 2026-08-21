"""Premier programme 
Formation Python
apprendre la programmation"""

nom = input("quel est votre nom ? ")
age = input("quel est votre ages ? ")

try:
    age_prochain = int(age) + 1
except ValueError: 
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else:
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("l'an prochain vous aurez " + str(age_prochain) + " ans")
