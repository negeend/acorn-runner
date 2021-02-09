import sys
from game_parser import read_lines
from game_parser import parse
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
try:
    filename = sys.argv[1]
    mode = sys.argv[2]
except IndexError:
    print('Usage: python3 solver.py <filename> <mode>')
    sys.exit()
def valid(maze, moves):
    player = Player()
    for n in range(len(maze)):
        for x, cell in enumerate(maze[n]):
            if cell.display == "X":
                i = x
                j = n
    for move in moves:
        if move == "a":
            i -= 1
        elif move == "d":
            i += 1
        elif move == "w":
            j -= 1
        elif move == "s":
            j += 1
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i].display == "*"):
            return False
        elif maze[j][i].display == 'F' and player.num_water_buckets == 0:
            return False
        elif maze[j][i].display == 'W':
            player.num_water_buckets += 1
    return True
    
def find_end(maze, moves):
    for n in range(len(maze)):
        for x, cell in enumerate(maze[n]):
            if cell.display == "X":
                i = x
                j = n
    for move in moves:
        if move == "a":
            i -= 1
        elif move == "d":
            i += 1
        elif move == "w":
            j -= 1
        elif move == "s":
            j += 1
    if maze[j][i].display == "Y":
        counter = 0
        for x in moves:
            if x == ',' or x == ' ':
                pass
            else:
                counter += 1
        print('Path has {} moves.'.format(counter))
        moves = moves[:-2]
        print('Path: {}'.format(moves))
        return True
    return False
        
def solve(maze):
    nums = []
    add = ''
    nums.append(add)
    maze = parse(read_lines(filename))
    while not find_end(maze, add):
        add = nums[0]
        nums.remove(nums[0])
        for j in ["a", "d", "w", "s"]:
            put = add + '{}, '.format(j)
            if valid(maze, put):
                nums.append(put)
    return True
 
if __name__ == "__main__":
    try:
        maze = parse(read_lines(filename))
        solution_found = solve(maze)
    except IndexError:
        print("There is no possible path.")