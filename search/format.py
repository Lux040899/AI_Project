import sys
import json

def format_dict(data):
    upper = data['upper']
    lower = data['lower']
    block = data['block']
    board_dict = {}
    for cell in upper:
        board_dict[(cell[1], cell[2])] = cell[0].upper()
    for cell in lower:
        board_dict[(cell[1], cell[2])] = cell[0]
    return board_dict
