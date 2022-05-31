# -*- coding: utf-8 -*-
"""
A set of tools for managing chess game data.
    Created on Sun May 29 16:26:29 2022

@author: Joshua Vincent
"""

import os
import time
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
    start_time = time.time()
    file_root, file_ext = os.path.splitext(file)
    
    if file_ext != ".epd":
        # File read must be of format "FEN; SF11'\n'"
        raise TypeError("Can only parse '.edp' files at the moment.")
        
    file = open(file)
    contents = file.read()
    contents = contents.split("\n")
    # contents = [(FEN position; SF 11 centipawn evaluation)]
    
    file_out = open(output, 'w')
    
    num_lines = 0
    for line in contents:
        if len(line) <= 1:
            break
        
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
        # 
        # FEN -> bitboard
        # 
        #
        #
        #
        #
        
        new_line = {
            'board':board,
            'turnInfo':turnInfo,
            'eval':sfEval}
        
        file_out.write(str(new_line) + '\n')
        num_lines += 1
    
    message = \
        f"""
        Finished parsing '{file_root + file_ext}'.
        Parsed {num_lines} positions in {(time.time() - start_time):.2f} sec.
        """
    print(message)
    
    file.close()
    file_out.close()

def fen_to_bitboard(fen):
    # Parses a FEN board position (string fen) into a bitboard representation
    # Returns (npArray bitboard), 12 x 64 bit long binary position representation
    # TODO add conversion of FEN board position to bitboard
    # 
    # FEN -> bitboard
    # for element in fen.code
    # if piece 
    # mark location at square = element
    # case number
    # increment square to next element with piece
    