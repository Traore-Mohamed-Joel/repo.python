"""
solde = 5000
mise = 500
choisir un nombre entre 1 et 10
si le_nombre_choisir est >= 5 , mise * 2
si le_nombre_choisir est < 5 , mise - 500
votre nouveau solde est mise - 5000
voulez vous continuer ? OUI ou NON ?
"""
import random

solde = 5000

while True:
    nombre = random.randint(1, 10)

    print("Bienvenue ! Votre solde est :", solde)

    try:
        mise = int(input("Quel est le montant de votre mise ? : "))
    except ValueError:
        print("Vous devez entrer un chiffre.")
        continue

    if mise <= 0:
        print("La mise doit être supérieure à 0.")
        continue

    if mise > solde:
        print("Solde insuffisant.")
        break

    if nombre >= 5:
        solde = solde + mise
        print("Bravo ! Vous avez gagné !")
    else:
        solde = solde - mise
        print("Dommage, vous avez perdu !")

    print("Le nombre choisi était :", nombre)
    print("Votre nouveau solde est :", solde)

    while True:
        reponse = input("Voulez-vous continuer ? OUI ou NON : ").upper()

        if reponse == "NON":
            print("Merci d'avoir joué !")
            break
        elif reponse == "OUI":
            break
        else:
            print("Vous devez répondre par 'OUI' ou par 'NON'.")

    if reponse == "NON":
        break