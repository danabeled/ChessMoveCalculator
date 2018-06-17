# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:17:05 2018

@author: Dan
"""


import unittest
from chessboard import ChessBoard

class PawnMoves(unittest.TestCase):
    
    def testPawnUnblocked(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(1, len(moves))
        self.assertIn((4, 5), moves)
        
    
    def testPawnUnblockedFirstSquareWhite(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 2, "White")
        moves = board.getSquare(4, 2).getMoveset(board.getRanks())
        self.assertEqual(2, len(moves))
        self.assertIn((4, 3), moves)
        self.assertIn((4, 4), moves)

    
    def testPawnBlockedFirstSquareWhite(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 2, "White")
        board.addPieceToBoard("Pawn", 4, 3, "White")
        moves = board.getSquare(4, 2).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        
    def testPawnConflictFirstSquareWhite(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 2, "White")
        board.addPieceToBoard("Pawn", 4, 4, "White")
        moves = board.getSquare(4, 2).getMoveset(board.getRanks())
        self.assertEqual(1, len(moves))
        self.assertIn((4, 3), moves)
        
    def testPawnBlockedFirstSquareBlack(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 7, "Black")
        board.addPieceToBoard("Pawn", 4, 6, "Black")
        moves = board.getSquare(4, 7).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        
    def testPawnConflictFirstSquareBlack(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 7, "Black")
        board.addPieceToBoard("Pawn", 4, 5, "Black")
        moves = board.getSquare(4, 7).getMoveset(board.getRanks())
        self.assertEqual(1, len(moves))
        self.assertIn((4, 6), moves)
    
    
    def testPawnUnblockedFirstSquareBlack(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 7, "Black")
        moves = board.getSquare(4, 7).getMoveset(board.getRanks())
        self.assertEqual(2, len(moves))
        self.assertIn((4, 6), moves)
        self.assertIn((4, 5), moves)     
        
        
    def testPawnUnblockedBlack(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "Black")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(1, len(moves))
        self.assertIn((4, 3), moves)
        
    def testPawnBlockedSameColor(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 5, "White")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        self.assertNotIn((4, 5), moves)
        
    def testPawnBlockedDiffColor(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 5, "Black")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertEqual(0, len(moves))
        self.assertNotIn((4, 5), moves)
        
    def testPawnBlockedAttackLeft(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 5, "Black")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertIn((3, 5), moves)
        
        
    def testPawnBlockedAttackRight(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 5, 5, "Black")
        moves = board.getSquare(4, 4).getMoveset(board.getRanks())
        self.assertIn((5, 5), moves)     
        
    def testPawnBlockedAttackBlackLeft(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 3, 5, "Black")
        moves = board.getSquare(3, 5).getMoveset(board.getRanks())
        self.assertIn((4, 4), moves)
        
        
    def testPawnBlockedAttackBlackRight(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 4, 4, "White")
        board.addPieceToBoard("Pawn", 5, 5, "Black")
        moves = board.getSquare(5, 5).getMoveset(board.getRanks())
        self.assertIn((4, 4), moves)
        
        