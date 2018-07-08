def mostra_tabuleiro(valores):
    tabuleiro = ''
    for i in range(0,3):
        for j in range(0,3):
            tabuleiro += str(valores[i][j]) +'|'
        tabuleiro += '\n'
    print(tabuleiro)

def jogada(x,y, player, tab_status):
    if x in range(0,3) and y in range(0,3) and tab_status[x][y] == 0:
        tab_status[x][y] = player
    return tab_status

def vencedor(tab_status):
    try_dp = lambda  : tab_status[0][0] == tab_status[1][1] and tab_status[1][1] == tab_status[2][2]
    try_ds = lambda  : tab_status[0][2] == tab_status[1][1] and tab_status[1][1] == tab_status[2][0]
    for i in range(0,3):
        try_rows = lambda var : tab_status[i][0] == tab_status[i][1] and tab_status[i][1] == tab_status[i][2]
        try_columns = lambda var : tab_status[0][i] == tab_status[1][i] and tab_status[1][i] == tab_status[2][i]
        if try_rows(i):
            return tab_status[i][0]
        elif try_columns(i):
            return tab_status[0][i]
    if try_dp():
        return tab_status[0][0]
    elif try_ds():
        return tab_status[0][2]
    return 0


tabuleiro = []
tabuleiro += [[0,0,0],[0,0,0],[0,0,0]]
venceu = 0
jogador = 1
while(venceu == 0):
    print("É a vez do jogador %d." %(jogador))    
    x = input()
    y = input()
    
    tabuleiro = jogada(int(x),int(y),jogador,tabuleiro)
    mostra_tabuleiro(tabuleiro)
    venceu = vencedor(tabuleiro)
    jogador = jogador % 2 + 1
print("Jogador %d foi o vencedor!"%(venceu)) 

