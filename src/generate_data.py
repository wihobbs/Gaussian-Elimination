## Copyright 2021 William Hobbs
import os
from typing import List
#from sage import ____ (rref)

## Rational class to preserve fractions across the code
class Rational():
    def __init__(self, num: int, den=1):
        self.num = num
        self.den = den

## Generate Matrices
## Matrices need an "n" value, and then a
## list of lists that generate values.

class Matrix():
    def __init__(self, n: int, m: int, v: List[List[float]]):
        assert(n % 1 == 0 and m % 1 == 0)
        self.n = n ## rows
        self.m = m ## columns
        self.v = v
        self.is_upper = False
        # self.sol = self.sageSolver(self)
        ## nested architecture of self.v: list of lists of row values

    def __equals__(self, x) -> bool:
        if (self.n != x.n and self.m != x.m):
            return False
        for i in range(self.n*self.m):
            if (self.v[i] != x.v[i]):
                return False
        return True
    
    def toString(self):
        ret = str("n: " + str(self.n) + "\nm: " + str(self.m) + "\n")
        for i in range(self.n):
            ret += "["
            for j in range(self.m):
                ret += "  "
                ret += str(self.v[i][j])
            ret += "]\n"
        ret += "This matrix is upper triangular: "
        ret += str(self.is_upper)
        return ret

    def check_upper(self):
        self.is_upper = True
        for i in range(self.m):
            for j in range(i+1, self.n):
                if self.v[j][i] != 0:
                    self.is_upper = False

    def swap_rows(self, row1: int, row2: int):
        self.v[row1], self.v[row2] = self.v[row2], self.v[row1]
    
    def scale_rows(self, num: float, row: int):
        for i in range(self.m):
            self.v[row][i] = self.v[row][i]*num
    
    ## So. The cooler thing to do here would be to have a "vector" class and
    ## overload the operators for that. Sadly, I started the project too late
    ## to do this.
    def add_rows(self, row1: int, row2: int):
        for i in range(self.m):
            self.v[row1][i] = self.v[row1][i] + self.v[row2][i]
    
    def add_and_scale_rows(self, row1: int, row2: int, scale: float):
        ## Scale the row, create temporary variable to do so
        for i in range(self.m):
            self.v[row1][i] = self.v[row1][i] + self.v[row2][i]*scale

"""     ## Use Sage to Row-Reduce Matrices (never finished)
    def sageSolver(self):
        sage_cli = "matrix(QQ, ["
        for i in range(self.n):
            sage_cli += "["
            for j in range(self.m):
                sage_cli += str(self.v[j*i + j])
                sage_cli += ","
        
        ## Call Sage within Docker container to get solved matrices
        os.system(sage_cli)
        return ret """

## Row-Reduction program
def reduce(x: Matrix) -> Matrix:
    while not x.is_upper:
    ## Move any rows with all zeros to the bottom.
        for i in range(x.n):
            zero = [0] * x.m
            if x.v[i] == zero:
                x.v.append(x.v[i])
                x.v[i].remove()
    
    ## Permutations: Put the pivots in ascending order going down the rows
        for i in range(x.n - 1):
            if x.v[i][i] > x.v[i+1][i+1]:
                x.swap_rows(i, i+1)
        print(x.toString())
    ## works

    ## Find the Pivot of the first row, zero out everything below it.
        for i in range(x.n):
            j = 0
            while (x.v[i][j] == 0): 
            ## Can assume that there will be one non-zero value since all zero rows were deleted above.
                j += 1
        ## First non-zero row entry found, now, get rid of everything below it.
            print(x.v[i][j])
            for k in range(i+1, x.n):
                x.add_and_scale_rows(k, i, (x.v[k][j]/x.v[i][j])*-1)
                print(x.toString())
                x.check_upper()
    
    ## After it becomes upper triangular, the work is easy. Just start eliminating numbers.
    print(x.toString())

def main():
    l = [[0.0, 2.0, 3.0, 4.0, 5.0], [6.0, 7.0, 8.0, 9.0, 10.0], [11.0, 12.0, 13.0, 14.0, 15.0], [16.0, 17.0, 18.0, 19.0, 20.0], [21.0, 22.0, 23.0, 24.0, 25.0]]
    x = Matrix(5, 5, l)
    print(x.toString())
    reduce(x)
    print(x.toString())

main()