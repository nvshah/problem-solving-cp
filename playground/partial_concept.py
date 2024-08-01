from functools import partial
from operator import and_
from collections import Counter

s = "aabfsbf"
*charFreqs, = Counter(s).values()
isOdd = partial(and_, 1)

# check if any character repeats odd times
anyCharWithOddCnt = any(map(isOdd, charFreqs))
print(anyCharWithOddCnt)