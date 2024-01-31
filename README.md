# Machine Problem Chess: Thinking Moves Ahead

* The program determines the number of moves it will take for the different chess pieces from their current position to any other tile in the board.
* The number in the output grid is the minimum number of moves it will take for the chess piece to reach each tile when there are occlusions in the board.
* A pawn may be promoted if it reaches the northernmost row of the board (the 8th row in the normal board). While a pawn may only move northward, once it reaches the end row, it         can be promoted to any of the pieces and may now move freely around the board.

## Program Mode
* The user will be asked to input which can be in this format:
    s1, s2, x1, y1, piece
    n
    n_i_1, n_i_2
    ...
* Wherein s1, s2 - horizontal size and vertical size of the board respectively.
  x1, y1 - starting position of the piece. 
  n - number of blocking pieces
  n_i_1, n_i_2 - coordinates of the ith blocking piece. There should be n of these
  piece - name of the piece. Use the following names. [pawn, rook, knight, bishop, queen, king]
* The output will be printed in this order: ((0,0)->(no. of columns,0)->(0,1)->(no. of columns,no. of rows) or the value of the output grid printed left to right going up as shown below.

![](direction.png)

* OR in this format
    s1, s2, x1, y1, x2, y2, pawn
    n
    n_1_1, n_1_2
    n_2_1, n_2_2
    …
* Wherein s1, s2 - horizontal size and vertical size of the board respectively.
  x1, y1 - starting position of the piece. 
  x2, y2 - desired ending position of the piece. May or may not be reachable. 
  n - number of blocking pieces
  n_i_1, n_i_2 - coordinates of the ith blocking piece. There should be n of these
  The piece will initially be a pawn. However it can be promoted to ANY of the chess pieces (rook, bishop, knight, apprentice, and queen).
* The output will be the number of moves for the pawn to reach the desired end square.

## Example:
INPUT 1:
8, 8, 3, 3, bishop
3
4, 2
2, 5
6, 4

* Visualization of board with blocking pieces
Source: https://lichess.org/editor/8/8/2P5/6P1/3B4/4P3/8/8_w_-_-_0_1
![](sample4.png)

* Visualization of solution with blocking pieces. The values are
the number of moves the bishop needs to reach each square in the
board. Unreachable squares have a value of -1. The starting position
has a value of 0
![](sample4.1.png)

* Actual output considering blocking pieces. Print left to right going up.
![](sample4.2.png)

INPUT 2:
8, 8, 0, 4, 1, 6, pawn
1
1, 7

* Visualization of board and calculation. Move 3 steps up. Promote to a bishop and move diagonally.
Source: https://lichess.org/editor/8/8/8/8/7p/8/8/6n1_w_-_-_0_1
![](sample5.png)

* OUTPUT: 4
3 + 1 = 4


