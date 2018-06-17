# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:53:21 2018

@author: Dan
"""


import unittest
from chessboard import ChessBoard
from boardInitializer import analyzeRow

class BoardInitTests(unittest.TestCase):
    
    def testAnalyzeEmptyRow(self):
        board = ChessBoard()
        analyzeRow("8", 1, board)
        row = board.getRank(1)
        self.assertEqual(row[0], 0)
        self.assertEqual(row[1], 0)
        self.assertEqual(row[2], 0)
        self.assertEqual(row[3], 0)
        self.assertEqual(row[4], 0)
        self.assertEqual(row[5], 0)
        self.assertEqual(row[6], 0)
        self.assertEqual(row[7], 0)
        
    def testAddAWhitePawn(self):
        board = ChessBoard()
        analyzeRow("P7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "Pa1")
        
    def testAddABlackPawn(self):
        board = ChessBoard()
        analyzeRow("p7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "pa1")
        
    def testAddAWhiteRook(self):
        board = ChessBoard()
        analyzeRow("R7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "Ra1")
        
    def testAddABlackRook(self):
        board = ChessBoard()
        analyzeRow("r7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "ra1")
        
    def testAddAWhiteKnight(self):
        board = ChessBoard()
        analyzeRow("N7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "Na1")
        
    def testAddABlackKnight(self):
        board = ChessBoard()
        analyzeRow("n7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "na1")
        
    def testAddAWhiteBishop(self):
        board = ChessBoard()
        analyzeRow("B7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "Ba1")
        
    def testAddABlackBishop(self):
        board = ChessBoard()
        analyzeRow("b7", 1, board)
        row = board.getRank(1)
        board.display()
        self.assertEqual(str(row[0]), "ba1")