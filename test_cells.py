from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game import Game
from player import Player
import game_parser


def test_cells():
    game = Game('board_hard.txt')
    player = Player()
    grid = game_parser.parse(game_parser.read_lines('board_hard.txt'))

    ## Testing cell.step() ##
    cell = Start('X')
    assert cell.step(game, player, grid, 'a') == '', 'cells testcase 1 failed, Start.step.'
    cell = End('Y')
    assert cell.step(game, player, grid, 'a') == 'end of game - successful', 'cells testcase 2 failed, End.step.'
    cell = Air(' ')
    assert cell.step(game, player, grid, 'w') == '', 'cells testcase 3 failed, Air.step.'
    cell = Wall('*')
    assert cell.step(game, player, grid, 's') == '\nYou walked into a wall. Oof!\n', 'cells testcase 4 failed, Wall.step.'
    cell = Fire('F')
    assert cell.step(game, player, grid, 'd') == 'end of game - unsuccessful', 'cells testcase 5 failed, Fire.step with no water buckets.'
    player.num_water_buckets = 1
    assert cell.step(game, player, grid, 'a') == '\nWith your strong acorn arms, you throw a water bucket at the fire.' \
                'You acorn roll your way through the extinguished flames!\n', 'cells testcase 6 failed, Fire.step with water bucket.'
    cell = Water('W')
    assert cell.step(game, player, grid, 's') == "\nThank the Honourable Furious Forest, you've found a bucket of water!\n", 'cells testcase 7 failed, Water.step'
    assert cell.step(game, player, grid, 'a') == '', 'cells testcase 8 failed, Water.step should only function when stepped on for the first time.'
    cell = Teleport('1')
    assert cell.step(game, player, grid, 'a') == '\nWhoosh! The magical gates break Physics as we know ' \
            'it and opens a wormhole through space and time.\n', 'cells testcase 9 failed, Teleport.step.'

def run_tests():
    test_cells()

