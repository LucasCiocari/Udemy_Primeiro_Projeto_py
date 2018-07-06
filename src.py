def mostra_tabuleiro(valores):
    tabuleiro = ''
    for i in range(0,3):
        for j in range(0,3):
            tabuleiro += str(valores[i][j]) +'|'
        tabuleiro += '\n'
    print(tabuleiro)

def jogada(x,y, player, tab_status):
    if x in range(0,3) and y in range(0,3):
        tab_status[x][y] = player
    return tab_status

def vencedor(tab_status):
    for i in range(0,3):
        try_rows = lambda var : tab_status[i][0] == tab_status[i][1] and tab_status[i][1] == tab_status[i][2]
        try_columns = lambda var : tab_status[0][i] == tab_status[1][i] and tab_status[1][i] == tab_status[2][i]
        if try_rows(i):
            return tab_status[i][0]
        elif try_columns(i):
            return tab_status[0][i]
    #Continuar a checagem de quem ganhou!!

