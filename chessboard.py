# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:11:57 2018

@author: Dan
"""

import logging
from pieceFactory import makePiece


logger = logging.getLogger('BOARD')
#logger.setLevel(logging.ERROR)
logger.setLevel(logging.DEBUG)

class ChessBoard:

    def __init__(self):
        self.__ranks = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]
        self.__blackCanCastle = 0
        self.__whiteCanCastle = 0
    
    def blackCanCastle(self):
        """Method sets black as able to castle to be counted in moves
        """
        self.__blackCanCastle = 1
        
    def whiteCanCastle(self):
        """Method sets white as able to castle to be counted in moves
        """
        self.__whiteCanCastle = 1
    
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
        if(color == 0):
            moveSum = self.__whiteCanCastle
        else:
            moveSum = self.__blackCanCastle
            
        for rank in self.__ranks:
            for square in rank:
                if(square != 0 and square.color == color):
                    moveSum += len(square.getMoveset(self.__ranks))        
        return moveSum
    
    def getRanks(self):
        """ Method returns all squares in chess board
        """
        return self.__ranks
    
    def addPieceToBoard(self, pieceType, x, y, color):
        """Method creates a piece and adds it to a square on the board
        overwriting previous contents
        
        Args:
            pieceType - "King", "Queen", "Rook", "Bishop", "Knight", "Pawn"
            x - x coordinate
            y - y coordinate
            color - "White", "Black"
        """
        self.__setRank__(x, y, makePiece(pieceType, x, y, color))
    
    def getRank(self, rankNumber):
        """Returns an entire rank of the board
        
        Args:
            rankNumber - Number of rank to get where 1 is white's back
                         rank and 8 is black's back rank
                         
        Returns:
            List of square values
        """
        return self.__ranks[8 - rankNumber]
    
    def getSquare(self, x, y):
        """Returns a specific square on the board
        """
        return self.__ranks[8 - y][x - 1]
    
    def __setRank__(self, x, y, value):
        self.__ranks[8 - y][x - 1] = value
        
    
### Integration tests ####
if __name__ == "__main__":
    print("Integration test board")
    board = ChessBoard()
    board.addPieceToBoard("Queen", 6, 3, "White")
    board.addPieceToBoard("King", 6, 1, "White")
    board.addPieceToBoard("King", 1, 8, "Black")
    board.addPieceToBoard("Pawn", 1, 7, "Black")
    board.addPieceToBoard("Knight", 1, 7, "Black")
    board.addPieceToBoard("Bishop", 4, 7, "Black")
    board.addPieceToBoard("Rook", 3, 7, "Black")
    board.display()
    print("White's moves", board.calculateAllMoves(0))
    print("Black's moves", board.calculateAllMoves(1))
        
        