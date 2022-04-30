# Que -> https://leetcode.com/problems/check-if-the-sentence-is-pangram/

def checkIfPangram(sentence: str) -> bool:
    return len(set(sentence)) == 26


sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
ans = checkIfPangram(sentence=sentence)
print(ans)
