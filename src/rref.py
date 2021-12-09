## Copyright 2021 William Hobbs
from typing import List
#from sage import ____ (rref)

## Rational class to preserve fractions across the code
""" class Rational():
    def __init__(self, num: int, den=1):
        assert(den != 0)
        self.num = num
        self.den = den

    def __add__(self, x: Rational):

    
    def __mul__(self, x: Rational):
        self.num = self.num * x.num
        self.den = self.den * x.den
    
    def toString(self):
        return (str(self.num) + "/" + str(self.den))

 """

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
        ## ret += "This matrix is upper triangular: "
        ## ret += str(self.is_upper)
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
            # print(self.toString())
    
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
    
    def permute(self):
        for i in range(self.n - 1):
            if self.v[i][i] < self.v[i+1][i]:
                self.swap_rows(i, i+1)
    
    def zeros_to_bottom(self):
        zeros_counter = 0
        for i in range(self.n):
            zero = [0] * self.m
            if self.v[i] == zero:
                self.v.pop(i)
                zeros_counter += 1
                break
            break
        for i in range(zeros_counter):
            self.v.append(zero)

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
    ## Move any rows with all zeros to the bottom.
    x.zeros_to_bottom()
    
    ## Permutations: Put the pivots in ascending order going down the rows
    x.permute()
    ## works

    ## Find the Pivot of the first row, zero out everything below it.
    for i in range(x.n):
        j = 0
        while (x.v[i][j] == 0 and j < x.m-1): ## this defaults to going out of range
            ## Can assume that there will be one non-zero value since all zero rows were deleted above.
            j += 1
        ## First non-zero row entry found, now, get rid of everything below it.
        print("Using " + str(x.v[i][j]) + " at " + str(i) + ", " + str(j) + " to reduce")
        if x.v[i][j] != 0:
            for k in range(i+1, x.n):
                print("Scaling row " + str(k) + " by: " + str((x.v[k][j]/x.v[i][j])*-1))
                x.add_and_scale_rows(k, i, (x.v[k][j]/x.v[i][j])*-1)
                x.zeros_to_bottom()
                x.permute() ## permute the rows after each swap
        print(x.toString())
    
    ## Start eliminating numbers.
    for i in range(x.n-1, 0, -1): 
        ## find the bottom non-zero row

        ## find the pivot
        j2 = 0
        while (x.v[i][j2] == 0 and j2 < x.m-1): ## this defaults to going out of range
            ## Can assume that there will be one non-zero value since all zero rows were deleted above.
            j2 += 1
            print(j2)
        
        ## reduce all rows above it
        for j in range(i-1, -1, -1):
            x.add_and_scale_rows(j, i, (x.v[j][j2]/x.v[i][j2]*-1))
        print("Reduced row " + str(j))
        x.zeros_to_bottom()
        print(x.toString())
    
    ## Scale rows by pivot.
    for i in range(x.n-1, -1, -1):
        j2 = 0
        while (x.v[i][j2] == 0 and j2 < x.m-1): ## this defaults to going out of range
            j2 += 1
        print(j2)
        if (x.v[i][j2] != 0):
            print("Scaling row " + str(i) + " by " + str(1/(x.v[i][j2])))
            x.scale_rows((1/(x.v[i][j2])), i)
    print("FINAL REDUCED MATRIX: ")
    print(x.toString())

def main():
    l = [[5.0, -3.0, 1.0, 1.0, 3.0], [1.0, 1.0, -1.0, 1.0, 0.0], [-2.0, -1.0, 2.0, 1.0, 1.0]]
    x = Matrix(3, 5, l)
    print("INITIAL MATRIX\n" + x.toString())
    reduce(x)

    m = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    y = Matrix(3, 3, m)
    print("INITIAL MATRIX\n" + y.toString())
    reduce(y)


main()