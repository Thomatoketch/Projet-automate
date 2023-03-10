import os
from fonction import *

list = os.listdir("Fichier TXT") # dir is your directory path
number_files = len(list)
numero = 9999

while int(numero) > number_files:
    print("Il y a ",number_files, " fichiers. Quel fichier voulez vous ouvrir ? ")
    numero = input()
file = "Fichier TXT/F1-"+numero+".txt"
fichier = open(file, "r")
lignes = fichier.readlines()
fichier.close()


nbr_symbole = int(lignes[0])
nbr_etats = int(lignes[1])
nbr_initial = int(lignes[2][0])
nbr_final = int(lignes[3][0])
nbr_transition = int(lignes[4])


etat_initiaux=[]
trouver_etat(etat_initiaux,2,lignes)

etat_finaux=[]
trouver_etat(etat_finaux,3,lignes)


print("les etats initiaux sont :",etat_initiaux)
print("les etats terminaux sont :",etat_finaux)
print("la table de transitions est :")


table = creation_matrice_vide(nbr_etats,nbr_symbole)


#remplissage matrice
for h in range(6,len(lignes)):
    i = int(lignes[h][0])
    j = 97-ord(lignes[h][1])
    if table[i][j] == "":
        table[i][j] = lignes[h][2]
    else :
        table[i][j] += lignes[h][2]


#affichage temporaire matrice
for g in range(nbr_etats):
    print(g, end='| ')
    for h in range(nbr_symbole):
        if table[g][h] == "":
            print("--", end=' | ')
        else:
            print(table[g][h], end=' | ')
    print("")

if nbr_initial > 1:
    rep = input("si vous voulez standardiser votre automate, tapez oui : ")
    if rep == "oui" :
        for i in range(nbr_initial):
            if etat_initiaux[i] in etat_finaux:
                etat_finaux.append("i")
        for i in range(6,len(lignes)-1):
            for j in etat_initiaux:
                if lignes[i][0] == str(j) :
                    with open("Fichier TXT/F1-"+numero+".txt", "a") as fichier:
                        fichier.write("\ni"+lignes[i][1:3])
        etat_initiaux = ["i"]

table_std = creation_matrice_vide(nbr_etats+1,nbr_symbole)
with open("Fichier TXT/F1-" + numero + ".txt", "r") as fichier:
    lignes = fichier.readlines()

#remplissage matrice
for h in range(6,len(lignes)):
    i = int(lignes[h][0])
    j = 97-ord(lignes[h][1])
    if table_std[i][j] == "":
        table_std[i][j] = lignes[h][2]
    else :
        table_std[i][j] += lignes[h][2]


print("\nTable de la matrice standardisée : ")


#affichage temporaire matrice
for g in range(nbr_etats+1):
    if g == nbr_etats :
        print("i", end='| ')
        for h in range(nbr_symbole):
            if table_std[g][h] == "":
                print("--", end=' | ')
            else:
                print(table_std[g][h], end=' | ')
    else :
        print(g, end='| ')
        for h in range(nbr_symbole):
            if table_std[g][h] == "":
                print("--", end=' | ')
            else:
                print(table_std[g][h], end=' | ')
    print("")