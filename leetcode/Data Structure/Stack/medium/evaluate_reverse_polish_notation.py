#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
import operator as op

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    operations = {
        # "*": lambda x,y: x*y,
        # "+": lambda x,y: x+y,
        # "-": lambda x,y: x-y,
        # "/": lambda x,y: float(x)/y
        "*": op.mul,
        "+": op.add,
        "-": op.sub,
        "/": op.truediv
    }

    stack = []
    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = operations[token](left, right)
            stack.append(int(result))
    return stack.pop()