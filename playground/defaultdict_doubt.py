from collections import defaultdict
from mimetypes import init

class A:
    def __init__(self) -> None:
        self.d = defaultdict(A)
    
a = A()
a.d[2]
print(len(a.d))