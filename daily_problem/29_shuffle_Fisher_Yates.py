'''
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''

import random

def shuffle(arr):
  n = len(arr)
  for x in range(n):
    i = random.randint(x, n-1)
    arr[x], arr[i] = arr[i], arr[x]
  return arr

if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7,8,9]
  arr2 = [x+1 for x in range(52)]
  print(shuffle(arr))
  print(shuffle(arr2))
