
import itertools as it

# --- Utils

def segregate_into_groups(lst, grpSize=2):
    '''
    Segregate List into Tuple of Sequential Groups 9each group size = {grpSize} 
    Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [(1,2), (3,4), (5, None)] 
    '''
    lst_iter = iter(lst)
    return it.zip_longest(*it.repeat(lst_iter, grpSize), fillvalue=None)


def fixSorting(a):
      i = l = 0
      r = len(a)-1
      while i < r:
            if a[i] > a[i+1]:
                  break
            i += 1

      l = i+1
      while l < r:
            if a[r-1] > a[r]:
                  break
            r -= 1
      else:
            r = i+1
      
      print(i, r)
      a[i], a[r] = a[r], a[i]

def fixSorting2(a):
      ''' ReCorrect the sorted order of array {a} by rectifying the correct loc of 2 misplaced elem '''
      s = enumerate(it.pairwise(a))

      f = it.dropwhile(lambda x: x[1][0] < x[1][1], s)
      e = next(f)
      l = e[0]
      t = it.dropwhile(lambda x: x[1][0] < x[1][1], s)
      _, e = next(t, None), next(t, None)
      r = e[0] if e else l+1

      print(l, r)

      a[l], a[r] = a[r], a[l]

def fixSorting3(a, key):
    ''' ReCorrect the sorted order of array {a} by rectifying the correct loc of 2 misplaced elem '''
    #s = enumerate(it.pairwise(a))
    def pred(idx):  # check for sorted order
        c, n = key(a[idx]), key(a[idx+1])
        return c < n

    s = iter(range(len(a))) 
    f = it.dropwhile(pred, s)  # Find first incorrect loc
    l = next(f)  # first incorrect location is ensured
    t = it.dropwhile(pred, s) # Find second incorrect loc
    e = next(t, None)  # second incorrect location may not be found
    r = e + 1 if e else l+1

    a[l], a[r] = a[r], a[l]


def get_boundaries(matrix):
      m, n = len(matrix), len(matrix[0])

      h = it.product((0, m-1), range(n))  # Horizontal - Rows as Boundary
      v = it.product(range(m), (0, n-1))  # Vertical - cols as Boundary

      bounds = it.chain(h, v)

      return bounds

def isPalindrome(s):
    m = len(s) // 2
    return all(starmap(eq, zip(s[:m], reversed(s))))

if __name__ == '__main__':
    a = [1, 3, 2, 4]
    a = [1,8,3,4,5,6,7,2,9,10]
    fixSorting2(a)
    print(a)