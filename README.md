# Chess Move Calculator

## Running Tests
I created for my local use a .bat file containing the command to run all tests
that were relevant for the project. However if using a non-windows machine the
.bat file will not be operatable, instead use the following command:

python -m unittest -v boardInitializer_test.py chessboard_test pieceFactory_test.py piecesKnight_test.py piecesKnight_test.py piecesKing_test.py piecesPawn_test.py piecesBishop_test.py piecesRook_test.py piecesQueen_test.py

## Design
The main three modules that make the calculation go are chessboard.py, pieces.py,
and pieceFactory.py. The class ChessBoard in chessboard.py is a container for the 
rank and files of the board. Pieces are added to the board by using the makePiece
method in pieceFactory. I used complete words as input in the factory because early
on I didn't know how I would be loading up complete boards. It was later in the
project's development I decided on .fen files (explained in a later section).
Finally pieces.py contains a Piece base class that handles core piece logic such as
determining if a move would be illegal, getting squares, and determining out of bounds.