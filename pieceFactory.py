# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:40:39 2018

@author: Dan
"""

from pieces import King, Queen, Rook, Bishop, Knight, Pawn

def makePiece(pieceString, x, y, color):
    """This method returns a piece in a given x, y, and color
    
    Args: 
        x - x coordinate - integer
        y - y coordinate - integer
        color - White, Black
        
    Returns:
        Piece object
    """
    if(pieceString == "King"):
        piece = King()
    elif(pieceString == "Queen"):
        piece = Queen()
    elif(pieceString == "Rook"):
        piece = Rook()
    elif(pieceString == "Bishop"):
        piece = Bishop()
    elif(pieceString == "Pawn"):
        piece = Pawn()
    elif(pieceString == "Knight"):
        piece = Knight()
    piece.setX(x)
    piece.setY(y)
    if(color == "White"):
        piece.setColor(0)
    if(color == "Black"):
        piece.setColor(1)
    return piece