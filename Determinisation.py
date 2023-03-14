def determinisation(etat_initiaux, table_matrix, nouvelle_matrix_vide, numero_automate, num_symbole, num_etat):
    trigger = 0
    
    # vérifier si l'automate est déterministe
    for each in str(table_matrix):
        for i in each:
            if len(i) > 1:
                trigger = 1
                break
                
        if trigger == 1:
            break

    if trigger == 0:
        etats_originaux = [x for x in range(num_etat)]
        print(f"L'automate {numero_automate} est déjà déterministe")
        
        #compléter l'automate avec l'etat poubelle
        table_matrix = compléter_etat_poubelle(table_matrix, etats_originaux, num_symbole)
        return table_matrix, etats_originaux

    # Déterminiser l'automate
    table_etat = []
    new_etat_initiaux = ""

    # Fusionner les états initiaux
    if (len(etat_initiaux) > 1):
        for each in etat_initiaux:
            new_etat_initiaux.join(each)
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

def compléter_etat_poubelle(table_matrix, table_etat, num_symbole):

    for each in range(len(table_matrix)):
        for i in range(len(table_matrix[each])):
            if table_matrix[each][i] == '':
                table_matrix[each][i] = 'p'

    table_etat.append("p")
    transition_poubelle = []
    for each in range(num_symbole):
        transition_poubelle.append("p")

    table_matrix.append(transition_poubelle)
    return table_matrix



def affichage_table_déterminisation(table_etat, matrice_déterminisation, num_symbole):
    print("\nTable de la matrice déterministe :\n ")

    print("-------------------")
    print("|{:<3} | ".format(""),end="")
    for k in range(num_symbole):
        letter = chr(k+97)
        print(f"{letter:^5}", end="|")
    print("")
    print("-------------------")

    index = 0
    for each in table_etat:

        print(f"|{each:<3}", end=" | ")
        for i in matrice_déterminisation[index]:
            print(f"{i:^5}", end="|")
        print("")
        index += 1
    print("-------------------")
