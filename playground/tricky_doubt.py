from mimetypes import init


class A:
    def __init__(self, v, a) -> None:
        self.a = v 
        self.n = a

q = A(10, None)
p = A(20, None)

t = p 

t.n = t = q

print(p.a, p.n.a)  # 20 10
print(t.a, t.n)  # 10 None