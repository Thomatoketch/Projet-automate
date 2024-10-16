"""
def determinisation(etat_initiaux, table_matrix, nouvelle_matrix_vide, numero_automate, num_symbole, num_etat):
    trigger = 0

    # vérifier si l'automate est déterministe
    for each in table_matrix:

        if len(etat_initiaux) != 1:
            trigger = 1
            break

        for i in each:
            if len(i) > 1:
                trigger = 1

                break
        if trigger == 1:
            break

    if trigger == 0:
        etats_originaux = [x for x in range(num_etat)]
        print(f"L'autom+ate {numero_automate} est déjà déterministe")

        table_matrix = compléter_etat_poubelle(table_matrix, etats_originaux, num_symbole)
        return table_matrix, etats_originaux

    # Déterminiser l'automate
    table_etat = []
    new_etat_initiaux = ""

    # Fusionner les états initiaux
    if (len(etat_initiaux) > 1):
        for each in etat_initiaux:
            new_etat_initiaux += str(each)
    else:
        new_etat_initiaux = f"{etat_initiaux[0]}"

    table_etat.append(new_etat_initiaux)

    # Remplir la matrice
    index = 0
    while (index < len(table_etat)):

        # transformer str en int
        buffer = [int(x) for x in table_etat[index]]

        for each in buffer:
            for i in range(num_symbole):
                if(index < len(nouvelle_matrix_vide)):
                    nouvelle_matrix_vide[index][i] += table_matrix[each][i]
                else:

                    nouvelle_matrix_vide.append(["" for each in range(num_symbole)])
                    nouvelle_matrix_vide[index][i] += table_matrix[each][i]

        for each in range(num_symbole):
            if nouvelle_matrix_vide[index][each] not in table_etat:
                table_etat.append(nouvelle_matrix_vide[index][each])

        index += 1

    # compléter la table avec l'état poubelle
    nouvelle_matrix_vide = compléter_etat_poubelle(nouvelle_matrix_vide, table_etat, num_symbole)

    return nouvelle_matrix_vide, table_etat
"""

def compléter_etat_poubelle(table_matrix, table_etat, num_symbole): 

    for each in range(len(table_matrix)):               #ajouter 'P' dans la table de transitions
        for i in range(len(table_matrix[each])):
            if table_matrix[each][i] == '':
                table_matrix[each][i] = 'P'

    table_etat.append("P")                              #ajouter 'P' dans la table des états initiaux
    transition_poubelle = []
    for each in range(num_symbole):
        transition_poubelle.append("P")                 #ajouter 'P' dans les états de transitions de l'état P

    table_matrix.append(transition_poubelle)
    return table_matrix



def affichage_table_déterminisation(table_etat, matrice_déterminisation, num_symbole, etats_sorties, indice):

    indice = "déterministe" if indice ==1 else "complémentaire"
    print(f"\nTable de l'automate {indice} et complet:\n ")

    print("-----------------"+"------"*num_symbole)
    print("|{:^5}|{:^9}|".format("E/S","ETAT"),end="")
    for k in range(num_symbole):
        letter = chr(k+97)
        print(f"{letter:^5}", end="|")
    print("")
    print("-----------------"+"------"*num_symbole)

    index = 0
    for each in table_etat:

        print(f"|{etats_sorties[index]:^5}", end="| ")
        print(f"{each:^7}", end=" |")
        for i in matrice_déterminisation[index]:
            print(f"{i:^5}", end="|")
        print("")
        index += 1
    print("-----------------"+"------"*num_symbole)


#Les états entrees et sorties déterministe
def trouver_entree_sorties_déterministe(etat_sortie, table_etat_déterministe,nbr_etat): #D'abord compléter avec des 'S' en langage normal.
                                                                                        #Ensuite ajouter un 'E'dans le main à la première case

    etats_entree_sorties_déterministe = [''] * len(table_etat_déterministe)

    for each in etat_sortie:
        each = str(each)
        index = 0
        h = 0
        for i in table_etat_déterministe:

            if each in i:
                etats_entree_sorties_déterministe[h] = "S"
            elif each in i and etats_entree_sorties_déterministe[index] == "":
                    etats_entree_sorties_déterministe[index] += "S"
            h+=1

    return etats_entree_sorties_déterministe

def automate_complément(etat_entree_sortie):                                           #Enfin, inverser le résultat pour le langage complémentaire

    index = 0
    for each in etat_entree_sortie:

        if each == "" or each == "E":
            etat_entree_sortie[index] += "S"
            index += 1
        elif "S" in each:
            etat_entree_sortie[index] = etat_entree_sortie[index].strip("S")
            index += 1

    return etat_entree_sortie
