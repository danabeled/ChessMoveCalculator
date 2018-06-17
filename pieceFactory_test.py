# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:03:47 2018

@author: Dan
"""

import unittest
from pieceFactory import makePiece

class TestMakingPieces(unittest.TestCase):
    
    def testKing(self):
        self.assertEqual(str(makePiece("King", 1, 1, 0)), "Ka1")
    
    def testXIsSet(self):
        self.assertEqual(makePiece("King", 1, 1, 0).getX(), 1)
    
    def testWhite(self):
        self.assertEqual(str(makePiece("King", 1, 1, "White"))[0], "K")
        
    def testBlack(self):
        self.assertEqual(str(makePiece("King", 1, 1, "Black"))[0], "k")
    
    def testQueen(self):
        self.assertEqual(str(makePiece("Queen", 1, 1, 0)), "Qa1")
    
    def testRook(self):
        self.assertEqual(str(makePiece("Rook", 1, 1, 0)), "Ra1")
    
    def testBishop(self):
        self.assertEqual(str(makePiece("Bishop", 1, 1, 0)), "Ba1")
    
    def testKnight(self):
        self.assertEqual(str(makePiece("Knight", 1, 1, 0)), "Na1")
    
    def testPawn(self):
        self.assertEqual(str(makePiece("Pawn", 1, 1, 0)), "Pa1")