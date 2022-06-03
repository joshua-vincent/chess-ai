# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:11:26 2022

@author: Josh
"""

# Test
# positions = ['R7/3n4/7p/p5k1/8/5K1P/PP6/8', '3r2k1/6pp/p4p2/4p3/p5P1/1bN1B2P/1P2KP2/8', '8/1p4RP/1k6/p7/P6r/2PK4/1P6/8', '2r5/R7/N2Bp1p1/k2pP1N1/1n3PP1/8/P2K4/8', '2q3k1/1b3ppp/pP6/8/1P2r3/4BB2/Q5Pb/3R3K']
# board = positions[0]

import numpy as np
from math import floor

white_pawn   = 0
white_knight = 1
white_bishop = 2
white_rook   = 3
white_queen  = 4
white_king   = 5
black_king   = 6
black_queen  = 7
black_rook   = 8
black_bishop = 9
black_knight = 10
black_pawn   = 11

def convert(board, bitboard=None):
    # Returns a bitboard representation of 
    # Assume board is a FEN string, starting at A8 (square = 56)
    square = 56
    if not bitboard:
        bitboard = np.zeros((12, 8, 8), dtype=np.int8)
    for piece in board:
        rank = get_rank(square)
        file = get_file(square)
        print(rank, file, piece, square)
        if piece == "P":
            bitboard[white_pawn, rank, file] = 1
        elif piece == "N":
            bitboard[white_knight, rank, file] = 1
        elif piece == "B":
            bitboard[white_bishop, rank, file] = 1
        elif piece == "R":
            bitboard[white_rook, rank, file] = 1
        elif piece == "Q":
            bitboard[white_queen, rank, file] = 1
        elif piece == "K":
            bitboard[white_king, rank, file] = 1
        elif piece == "k":
            bitboard[black_king, rank, file] = 1
        elif piece == "q":
            bitboard[black_queen, rank, file] = 1
        elif piece == "r":
            bitboard[black_rook, rank, file] = 1
        elif piece == "b":
            bitboard[black_bishop, rank, file] = 1
        elif piece == "n":
            bitboard[black_knight, rank, file] = 1
        elif piece == "p":
            bitboard[black_pawn, rank, file] = 1
        elif piece.isdigit():
            square += int(piece)
            continue
        elif piece == "/":
            square -= 16
            continue
        elif piece not in 'PNBRQKkqrnbp/':
            raise ValueError("Encountered unexpected character while parsing FEN string")
        square += 1
    return bitboard

def get_rank(square):
    # Returns rank [0 .. 7] of square [0 .. 63]
    # Assumes square is in little endian order, i.e. square = 0 --> square A1
    return floor(square/8)

def get_file(square):
    # Returns file [0 .. 7] of square [0 .. 63]
    # Assumes square is in little endian order, i.e. square = 0 --> square A1
    return square % 8