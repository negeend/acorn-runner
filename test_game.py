from game import Game
from player import Player
from game_parser import read_lines
from game_parser import parse


def test_game():
    player = Player()
    player.row = 0
    player.col = 1
    game = Game('board_hard.txt')
    grid = parse(read_lines('board_hard.txt'))

## Testing gameMove() ##

    ## Positive test cases ##
    assert game.gameMove('a') == [1, 'a, '], 'Positive testcase 1 failed.'
    assert game.gameMove('d') == [2, 'a, d, '], 'Positive testcase 2 failed.'
    assert game.gameMove('s') == [3, 'a, d, s, '], 'Positive testcase 3 failed.'
    assert game.gameMove('w') == [4, 'a, d, s, w, '], 'Positive testcase 5 failed.'

    ## Negative test cases ##
    assert game.gameMove(1) == None, 'Negative testcase 1 failed, integer type move.'
    assert game.gameMove([]) == None, 'Negative testcase 2 failed, list type move.'

    ## Edge cases ##

## move_action() ##

    ## Positive test cases ##
    assert game.move_action(grid, player, 's') == '', 'Postive testcase 1 failed.'
    assert game.move_action(grid, player, 'a') == '', 'Positve testcase 2 failed.'


    ## Negative test cases ##
    assert game.move_action(grid, player, 1) == None, 'Negative testcase 1 failed'


    ## Edge cases ## 
    player.row = -1
    player.col = 1
    assert game.move_action(grid, player, 'w') == '\nYou walked into a wall. Oof!\n', 'Edgecase 1 failed, should act as a wall when stepping off the grid.'
    player.row = 1
    player.col = -1
    assert game.move_action(grid, player, 'a') == '\nYou walked into a wall. Oof!\n', 'Edgecase 2 failed, should act as a wall when stepping off the grid.'


def run_tests():
    test_game()
