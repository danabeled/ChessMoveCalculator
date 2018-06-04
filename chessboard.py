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
                      [0,0,0,0,0,0,pieces.Rook(7,7,0),0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,pieces.Knight(4, 5, 0),0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,pieces.Pawn(5, 2, 0),pieces.Pawn(5, 2, 1),0,0,0],
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
                    moveSum += len(self.removeIllegalMoves(square))
        return moveSum
    
    def removeIllegalMoves(self, p):
        """Removes all illegal moves from a piece's moveset
        
        Pieces stored movesets are calculated based on current x, y or 
        hardcoded. Therefore the board must remove moves that are invalid
        based on it's knowledge of the board. Moves cannot be made if a
        piece of the same color is on the square
        
        Args:
            p: piece to get moveset 
            
        Returns:
            Parried down move list for the piece
        """
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
        
        For some pieces it was easier to make their complete moveset than 
        calculate in the subclass, since the moves were so limited, this makes 
        the need to check movesets if it is outside the array
        
        Args:
            move: A move where [0] is the x coordinate and [1] is the y 
            coordinate
            
        Returns:
            boolean of if within board or not
        """
        return move[0] > 8 or move[0] < 1 or move[1] > 8 or move[1] < 1
    
    def getSquare(self, x, y):
        """Fetches the object stored at the x,y coordinate in the ranks array
        
        Args:
            x: File number
            y: Rank number
            
        Returns:
            Object stored in array at that square, or 0 if nothing stored there
        
        For readability, moves are stored with their actual rank/file numbers.
        These must be translated into array locations.
        """
        return self.ranks[8 - y][x - 1] 
        
    def occupiedBySameColor(self, move, piece):
        """Determines if there is a piece of the same color in a sqaure
        
        Args:
            move: An x, y pair where [0] is the x and [1] is the y
            
        Returns:
            0 if no piece, or piece is of other color
            1 if piece of same color
        """
        square = self.getSquare(move[0], move[1])
        logger.debug('Object for square %r', square)
        if square == 0:
            return 0
        else:            
            logger.debug('Color for square %r', square.color)
            logger.debug('Color for piece %r', piece.color)
            return square.color == piece.color
        
knight = pieces.Knight(4, 5, 0)
king = pieces.King(5, 1, 0)
rook = pieces.Rook(7,7,0)
print(king.getMoveset())
board = ChessBoard()
print("King's moves:", board.removeIllegalMoves(king))
print("Knights's moves:", board.removeIllegalMoves(knight))
print("Rook's moves:", board.removeIllegalMoves(rook))
board.display()
print(board.calculateAllMoves(0))