"""Premier programme 
Formation Python
apprendre la programmation
nom = input("quel est votre nom ? ")
age = input("quel est votre ages ? ")

try:
    age_prochain = int(age) + 1
except ValueError: 
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else:
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("l'an prochain vous aurez " + str(age_prochain) + " ans")"""

n = 0
# print(n)
# n = 1
# print(n)
# n = n + 1
# print(n)

# while n < 4:
#     print("Valeur de n: " + str(n))
#     n = n + 1
# print("fin de la boucle")

mot_de_passe = ""
while not mot_de_passe == "TOTO" :
    mot_de_passe = input("quel est le mot de passe ? ")

print("Mot de passe correct, vous avez accés au compte")