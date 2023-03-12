def est_deterministe (table,nbr_initial):

    for i in range (len(table)):
        for j in range (len(table[i])):
            if len(table[i][j])>1:
                print("Cet automate n'est pas déterministe car il ne possède pas au plus 1 transition pour un état ")
            if nbr_initial > 1:
                print("Cet automate n'est pas déterministe car il possède plusieurs états initiaux")


def est_complet (table):
    k=0
    for i in range (len(table)):
        for j in range (len(table[i])):
            if table[i][j]=='':
                k=k+1
    if k>0:
        print("cet automate n'est pas complet car il possède des états vides ")
    else:
        print("Cet automate est complet")
