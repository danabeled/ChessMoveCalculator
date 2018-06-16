# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:12:10 2018

@author: Dan
"""
import logging
logger = logging.getLogger('PIECE')
logger.setLevel(logging.DEBUG)

class Piece:
      
    def __init__(self, current_x, current_y, color):
        
        #self.logger.setLevel(logging.ERROR)
        
        self.x = current_x
        self.y = current_y
        self.color = color
        
    pieceLetter = "NA"
    
    def __getMoveset__(self, ranks):
        print("Nothing should get here")
    
    def __str__(self):
        toStrValue = ""
        if(self.color ==  0):
            toStrValue = self.pieceLetter.upper()
        else:
            toStrValue = self.pieceLetter.lower()
            
        return toStrValue + chr(ord('a') + self.x - 1) + str(self.y)
    
    
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
    
    
    
    def removeIllegalMoves(self, ranks):
        """Removes all illegal moves from a piece's moveset
        
        Pieces stored movesets are calculated based on current x, y or 
        hardcoded. Therefore if hardcoded the board must remove moves that 
        are invalid based on it's knowledge of the board. Moves cannot be 
        made if a piece of the same color is on the square.
        May be able to remove this once we abstract more logic into the pieces
        
        Args:
            p: piece to get moveset 
            
        Returns:
            Parried down move list for the piece
        """
        moveset = self.__getMoveset__(ranks)
        correctMoveSet = []
        for move in moveset:
            logger.debug('Evaluating move %r', move)
            if(self.outOfBounds(move) or self.occupiedBySameColor(move, ranks)):
                logger.debug('Invalid move found %r', move)
            else:
                correctMoveSet.append(move)
        return correctMoveSet       
    
    
    def occupiedBySameColor(self, move, ranks):
        """Determines if there is a piece of the same color in a sqaure
        
        Args:
            move: An x, y pair where [0] is the x and [1] is the y
            
        Returns:
            0 if no piece, or piece is of other color
            1 if piece of same color
        """
        square = getSquare(move[0], move[1], ranks)
        logger.debug('Object for square %r', square)
        if square == 0:
            return 0
        else:            
            logger.debug('Color for square %r', square.color)
            logger.debug('Color for piece %r', self.color)
            return square.color == self.color
        
    def getMoveset(self, ranks):
        return self.removeIllegalMoves(ranks)
    
class King(Piece):
    pieceLetter = "k"
    
    def __getMoveset__(self, ranks):
        return [(self.x + 1, self.y),
                (self.x + 1, self.y + 1),
                (self.x + 1, self.y - 1),
                (self.x - 1, self.y),
                (self.x - 1, self.y + 1),                
                (self.x - 1, self.y - 1),
                (self.x, self.y + 1),                
                (self.x, self.y - 1)]    
                
class Pawn(Piece):
    pieceLetter = "p"
    
    def checkSquareIfAppend(self, move, moves, ranks):
        square = getSquare(move[0], move[1], ranks)
        if(square != 0 and (not self.occupiedBySameColor(move, ranks))):
            moves.append((move[0], move[1]))
        return moves
    
    def __getMoveset__(self, ranks):
        moves = [(self.x, self.y + 1)]
        
        attackingMoves = [(self.x - 1, self.y + 1), (self.x + 1, self.y + 1)]
        for move in attackingMoves:
            moves = self.checkSquareIfAppend(move, moves, ranks)
        return moves
    
class Rook(Piece):
    pieceLetter = "r"
    
    def __getMoveset__(self, ranks):
        moves = []
        
        moves = addStraightMoves(moves, self.x, self.y, self.color, ranks)
        
        return moves

class Bishop(Piece):
    pieceLetter = "b"
    
    def __getMoveset__(self, ranks):
        moves = []
        
        moves = addDiagMoves(moves, self.x, self.y, self.color, ranks)
                
        return moves


class Queen(Piece):
    pieceLetter = "q"
    
    def __getMoveset__(self, ranks):
        moves = []
        
        moves = addDiagMoves(moves, self.x, self.y, self.color, ranks)
        moves = addStraightMoves(moves, self.x, self.y, self.color, ranks)
                
        return moves

class Knight(Piece):
    pieceLetter = "n"
    
    def __getMoveset__(self, ranks):
        return [(self.x - 1, self.y + 2),
                (self.x + 1, self.y + 2),
                (self.x + 2, self.y + 1),
                (self.x + 2, self.y - 1),
                (self.x - 2, self.y + 1),
                (self.x - 2, self.y - 1),
                (self.x - 1, self.y - 2),
                (self.x + 1, self.y - 2)]

def addStraightMoves(currentMoves, selfX, selfY, selfColor, ranks):
    #Add moves to the left
    x = selfX - 1
    while(x > 0):
        currentMoves.append((x, selfY))
        square = getSquare(x, selfY, ranks)
        x = x - 1
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((x, selfY))
            break
    #Add moves to the right
    x = selfX + 1
    while(x < 9):
        currentMoves.append((x, selfY))
        square = getSquare(x, selfY, ranks)       
        x = x + 1     
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((x, selfY))
            break
    y = selfY - 1
    #Add moves to the bottom
    while(y > 0):
        currentMoves.append((selfX, y))
        square = getSquare(selfX, y, ranks)        
        y = y - 1    
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((selfX, y))
            break  
    #Add moves to the top
    y = selfY + 1
    while(y < 9):
        currentMoves.append((selfX, y))
        square = getSquare(selfX, y, ranks)    
        y = y + 1        
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((selfX, y))  
            break
    
    return currentMoves
    
def addDiagMoves(currentMoves, selfX, selfY, selfColor, ranks):
    
    #Add moves to the left-down
    x = selfX - 1
    y = selfY - 1
    while(x > 0 and y > 0):
        square = getSquare(x, y, ranks)
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((x, y))
            break
        currentMoves.append((x, y))
        x = x - 1
        y = y - 1
        
    #Add moves to the left-up
    x = selfX - 1
    y = selfY + 1    
    while(x > 0 and y < 9):
        square = getSquare(x, y, ranks)
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((x, y))
            break    
        currentMoves.append((x, y))
        x = x - 1
        y = y + 1
        
    #Add moves to the right-down
    x = selfX + 1
    y = selfY - 1    
    while(x < 9 and y > 0):
        square = getSquare(x, y, ranks)
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((x, y))
            break 
        currentMoves.append((x, y))  
        x = x + 1
        y = y - 1 
        
    #Add moves to the right-up
    x = selfX + 1
    y = selfY + 1
    while(x < 9 and y < 9):
        square = getSquare(x, y, ranks)
        if(square != 0):
            if(square.color != selfColor):
                currentMoves.append((x, y))
            break
        currentMoves.append((x, y))
        x = x + 1
        y = y + 1
    
    return currentMoves

       
def getSquare(x, y, ranks):
    """Fetches the object stored at the x,y coordinate in the ranks array
    
    Args:
        x: File number
        y: Rank number
        
    Returns:
        Object stored in array at that square, or 0 if nothing stored there
    
    For readability, moves are stored with their actual rank/file numbers.
    These must be translated into array locations.
    """
    return ranks[8 - y][x - 1]     
        
king = King(5, 1, 1)
print(king.getMoveset([[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,Rook(7,7,0),0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,Knight(4, 5, 0),0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,Pawn(5, 2, 0),Pawn(5, 2, 1),0,0,0],
                      [0,0,0,0,King(5, 1, 0),0,0,0]]))