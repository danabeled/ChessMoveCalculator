# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:11:57 2018

@author: Dan
"""
import pieces
import logging


logger = logging.getLogger('BOARD')
#logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)

class ChessBoard:
    
    def __init__(self):
        self.ranks = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,pieces.Rook(7,7,0),pieces.Rook(8,7,1)],
                      [0,0,0,0,0,0,pieces.Pawn(7,6,0),0],
                      [0,0,0,pieces.Knight(4, 5, 0),0,0,0,0],
                      [0,pieces.Queen(2,4,0),0,0,0,0,0,0],
                      [0,0,pieces.Pawn(5, 2, 1),0,pieces.Pawn(5, 2, 1),0,0,0],
                      [0,pieces.Bishop(2,2,0),0,pieces.Pawn(5, 2, 0),pieces.Pawn(5, 2, 1),0,0,0],
                      [0,0,0,0,pieces.King(5, 1, 0),0,0,0]]
    def display(self):
        """Prints into console visual representation of board
        
        Args:
            None
            
        Returns:
            None
        """
        for rank in self.ranks:
            for square in rank:
                print(square, end="\t")
            print("")
            
    def calculateAllMoves(self, color):
        """For a given color player summer all the legal movies he has
        
        Args: 
            Color player 0 is white, 1 is black
        
        Returns:
            Sum of all moves
        
        """
        moveSum = 0
        for rank in self.ranks:
            for square in rank:
                if(square != 0 and square.color == color):
                    moveSum += len(square.getMoveset(self.ranks))
        return moveSum
    
    
        
        
knight = pieces.Knight(4, 5, 0)
king = pieces.King(5, 1, 0)
rook = pieces.Rook(7,7,0)
bishop = pieces.Bishop(2,2,0)
queen = pieces.Queen(2,4,0)
pawn = pieces.Pawn(4, 2, 0)
board = ChessBoard()
board.display()
print("King's moves:", king.getMoveset(board.ranks))
print("Knights's moves:", knight.getMoveset(board.ranks))
print("Rook's moves:", rook.getMoveset(board.ranks))
print("Bishop's moves:", bishop.getMoveset(board.ranks))
print("Queen's moves:", queen.getMoveset(board.ranks))
print("Pawn's moves: ", pawn.getMoveset(board.ranks))
board.display()
print(board.calculateAllMoves(0))