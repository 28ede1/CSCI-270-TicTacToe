from ttutil import print_board
from players import random_player_fn, create_optimal_player_fn

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

def board_is_filled(board):
    return 0 not in board

def play_game(player1_fn, player2_fn):
    """
    pseudo

    initialize game board historlist
    create empty board
    add empty board to history
    set current_player = 1  # X starts use *-1 to switch

    while game not over:  # check both win conditions and full board
        get the current board (latest board from history)

        if current_player == 1, move = player1_fn(board)
        else, move = player2_fn(board)

        board[move] = current_player (1, or 2)
        add a copy of board to history
    """
    game_history = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    turn = 1 # x (player 1) is pos, o (player 2) is neg
    
    while not board_is_filled(game_history[-1]) and (check_win_conditions(game_history[-1]) == 0):
        new_board = list(game_history[-1])

        if turn == 1:
            next_move = player1_fn(new_board)
            new_board[next_move] = 1
        else:
            next_move = player2_fn(new_board)
            new_board[next_move] = 2

        game_history.append(new_board)
        turn *= -1

    return game_history

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
    """
    'maximizer' stores which player is currently maximizing
    'current_turn' stores whose turn it currently is
    'playerbook' is a dictionary that (based on current board state key) stores a list of best moves to make
    """
    def minimax(board, maximizer, current_turn, move_playbook):
        winner = check_win_conditions(board)
        best_moves = []

        
        if winner != 0:
            if maximizer == winner:
                minimax_value = 1
            else:
                minimax_value = -1

        elif board_is_filled(board):
            minimax_value = 0

        else:
            next_player = 1 if current_turn != 1 else 2
            minimax_value = float("-inf") if maximizer == current_turn else float("inf")

            for i in range(len(board)):
                if board[i] == 0:
                    
                    board[i] = current_turn
                    possible_move_final_outcome = minimax(board, maximizer, next_player, move_playbook)

                    if maximizer == current_turn:
                        if possible_move_final_outcome > minimax_value:
                            best_moves = [i]
                            minimax_value = possible_move_final_outcome
                        elif possible_move_final_outcome == minimax_value:
                            best_moves.append(i)
                            minimax_value = possible_move_final_outcome

                    else:
                        if possible_move_final_outcome < minimax_value:
                            best_moves = [i]
                            minimax_value = possible_move_final_outcome
                        elif possible_move_final_outcome == minimax_value:
                            best_moves.append(i)
                            minimax_value = possible_move_final_outcome
                    
                    board[i] = 0
        move_playbook[tuple(board)] = best_moves

        return minimax_value
    new_playbook = {}
    minimax([0,0,0,0,0,0,0,0,0], 1, 1, new_playbook)
    return new_playbook
    
if __name__ == "__main__":
    # game = play_game(random_player_fn, random_player_fn)
    # report_game(game)


    # playbook = compile_playbook()
    # test = playbook[(0, 0, 0, 0, 1, 0, 0, 0, 0)]
    # print(test)


    playbook = compile_playbook()

    player1 = create_optimal_player_fn(playbook)
    player2 = create_optimal_player_fn(playbook)
    play_tournament(100, player1, player2)
