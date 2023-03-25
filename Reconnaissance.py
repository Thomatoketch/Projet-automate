def reconnaissance_mots(nouveaux_etats, mot, table_transition, etat_sorties,nbr_symbole):

    #créer une dictionnaire pour indexer chaque état
    dictionnaire_etat = {}
    index = 0;
    buffer = nouveaux_etats[0]

    for each in nouveaux_etats:
        dictionnaire_etat[each] = index
        index += 1

    #Parcourir le mot par la table de transition
    for i in range(len(mot)):

        if (ord(mot[i])-97) >= nbr_symbole or (ord(mot[i])-97) < 0:

            print("Le mot n'est pas connaissable par l'automate")
            return

        buffer = table_transition[dictionnaire_etat.get(buffer)][ord(mot[i])-97]
        if buffer == "P":
            print("Le mot n'est pas connaissable par l'automate")
            return

    liste_sortie = []
    index = 0

    #créer la liste pour stocker les états de sortie
    for each in etat_sorties:
        if each == "S":
            liste_sortie.append(nouveaux_etats[index])
        index += 1
    print("Le mot est connaissable par l'automate") if buffer in liste_sortie else print("Le mot n'est pas connaissable par l'automate")