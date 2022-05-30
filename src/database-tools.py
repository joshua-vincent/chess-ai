# -*- coding: utf-8 -*-
"""
A set of tools for managing chess game data.
    Created on Sun May 29 16:26:29 2022

@author: Joshua Vincent
"""

import os
import numpy as np

# import re
# import pandas as pd
# class Bitboard:
#     pass


"""
Read positional or game data file into Bitboard (.btb) format.
Dataframe of Bitboards, TurnInfo, and Evaluations.

Bitboards describe board positional states as 8x8 binary fields.
A position is described by 12 total 8x8 fields, there is one for each piece.
Pieces are ordered [P N B R Q K k q r b n p]
Squares are represented in little endian order.

TurnInfo contains data regarding side to move, castling, en passant, etc.

Evaluations are Stockfish 11 positional evaluations in centipawn units.
"""
def from_file(file, output='test/test.btb'):
    file_root, file_ext = os.path.splitext(file)
    
    if file_ext not ".epd":
        # File read must be of format "FEN; SF11'\n'"
        raise TypeError("Can only parse '.edp' files at the moment.")
        
    file = open(file)
    contents = file.read()
    contents = contents.split("\n")
    # contents = [(FEN position; SF 11 centipawn evaluation)]
    
    file_out = open(output, 'w')
    
    for line in contents:
        line = line.replace(";", "").split(" ")
        
        board = line[0]
        turn = line[1]
        castling = line[2]
        enPassant = line[3]
        hfmClock = line[4]
        fmClock = line [5]
        sfEval = line[6].split("=")[1]
        
        turnInfo = {
            'turn':turn,
            'castling':castling,
            'enPassant':enPassant,
            'half move clock':hfmClock,
            'full move clock':fmClock
            }
        
        #TODO add conversion of FEN board position to bitboard
        
        new_line = {
            'board':board,
            'turnInfo':turnInfo,
            'eval':sfEval}
        
        file_out.write(new_line + '\n')
    
    file.close()
    file_out.close()