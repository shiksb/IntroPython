def game_of_life(board):
    #Your codes here

    return next_board


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

    print("Input Board:", inp_board)
    print("Your next board:", game_of_life(inp_board))
    print("Expected next board:", out_board)

    print("Input Board:", out_board)
    print("Your next board:", game_of_life(out_board))
    print("Expected next board:", inp_board)
