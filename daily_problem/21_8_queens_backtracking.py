import random, pprint

def is_safe(board, row, col):
  # check left side of row
  for i in range(col):
    if board[row][i] == 1:
      return False
  # check diagonal up left
  for x, y in zip(range(row,-1,-1), range(col ,-1,-1)):
    if board[x][y] == 1:
      return False
  # check lower  diagonal left side
  for x, y in zip(range(row,Q,1), range(col,-1,-1)):
    if board[x][y] == 1:
      return False

  return True

def solve(board,col):
  # one queen per col
  # So, just need to know on what row to place

   # base case: If all queens are placed
   # then return true
  if col >= Q:
    return True

  for queen in range(Q):

    if is_safe(board, queen, col):
      board[queen][col] = 1
      # recursive call
      if solve(board, col+1) == True:
        return True
      # back to 0 if not so :(
      board[queen][col] = 0

  return board

if __name__ == '__main__':
  global Q
  Q = 15
  board = [[0 for x in range(Q)]for y in range(Q)]
  if solve(board,0) == True:
    pprint.pprint(board)
