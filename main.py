# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:55:48 2018

@author: Dan
"""

from chessboard import ChessBoard
import pieces


knight = pieces.Knight(4, 5, 0)
king = pieces.King(5, 1, 0)
rook = pieces.Rook(6,7,0)
bishop = pieces.Bishop(2,2,0)
queen = pieces.Queen(2,4,0)
pawn = pieces.Pawn(4, 2, 0)
board = ChessBoard()
board.addPieceToBoard("King", 5, 1, "White")
board.display()
print("King's moves:", board.getRank(5, 1).getMoveset(board.getRanks()))
print(repr(knight))
print("Knights's moves:", knight.getMoveset(board.getRanks()))
print("Rook's moves:", rook.getMoveset(board.getRanks()))
print("Bishop's moves:", bishop.getMoveset(board.getRanks()))
print("Queen's moves:", queen.getMoveset(board.getRanks()))
print("Pawn's moves: ", pawn.getMoveset(board.getRanks()))
board.display()
print(board.calculateAllMoves(0))