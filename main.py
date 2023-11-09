import random
board =[["x","a","*","*","*"],["x","b","*","*","*"],["x","x","*","*","*"],["x","*","*","*","*"],["x","*","*","*","*"]]
array = ["_","x","e","r"]


for i in board:
    print(i)

UX = input("give x coordinates")
int_UX = int(UX)

UY = input("give y coordinates")
int_UY = int(UY)

choice = board[int_UY][int_UX]
#back = board[int_UY][int_UX-1]
#front = board[int_UY][int_UX+1]
#up = board[int_UY-1][int_UX]
#down = board[int_UY+1][int_UX]
print(choice , "choice")
score = 0

def check_logic(int_UY,int_UX):
    #global int_UX
    #global int_UY
    global  choice
    global score
    '''
    if int_UX - 1 > 0:
        back = board[int_UY][int_UX - 1]
        print(back, "- back")
        print(int_UY,int_UX - 1)

    if int_UX + 1 < 5:
        front = board[int_UY][int_UX + 1]
        print(front,"- front")
        print(int_UY, int_UX + 1)

    if int_UY - 1 > 0:
        up = board[int_UY - 1][int_UX]
        print(up, "- up")
    '''
    if int_UY + 1 < 5:
        down = board[int_UY + 1][int_UX]
        print(down, "= down")
        print(int_UY+1, int_UX)


    if down == choice:
        print(choice,"line48")
        score = score +1
        print(score)
        check_logic(int_UY+1, int_UX)



check_logic(int_UY,int_UX)








'''
if int_UY != 0:
    if board[int_UY][int_UX] == board[int_UY-1][int_UX]:
        print(board[int_UY][int_UX], "is found at", int_UY-1 , int_UX )
        
shape = board[int_UX][ int_UY]
if shape == board[int_UX][int_UY]:
    print(int_UX)
'''


