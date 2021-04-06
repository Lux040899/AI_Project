import sys
import json

def format_dict(data):
    upper = data['upper']
    lower = data['lower']
    block = data['block']
    board_dict = {}
    blocked = []
    for cell in upper:
        board_dict[(cell[1],cell[2])] = cell[0].upper()
    for cell in lower:
        board_dict[(cell[1],cell[2])] = cell[0]
    for cell in block:
        blocked.append((cell[1],cell[2]))

    return (board_dict, blocked)
