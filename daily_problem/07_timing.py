def auto_fill(words,strt):
    results = set()
    for x in words:
        if x.startswith(strt):
            results.add(x)
    return results

words = ['dogs', 'doug', 'dough', 'eang', 'dope']

print(auto_fill(words, 'dop'))

END_HERE = 'ENDS_HERE'

class Trie():
    def __init__(self):
        self.trie = {}

    def insert(self,text):
        trie = self.trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[END_HERE] = True

    def elements(self, prefix):
        trie = self.trie
        for letter in prefix:
            if prefix in trie:
                trie = trie[letter]
            else:
                return []
        return self._elements(self.trie)

    def _elements(self, trie):
        results = []
        for key,value in trie.items():
            if key == END_HERE:
                subresults = ['']
            else:
                subresults = [key + s for s in self._elements(value)]
            results.extend(subresults)
        return results


trie = Trie()

for x in words:
    trie.insert(x)

def do(s):
    sufx = trie.elements(s)
    return [s + w for w in sufx]

print(do('do'))
