def wrapper(f):
    
    def fun(l):
        nl = []
        for n in l:
            p = n[-10:]
            nl.append(f'+91 {p[:5]} {p[5:]}')
        return f(nl)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
