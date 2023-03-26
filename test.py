from fonction import *


def determinisation_bis(table_entrée_sortie, nbr_symbole, nbr_etats, nbr_initial, etat_initiaux,
                        etat_finaux,table_transition, numero_automate, complet):
    table_deterministe = [[""] * nbr_symbole for i in range(nbr_etats)]

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
        #buffer = list(set([int(x) for x in table_etat[index]]))
        buffer = [int(x) for x in table_etat[index]]
        for each in buffer:
            for i in range(nbr_symbole):
                if (index < len(table_deterministe)):
                    if table_transition[each][i] != "":
                        if table_transition[each][i] not in table_deterministe[index][i] :
                            table_deterministe[index][i] += table_transition[each][i]
                else:
                    if table_transition[each][i] != "":
                        table_deterministe.append(["" for each in range(num_symbole)])
                        table_deterministe[index][i] += table_transition[each][i]

        for each in range(nbr_symbole):
            if table_deterministe[index][each] not in table_etat and table_deterministe[index][each] != "":
                table_etat.append(table_deterministe[index][each])
        index += 1


    if est_complet(table_deterministe) == 0 :
        table_deterministe = compléter_etat_poubelle(table_deterministe, table_etat, nbr_symbole)

    return table_deterministe, table_etat



def compléter_etat_poubelle(table_matrix, table_etat, num_symbole):

    for each in range(len(table_matrix)):
        for i in range(len(table_matrix[each])):
            if table_matrix[each][i] == '':
                table_matrix[each][i] = 'P'

    table_etat.append("P")
    transition_poubelle = []
    for each in range(num_symbole):
        transition_poubelle.append("P")

    table_matrix.append(transition_poubelle)
    return table_matrix
