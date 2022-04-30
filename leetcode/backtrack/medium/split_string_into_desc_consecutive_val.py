# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

def splitString(s: str) -> bool:
    l = len(s)
    n = int(s)
    def dfs(i, prev=None):
        print(i, prev, '-----------')
        if i == l:  # reach end (nothing to Explore)
            return prev != n  # As we need to split string atleast

        for j in range(i, l):  
            e = j+1  # end index
            val = int(s[i:e]) # current extraction
            print(j, val, 'Iter')
            if prev != None:
                if val+1 == prev and dfs(e, val):  # curr val becomes {prev} & seek for next number 
                    return True 
            else:
                if dfs(e, val):
                    return True 
            
        return False 

    return dfs(0)

def splitString2(s: str) -> bool:
    l = len(s)

    def dfs(idx, prev):
        if idx == l:
            return True 
        
        for i in range(idx, l):
            val = int(s[idx:i+1]) # curr split val
            if val+1 == prev and dfs(i+1, val):  # seek for next split
                return True 
            
    # As we need to split string atleast
    # & First split will not have prev val
    for i in range(l):
        val = int(s[:i+1])
        if dfs(i+1, val):
            return True
    
    return False


s = "1234"
s = "050043"
s = "9080701"
s = "1051546050"
ans = splitString(s)
ans2 = splitString2(s)
print(ans, ans2)