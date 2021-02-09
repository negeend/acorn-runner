"""
Author: Negeen Daudi
Date: 20 May 2020
Purpose: This file returns the board which will be printed to screen for the player.
"""

from player import Player

def grid_to_string(grid, player):
    """
    Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    if type(player) != Player:
        return 
    if type(grid) != list:
        return
    for elem in grid:
        if type(elem) != list:
            return
    if len(grid) == 0:
        return
    grid_string = ''
    i = 0 

    r = player.row
    c = player.col
    player_cell = grid[r][c]
    while i < len(grid):
        x = 0
        while x < len(grid[i]):
            if i == r and x == c:
                grid_string += 'A'
            else:
                grid_string += grid[i][x].display
            x += 1
        grid_string += '\n'
        i += 1
    if player.num_water_buckets == 1:
        grid_string += '\nYou have {} water bucket.'.format(player.num_water_buckets)
        return grid_string
    grid_string += '\nYou have {} water buckets.'.format(player.num_water_buckets)
    return grid_string



