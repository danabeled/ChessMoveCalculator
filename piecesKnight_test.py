# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:33:04 2018

@author: Dan
"""


import unittest
from chessboard import ChessBoard

class KnightMoves(unittest.TestCase):
    
    def testKnightCenterAllMoves(self):
        board = ChessBoard()
        board.addPieceToBoard("Knight", 4, 4, 0)
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(8, len(moves))
        self.assertIn((2, 3), moves)
        self.assertIn((2, 5), moves)
        self.assertIn((3, 6), moves)
        self.assertIn((3, 2), moves)
        self.assertIn((5, 2), moves)
        self.assertIn((5, 6), moves)
        self.assertIn((6, 3), moves)
        self.assertIn((6, 5), moves)
        
    def testKnightCenterJumps(self):
        board = ChessBoard()
        board.addPieceToBoard("Knight", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 4, "White")
        board.addPieceToBoard("Pawn", 3, 5, "White")
        board.addPieceToBoard("Pawn", 4, 5, "White")
        board.addPieceToBoard("Pawn", 5, 5, "White")
        board.addPieceToBoard("Pawn", 5, 4, "White")
        board.addPieceToBoard("Pawn", 5, 3, "White")
        board.addPieceToBoard("Pawn", 4, 3, "White")
        board.addPieceToBoard("Pawn", 3, 3, "White")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(8, len(moves))
        self.assertIn((2, 3), moves)
        self.assertIn((2, 5), moves)
        self.assertIn((3, 6), moves)
        self.assertIn((3, 2), moves)
        self.assertIn((5, 2), moves)
        self.assertIn((5, 6), moves)
        self.assertIn((6, 3), moves)
        self.assertIn((6, 5), moves)
    
    def testKnightCenterConflictingSquareSameColor(self):
        board = ChessBoard()
        board.addPieceToBoard("Knight", 4, 4, 0)
        board.addPieceToBoard("Pawn", 2, 3, 0)
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertNotIn((2, 3), moves)
    
    def testKnightCenterConflictingSquareDiffColor(self):
        board = ChessBoard()
        board.addPieceToBoard("Knight", 4, 4, "White")
        board.addPieceToBoard("Pawn", 2, 3, "Black")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertIn((2, 3), moves)
        