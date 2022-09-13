WIDTH = 10
HEIGHT = 20

# milliseconds
TIMEOUT = 800
MIN_TIMEOUT = 200
DEC_TIME = int((TIMEOUT-MIN_TIMEOUT)/10)

LINE_SCORE = 100
LEVEL_SCORE = 20 * LINE_SCORE

# strings representing blocks and grid borders
BLOCK = '[]'
V_BORDER = '||'
H_BORDER = '='
EMPTY = 0

WIN_X = 4
WIN_Y = 1
OFFSET_X = len(V_BORDER)
OFFSET_Y = 1
# initial position when a new tetromino is spawned
START_X = (WIDTH - 4) >> 1
START_Y = 0

# information window properties
IWIN_X = WIN_X + len(BLOCK) * (WIDTH + 2) + 1
IWIN_Y = WIN_Y + 1
IOFF_X = 1

# controlling signals
DOWN = 258
ROTATE = 259
LEFT = 260
RIGHT = 261
DROP = ord(' ')
PAUSE = ord('p')
QUIT = ord('q')


# the coordinates of each tetris block, represented as (y, x) on a 4x4 grid,
TETROMINOS = (
    ((0, 0), (0, 1), (1, 0), (1, 1)),

    ((0, 2), (1, 2), (2, 2), (3, 2)),
    ((1, 0), (1, 1), (1, 2), (1, 3)),

    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 1), (1, 0), (1, 1), (2, 0)),

    ((0, 1), (0, 2), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (1, 1), (2, 1)),

    ((0, 1), (0, 2), (1, 1), (2, 1)),
    ((1, 0), (1, 1), (1, 2), (2, 2)),
    ((0, 1), (1, 1), (2, 0), (2, 1)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),

    ((0, 1), (1, 1), (2, 1), (2, 2)),
    ((1, 0), (1, 1), (1, 2), (2, 0)),
    ((0, 0), (0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 0), (1, 1), (1, 2)),

    ((0, 1), (1, 1), (1, 2), (2, 1)),
    ((1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 1), (1, 0), (1, 1), (2, 1)),
    ((0, 1), (1, 0), (1, 1), (1, 2))
)

# index chain to get the rotated tetromino
#       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
NEXT = (0, 2, 1, 4, 3, 6, 5, 8, 9, 10, 7, 12, 13, 14, 11, 16, 17, 18, 15)

# colors of different tetrominoes
COLORS = (1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7)

# rearrange the probability of each tetromino
PIECES = (0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)