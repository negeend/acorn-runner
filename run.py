"""
Author: Negeen Daudi
Date: 20 May 2020
Purpose: This file is the entry point of the program.
"""

from game import Game
from player import Player
import game_parser
from grid import grid_to_string
import os
import sys

try:
    filename = sys.argv[1]
except IndexError:                                        ## Checking if a command line argument is given ##
    print('Usage: python3 run.py <filename> [play]')
    exit()


## Running the Game ##
try:
    grid = game_parser.parse(game_parser.read_lines(filename))
    player = Player()
    Player.initial_player_position(player, grid)
    board = grid_to_string(grid, player)
    game = Game(filename)
    print(board)
    print()
except ValueError as e:
    print(e)
    exit()

while True:
    player_input = input("Input a move: ")
    #os.system('clear')
    player_input = player_input.lower()
    if player_input == 'q':
        print('\nBye!')
        break
    move = Player.move(player, player_input)
    message = Game.move_action(game, grid, player, move)
    board = grid_to_string(grid, player)
    print(board)
    ## Checking for valid input ##
    if player_input != 'a' and player_input != 'w' and player_input != 's' \
        and player_input != 'd' and player_input != 'e':
        print("\nPlease enter a valid move (w, a, s, d, e, q).\n") 
        continue
    elif message == '\nYou walked into a wall. Oof!\n':
        pass
    else:
        moves = Game.gameMove(game, player_input)
        moves[1] = moves[1][:-2]                                    ## Getting rid of the trailing ', ' ##
    if message == 'end of game - successful':
        print('\n\nYou conquer the treacherous maze set up by the Fire Nation and ', end = '')
        print('reclaim the Honourable Furious Forest Throne, restoring your hometown ', end = '')
        print('back to its former glory of rainbow and sunshine! Peace reigns over the lands.')
        if game.move_counter == 1:
            print('\nYou made {} move.'.format(moves[0]))
            print('Your move: {}'.format(moves[1]))
        else:
            print('\nYou made {} moves.'.format(moves[0]))
            print('Your moves: {}'.format(moves[1]))
        print('\n=====================')
        print('====== YOU WIN! =====')
        print('=====================')
        exit()
    if message == 'end of game - unsuccessful':
        print('\n\nYou step into the fires and watch your dreams disappear :(.')
        print('\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced ', end = '')
        print('to a pile of ash and is scattered to the winds by the next storm... ', end = '') 
        print('You have been roasted.')
        if game.move_counter == 1:
            print('\nYou made {} move.'.format(moves[0]))
            print('Your move: {}'.format(moves[1]))
        else:
            print('\nYou made {} moves.'.format(moves[0]))
            print('Your moves: {}'.format(moves[1]))
        print('\n=====================')
        print('===== GAME OVER =====')
        print('=====================')
        exit()
    print(message)
