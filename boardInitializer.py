# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:47:38 2018

@author: Dan
"""

from chessboard import ChessBoard
from pieces import Pawn

def initBoard(fileLocation):
    board = ChessBoard()
    
    infile = open(fileLocation, "r")
    data = infile.read().split('/')
    print(data)
    infile.close()

def analyzeRow(rowText, rowNumber, board):
    if(rowText[0].islower()):
        color = "Black"
    if(rowText[0].isupper()):
        color = "White"
    if(rowText[0].upper() == "P"):
        board.addPieceToBoard("Pawn", 1, rowNumber, color)
    if(rowText[0].upper() == "R"):
        board.addPieceToBoard("Rook", 1, rowNumber, color)
    if(rowText[0].upper() == "N"):
        board.addPieceToBoard("Knight", 1, rowNumber, color)
    if(rowText[0].upper() == "B"):
        board.addPieceToBoard("Bishop", 1, rowNumber, color)
    
initBoard("initial.fen")