
def strStr1(haystack, needle):
    ''' 
    find if needle is present in haystack if yes then return index else -1 
    Brute Force approach
    '''
    if needle == "":
        return 0 
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1

''' Top Down Approach to Solve lPS i.e longest prefix substring '''

def strStr2(haystack, needle):
    ''' KMP knut-morris-prat algo to find the substr using lPS (longest prefix suffix) technique '''

    if needle == "":
        return 0 

    # ---- Prepare the LPS ------
    
    # find the lps for needle (ie longest prefix substring for each index of needle)

    # prevLps points to current index of needle where we can compare next character to account in prefix=suffix match cnt
    prevLPS = 0  # lps for str with 1 len is 0 as there is no prefix in string with 1 length
    i = 1 # keep track of string length
    needle_size = len(needle)
    # lps keep track of length of longest prefix = longest suffix for each index in needle
    lps = [0] * needle_size 

    while i < needle_size:
        if needle[prevLPS] == needle[i]:
            # Found prefix = suffix for current string as well whose lennght is +1 to prev
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            # lps for str with 1 len is 0 as there is no prefix in string with 1 length
            lps[i] = 0
            i += 1
        else:
            # As we check for prefix
            # for any string of len l lps[i] denotes how many char from prefix & suffix match maximum
            # lps[i] = the idx before which prefix matches with suffix
            # thus take jump of that size backward to check any matches
            prevLPS = lps[prevLPS-1] # prevlps now points to the idx where we can match for lps[prevLPS-1]+1 substr match cnt
            
    #---- Search ----

    h = 0  # hasystack ptr
    n = 0 # needle ptr

    while h < len(haystack):
        if haystack[h] == needle[n]:
            h, n = h+1, n+1
        else:
            if n == 0: # exhaust out a needle 
                h += 1  # so we need to move haystack ptr forward
            else:
                # if you have found some string part matching eaarlier then you can utilised the LPS
                n = lps[n-1] # jump to idx where next prefix needs to be matched (ie skiped the matched prefix)
        
        if n == needle_size:
            # found the substr
            return h - needle_size
    return -1


def strStr3(haystack, needle):
    return haystack.find(needle)

if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    print(strStr1(haystack, needle))