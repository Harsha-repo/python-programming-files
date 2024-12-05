def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]==1:
            return  False
    
    return True
def solve_n_queens_util(board,row,n):
    if row>=n:
        return True
    

    for i in range(n):
        if is_safe(board,row,i,n):
            board[row][i]=1

            if solve_n_queens_util(board,row+1,n):
              return True
        
        board[row][i]=0
    
    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _  in range(n)]

    if solve_n_queens_util(board,0,n):
        printboard(board,n)
        return True
    else:
        print('no solution foound')
        return False
    
def printboard(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print('.',end=" ")
        print()

n=8
solve_n_queens(n)