
def create_board() -> list:
    '''
    :return: list for first board in each game
    '''
    return ['1','2','3','4','5','6','7','8','9']

def print_board(board):
    '''
    print all elements in list(board) in board format
    :param board: list of each board
    :return: no return
    '''
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]}')
    print()

def get_move(player, board) -> int:
    '''
    get from players choice of place on the board
    :param player: player in the current turn
    :param board: The current game board (updated with previous player selections for current turn)
    :return: player's choice
    '''
    while True:
        _choice = input(f'Player {player}, choose a place on the board:')
        if not _choice.isdigit() or int(_choice) < 1 or int(_choice) > 9  or _choice != board[int(_choice) - 1]:
            print('You need to choose a number between 1-9 except for the occupied spaces. Try again')
        else:
            break
    return int(_choice)

def make_move(board, position, symbol) -> list:
    '''
    Updating player selection on the game board
    :param board: The current game board (updated with previous player selections)
    :param position: A place on the board chosen by the player on the current turn
    :param symbol: A symbol that will appear on the game board in the location chosen by the player
    :return: list for an updated game board that includes the current turn selection
    '''
    new_list = board
    new_list.pop(position)
    new_list.insert(position, symbol)
    return new_list

def check_winner(board, symbol) -> bool | None:
    '''
    Checks if there is a winner
    :param board: Updated game board with all player selections
    :param symbol: The current player's symbol for checking victory on the game board
    :return:    True if there is a winner else None
    '''
    for i in range(3):
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
    '''
    Checking if the game is over and there is no winner
    :param board: Updated game board with all player selections
    :return: True If the entire board is full and there is no winner
    '''
    return all(i == '❌'  or i == '⭕' for i in board)

def switch_player(current) -> str:
    '''
    switch player for new turn
    :param current: The previous player
    :return: current: The player after switch turn
    '''
    if current == '❌':
        current = '⭕'
    else:
        current = '❌'
    return current

def play_game() -> str:
    '''
    running up the game with other functions
    :return: winner or draw
    '''
    print_board(create_board())
    _player = '⭕'
    new_board = None
    while True:
        _player = switch_player(_player)
        if new_board is None:
            new_board = create_board()
        place = get_move(_player, new_board) - 1
        new_board = make_move(new_board, place, '❌' if _player == '❌' else '⭕')
        print_board(new_board)
        if check_winner(new_board, _player):
            print(f'*** The winner is {_player} ! ***\n')
            return _player
        if is_tie(new_board):
            print(f'*** Game over. the result is draw ***\n')
            _player = 'draw'
            return _player

def scoreboard(new, total_x, total_o, total_draw) -> list:
    '''
    Prints and returns a scoreboard
    :param new: Current game result
    :param total_x: previous total winning of X
    :param total_o: previous total winning of O
    :param total_draw: previous total draw result
    :return: An updated list of the players' total wins and total draws, after updating the current game result
    '''
    if new == '❌':
        total_x += 1
    elif new == '⭕':
        total_o += 1
    else:
        total_draw += 1
    print(f'X total score: {total_x}\nO total score: {total_o}\nDraw total score: {total_draw}\n')
    return [total_x, total_o, total_draw]

def another_round() -> bool:
    '''
    Getting from user choose if to continue for another game
    :return: True if the user chose to continue for another game. else False
    '''
    while True:
        x = input('do you want to play again? (y/n): ')
        if x == 'y':
            return True
        elif x == 'n':
            return False
        else:
            print(f"Your answer should be y or n only. Try again")



total_score = [0, 0, 0]
while True:
    score = play_game()
    total_score = scoreboard(score, total_score[0], total_score[1], total_score[2])
    if not another_round():
        break

