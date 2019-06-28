# what could go wrong
def find_word(str, dict):
    temp_word = ''
    ans = []
    for x in str:
        temp_word += x
        if temp_word in dict.values():
            ans.append(temp_word)
            temp_word = ''
    return ans

if __name__ == '__main__':
    dict = {
        1:'baby',
        2: 'estelle',
        3: 'best',
        4: 'is',
        5: 'the'
    }
    str = 'estelleisthebest'
    print(find_word(str,dict))
