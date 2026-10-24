# 2. Tic Tac Toe Game
board=[' ']*9

def show():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])

def win(p):
    lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(board[i]==p for i in line) for line in lines)

for turn in range(9):
    p='X' if turn%2==0 else 'O'
    pos=int(input(f'{p} position (1-9): '))-1
    board[pos]=p
    show()
    if win(p):
        print(p,'wins!')
        break
else:
    print('Draw!')

# Output:
# X wins!