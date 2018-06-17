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
        board.addPieceToBoard("Rook", 4, 4, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(14, len(moves))
        self.assertIn((4, 3), moves) #1
        self.assertIn((4, 2), moves) #2
        self.assertIn((4, 1), moves) #3
        self.assertIn((4, 5), moves) #4
        self.assertIn((4, 6), moves) #5
        self.assertIn((4, 7), moves) #6
        self.assertIn((4, 8), moves) #7
        self.assertIn((5, 4), moves) #8
        self.assertIn((6, 4), moves) #9
        self.assertIn((7, 4), moves) #10
        self.assertIn((8, 4), moves) #11
        self.assertIn((3, 4), moves) #12
        self.assertIn((2, 4), moves) #13
        self.assertIn((1, 4), moves) #14
        
    def testCenterAllMovesBlockedSame(self):
        board = ChessBoard()
        board.addPieceToBoard("Rook", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 3, "White")
        board.addPieceToBoard("Pawn", 4, 5, "White")
        board.addPieceToBoard("Pawn", 3, 4, "White")
        board.addPieceToBoard("Pawn", 5, 4, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        
    def testCenterAllMovesBlockedDiff(self):
        board = ChessBoard()
        board.addPieceToBoard("Rook", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 3, "Black")
        board.addPieceToBoard("Pawn", 4, 5, "Black")
        board.addPieceToBoard("Pawn", 3, 4, "Black")
        board.addPieceToBoard("Pawn", 5, 4, "Black")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(4, len(moves))