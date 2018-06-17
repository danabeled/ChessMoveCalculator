# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:55:48 2018

@author: Dan
"""

from chessboard import ChessBoard
from boardInitializer import initBoard


def evaluateBoard():
    file = input("Enter file (.fen extension included) location: ")
    board = initBoard(file)
    print("Imported board:")
    board.display()
    print("White has", board.calculateAllMoves(0), "moves")
    print("Black has", board.calculateAllMoves(1), "moves")
    choose_display_moves = ""
    while(choose_display_moves.upper() != "N"):
        choose_display_moves = input("Would you like to see the moves of a piece? (Y/N) ")
        if(choose_display_moves.upper() == "Y"):
            x, y = eval(input("Enter an x, y coordinate: "))
            square = board.getSquare(x, y)
            if(square == 0):
                print("No piece there...")
            else:
                print("Piece: ", square, "moveset is", square.getMoveset(board.getRanks()))
                
evaluateBoard()
