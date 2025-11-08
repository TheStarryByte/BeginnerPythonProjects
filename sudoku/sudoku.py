def find_next_empty(puzzle):
    # it finds the row, col that is not filled yet repat with -1
    # return row, col tuple or none if there is none
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # figures if guess is valid
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = []
    for i in range (9):
        col_vals.append(puzzle[i][col])
        if guess in col_vals:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range (row_start, row_start + 3):
            for c in range (col_start, col_start + 3):
                if puzzle [r][c] == guess:
                    return False

        # if we get here then its valid
def solve_sudoku(puzzle):
    # solve sudoku using backtracking technique
    # our puzzle is list of lists
    #return whether a solution exits
    # mutates puzzle to be the solution

    # first step 1 choose where in the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    # step 1.2 if there is nowhere then were done because we only allowed valid inputs
    if row is None:
        return True
    # step 2 if there is a place then we guess number from 1 to 9
    for guess in range(1, 10): # 1,2,3......9
        # step 3 check if it is valid  guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recurse using puzzle
            # recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5 if not valid or if it does not solve puzzle
        # backtrack try another number
        puzzle [row][col] = -1

    # if no number works then this puzzle in unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
