"""
Author: Negeen Daudi
Date: 20 May 2020
Purpose: This file contains the game engine, holding all relevant data regarding the game's state.
"""

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

class Game:
    def __init__(self, filename):
        self.filename = filename
        self.move_counter = 0
        self.all_moves = ''
        pass

    def gameMove(self, move):
        if type(move) != str:
            return
        self.all_moves += '{}, '.format(move)
        self.move_counter += 1
        return [self.move_counter, self.all_moves]

    def move_action(self, grid, player, move):
        if type(move) != str:
            return
        r = player.row
        c = player.col
        cell = grid[r][c]
        if r < 0 or c < 0:
            return Wall.step(cell, self, player, grid, move)
        return cell.step(self, player, grid, move)


