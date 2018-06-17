# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:08:36 2018

@author: Dan
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:33:04 2018

@author: Dan
"""


import unittest
from chessboard import ChessBoard
from pieces import King

class KingMoves(unittest.TestCase):
    
    def testKingCenterAllMoves(self):
        board = ChessBoard()
        board.addPieceToBoard("King", 4, 4, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertEqual(8, len(moves))
        self.assertIn((3, 3), moves)
        self.assertIn((3, 4), moves)
        self.assertIn((3, 5), moves)
        self.assertIn((4, 5), moves)
        self.assertIn((5, 5), moves)
        self.assertIn((5, 4), moves)
        self.assertIn((5, 3), moves)
        self.assertIn((4, 3), moves)
        
        
    def testKingCenterConflictingSquareSameColor(self):
        board = ChessBoard()
        board.addPieceToBoard("King", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 3, "White")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertNotIn((4, 3), moves)
    
    def testKingCenterConflictingSquareDiffColor(self):
        board = ChessBoard()
        board.addPieceToBoard("King", 4, 4, "White")
        board.addPieceToBoard("Pawn", 4, 3, "Black")
        moves = board.getRank(4, 4).getMoveset(board.getRanks())
        self.assertIn((4, 3), moves)
        