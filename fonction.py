def est_deterministe (table,nbr_initial):
    deterministe = False
    if nbr_initial > 1:
        print("Cet automate n'est pas déterministe car il possède plusieurs états initiaux")
    for i in range (len(table)):
        for j in range (len(table[i])):
            if len(table[i][j])>1 and deterministe == False:
                print("Cet automate n'est pas déterministe car il ne possède pas au plus 1 transition pour un état ")
                deterministe = True


def est_complet (table):
    k=0
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j]=='':
                k=k+1
    if k>0:
        print("cet automate n'est pas complet car il possède des états vides \n")
        return 0
    else:
        print("Cet automate est complet\n")
        return 1


def affichage_table(nbr_etats,table_entrée_sortie,nbr_initial,nbr_symbole,table_std,std):
    print("-------" + "-".join(["------" for i in range(nbr_symbole + 1)]) + "-")
    print("|{:^5}|{:^6}|".format("E/S", "ETAT"), end="")
    for k in range(nbr_symbole):
        letter = chr(k + 97)
        print(f"{letter:^6}", end="|")
    print("")
    print("------+" + "+".join(["------" for i in range(nbr_symbole + 1)]) + "-")

    for g in range(nbr_etats):
        if g == nbr_etats-1 and nbr_initial == 1 and std == 1:
            break
        print(f"|{table_entrée_sortie[g]:^5}", end="| ")
        if g == nbr_etats-1 and std == 1:
            print(f"{'i':^4}", end=' | ')
            for h in range(nbr_symbole):
                if table_std[g][h] == "":
                    print(f"{'--':^4}", end=' | ')
                else:
                    print(f"{table_std[g][h]:^4}", end=' | ')
        else:
            print(f"{g:^4}", end=' | ')
            for h in range(nbr_symbole):
                if table_std[g][h] == "":
                    print(f"{'--':^4}", end=' | ')
                else:
                    print(f"{table_std[g][h]:^4}", end=' | ')
        print("")
    print("-------" + "-".join(["------" for i in range(nbr_symbole + 1)]) + "-")
