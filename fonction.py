def trouver_etat(etat,nbLigne,lignes):
    i = 0
    debut_etat = ""
    while debut_etat != ' ':
        debut_etat = lignes[nbLigne][i]
        i += 1
    while i < len(lignes[nbLigne]) - 1:
        temp = ""
        while lignes[nbLigne][i] != " " and i < len(lignes[nbLigne]) - 1:
            temp += lignes[nbLigne][i]
            i += 1
        etat.append(int(temp))
        i += 1

# creation de la matrice vide
def creation_matrice_vide(nbr_etats,nbr_symbole):
    matrice = []
    for g in range(nbr_etats):
        ligne = []
        for h in range(nbr_symbole):
            ligne.append('')
        matrice.append(ligne)
    return matrice

def affichage_matrice(table,nbr_etats,nbr_symbole):
    for g in range(nbr_etats+1):
        if g == nbr_etats:
            print("\n\n\n")
            print("i", end='| ')
            for h in range(nbr_symbole):
                if table[g][h] == "":
                    print("--", end=' | ')
                else:
                    print(table[g][h], end=' | ')
        else:
            print(g, end='| ')
            for h in range(nbr_symbole):
                if table[g][h] == "":
                    print("--", end=' | ')
                else:
                    print(table[g][h], end=' | ')
        print("")