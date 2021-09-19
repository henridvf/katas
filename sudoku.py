import numpy as np

def done_or_not(board):
    rows_chk, cols_chk, regions_chk = False, False, False
    board = np.array(board)
    digits = [1,2,3,4,5,6,7,8,9]

    # check rows
    for row in range(0, 9):
        rows_chk = True if all(digit in board[row, :] for digit in digits) else False

    # checks columns
    for col in range(0, 9):
        cols_chk = True if all(digit in board[:, col] for digit in digits) else False
    
    # check regions
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            regions_chk = True if all(digit in board[row:row+3, col:col+3] for digit in digits) else False
    
    # Result
    if rows_chk == False or cols_chk == False or regions_chk == False:
        return 'Try again!'
    else:
        return 'Finished!'



# print(done_or_not(
#     [[1, 3, 2, 5, 7, 9, 4, 6, 8]
#     ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#     ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#     ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#     ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#     ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#     ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#     ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#     ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

print(done_or_not(
    [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))