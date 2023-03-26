import os
from fonction import *
from determinisation import *
from Reconnaissance import *
from test import *

liste = os.listdir("Fichier TXT") # dir is your directory path
number_files = len(liste)
numero = 9999

while int(numero) > number_files:
    print("Il y a ",number_files, " fichiers. Quel fichier voulez vous ouvrir ? ")
    numero = input()

file_path = "Fichier TXT/F3-"+numero+".txt"

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


#table des etats d'entrée et sorties
table_entrée_sortie = [""] * nbr_etats
for i in range(nbr_etats):
    if i in etat_finaux:
        table_entrée_sortie[i] = "S"
    if i in etat_initiaux:
        table_entrée_sortie[i] += "E"


print("Les etats initiaux sont :",etat_initiaux)
print("Les etats terminaux sont :",etat_finaux)


# Créer une table de transition vide
table_transition = [[""] * nbr_symbole for i in range(nbr_etats)]

# Ajouter les transitions
for i in range(nbr_transition):
    transition = lignes[6+i].strip()
    etat_depart = int(transition[0])
    symbole = ord(transition[1]) - ord('a')
    etat_arrivee = transition[2]
    table_transition[etat_depart][symbole] += etat_arrivee

print("Table de transition:")
affichage_table(nbr_etats,table_entrée_sortie,nbr_initial,nbr_symbole,table_transition,0)

etat_initiaux_std = etat_initiaux
etat_finaux_std = etat_finaux
nbr_initial_std = nbr_initial

print("Voici les informations concernant cet automate:\n")
est_deterministe(table_transition, nbr_initial)
if nbr_initial>1:
    print("Cet automate n'est pas standard car il possède plusieurs entrées\n")
else:
    print("Cet automate ne possède qu'une seule entrée, il est donc standard\n")
complet = est_complet(table_transition)

# Standardiser l'automate si nécessaire
if nbr_initial > 1:
    rep = input("si vous voulez standardiser votre automate, tapez oui : ")
    if rep == "oui" :
        for i in range(nbr_initial):
            if etat_initiaux_std[i] in etat_finaux:
                etat_finaux.append("i")

        for i in range(6,len(lignes)):
            for j in etat_initiaux_std:
                if lignes[i][0] == str(j) :
                    lignes.append("\ni"+lignes[i][1:3])
        etat_initiaux_std = ["i"]

        with open("Fichier TXT STD/F3-" + numero + "-std.txt", "w") as fichier:
            if nbr_initial > 1 :
                lignes[1] = str(int(lignes[1])+1) + "\n"
                lignes[2] = "1 i\n"
                lignes[4] = str(len(lignes) - 6) + "\n"
            for i in range(len(lignes)) :
                fichier.write(str(lignes[i]))

        table_std = [[""] * nbr_symbole for i in range(nbr_etats+1)]

        with open("Fichier TXT STD/F3-" + numero + "-std.txt", "r") as fichier:
            lignes = fichier.readlines()

        nbr_etats_std = nbr_etats + 1
        nbr_transition = int(lignes[4].strip())

        # Ajouter les transitions
        for i in range(nbr_transition):
            transition = lignes[6+i].strip()
            if transition[0] not in str([0,1,2,3,4,5,6,7,8,9]):
                etat_depart = nbr_etats_std-1
            else :
                etat_depart = int(transition[0])
            symbole = ord(transition[1]) - ord('a')
            etat_arrivee = transition[2]
            if table_std[etat_depart][symbole] != etat_arrivee:
                table_std[etat_depart][symbole] += etat_arrivee

        # Mise a jour de la table des etats d'entrée et sorties
        table_entrée_sortie_std = [""] * nbr_etats_std
        for i in range(nbr_etats_std):
            if i in etat_finaux:
                table_entrée_sortie_std[i] = "S"
            if i == nbr_etats_std-1 :
                table_entrée_sortie_std[i] += "E"


        print("\nTable de la matrice standardisée : ")
        affichage_table(nbr_etats_std,table_entrée_sortie_std,nbr_initial_std,nbr_symbole,table_std,1)





rep2=input("Si vous voulez déterminiser et ensuite compléter votre automate, tapez oui: ")
if rep2=="oui":
    nouvelle_matrice_déterminisation = determinisation_bis(table_entrée_sortie, nbr_symbole, nbr_etats, nbr_initial, etat_initiaux, etat_finaux,table_transition,numero,complet)
    nouveaux_etats = [str(x) for x in nouvelle_matrice_déterminisation[1]]

    #Les états entrees et sorties déterministe
    nouvelle_etats_sorties_déterministe = trouver_entree_sorties_déterministe(etat_finaux, nouveaux_etats,nbr_etats)
    #L'état initial
    nouvelle_etats_sorties_déterministe[0] += "E"

    affichage_table_déterminisation(nouveaux_etats, nouvelle_matrice_déterminisation[0], nbr_symbole, nouvelle_etats_sorties_déterministe,1)

rep3=input("Si vous souhaitez savoir si un mot est reconnu par votre automate, tapez oui: ")
if rep3=="oui":
    #La reconnaissance de mot
    mot = input("Inserer le mot que vous souhaitez rechercher : ")
    etats_sorties = trouver_entree_sorties_déterministe(etat_finaux, nouveaux_etats, nbr_etats)
    reconnaissance_mots(nouveaux_etats, mot, nouvelle_matrice_déterminisation[0], etats_sorties, nbr_symbole)

rep4=input("Si vous souhaitez afficher la table qui reconnait le langage complémentaire de votre automate, tapez oui: ")
if rep4=="oui":
    #complément
    etat_entree_sorties_complement = automate_complément(nouvelle_etats_sorties_déterministe)
    #affichage de table complémentaire
    affichage_table_déterminisation(nouveaux_etats, nouvelle_matrice_déterminisation[0], nbr_symbole, etat_entree_sorties_complement,2)



"""
est_deterministe (table_transition,nbr_initial)
est_complet (table_transition)

#Créer une nouvelle matrice vide pour les transitions de déterministe
new_table = [[""] * nbr_symbole for i in range(nbr_etats)]

#Déterminisation
nouvelle_matrice_déterminisation = determinisation(etat_initiaux, table_transition, new_table, numero, nbr_symbole, nbr_etats)
#nouveaux_etats déterministes
nouveaux_etats = [str(x) for x in nouvelle_matrice_déterminisation[1]]


#Les états entrees et sorties déterministe
nouvelle_etats_sorties_déterministe = trouver_entree_sorties_déterministe(etat_finaux, nouveaux_etats)
#L'état initial
nouvelle_etats_sorties_déterministe[0] += "E"

#affichage de table déterministe
affichage_table_déterminisation(nouveaux_etats, nouvelle_matrice_déterminisation[0], nbr_symbole, nouvelle_etats_sorties_déterministe,1)

#complément
etat_entree_sorties_complement = automate_complément(nouvelle_etats_sorties_déterministe)

#affichage de table complémentaire
affichage_table_déterminisation(nouveaux_etats, nouvelle_matrice_déterminisation[0], nbr_symbole, etat_entree_sorties_complement,2)


#La reconnaissance de mot
mot = input("Inserer le mot pour l'automate : ")
etats_sorties = trouver_entree_sorties_déterministe(etat_finaux, nouveaux_etats)
reconnaissance_mots(nouveaux_etats, mot, nouvelle_matrice_déterminisation[0], etats_sorties)
"""
