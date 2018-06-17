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
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
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
        
    
        
        