players={'1':'X','2':'O'}

board =[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def boardupdate(i,j,value):
    board[i][j] = value

def printboard():
    for line in board:
        print(line)
        
def userinput(player):
     
    indexes =input(f'PLAYER {player} please input the indexes of the cell:')
    i = int(indexes.split()[0])
    j = int(indexes.split()[1])
    while board[i][j] != ' ':
        indexes =input(f'PLAYER {player} please input the indexes of the cell:')
        i = int(indexes.split()[0])
        j = int(indexes.split()[1])
    boardupdate(i,j,players[player])
        
def boardisnotfull():
    if board[0].count(' ') == 0 and board[1].count(' ') == 0 and board[2].count(' ') == 0:
        return False
    return True

def winner():
   
    #chaech in lines
    for line in board:
        if line.count('O') == 3:
            return '2'
        if line.count('X') == 3:
            return '1'
    #check in columns
    i=0
    while i<3:
        if board[0][i] == board[1][i] and board[1][i]==board[2][i]:
            if board[0][i]=='X':
                return '1'
            if board[0][i]=='O':
                return '2'
        
        i+=1
    
   #check in diagonal
    if board[0][0] == board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]=='X':
             return '1'
        if board[0][0]=='O':
              return '2'
            
    if board[0][2] == board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]=='X':
             return '1'
        if board[0][2]=='O':
              return '2'
        
    #the gameis not over
    return None
     
    
board =[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
printboard()
i=0
while boardisnotfull() and winner() == None:
    if i%2==0:
        userinput('1')
    else:
        userinput('2')
    printboard()
    i+=1
res = winner()
if res != '0':
    print(f'The winner is player {winner()}!!!!!!!!!!!!!!')
print ("Game is over.")