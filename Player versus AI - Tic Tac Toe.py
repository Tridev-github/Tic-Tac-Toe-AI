board = [['','',''],['','',''],['','','']]

def player():
    while True:
        try:
            x = [int(place) for place in input("Give the coordinates of the block you want to insert in ").split(" ")]
            if board[x[0]][x[1]]=='':
                board[x[0]][x[1]]='o'
                break
            else:
                print("Already choosen, choose another block")
        except:
            print("Choose the correct block")

def minimax(isMax):
    score = checkResult()
    if (score == 1):
        return score
    if (score == -1):
        return score
    if (score==0):
        return 0

    if (isMax):
        best = -1000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == ''):
                    board[i][j] = 'x'
                    best = max(best, minimax(not isMax))
                    board[i][j] = ''
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == ''):
                    board[i][j] = 'o'
                    best = min(best, minimax(not isMax))
                    board[i][j] = ''
        return best
def ai():
    optimum=-100
    optimumMove=[-1,-1]
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                board[i][j]='x'
                temp = minimax(False)
                board[i][j]=''
                if temp>optimum:
                    optimumMove.clear()
                    optimumMove.append(i)
                    optimumMove.append(j)
                    optimum=temp
    board[optimumMove[0]][optimumMove[1]]='x'

def checkResult():
    draw = 0
    for i in range(3):
        row_x=0
        col_x=0
        row_o = 0
        col_o = 0
        diag_x=0
        diag_o=0

        for j in range(3):
            if  board[i][j]=='x':
                row_x+=1
            if  board[i][j]=='o':
                row_o+=1
            if board[j][i] == 'x':
                col_x += 1
            if board[j][i] == 'o':
                col_o += 1
            if board[i][j]=='':
                draw+=1
            if board[j][j]=='x':
                diag_x+=1
            if board[j][j]=='o':
                diag_o+=1
        if board[0][2]==board[1][1]==board[2][0]:
            if board[1][1]=='x':
                return 1
            elif board[1][1]=='o':
                return -1
        if row_x==3 or col_x==3 or diag_x==3:
            return 1
        if row_o==3 or col_o==3 or diag_o==3:
            return -1
    if draw == 0:
        return 0
    return 5


for i in range(3):
    print(board[i])
while True:
    player()
    print("Player:")
    for i in range(3):
        print(board[i])
    if checkResult()==0:
        print("Draw")
        break
    elif checkResult()==1:
        print("AI wins")
        break
    elif checkResult()==-1:
        print("Player wins")
        break
    print("AI:")
    ai()
    for i in range(3):
        print(board[i])
    if checkResult()==0:
        print("Draw")
        break
    elif checkResult()==1:
        print("AI wins")
        break
    elif checkResult()==-1:
        print("Player wins")
        break
