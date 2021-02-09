from player import Player

class Start:
    def __init__(self, display):
        self.display = 'X'

    def step(self, game, player, grid, move):
        return ''
        pass

class End:
    def __init__(self, display):
        self.display = 'Y'

    def step(self, game, player, grid, move):
        return 'end of game - successful'

class Air:
    def __init__(self, display):
        self.display = ' '

    def step(self, game, player, grid, move):
        return ''

class Wall:
    def __init__(self, display):
        self.display = '*'

    def step(self, game, player, grid, move):
        r = player.row
        c = player.col
        if move == 'a':
            player.col += 1
        if move == 'd':
            player.col -= 1
        if move == 'w':
            player.row += 1
        if move == 's':
            player.row -= 1
        return '\nYou walked into a wall. Oof!\n'


class Fire:
    def __init__(self, display):
        self.display = 'F'
        self.function = True

    def step(self, game, player, grid, move):
        if self.function == True:
            if player.num_water_buckets == 0:
                return 'end of game - unsuccessful'
            player.num_water_buckets -= 1
            self.display = ' '
            self.function = False
            return '\nWith your strong acorn arms, you throw a water bucket at the fire.' \
                'You acorn roll your way through the extinguished flames!\n'
        return ''

class Water:
    def __init__(self, display):
        self.display = 'W'
        self.function = True

    def step(self, game, player, grid, move):
        if self.function == True:
            player.num_water_buckets += 1
            message = "\nThank the Honourable Furious Forest, you've found a bucket of water!\n"
            self.display = ' '
            self.function = False
            return message
        return ''

class Teleport:
    def __init__(self, display):
        self.display = display

    def step(self, game, player, grid, move):
        r = player.row
        c = player.col
        cell = grid[r][c]
        for lists in grid:
            for cell in lists:
                if cell.display == grid[r][c].display:
                    if grid.index(lists) == r and lists.index(cell) == c:
                        continue
                    player.row = grid.index(lists)
                    player.col = lists.index(cell)
        return '\nWhoosh! The magical gates break Physics as we know ' \
            'it and opens a wormhole through space and time.\n'