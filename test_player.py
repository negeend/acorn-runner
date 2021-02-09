from player import Player
import game_parser

def test_player():
    player = Player()
## Testing Player.move() ##
    ## Positive test cases ##
    assert player.move('a') == 'a', 'Positive test case 1 failed, move "a".'
    assert player.move('w') == 'w', 'Positive test case 2 failed, move "w".'
    assert player.move('s') == 's', 'Positive test case 3 failed, move "s".'
    assert player.move('d') == 'd', 'Positive test case 4 failed, move "d".'
    assert player.move('e') == 'e', 'Positive test case 5 failed, move "e".'

    ## Negative test cases ##
    assert player.move(5) == None, 'Negative test case 1 failed, non-string move.'

    ## Edge cases ##

## Testing Player.initial_player_position() ##

    ## Positive test cases ##
    grid = game_parser.parse(game_parser.read_lines('board_simple.txt'))
    assert player.initial_player_position(grid) == [0, 2], 'Positive test case 1 failed.' 
    grid = game_parser.parse(game_parser.read_lines('board_medium.txt'))
    assert player.initial_player_position(grid) == [0, 2], 'Positive test case 2 failed.' 
    grid = game_parser.parse(game_parser.read_lines('board_hard.txt'))
    assert player.initial_player_position(grid) == [0, 1], 'Positive test case 3 failed.' 
    grid = game_parser.parse(game_parser.read_lines('board.txt'))
    assert player.initial_player_position(grid) == [0, 1], 'Positive test case 4 failed.'
    grid = game_parser.parse(game_parser.read_lines('board_test.txt'))
    assert player.initial_player_position(grid) == [1, 0], 'Positive test case 5 failed.'

    ## Negative test cases ##
    assert player.initial_player_position('string') == None, 'Negative test case 1 failed.'
    assert player.initial_player_position([1, 2, 3]) == None, 'Negative test case 2 failed.'
    assert player.initial_player_position([]) == None, 'Negative test case 3 failed.'

    ## Edge cases ##


def run_tests():
    test_player()


