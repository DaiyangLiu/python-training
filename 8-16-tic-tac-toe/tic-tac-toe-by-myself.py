# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    print("这是个井字格游戏，X 先行，O后行\n"
          "井字格序号如下所示：\n"
          " 0 | 1 | 2 \n"
          "-----------\n"
          " 3 | 4 | 5 \n"
          "-----------\n"
          " 6 | 7 | 8 \n")

def ask_yes_no(question):
    response = None
    while response  not in ('y','n'):
        response=input(question).lower()
    return response

def ask_number(question,low,high):
    number = -1
    while number not in range(low,high):
        number = int(input(question))
    return number

def pieces():
    response = ask_yes_no("你愿意先行吗？(y/n):")
    if response == 'y':
        print("你先行棋，你的水平需要先行。")
        human = X
        computer = O
    else:
        print("小心，你的自大会毁掉你。")
        human= O
        computer = X
    return computer, human

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print(board[0]," | ",board[1], " | ",board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])

def legal_moves(board):
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            win=board[row[0]]
            return win

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    legal=legal_moves(board)

    location = None
    while location not in legal:
        location = ask_number("下一步行棋位置（0-8）：",0,NUM_SQUARES)
        if location not in legal:
            print("该行棋位置已经有棋子了，请选择其他未被占用的棋子。")

    return location

def computer_move(board, computer,human):
    board = board[:]
    legal = legal_moves(board)
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)

    for move in legal:
        board[move] = computer
        if winner(board) == computer:
            print("computer_move:",move)
            return move
        board[move] = EMPTY

    for move in legal:
        board[move] = human
        if winner(board) == human:
            print("computer_move:", move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal:
            print("computer_move:", move)
            return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner,computer,human):
    if the_winner == TIE:
        print("平局")
    elif the_winner == X:
        if human == X:
            print("算你走运，你赢了")
        else:
            print("你怎么可能斗得过我")
    else:
        if human == O:
            print("算你走运，你赢了")
        else:
            print("你怎么可能斗得过我")

if __name__=='__main__':
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()

    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner,computer, human)
