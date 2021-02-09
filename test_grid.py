from grid import grid_to_string
from player import Player
import game_parser

def test_grid():
    player = Player()

    ## Positive test cases ##

    grid = game_parser.parse(game_parser.read_lines('board_simple.txt'))
    assert grid_to_string(grid, player) == "A*X**\n*   *\n**Y**\n\nYou have 0 water buckets.", "Positive test case 1 failed."
    grid = game_parser.parse(game_parser.read_lines('board_medium.txt'))
    assert grid_to_string(grid, player) == "A*X***\n*    *\n* ** *\n*    *\n*    *\n****Y*\n\nYou have 0 water buckets.", "Positive test case 2 failed."
    grid = game_parser.parse(game_parser.read_lines('board_hard.txt'))
    assert grid_to_string(grid, player) == "AX*************\n*       2 *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***      *\n* 1********F  *\n*************Y*\n\nYou have 0 water buckets.", "Positive test case 3 failed."
    grid = game_parser.parse(game_parser.read_lines('board.txt'))
    assert grid_to_string(grid, player) == "AXY*********\n*          *\n*     1    *\n*          *\n***        *\n*1*        *\n************\n\nYou have 0 water buckets.", "Positive test case 4 failed."
    grid = game_parser.parse(game_parser.read_lines('1move.txt'))
    assert grid_to_string(grid, player) == "A*\nXY\n**\n\nYou have 0 water buckets.", "Positive test case 5 failed."

    ## Negative test cases ##

    grid = game_parser.parse(game_parser.read_lines('board_simple.txt'))
    assert grid_to_string(grid, 'Jack') == None, 'Negative test case 1 failed, player is not a Player object.'
    assert grid_to_string(34, player) == None, 'Negative test case 2 failed, grid is not a list.'
    bad_grid = [1, 2, 'a']
    assert grid_to_string(bad_grid, player) == None, 'Negative test case 3 failed, element in grid is not a list.'

    ## Edge cases ##
    empty_grid = []
    assert grid_to_string(empty_grid, player) == None, 'Edge case 1 failed, empty grid.'


def run_tests():
    test_grid()

