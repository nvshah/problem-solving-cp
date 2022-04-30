# https://leetcode.com/problems/remove-k-digits/

'''
problem

Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.

Eg -> Input: num = "1432219", k = 3
      Output: "1219"

      Input: num = "10200", k = 1
      Output: "200"

      Input: num = "10", k = 2
      Output: "0"

Soln
 Idea :- Keep Track of Monotonic Incr Stack (Ivariant for stack) &
        At last after all traversal if there is need for more removal 
        Then remove from RHS (ie LSB) ie from top of stack one by one

  Monotonic Increasing Stack,
    -> In case of Decreasing Order, we will remove from MSB (ie from left side)
    In case of Increasing Order, we will consider removing from LSB (ie from Right side)
 k=2
 1) 5,4,3,2,1 -> 3,2,1
 2) 1,2,3,4,5 -> 1,2,3
'''

def removeKdigits(num: str, k: int) -> str:
    # Monotonic Increasing Stack
    stack = ['-1']  # dummy val inorder to avoid freq empty stack checks 

    for n in num:
        while k and stack[-1] > n:  # Invariant Check
            stack.pop()  # remove 1 digit
            k -= 1
        stack.append(n)
    # stack := monotonic increasing now ! 
    # so onwards removal can be done from right side (ie from top of the stack)
    res = "".join(stack[1:len(stack)-k]) 
    return str(int(res)) if res else "0"

def simplifyNum(n):
    return str(int(n)) # assuming n is not empty

def removeKdigits2(num: str, k: int) -> str:
    # Monotonic Increasing Stack
    stack = ['-1']  # dummy val inorder to avoid freq empty stack checks 
    size = len(num)
    for i, n in enumerate(num):
        while stack[-1] > n:  # Invariant Check (for Monotonic Incr)
            if k:
                stack.pop()  # remove 1 digit
                k -= 1
            else:
                res = "".join(stack[1:]) + num[i:]
                return simplifyNum(res)
        stack.append(n)
    # stack := monotonic increasing now ! 
    # so onwards removal can be done from right side (ie from top of the stack)
    res = "".join(stack[1:len(stack)-k]) 
    return simplifyNum(res) if res else "0"

num = "1432219"
k = 3

num = "10200"
k = 1

num = "10"
k = 2

ns = removeKdigits2(num, k)
print(ns)
