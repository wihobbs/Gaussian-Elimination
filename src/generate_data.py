## Copyright 2021 William Hobbs
import sys
import List
from random import randint
#from sage import ____ (rref)


## Generate Matrices
## Matrices need an "n" value, and then a
## list of lists that generate values.

class Matrix():
    def __init__(self, n: int, m: int):
        assert(n % 1 == n and m % 1 == m)
        self.n = n
        self.m = m
        self.v = self.generate(self.n, self.m)
    
    def generate(n: int, m: int):
        v = []
        for i in range(n*m):
            v[i] = randint(0, 100)
        return v
    
    def toString(self):
        print("n: " + self.n + "\nm: " + self.m + "\n")
        

Matrix(5, 4)

## Use Sage to Row-Reduce the Matrices
def reduce(n: int, m: int, matrix: List[int]) -> List[int]:
    return null

## Call C binaries (my code) to check their validity
