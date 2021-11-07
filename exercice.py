#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici

# TODO: Définissez vos fonction ici
# Exercice 1
def comparateur_de_fichiers(fichier1, fichier2):
    with open(fichier1, "r", encoding="cp1252") as f1,  open(fichier2, "r", encoding="cp1252") as f2:
        numero_ligne = 0
        for l_1, l_2 in zip(f1, f2):
            if l_1 != l_2:
                print(f"Les fichiers sont differents a la ligne {numero_ligne + 1}.")
                print(f"{l_1}est different de \n{l_2}")
                break
            numero_ligne += 1
    
    return l_1, l_2

# Exercice 2
def tripler_espaces(fichier_lecture, fichier_ecriture):
    with open(fichier_lecture, "r", encoding="cp1252") as f_lect, open(fichier_ecriture, "w", encoding="cp1252") as f_ecrit:
        f_ecrit.write(f_lect.read().replace(" ", "   "))

# Exercice 3
def notes_lettrees(fichier_notes, fichier_lettres):
    with open(fichier_notes, "r", encoding="cp1252") as f_notes, open(fichier_lettres, "w", encoding="cp1252") as f_lettres:
        for note in f_notes:
            note = note.strip()
            note_int = int(note)
            if note_int in range(PERCENTAGE_TO_LETTER["A*"][0], PERCENTAGE_TO_LETTER["A*"][1]):
                f_lettres.write(f"{note_int} A*\n")
            if note_int in range(PERCENTAGE_TO_LETTER["A"][0], PERCENTAGE_TO_LETTER["A"][1]):
                f_lettres.write(f"{note_int} A\n")
            if note_int in range(PERCENTAGE_TO_LETTER["B+"][0], PERCENTAGE_TO_LETTER["B+"][1]):
                f_lettres.write(f"{note_int} B+\n")
            if note_int in range(PERCENTAGE_TO_LETTER["B"][0], PERCENTAGE_TO_LETTER["B"][1]):
                f_lettres.write(f"{note_int} B\n")
            if note_int in range(PERCENTAGE_TO_LETTER["C+"][0], PERCENTAGE_TO_LETTER["C+"][1]):
                f_lettres.write(f"{note_int} C+\n")
            if note_int in range(PERCENTAGE_TO_LETTER["C"][0], PERCENTAGE_TO_LETTER["C"][1]):
                f_lettres.write(f"{note_int} C\n")
            if note_int in range(PERCENTAGE_TO_LETTER["F"][0], PERCENTAGE_TO_LETTER["F"][1]):
                f_lettres.write(f"{note_int} F\n")

# Exercice 4
def stocker_recette():
    action = input("Que voulez-vous faire? (Ajouter, Modifier, Supprimer ou Fermer) ")
    while action != "Fermer":

        if action == 'Ajouter':
            ajouter_recette("livre_de_recettes.txt")

        if action == 'Modifier':
            modifier_recette("livre_de_recettes.txt")
        
        if action == 'Supprimer':
            supprimer_recette("livre_de_recettes.txt")
        
        action = input("Que voulez-vous faire? (Ajouter, Modifier, Supprimer ou Fermer) ")

def ajouter_recette(nom_fichier):
    nom_recette = input("Veuillez entrer le nom de la recette à ajouter (en un mot) : ")
    ingredients = input("Veuillez entrer tous les ingédients séparés d'une virgule : ")
    with open(nom_fichier, "a", encoding="cp1252") as f:
        f.write(f'{nom_recette} : {ingredients}\n')

def supprimer_recette(nom_fichier):
    nom_recette = input("Veuillez entrer le nom de la recette à supprimer (en un mot) : ")
    liste_lignes = []
    with open(nom_fichier, "r", encoding="cp1252") as f:
        liste_lignes = f.readlines()
    with open(nom_fichier, "w", encoding="cp1252") as f:
        for ligne in liste_lignes:
            elements_ligne = ligne.split()
            if elements_ligne[0] != nom_recette:
                f.write(ligne)

def modifier_recette(nom_fichier):
    nom_recette = input("Veuillez entrer le nom de la recette à modifier (en un mot) : ")
    nouveaux_ingredients = input("Veuillez entrer tous les nouveaux ingédients séparés d'une virgule : ")
    liste_lignes = []
    with open(nom_fichier, "r", encoding="cp1252") as f:
        liste_lignes = f.readlines()
        modification_est_effectuee = False
        for ligne in range(len(liste_lignes)):
            elements_ligne = liste_lignes[ligne].split()
            if elements_ligne[0] == nom_recette:
                liste_lignes[ligne] = liste_lignes[ligne].replace(elements_ligne[2], nouveaux_ingredients)
                modification_est_effectuee = True
        if not modification_est_effectuee:
            modifier_recette(nom_fichier)
    with open(nom_fichier, "w", encoding="cp1252") as f:
        f.writelines(liste_lignes)

# Exercice 5
def lire_nombres(nom_fichier):
    liste_nombres = []
    with open(nom_fichier, "r", encoding="cp1252") as f:
        for ligne in f:
            liste_mots = ligne.split()
            for mot in liste_mots:
                if mot.isnumeric():
                    liste_nombres.append(int(mot))

    return(sorted(liste_nombres))

#Exercice 6
def ecrire_ligne_sur_deux(nom_fichier_lecture, nom_fichier_ecriture):
    liste_lignes = []
    with open(nom_fichier_lecture, "r", encoding="cp1252") as f:
        for index_ligne, ligne in enumerate(f):
            if index_ligne % 2 == 0:
                liste_lignes.append(ligne)
    with open(nom_fichier_ecriture, "w", encoding="cp1252") as f:
        f.writelines(liste_lignes)




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    ligne1, ligne2 = comparateur_de_fichiers("comp1.txt", "comp2.txt")

    tripler_espaces("exemple.txt", "exemple_3_esp.txt")

    notes_lettrees("notes.txt", "lettres.txt")

    stocker_recette()

    print(lire_nombres("exemple.txt"))

    ecrire_ligne_sur_deux("exemple.txt", "exemple_2.txt")
