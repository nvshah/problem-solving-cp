# https://leetcode.com/problems/flatten-nested-list-iterator/
from typing import List

'''Concept :- Stack'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> List[NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = []
        if nestedList:
            self.fillStack(nestedList)  # put all elem on stack
         
    def fillStack(self, lst):
        self.stack.extend(lst[::-1])
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
             
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger(): 
                return True
            else:
                t = self.stack.pop()  # remove list from stack
                lst = t.getList()     # get list at top of stack
                self.fillStack(lst)   # fill all elem of lst onto stack
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())