# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:12:10 2018

@author: Dan
"""

class Piece:
      
    def __init__(self, current_x, current_y, color):
        self.x = current_x
        self.y = current_y
        self.color = color
        
    def getMoveset(self):
        """
        This method returns a complete moveset, it does not check the board 
        for conlicting pieces
        """
        print("No piece should get here")
    pieceLetter = "NA"
    def __str__(self):
        toStrValue = ""
        if(self.color ==  0):
            toStrValue = self.pieceLetter.upper()
        else:
            toStrValue = self.pieceLetter.lower()
            
        return toStrValue + chr(ord('a') + self.x - 1) + str(self.y)
    
class King(Piece):
    pieceLetter = "k"
    
    def getMoveset(self):
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
    
    def getMoveset(self):
        return [(self.x, self.y +1)]

class Rook(Piece):
    pieceLetter = "r"
    
    def getMoveset(self):
        moves = []
        
        #Add moves to the left
        x = self.x - 1
        while(x > 0):
            moves.append((x, self.y))
            x = x - 1
        #Add moves to the right
        x = self.x + 1
        while(x < 9):
            moves.append((x, self.y))
            x = x + 1
        y = self.y - 1
        #Add moves to the bottom
        while(y > 0):
            moves.append((self.x, y))
            y = y - 1
        #Add moves to the top
        y = self.y + 1
        while(y < 9):
            moves.append((self.x, y))
            y = y + 1
        
        return moves

class Bishop(Piece):
    pieceLetter = "b"
    
    def getMoveset(self):
        moves = []
        
        #Add moves to the left-down
        x = self.x - 1
        y = self.y - 1
        while(x > 0 and y > 0):
            moves.append((x, y))
            x = x - 1
            y = y - 1
            
        #Add moves to the left-up
        x = self.x - 1
        y = self.y + 1
        while(x > 0 and y < 9):
            moves.append((x, y))
            x = x - 1
            y = y + 1
            
        #Add moves to the right-down
        x = self.x + 1
        y = self.y - 1
        while(x < 9 and y > 0):
            moves.append((x, y))
            x = x + 1
            y = y - 1
        
        #Add moves to the right-up
        x = self.x + 1
        y = self.y + 1
        while(x < 9 and y < 9):
            moves.append((x, y))
            x = x + 1
            y = y + 1
        
        return moves

class Knight(Piece):
    pieceLetter = "n"
    
    def getMoveset(self):
        return [(self.x - 1, self.y + 2),
                (self.x + 1, self.y + 2),
                (self.x + 2, self.y + 1),
                (self.x + 2, self.y - 1),
                (self.x - 2, self.y + 1),
                (self.x - 2, self.y - 1),
                (self.x - 1, self.y - 2),
                (self.x + 1, self.y - 2)]