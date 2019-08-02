'''
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


'''
def is_valid(string,cut):
  my_string = string.split()
  cut_strip = cut.strip().split()
  for x in cut_strip:
    if x not in my_string:
      return False
  return True

def cut_me_baby(string, k, ans=[]):
  if len(string) == 0:
    return True

  for x in range(k, 1, -1):
    cut = string[:x]
    if is_valid(string,cut):
      ans.append(cut)
      if cut_me_baby(string[x:], k):
        return True, ans
      ans.pop()

  return False


if __name__ == '__main__':
  str1 = 'the quick brown fox jumps over the lazy dog and I love you'
  str2 = 'what is the time in England and do foxes love boxes'
  print(cut_me_baby(str1, 10))
