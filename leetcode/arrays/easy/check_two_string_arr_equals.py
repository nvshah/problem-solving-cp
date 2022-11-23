# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    pairs = zip_longest(chain.from_iterable(word1), chain.from_iterable(word2))
    return all(starmap(eq, pairs))

def arrayStringsAreEqual2(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)