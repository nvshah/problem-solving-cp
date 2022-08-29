from collections import Counter

s1 = 'aba'
s2 = 'abc'

c1 = Counter(s1) 
c2 = Counter(s2) 

a1 = c2 - c1 

c2.subtract(c1)

c2 = Counter(c2)    

for k in c2: 
    print(k)