def print_board(board):
    """ Function to print the board with 'Q' for queens and '.' for empty spaces """
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def solve_n_queens(n):
    """ Function to solve the N-Queens problem using Backtracking + Branch and Bound """
    board = [[0]*n for _ in range(n)]  # Initialize the board
    col_used = [False] * n            # Columns under attack
    diag1 = [False] * (2*n - 1)       # Diagonal (row + col) under attack
    diag2 = [False] * (2*n - 1)       # Diagonal (row - col + (n-1)) under attack

    def backtrack(row):
        """ Helper function to place queens row by row """
        if row == n:  # All queens placed successfully
            print_board(board)
            return True  # Found a valid solution
        
        for col in range(n):
            # Check if placing a queen in this column and diagonals is safe (no conflict)
            if not col_used[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                # Place the queen
                board[row][col] = 1
                col_used[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                
                # Print board after placing the queen
                print(f"Placing queen at ({row}, {col}):")
                print_board(board)
                
                # Recursively place queen in the next row
                if backtrack(row + 1):
                    return True
                
                # Backtrack: remove queen and reset constraints
                board[row][col] = 0
                col_used[col] = diag1[row + col] = diag2[row - col + n - 1] = False
                print(f"Backtracking from ({row}, {col}):")
                print_board(board)

        return False  # No valid placement found in this row

    # Start the backtracking process from the first row
    if not backtrack(0):
        print("No solution exists.")
    else:
        print("Solution found!")

# Example usage: Solving the 4-Queens problem
n = 4
solve_n_queens(n)
