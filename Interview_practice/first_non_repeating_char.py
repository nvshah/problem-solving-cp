from collections import Counter as ctr, defaultdict
#from typing import OrderedDict 
import itertools as it


def first_non_repeat_char(s):
    ''' 
    Find the First Non Reeating Character in String
    Complexity -> O(2n)
    NOTE -> THis will Work Just because dictionary from 3.7 + are inserting element in same order as arrival
    '''
    freq_cnt = ctr(s)
    for char,count in freq_cnt.items():
        if count == 1:
            return char
    return -1

def first_non_repeat_char_2(s):
    ''' 
    Find the First Non Reeating Character in String
    idea -> hashMap
    Manual Counter as in some version dict are unordered
    Complexity -> O(2n)
    '''
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    prev = None
    for c in s:
        if prev == c:  # Avoiding Complex Hash Function calculation if any at memory overhead
            continue
        if d[c] == 1:  
            return c
        prev = c

def first_non_repeat_char_3(s):
    ''' 
    Find the First Non Reeating Character in String
    idea -> as char range in (1, 26)
    Manual Counter as in some version dict are unordered
    Complexity -> O(2n)
    '''
    ctr = [0] * 26
    for c in s:
        ctr[c] += 1

    if len(s) > 26:
        for i in ctr:
            if i == 1:
                return chr(i+97)
    else:
        for c in s:
            if ctr[ord(c)-97] == 1:
                return c
    return '_'
        
def first_non_repeat_char_4(s):
    '''
     Not good complexity but simple
    '''
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'

s = 'aaabcccdeeef'
s = 'abcbad'
s = 'abcabcabc'
a = first_non_repeat_char(s)
print(a)
