# https://leetcode.com/problems/decode-string/

def decodeString(s: str) -> str:
    stack = []
    for c in s:
        if c == ']':
            # CASE 1
            # 1. get the word
            w = "" # word
            while stack[-1] != "[":
                t = stack.pop()
                w = t + w  # add at begin
            stack.pop() # remove "["

            # 2. get the #times to repeat the word
            num = ""
            while stack and stack[-1].isdigit():
                d = stack.pop() #digit
                num = d + num   # as we are going from right -> left
            num = int(num)
            nword = w * num 

            # 3. record resolved word between [...] innstack for further nesting use
            stack.append(nword)
        else:
            # CASE 2
            stack.append(c)

    return "".join(stack)
    



