def isValid(m, n, y, x):
    return y >= 0 and x >= 0 and y < m and x < n

def countAliveNeighbors(board, m, n, i, j):
    # go around all the neighbors of position (i, j), skipping (i, j) itself
    count = 0
    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            # valid position
            if not (y == i and j == x) and isValid(m, n, y, x):
                # position is alive
                if board[y][x] == "X":
                    count += 1
    return count

def game_of_life(board):
    m = len(board)
    n = len(board[0])
    # initialize next_board to be dead
    next_board = [[" " for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            curr_count = countAliveNeighbors(board, m, n, i, j)
            # current cell is alive
            if board[i][j] == "X":
                # next_board is dead, so only need to modify for
                # live positions
                if 2 <= curr_count <= 3:
                    next_board[i][j] = "X"
            # current cell is dead
            else:
                if curr_count == 3:
                    next_board[i][j] = "X"
    return next_board

def printBoard(expression, board):
    print(expression)
    for line in board:
        print(line)

if __name__ == '__main__':

    inp_board = [
            [" "," "," "," "," "],
            [" "," "," "," "," "],
            [" ","X","X","X"," "],
            [" "," "," "," "," "],
            [" "," "," "," "," "]
    ]

    out_board = [
            [" "," "," "," "," "],
            [" "," ","X"," "," "],
            [" "," ","X"," "," "],
            [" "," ","X"," "," "],
            [" "," "," "," "," "]
    ]

    printBoard("Input Board:", inp_board)
    printBoard("Your next board:", game_of_life(inp_board))
    printBoard("Expected next board:", out_board)

    printBoard("Input Board:", out_board)
    printBoard("Your next board:", game_of_life(out_board))
    printBoard("Expected next board:", inp_board)
