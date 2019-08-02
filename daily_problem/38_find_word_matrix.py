'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

'''

def find_word(matrix, word):
# left to right
  for x in matrix:
    if ''.join(x) == word:
      return True, word
  for x in range(len(matrix)):
    col = [row[x] for row in matrix]
    if ''.join(col) == word:
      return True, word







if __name__ == '__main__':
  m = [
  ['F', 'M', 'A', 'M'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']
  ]
  word = 'FOAM'
  print(find_word(m, word))
