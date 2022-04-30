# https://leetcode.com/problems/word-pattern/

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()

    if len(pattern) != len(words): return False 

    # Dual Mapping (Bidirectional mapping using 2 hashMaps)
    charToWord = {}
    wordToChar = {}

    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:  # check {c} -> {w}
            return False 
        if w in wordToChar and wordToChar[w] != c:  # check {w} -> {c}
            return False 
        
        charToWord[c] = w 
        wordToChar[w] = c

    return True


# Better 
def wordPattern2(pattern: str, s: str) -> bool:
    words, w_to_p = s.split(' '), dict()

    if len(pattern) != len(words): return False

    # There should be unique char <-> unique word mapping
    if len(set(pattern)) != len(set(words)): return False # for the case w = ['dog', 'cat'] and p = 'aa'

    for i in range(len(words)):
        if words[i] not in w_to_p: 
            w_to_p[words[i]] = pattern[i]
        elif w_to_p[words[i]] != pattern[i]: 
            return False

    return True
