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
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,pieces.Pawn(5, 2, 0),0,0,0],
                      [0,0,0,0,pieces.King(5, 1, 0),0,0,0]]
    def display(self):
        for rank in self.ranks:
            for square in rank:
                print(square, end="\t")
            print("")
    def calculateAllMoves():
        print("Not implemented")
    
    def removeIllegalMoves(self, p):
        moveset = p.getMoveset();
        correctMoveSet = []
        for move in moveset:
            logger.debug('Evaluating move %r', move)
            if(self.outOfBounds(move) or self.occupiedBySameColor(move, p)):
                logger.debug('Invalid move found %r', move)
            else:
                correctMoveSet.append(move)
        return correctMoveSet
    
    def outOfBounds(self, move):
        """Determines if a move is within the board 
        
        For some pieces it was easier to make their complete moveset than calculate
        in the subclass, since the moves were so limited, this makes the need
        to check movesets
        
        Args:
            move: A move where [0] is the x coordinate and [1] is the y coordinate
            
        Returns:
            boolean of if within board or not
        """
        return move[0] > 8 or move[0] < 1 or move[1] > 8 or move[1] < 1
    
    def getSquare(self, x, y):
        return self.ranks[8 - y][x - 1] 
        
    def occupiedBySameColor(self, move, piece):
        square = self.getSquare(move[0], move[1])
        logger.debug('Object for square %r', square)
        if square == 0:
            return 0
        else:            
            logger.debug('Color for square %r', square.color)
            logger.debug('Color for piece %r', piece.color)
            return square.color == piece.color
        
        
king = pieces.King(5, 1, 0)
print(king.getMoveset())
board = ChessBoard()
print(board.removeIllegalMoves(king))
board.display()