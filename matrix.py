import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here (done)
        
        determinant = 0
        
        if self.h == 1:
            
            determinant = self[0][0]
            
        elif self.h == 2: 
            
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            determinant = a*d - b*c
            
        return determinant
            
    

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here (done)
        
        trace = 0
        
        for i in range(self.h):
            trace += self.g[i][i]
            
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
       
        # TODO - your code here (done)
        
        inverse = []
        
        if self.h == 1:
            inverse.append([1 / self.g[0][0]])
        
        elif self.h == 2:
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The denominator of a fraction cannot be zero')
            
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
            
                factor = 1 / (a*d - b*c)
                inverse = [[d , -b],[-c , a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
        return Matrix(inverse)
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here (done)
        
        matrix_transpose = []
    
        for i in range(self.w):
            new_row = []
        
            for j in range(self.h):
                new_row.append(self.g[j][i])
            
            matrix_transpose.append(new_row)

    
        return Matrix(matrix_transpose)
    
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrixSum = []

        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            matrixSum.append(row)
            
        return Matrix(matrixSum)
        
        #   
        # TODO - your code here (done)(
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        result = []
    
        for i in range(self.h):
            neg_row = []
        
            for j in range(self.w):    
                ij = self[i][j]
                neg_ij = ij * -1
                neg_row.append(neg_ij)
            result.append(neg_row)
        
        return Matrix(result)
        
        #   
        # TODO - your code here (done)
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        grid = zeroes(self.h, self.w)
        #matrixSub = []

        for i in range(self.h):
            #row = []
            for j in range(self.w):
                grid[i][j] = self.g[i][j] - other.g[i][j]
                # row.append(self.g[i][j] - other.g[i][j])
            # matrixSub.append(row)
         
        #return matrixSub
        return grid
        
        #   
        # TODO - your code here (done)
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
            
        def dot_product(vector_one, vector_two):
    
            result = 0 
    
            for i in range(len(vector_one)):
                result += vector_one[i] * vector_two[i]
    
            return result
    
        product = []
        transB = other.T()
    
        for row1 in range(self.h):
            new_row = []
        
            for row2 in range(transB.h):
            
                dotprod = dot_product(self[row1], transB[row2])
                new_row.append(dotprod)
            product.append(new_row)
            

        return Matrix(product)
        #   
        # TODO - your code here (transpose multiplication) (done)
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            new_grid = []
            
            for row in self.g:
                new_row = []
                
                for value in row:
                    new_row.append(value * other)
                    
                new_grid.append(new_row)
            
            return Matrix(new_grid)
            pass
    
        
            #   
            # TODO - your code here (scalar)(done)
            #
            