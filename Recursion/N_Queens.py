def solveNQueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
            
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result



# Example usage:
n = 4
solutions = solveNQueens(n)

print(f"All solutions for {n}-Queens problem:")

for i, solution in enumerate(solutions, 1):
    print(f"\nSolution {i}:")
    for row in solution:
        print(row)
