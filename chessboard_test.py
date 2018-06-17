# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:52:06 2018

@author: Dan
"""

import unittest
from chessboard import ChessBoard

class ChessBoardTests(unittest.TestCase):
    
    def testSumTwoPieces(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 1, 2, "White")
        board.addPieceToBoard("Pawn", 2, 2, "White")
        self.assertEqual(board.calculateAllMoves(0), 4)
    
    def testSumFourPieces(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 5, 2, "White")
        board.addPieceToBoard("Pawn", 4, 2, "White")
        board.addPieceToBoard("Pawn", 6, 2, "White")
        board.addPieceToBoard("King", 5, 1, "White")
        self.assertEqual(board.calculateAllMoves(0), 8)
        
        
    def testSumFourPiecesWhiteCanCastle(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 5, 2, "White")
        board.addPieceToBoard("Pawn", 4, 2, "White")
        board.addPieceToBoard("Pawn", 6, 2, "White")
        board.addPieceToBoard("King", 5, 1, "White")
        board.whiteCanCastle()
        self.assertEqual(board.calculateAllMoves(0), 9)
        
        
    def testSumFourPiecesBlackCanCastle(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 5, 2, "Black")
        board.addPieceToBoard("Pawn", 4, 2, "Black")
        board.addPieceToBoard("Pawn", 6, 2, "Black")
        board.addPieceToBoard("King", 4, 1, "Black")
        board.blackCanCastle()
        self.assertEqual(board.calculateAllMoves(1), 6)
        
    def testOppositeNotCounted(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 5, 2, "White")
        board.addPieceToBoard("Pawn", 4, 2, "White")
        board.addPieceToBoard("Pawn", 6, 2, "White")
        board.addPieceToBoard("King", 5, 1, "White")
        board.addPieceToBoard("King", 5, 8, "Black")
        board.blackCanCastle()
        self.assertEqual(board.calculateAllMoves(1), 6)
        
    def testOppositeNothing(self):
        board = ChessBoard()
        board.addPieceToBoard("Pawn", 5, 2, "Black")
        board.addPieceToBoard("Pawn", 4, 2, "Black")
        board.addPieceToBoard("Pawn", 6, 2, "Black")
        board.addPieceToBoard("King", 5, 1, "Black")
        board.blackCanCastle()
        self.assertEqual(board.calculateAllMoves(0), 0)