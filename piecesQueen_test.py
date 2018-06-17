# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:24:51 2018

@author: Dan
"""

import unittest
from chessboard import ChessBoard

class QueenMoves(unittest.TestCase):
    
    def testCenterAllMoves(self):
        board = ChessBoard()
        board.addPieceToBoard("Queen", 4, 4, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(27, len(moves))
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
        self.assertIn((3, 3), moves) #15
        self.assertIn((2, 2), moves) #16
        self.assertIn((1, 1), moves) #17
        self.assertIn((5, 5), moves) #18
        self.assertIn((6, 6), moves) #19
        self.assertIn((7, 7), moves) #20
        self.assertIn((8, 8), moves) #21
        self.assertIn((5, 3), moves) #22
        self.assertIn((6, 2), moves) #23
        self.assertIn((7, 1), moves) #24
        self.assertIn((3, 5), moves) #25
        self.assertIn((2, 6), moves) #26
        self.assertIn((1, 7), moves) #27
        
    def testCenterAllMovesBlockedSame(self):
        board = ChessBoard()
        board.addPieceToBoard("Queen", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 4, "White")
        board.addPieceToBoard("Pawn", 3, 5, "White")
        board.addPieceToBoard("Pawn", 4, 5, "White")
        board.addPieceToBoard("Pawn", 5, 5, "White")
        board.addPieceToBoard("Pawn", 5, 4, "White")
        board.addPieceToBoard("Pawn", 5, 3, "White")
        board.addPieceToBoard("Pawn", 4, 3, "White")
        board.addPieceToBoard("Pawn", 3, 3, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        
    def testCenterAllMovesBlockedDiff(self):
        board = ChessBoard()
        board.addPieceToBoard("Queen", 4, 4, "Black")
        board.addPieceToBoard("Pawn", 3, 4, "White")
        board.addPieceToBoard("Pawn", 3, 5, "White")
        board.addPieceToBoard("Pawn", 4, 5, "White")
        board.addPieceToBoard("Pawn", 5, 5, "White")
        board.addPieceToBoard("Pawn", 5, 4, "White")
        board.addPieceToBoard("Pawn", 5, 3, "White")
        board.addPieceToBoard("Pawn", 4, 3, "White")
        board.addPieceToBoard("Pawn", 3, 3, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(8, len(moves))