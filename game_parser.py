"""
Author: Negeen Daudi
Date: 20 May 2020
Purpose: A quick example on what this file contains.
"""

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def read_lines(filename):
    """Read in a file and return the contents as a list of strings."""
    try:
        file = open(filename, 'r')
        list_of_strings = []
        while True:
            line = file.readline().strip('\n')
            if line == '':
                break
            list_of_strings.append(line)
        file.close()
        result = list_of_strings
        if len(result) == 0:
            raise ValueError("Invalid configuration file: empty.")
    except FileNotFoundError:
        print('{} does not exist!'.format(filename))
        exit()
    return result


def parse(lines):
    """
    Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    i = 0
    num_of_Xs = 0
    num_of_Ys = 0
    teleport_pads = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    ## Changing the string objects to their respective cell object ##
    list_of_lists = []
    while i < len(lines):
        listCopy = []
        for char in lines[i]:
            if char == ' ':
                char = Air(char)
                listCopy.append(char)
            elif char == '*':
                char = Wall(char)
                listCopy.append(char)
            elif char == 'W':
                char = Water(char)
                listCopy.append(char)
            elif char == 'F':
                char = Fire(char)
                listCopy.append(char)
            elif char == 'X':
                char = Start(char)
                listCopy.append(char)
                num_of_Xs += 1            ## A counter to check that there is only 1 starting point ##
            elif char == 'Y':
                char = End(char)
                listCopy.append(char)
                num_of_Ys += 1            ## A counter to check that there is only 1 ending point ##
            elif char in teleport_pads:
                char = Teleport(char)
                listCopy.append(char)
            elif char == '\n':
                pass
            else:
                raise ValueError("Bad letter in configuration file: {}.".format(char))
        list_of_lists.append(listCopy)
        i += 1

    if num_of_Xs != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(num_of_Xs))
    if num_of_Ys != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(num_of_Ys))

    ## Checking that any teleport pads are in pairs ##
    teleport_pads = []
    for inner_list in list_of_lists:
        for cell in inner_list:
            try:
                if int(cell.display) in range(1,10):
                    teleport_pads.append(cell.display)
            except:
                continue
    for pad in teleport_pads:
        if teleport_pads.count(pad) != 2:
            raise ValueError('Teleport pad {} does not have an exclusively matching pad.'.format(pad))
        
    return list_of_lists


# print(parse(read_lines('small_board.txt')))