from pprint import pprint


def find_next_empty(puzzle):
    # finds the next row (any open space has -1) col on the puzzle that = to -1
    # retun row, col tuple (or(none, None))  if there is no empty space then return a tuple none,, none
    
    # keep in mind that we are using 0-8 for our indicies 
    # check each row and each colum and return the row colum value of the first empty space 
    for r in range(9): # for each row in the 9 rows 
        for c in range(9): # range 9 is 0 to 8
            if puzzle[r][c] == -1: # how we index, we pick out the row, and then within that row we use C to index again and get the column, if it = -1 then we return it 
                return r, c
            
    return None, None  # if no spaces are left (first none gets to row second get to column)


def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col of the uzzle is a valid guess 
    # returns True if is valid, False otherwise 
    
    #lets start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #now the column
#    col_vals = []
#    for i in range(9):
   #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # and then the square 
    # this is tricky, but we want to get where the 3x3 square starts 
    # and iterate over the 3 values in the row/colum 
    row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True

def solve_sudoku(puzzle):
    # solve sudoku using a backtracking technique 
    # our puzzle will be a list of lists, inner list is the row 
    # returning whether a solution exists 
    # we are mutating to be the solution if solution exists
    
    # step 1: choose somewhere on the puzzle to make a guess (we can try every combination until it is valid)
    row, col = find_next_empty(puzzle) # so we can find the empty spaces 
    
    # step 1.1:  if there's nowhere left, then we're done because we only allowed valid inputs (we need some validation checks)
    # we only have to check one 
    if row is None: 
        return True # this means we have solved the puzzle 
    
    # step 2:if there is a place to put a number, then make a guess between 1 and 9 
    for guess in range(1, 10): # range (1, 10) is 1, 2 3... 9
        # step 3: check if this is valid guess 
        if is_valid(puzzle, guess, row, col): # another helper function using the info we need 
            # step 3.1 if this is valid, then place that guess on the puzzle 
            puzzle[row][col] = guess
            # now recurse using this puzzle 
            # step 4: recursively call our function 
            if solve_sudoku(puzzle):
                return True
            
            # step 5: if not valid or if our guess does not solve the puzzle, the we need to 
            # backtrack and try a new number 
            puzzle[row][col] = -1 # reset the guess 
        
        # step 6: if none of th numbers that we try work, then this puzzle is unsolvable
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
    pprint(example_board)