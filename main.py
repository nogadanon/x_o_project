

def create_board() -> list:
    return ['1','2','3','4','5','6','7','8','9']

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]}')

def get_move(player, board) -> int:
    if player == 1:
        icon = '❌'
    else:
        icon = '⭕'
    while True:
        _choice = input(f'Player {icon}, choose a place on the board:')
        if int(_choice) == int(board[int(_choice) - 1]):
            break
        else:
            print('You need to choose a number between 1-9 except for the occupied spaces. Try again')
    return int(_choice)



def make_move(board, position, symbol): #-> list:
    new_list = board
    new_list.pop(position)
    new_list.insert(position, symbol)
    return new_list


def check_winner(board, symbol) -> bool:
    for i in board:
        if board[i] == board[i + 3] == board[i + 6] == symbol:
            return True
    i = 0
    while i <= 6:
        if board[i] == board[i + 1] == board[i + 2] == symbol:
            return True
        else:
            i += 3
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True

def is_tie(board) -> bool:
    return all(i for i in board == '❌' or '⭕')

def switch_player(current = 1) -> int:
    if current == 1:
        player_is = '❌'
    else:
        player_is = '⭕'
    current = (current) * -1
    return player_is

def play_game():
    print_board(create_board())
    _player = switch_player()
    place = get_move(1, create_board()) - 1
    new_board = make_move(create_board(), place, '❌' if switch_player() == '❌' else '⭕')
    print_board(new_board)


    #def make_move(board, position, symbol) -> list:



play_game()


#player
#board
#sy