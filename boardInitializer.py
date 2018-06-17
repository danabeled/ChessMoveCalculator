# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:47:38 2018

@author: Dan
"""

from chessboard import ChessBoard
from pieces import Pawn

def initBoard(fileLocation):
    board = ChessBoard()
    
    try:    
        infile = open(fileLocation, "r")
    except FileNotFoundError:
        print("File", fileLocation, "could not be found, please check your input")
        return
    
    data = infile.read().split('/')
    if(len(data) != 8):
        print("Input file", fileLocation, "did not contain enough ranks, please check your input")
        return
    counter = 8
    for row in data:
        try:
            analyzeRow(row, counter, board)
        except ValueError:
            print("A bad value was in row", counter)
            return
        counter -= 1
    infile.close()
    print("Imported board:")
    board.display()
    return board

def analyzeRow(rowText, rowNumber, board):
    counter = 1
    for character in rowText:
        if(character.islower()):
            color = "Black"
        if(character.isupper()):
            color = "White"
        pieceString = ""
        if(character.upper() == "P"):
            pieceString = "Pawn"
        elif(character.upper() == "R"):
            pieceString = "Rook"
        elif(character.upper() == "N"):
            pieceString = "Knight"
        elif(character.upper() == "B"):
            pieceString = "Bishop"
        elif(character.upper() == "Q"):
            pieceString = "Queen"
        elif(character.upper() == "K"):
            pieceString = "King"
        if(pieceString != ""):
            board.addPieceToBoard(pieceString, counter, rowNumber, color)
            counter += 1
        elif(character.isnumeric()):
            counter += int(character)
        else:
            raise ValueError('An unknown value was in the .fen file.') 
    
b1 = initBoard("input\\initial.fen")
print("Number of moves:", b1.calculateAllMoves(0))
b2 = initBoard("input\\midgame.fen")
print("Number of moves, white:", b2.calculateAllMoves(0))
print("Number of moves, black:", b2.calculateAllMoves(1))
b3 = initBoard("input\\midendgame.fen")
b4 = initBoard("input\\noslash.fen")
b4 = initBoard("input\\badvalues.fen")