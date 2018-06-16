# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:40:39 2018

@author: Dan
"""

from pieces import King

def makePiece(pieceString, x, y, color):
    if(pieceString == "King"):
        piece = King()
    piece.setX(x)
    piece.setY(y)
    if(color == "White"):
        piece.setColor(0)
    if(color == "Black"):
        pice.setColor(1)
    return piece