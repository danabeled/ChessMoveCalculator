# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:11:57 2018

@author: Dan
"""
import pieces
import logging
from pieceFactory import makePiece


logger = logging.getLogger('BOARD')
#logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)

class ChessBoard:
    
    def __init__(self):
        self.__ranks = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,pieces.Rook(6,7,0),pieces.Rook(7,7,1),0],
                      [0,0,0,0,0,0,pieces.Pawn(7,6,0),0],
                      [0,0,0,pieces.Knight(4, 5, 0),0,0,0,0],
                      [0,pieces.Queen(2,4,0),0,0,0,0,0,0],
                      [0,0,pieces.Pawn(5, 2, 1),0,pieces.Pawn(5, 2, 1),0,0,0],
                      [0,pieces.Bishop(2,2,0),0,pieces.Pawn(5, 2, 0),pieces.Pawn(5, 2, 1),0,0,0],
                      [0,0,0,0,0,0,0,0]]
    def display(self):
        """Prints into console visual representation of board
        
        Args:
            None
            
        Returns:
            None
        """
        for rank in self.__ranks:
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
        for rank in self.__ranks:
            for square in rank:
                if(square != 0 and square.color == color):
                    moveSum += len(square.getMoveset(self.__ranks))
        return moveSum
    
    def getRanks(self):
        return self.__ranks
    
    def addPieceToBoard(self, pieceType, x, y, color):
        self.__setRank__(x, y, makePiece(pieceType, x, y, color))
    
    def getRank(self, x, y):
        return self.__ranks[8 - y][x - 1]
    
    def __setRank__(self, x, y, value):
        self.__ranks[8 - y][x - 1] = value
        
    
        
        
knight = pieces.Knight(4, 5, 0)
king = pieces.King(5, 1, 0)
rook = pieces.Rook(6,7,0)
bishop = pieces.Bishop(2,2,0)
queen = pieces.Queen(2,4,0)
pawn = pieces.Pawn(4, 2, 0)
board = ChessBoard()
board.addPieceToBoard("King", 5, 1, "White")
board.display()
print("King's moves:", board.getRank(5, 1).getMoveset(board.getRanks()))
print(repr(knight))
print("Knights's moves:", knight.getMoveset(board.getRanks()))
print("Rook's moves:", rook.getMoveset(board.getRanks()))
print("Bishop's moves:", bishop.getMoveset(board.getRanks()))
print("Queen's moves:", queen.getMoveset(board.getRanks()))
print("Pawn's moves: ", pawn.getMoveset(board.getRanks()))
board.display()
print(board.calculateAllMoves(0))