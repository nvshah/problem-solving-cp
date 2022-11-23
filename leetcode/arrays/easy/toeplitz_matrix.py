# https://leetcode.com/problems/toeplitz-matrix/
from typing import List
from itertools import product

def isToeplitzMatrix3(matrix: List[List[int]]) -> bool:
    m, n = len(matrix), len(matrix[0])
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != matrix[i-1][j-1]:
                return False 
    
    return True

def isToeplitzMatrix1(matrix: List[List[int]]) -> bool:
    diag = {}
    
    for r, c in product(range(len(matrix)), range(len(matrix[0]))):
        v = matrix[r][c]
        k = r-c
        if k not in diag:
            diag[k] = v
        elif diag[k] != v:
            return False
    
    return True

def isToeplitzMatrix2(matrix: List[List[int]]) -> bool:
    m, n = len(matrix), len(matrix[0])
    def is_identical_diag(r, c):
        val = matrix[r][c]
        r, c = r+1, c+1
        while r < m and c < n: 
            if matrix[r][c] != val:
                return False 
        return True

    for i in range(m):
        if not is_identical_diag(i): return False 
    
    for j in range(1, n):
        if not is_identical_diag(j): return False 
    
    return True
    
    

