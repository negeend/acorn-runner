from game_parser import parse
from game_parser import read_lines
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def test_parse():

    lines = read_lines('small_board.txt')
    grid = parse(lines)
    assert type(grid[0][0]) == Wall
    assert type(grid[0][1]) == Start
    assert type(grid[0][2]) == End
    lines = read_lines('board_everything.txt')
    grid = parse(lines)
    assert type(grid[0][0]) == Wall
    assert type(grid[0][1]) == Start
    assert type(grid[0][2]) == Wall
    assert type(grid[0][3]) == Wall
    assert type(grid[1][0]) == Wall
    assert type(grid[1][1]) == Water
    assert type(grid[1][2]) == Fire
    assert type(grid[1][3]) == Wall
    assert type(grid[2][0]) == Wall
    assert type(grid[2][1]) == Teleport
    assert type(grid[2][2]) == Teleport
    assert type(grid[2][3]) == Wall
    assert type(grid[3][0]) == Wall
    assert type(grid[3][1]) == Air
    assert type(grid[3][2]) == Air
    assert type(grid[3][3]) == Wall
    assert type(grid[4][0]) == Wall
    assert type(grid[4][1]) == End
    assert type(grid[4][2]) == Wall
    assert type(grid[4][3]) == Wall

    ## Negative test cases ##
    ''' Bad letter in configuration file '''
    lines = read_lines('board_bad.txt')
    try:
        parse(lines)
        assert False
    except AssertionError:
        print("parse: Testcase 1 failed (did not throw an exception)")
    except ValueError:
        pass
    
    ''' No ending position '''
    lines = read_lines('board_noend.txt')
    try:
        parse(lines)
        assert False
    except AssertionError:
        print("parse: Testcase 2 failed (did not throw an exception)")
    except ValueError:
        pass

    ''' No starting position '''
    lines = read_lines('board_nostart.txt')
    try:
        parse(lines)
        assert False
    except AssertionError:
        print("parse: Testcase 3 failed (did not throw an exception)")
    except ValueError:
        pass

    ''' Teleport pad with out matching pad '''
    lines = read_lines('board_onepad.txt')
    try:
        parse(lines)
        assert False
    except AssertionError:
        print("parse: Testcase 4 failed (did not throw an exception)")
    except ValueError:
        pass

def test_read_lines():

    ''' Empty configuration file '''
    try:
        read_lines('board_empty.txt')
    except AssertionError:
        print("read_lines: Testcase 1 failed (did not throw an exception)")
    except ValueError:
        pass

def run_tests():
    test_parse()
    test_read_lines()

#print(parse(read_lines('small_board.txt')))
run_tests()