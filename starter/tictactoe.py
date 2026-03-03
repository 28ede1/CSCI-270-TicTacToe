from ttutil import print_board

def check_row_win(player, board):
    left = 0
    right = 3
    winning_row = [player] * 3
    while right <= len(board):
        current_row = board[left:right]

        if current_row == winning_row:
            return True
        left += 3
        right += 3
    return False
    

def check_col_win(player, board):
    left = 0
    mid = 3
    right = 6
    winning_col = [player] * 3

    while right < len(board):
        current_col = [board[left], board[mid], board[right]]
        if current_col == winning_col:
            return True
        
        left += 1
        mid += 1
        right += 1
    return False

def check_diagonal_win(player, board):
    winning_diag = [player] * 3
    forward_diagonal = [board[0], board[4], board[8]]
    backward_diagonal = [board[2], board[4], board[6]]

    return forward_diagonal == winning_diag or backward_diagonal == winning_diag

def check_win_conditions(board):
    player_x_has_won = check_row_win(1, board) or check_col_win(1, board) or check_diagonal_win(1, board)
    player_o_has_won = check_row_win(2, board) or check_col_win(2, board) or check_diagonal_win(2, board)


    if (not player_o_has_won and not player_x_has_won):
        return 0
    elif (player_x_has_won and player_o_has_won):
        raise Exception(f"There are two winners: {board}")
    elif player_x_has_won:
        return 1
    else:
        return 2
    
def play_game(player1_fn, player2_fn):
    raise NotImplementedError("Fill this in!")


def report_game(game):
    winner = check_win_conditions(game[-1])
    if winner == 0:
        print("\ntie!")
    else:
        print(f"\nplayer {winner} won!")
    for board in game:
        print_board(board)
        print("")
    return winner


def play_tournament(num_rounds, player1_fn, player2_fn):
    record = [0, 0, 0]  # ties, player1 wins, player2 wins
    for _ in range(num_rounds):
        game = play_game(player1_fn, player2_fn)
        winner = check_win_conditions(game[-1])
        record[winner] += 1
        game = play_game(player2_fn, player1_fn)
        winner = check_win_conditions(game[-1])
        if winner == 1:
            winner = 2
        elif winner == 2:
            winner = 1
        record[winner] += 1
    print(f"P1-P2-T: {record[1]}-{record[2]}-{record[0]}")


def compile_playbook():
    raise NotImplementedError("Fill this in!")
