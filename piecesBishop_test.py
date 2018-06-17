# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:24:51 2018

@author: Dan
"""

import unittest
from chessboard import ChessBoard

class BishopMoves(unittest.TestCase):
    
    def testCenterAllMoves(self):
        board = ChessBoard()
        board.addPieceToBoard("Bishop", 4, 4, "White")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(13, len(moves))
        self.assertIn((3, 3), moves) #1
        self.assertIn((2, 2), moves) #2
        self.assertIn((1, 1), moves) #3
        self.assertIn((5, 5), moves) #4
        self.assertIn((6, 6), moves) #5
        self.assertIn((7, 7), moves) #6
        self.assertIn((8, 8), moves) #7
        self.assertIn((5, 3), moves) #8
        self.assertIn((6, 2), moves) #9
        self.assertIn((7, 1), moves) #10
        self.assertIn((3, 5), moves) #11
        self.assertIn((2, 6), moves) #12
        self.assertIn((1, 7), moves) #13
        
    def testCenterAllMovesBlockedSame(self):
        board = ChessBoard()
        board.addPieceToBoard("Bishop", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 3, "White")
        board.addPieceToBoard("Pawn", 5, 5, "White")
        board.addPieceToBoard("Pawn", 3, 5, "White")
        board.addPieceToBoard("Pawn", 5, 3, "White")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        
    def testCenterAllMovesBlockedDiff(self):
        board = ChessBoard()
        board.addPieceToBoard("Bishop", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 3, "Black")
        board.addPieceToBoard("Pawn", 5, 5, "Black")
        board.addPieceToBoard("Pawn", 3, 5, "Black")
        board.addPieceToBoard("Pawn", 5, 3, "Black")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(4, len(moves))