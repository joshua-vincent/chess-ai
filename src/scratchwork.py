# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:58:29 2022

@author: Josh
"""

# Test
# positions = ['R7/3n4/7p/p5k1/8/5K1P/PP6/8', '3r2k1/6pp/p4p2/4p3/p5P1/1bN1B2P/1P2KP2/8', '8/1p4RP/1k6/p7/P6r/2PK4/1P6/8', '2r5/R7/N2Bp1p1/k2pP1N1/1n3PP1/8/P2K4/8', '2q3k1/1b3ppp/pP6/8/1P2r3/4BB2/Q5Pb/3R3K']
# board = positions[0]
# for (piece, kind) in enumerate(board.replace("/", "")):
#     values.append((piece, kind))
# print(tabulate(values, headers=["Element", "Value"]))

from tabulate import tabulate
import numpy as np
from math import floor

squares = np.zeros((12, 8, 8), dtype=np.bool_)
values = []

def get_rank(square):
    # Returns rank [0 .. 7] of square [0 .. 63]
    # Assumes square is in little endian order, i.e. square = 0 implies A1
    return floor(square/8) - 1

def get_file(square):
    # Returns file [0 .. 7] of square [0 .. 63]
    # Assumes square is in little endian order, i.e. square = 0 implies A1
    return square % 8

def convert(positons, bitboard=squares):
    # Returns a bitboard representation of 
    # Assume board is a FEN string, starting at A8 (square = 56)
    for board in positions:
        square = 56
        for (piece, kind) in enumerate(board):
            rank = get_rank(square)
            file = get_file(square)
            
            if kind == 'P':
                bitboard[0][square] = 1
            if kind == 'N':
                bitboard[1][square] = 1
            if kind == 'B':
                bitboard[2][square] = 1
            if kind == 'R':
                bitboard[3][square] = 1
            if kind == 'Q':
                bitboard[4][square] = 1
            if kind == 'K':
                bitboard[5][square] = 1
            if kind == 'k':
                bitboard[6][square] = 1
            if kind == 'q':
                bitboard[7][square] = 1
            if kind == 'r':
                bitboard[8][square] = 1
            if kind == 'b':
                bitboard[9][square] = 1
            if kind == 'n':
                bitboard[10][square] = 1
            if kind == 'p':
                bitboard[11][square] = 1
            elif kind.isdigit():
                square += square
            else:
                raise ValueError("Encountered unexpected character while parsing FEN string")
            square += 1
            

with open("chess_ai/training_data/FEN_positions_len_5.txt") as file:
    positions = file.read()
    positions = positions.split["\n"]
    
    
        
        # FEN -> bitboard
        # for element in fen.code
        # if piece 
        # mark location at square = element
        # case number
        # increment square to next element with piece
        