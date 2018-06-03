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
