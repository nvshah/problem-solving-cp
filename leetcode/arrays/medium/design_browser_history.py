# https://leetcode.com/problems/design-browser-history/

class ListNode:
    def __init__(self, val, prev=None, nxt=None):
      self.val = val
      self.prev = prev
      self.next = nxt
# Via Linked List
class BrowserHistory1:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps:
            self.cur, steps = self.cur.prev, steps-1

        return self.cur.val        

    def forward(self, steps: int) -> str:
        while self.cur.nxt and steps:
            self.cur, steps = self.cur.nxt, steps-1

        return self.cur.val    

# Via Array (BETTER)
class BrowserHistory2:

    def __init__(self, homepage: str):
        self.cur = 0
        self.len = 1  # actual/true length of an array of pages
        self.history = [homepage]

    def visit(self, url: str) -> None:
        # As there can be soft spots ahead of cur position which are released but not freed 
        if len(self.history) <= self.cur+1:
            # No soft spots ahead (ie no need to clear forward browsing data)
            self.history.append(url)
        else:
            # Soft spot (released memory) is there ahead, so put {url} in those spots
            self.history[self.cur+1] = url 
        self.cur += 1
        self.len = self.cur + 1 # Actual size of current pages in history

    def back(self, steps: int) -> str:
        self.cur = max(self.cur-steps, 0)
        return self.history[self.cur]       

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur+steps, self.len-1)
        return self.history[self.cur]  
        


#Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory(homepage)
obj.visit(url)
param_2 = obj.back(steps)
param_3 = obj.forward(steps)