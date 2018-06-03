# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:11:57 2018

@author: Dan
"""

class ChessBoard:
    
    def __init__(self):
        self.ranks = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,Pawn(5, 2, 0),0,0,0],
                      [0,0,0,0,King(5, 1, 0),0,0,0]]
    def display(self):
        for rank in self.ranks:
            for square in rank:
                print(square, end="\t")
            print("")
    def calculateAllMoves():
        print("Not implemented")
    
    def removeIllegalMoves(self, p):
        moveset = p.getMoveset();
        for move in moveset:
            if(move[0] > 8 or move[0] < 1 or move[1] > 8 or move[1] < 1):
                moveset.remove(move)
        return moveset

class Piece:
        
    def __init__(self, current_x, current_y, color):
        self.x = current_x
        self.y = current_y
        self.color = color
        
    def getMoveset(self):
        print("No piece should get here")
    
class King(Piece):
        
    
    def __str__(self):
        return "K"  
    
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
    def __str__(self):
        return "p"  

        
king = King(5, 1, 0)
print(king.getMoveset())
board = ChessBoard()
print(board.removeIllegalMoves(king))
board.display()