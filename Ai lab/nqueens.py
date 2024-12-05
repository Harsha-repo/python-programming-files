

def is_safe(board, row, col, n): # board is plane , row is row and col is col and n is size of the board 
    # Check if there's a queen in the same column
    for i in range(row):                        # how we traverse is like we will start from the zeroth row and start placing all the queens 
                                                # we ensure to travel till the  last row by not placing the queen in the same column    
        if board[i][col] == 1:
            return False
# another checking is done in the diagonals checking the right up and left up diagonals and ensuring that we will not palce the queen in any of the diagonals
# below two fucntions do that 

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):     # the zip fucntion creates the pairs (x,y) af the row and column and checks 
                                                                # if the pair already has a queen then returns false 
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

# this is fucntion that checks each row  and palces the queens
def solve_n_queens_util(board, row, n):
    # If all queens are placed
    if row >= n:                   # if the all rows   are traversed  then its like we palced all the queens
        return True



    # Try placing the queen in all columns one by one 
    for i in range(n):
        if is_safe(board, row, i, n):
            # Place the queen
            board[row][i] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, row + 1, n):
                return True

            # If placing queen in board[row][i] doesn't lead to a solution,
            # then remove the queen
            board[row][i] = 0

    # If the queen cannot be placed in any column in this row, return False
    return False

def solve_n_queens(n):
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)] 

    if solve_n_queens_util(board, 0, n):
        print_board(board, n)
        return True
    else:
        print("No solution exists")
        return False

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Example usage:
n = 8
solve_n_queens(n)
