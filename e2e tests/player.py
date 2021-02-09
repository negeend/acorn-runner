"""
Author: Negeen Daudi
Date: 20 May 2020
Purpose: A quick example on what this file contains.
"""

class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0

    def move(self, move):
        if type(move) != str:
            return
        r = self.row
        c = self.col
        if move == 'a':
            self.col -= 1
            return 'a'
        if move == 'd': 
            self.col += 1
            return 'd'
        if move == 'w':
            self.row -= 1
            return 'w'
        if move == 's':
            self.row += 1
            return 's'
        if move == 'e':
            return 'e'

    def initial_player_position(self, grid):
        if type(grid) != list:
            return
        for elem in grid:
            if type(elem) != list:
                return
        if len(grid) == 0:
            return
        for lists in grid:
            for cell in lists:
                if cell.display == 'X':
                    self.row = grid.index(lists)
                    self.col = lists.index(cell)
                    return [self.row, self.col]
                