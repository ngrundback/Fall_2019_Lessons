'''
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

'''
def is_palindrom(sub):
  return sub[::-1] == sub

def palindrom(word):
  longest = ''
  length = len(word)
  for x in range(length-1):
    for y in range(1, length):
      substring = word[x:y]
      if is_palindrom(substring) and len(substring) > len(longest):
        longest = substring
  return longest



if __name__ == '__main__':
  word1 = 'aabcdcb'
  word2 = 'bannas'
  print(palindrom(word1))
  print(palindrom(word2))
