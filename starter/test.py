from players import *
from tictactoe import *
from ttutil import *

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