# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:17:05 2018

@author: Dan
"""


import unittest
from chessboard import ChessBoard
from pieces import Pawn

class PawnMoves(unittest.TestCase):
    
    def testPawnUnblocked(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(1, len(moves))
        self.assertIn((4, 5), moves)
        
    def testPawnBlockedSameColor(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 5, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        self.assertNotIn((4, 5), moves)
        
    def testPawnBlockedDiffColor(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 5, "Black")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        self.assertNotIn((4, 5), moves)
        
    def testPawnBlockedAttackLeft(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 5, "Black")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertIn((3, 5), moves)
        
        
    def testPawnBlockedAttackRigh(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 5, 5, "Black")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertIn((5, 5), moves)
        