from players import *
from tictactoe import *
from ttutil import *

"""
given some player (1 or 2)

have 1 function check for row win condition

have 1 function check for col win condition

have 1 function check for diagonal win condition

return True/False


for the main function:

have one variable store result of the checking all 3 for player 1 (p1_won?)
have another variable store result of checking all 3 for player 1 (p2_won?)


if p1_won return 1
if p2_won return 2
if two winners 
return exception 

"""

def test_check_row_win():
    board_1 = [1, 1, 1, 0, 2, 0, 2, 0, 0]
    board_2 = [2, 0, 0, 1, 1, 1, 0, 2, 0]
    board_3 = [2, 0, 2, 1, 2, 0, 1, 1, 1]
    board_4 = [1, 1, 0, 2, 2, 0, 0, 0, 0]
    board_5 = [2, 2, 2, 1, 1, 0, 0, 0, 0]

    assert check_row_win(1, board_1) == True
    assert check_row_win(1, board_2) == True
    assert check_row_win(1, board_3) == True
    assert check_row_win(1, board_4) == False
    assert check_row_win(1, board_5) == False

    assert check_row_win(2, board_4) == False
    assert check_row_win(2, board_5) == True


def test_check_col_win():
    board_1 = [1, 2, 0, 1, 0, 2, 1, 0, 0] 
    board_2 = [2, 1, 0, 0, 1, 2, 0, 1, 0]
    board_3 = [2, 0, 1, 0, 2, 1, 0, 0, 1] 
    board_4 = [1, 2, 0, 1, 2, 0, 0, 0, 0] 
    board_5 = [2, 0, 0, 2, 1, 0, 2, 1, 0] 

    assert check_col_win(1, board_1) == True
    assert check_col_win(1, board_2) == True
    assert check_col_win(1, board_3) == True
    assert check_col_win(1, board_4) == False
    assert check_col_win(1, board_5) == False

    assert check_col_win(2, board_4) == False
    assert check_col_win(2, board_5) == True

def test_check_diagonal_win():
    board_1 = [1, 2, 0, 0, 1, 2, 0, 0, 1] 
    board_2 = [0, 2, 1, 2, 1, 0, 1, 0, 0] 
    board_3 = [2, 0, 0, 0, 2, 1, 0, 1, 2]  
    board_4 = [1, 2, 0, 0, 2, 1, 0, 0, 0]  
    board_5 = [2, 1, 2, 0, 2, 0, 2, 0, 1]  

    assert check_diagonal_win(1, board_1) == True
    assert check_diagonal_win(1, board_2) == True
    assert check_diagonal_win(1, board_3) == False
    assert check_diagonal_win(1, board_4) == False
    assert check_diagonal_win(1, board_5) == False

    assert check_diagonal_win(2, board_4) == False
    assert check_diagonal_win(2, board_3) == True
    assert check_diagonal_win(2, board_5) == True

def test_check_win_conditions():
    assert check_win_conditions([1, 2, 2, 0, 1, 1, 2, 0, 0]) == 0
    assert check_win_conditions([1, 2, 2, 0, 1, 1, 2, 0, 1]) == 1
    assert check_win_conditions([2, 2, 2, 0, 1, 1, 1, 0, 0]) == 2

    try:
        check_win_conditions([2, 2, 2, 1, 1, 1, 0, 0, 0])
        assert False  # If we reach this, no exception was raised → FAIL
    except Exception:
        pass  # Expected behavior

if __name__ == "__main__":
    test_check_row_win()
    print("test_check_row_win ✅")

    test_check_col_win()
    print("test_check_col_win ✅")

    test_check_diagonal_win()
    print("test_check_diagonal_win ✅")

    test_check_win_conditions()
    print("test_check_win_conditions ✅")