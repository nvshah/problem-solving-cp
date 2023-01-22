# https://leetcode.com/problems/detect-capital/description/

import re

def detectCapitalUse(word: str) -> bool:
    # regex = r"^[a-z]+$|^[A-Z]+$|^[A-Z][a-z]+$"
    # res = re.match(regex, word)
    # return bool(res)   
    return (word == word.lower()) 
    or (word == word.upper()) 
    or (word[1:] == word[1:].lower())