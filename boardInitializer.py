# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:47:38 2018

@author: Dan
"""

from chessboard import ChessBoard
from pieces import Pawn

def initBoard(fileLocation):
    """This method reads a .fen file and returns a board representing its state
    
    Args:
        Complete or partial filepath to .fen file
        
    Returns:
        Board representing contents of file, or None if an error during analysis
    
    """
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
    return board

def analyzeRow(rowText, rowNumber, board):
    """This method analyzes a section of a .fen file
    
    Args:
        rowText - The text between the slashes of a .fen file
        
        rowNumber - Rank number that is being analyzed
        
        board - Board that pieces are being added to
        
    Returns:
        None
    """
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

### Integration tests ####
if __name__ == "__main__":
    inputfiles = ["input\\initial.fen", "input\\midgame.fen", "input\\midgame2.fen", 
                  "input\\midgame3.fen", "input\\midendgame.fen",
                  "input\\noslash.fen", "input\\badvalues.fen", "input\\endgame1.fen",
                  "input\\endgame2.fen", "input\\endgame3.fen", "input\\queensgambitsuperaccepted.fen",
                  "input\\queensgambitdeclined.fen", "input\\ruylopez.fen",
                  "input\\ruylopezexchangevariation.fen"]
    for inputfile in inputfiles:
        b = initBoard(inputfile)
        print("Evaluting file", inputfile)
        if(b != None):
            b.display()
            print("Number of moves, white:", b.calculateAllMoves(0))
            print("Number of moves, black:", b.calculateAllMoves(1))