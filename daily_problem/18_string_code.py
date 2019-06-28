# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a
# single count and character. For example, the string
# "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string
# to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.

def encode(word):
    current_letter = word[0]
    count = 1
    ans = ''
    for x in range(1,len(word)):
        if word[x] == current_letter:
            count += 1
        else:
            ans += str(count) + word[x-1]
            count = 1
            current_letter = word[x]
    ans += str(count) + word[-1]
    return ans

print(encode('AAAABBBCCDAA'))

def decode(word):
    ans = ''
    for y in word:
        if y.isdigit():
            count = int(y)
        else:
            ans += y * count
            count = 0
    return ans

print(decode('4A3B2C1D2A'))
