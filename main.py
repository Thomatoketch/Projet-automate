import os
from fonction import *

liste = os.listdir("Fichier TXT") # dir is your directory path
number_files = len(liste)
numero = 9999

while int(numero) > number_files:
    print("Il y a ",number_files, " fichiers. Quel fichier voulez vous ouvrir ? ")
    numero = input()

file_path = "Fichier TXT/F1-"+numero+".txt"

# Lire le contenu du fichier sélectionné
with open(file_path, "r") as f:
    lignes = f.readlines()

nbr_symbole = int(lignes[0].strip())
nbr_etats = int(lignes[1].strip())
nbr_initial = int(lignes[2][0].strip())
etat_initiaux = list(map(int, lignes[2][1:].strip().split()))
nbr_final = int(lignes[3][0].strip())
etat_finaux = list(map(int, lignes[3][1:].strip().split()))
nbr_transition = int(lignes[4].strip())

print("les etats initiaux sont :",etat_initiaux)
print("les etats terminaux sont :",etat_finaux)
print("la table de transitions est :")


# Créer une table de transition vide
table_transition = [[""] * nbr_symbole for i in range(nbr_etats)]

# Ajouter les transitions
for i in range(nbr_transition):
    transition = lignes[6+i].strip()
    etat_depart = int(transition[0])
    symbole = ord(transition[1]) - ord('a')
    etat_arrivee = int(transition[2])
    table_transition[etat_depart][symbole] = etat_arrivee

# Afficher la table de transition
print("Table de transition:")
print("  | " + " | ".join([f"{chr(i + ord('a')):^4}"for i in range(nbr_symbole)]))
print("--+" + "+".join(["------" for i in range(nbr_symbole)]))

for g in range(nbr_etats):
    print(g, end=' | ')
    for h in range(nbr_symbole):
        if table_transition[g][h] == "":
            print(f"{'--':^4}", end=' | ')
        else:
            print(f"{table_transition[g][h]:^4}", end=' | ')
    print("")

# Standardiser l'automate si nécessaire
if nbr_initial > 1:
    rep = input("si vous voulez standardiser votre automate, tapez oui : ")
    if rep == "oui" :
        for i in range(nbr_initial):
            if etat_initiaux[i] in etat_finaux:
                etat_finaux.append("i")

        for i in range(6,len(lignes)-1):
            for j in etat_initiaux:
                if lignes[i][0] == str(j) :
                    lignes.append("\ni"+lignes[i][1:3])
        etat_initiaux = ["i"]


with open("Fichier TXT STD/F1-" + numero + "-std.txt", "w") as fichier:
    if nbr_initial > 1 :
        lignes[1] = str(int(lignes[1])+1) + "\n"
        lignes[2] = "1 i\n"
        lignes[4] = str(len(lignes) - 6) + "\n"
    for i in range(len(lignes)) :
        fichier.write(str(lignes[i]))


table_std = [[""] * nbr_symbole for i in range(nbr_etats+1)]


with open("Fichier TXT STD/F1-" + numero + "-std.txt", "r") as fichier:
    lignes = fichier.readlines()

#remplissage matrice
for h in range(6,len(lignes)):
    if 'i' == lignes[h][0] :
        i = nbr_etats
    else :
        i = int(lignes[h][0])
    j = 97-ord(lignes[h][1])
    if table_std[i][j] == "":
        table_std[i][j] = lignes[h][2]
    else :
        table_std[i][j] += lignes[h][2]

print("\nTable de la matrice standardisée : ")
print("  | " + " | ".join([f"{chr(i + ord('a')):^4}"for i in range(nbr_symbole)]))
print("--+" + "+".join(["------" for i in range(nbr_symbole)]))

#affichage temporaire matrice
for g in range(nbr_etats+1):
    if g == nbr_etats and nbr_initial == 1 :
        break
    if g == nbr_etats:
        print("i", end=' | ')
        for h in range(nbr_symbole):
            if table_std[g][h] == "":
                print(f"{'--':^4}", end=' | ')
            else:
                print(f"{table_std[g][h]:^4}", end=' | ')
    else :
        print(g, end=' | ')
        for h in range(nbr_symbole):
            if table_std[g][h] == "":
                print(f"{'--':^4}", end=' | ')
            else:
                f"{i:*^9d}"
                print(f"{table_std[g][h]:^4}", end=' | ')
    print("")


#Créer une nouvelle matrice vide pour les transitions de déterministe
new_table = [[""] * nbr_symbole for i in range(nbr_etats)]

#Déterminisation
nouvelle_matrice_déterminisation = determinisation(etat_initiaux, table_transition, new_table, numero, nbr_symbole, nbr_etats)

#Affichage de la table de déterminisation
affichage_table_déterminisation(nouvelle_matrice_déterminisation[1], nouvelle_matrice_déterminisation[0], nbr_symbole)
