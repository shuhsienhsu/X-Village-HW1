import random

from copy import deepcopy

class Matrix:
    #rows = 0
    #cols = 0
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        #self.matrix = nrows*[ncols*[0]]
        self.matrix = [ [None] * ncols for i in range(nrows) ]
        for i in range(nrows):
            for j in range(ncols):
                self.matrix[i][j] = random.randint(0,9)
                #print(i, j, self.matrix[i][j], end=' ')
            #print()
        self.rows = nrows
        self.cols = ncols

    def add(self, m):
        """return a new Matrix object after summation"""
        if(self.rows != m.rows or self.cols != m.cols):
            print("Matrixs' size should be in the same size")
            return None
        else:
            matrix_temp = Matrix(self.rows, self.cols)            
            for i in range(self.rows):
                for j in range(self.cols):
                    matrix_temp.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
            return matrix_temp

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if(self.rows != m.rows or self.cols != m.cols):
            print("Matrixs' size should be in the same size")
        else:
            matrix_temp = Matrix(self.rows, self.cols)            
            for i in range(self.rows):
                for j in range(self.cols):
                    matrix_temp.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
            return matrix_temp

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if(self.cols != m.rows):
            print("You can't multiply the matrixs")
        else:
            matrix_temp = Matrix(self.rows, m.cols)            
            for i in range(self.rows):
                temp = 0
                for j in range(m.cols):
                    for k in range(self.cols):
                        temp += self.matrix[i][k] * m.matrix[k][j]
                    matrix_temp.matrix[i][j] = temp
            return matrix_temp

    def transpose(self):
        """return a new Matrix object after transpose"""
        matrix_temp = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                matrix_temp.matrix[i][j] = self.matrix[j][i]
        return matrix_temp
    
    def display(self):
        """Display the content in the matrix"""
        for k in range(self.rows):
            for l in range(self.cols):
                print('{:^5}'.format(self.matrix[k][l]), end='')
            print()
        print()

print("matrix1:")
mymatrix = Matrix(9,3)
mymatrix.display()
print("matrix2:")
mymatrix02 = Matrix(9,3)
mymatrix02.display()
print("matrix3:matrix1+matrix2")
mymatrix03 = mymatrix.add(mymatrix02)
mymatrix03.display()
print("matrix4:matrix1-matrix2")
mymatrix04 = mymatrix.sub(mymatrix02)
mymatrix04.display()
print("matrix5:")
mymatrix05 = Matrix(3,4)
mymatrix05.display()
print("matrix6:matrix1*matrix5")
mymatrix06 = mymatrix.mul(mymatrix05)
mymatrix06.display()
print("matrix7:transpose of matrix4")
mymatrix07 = mymatrix04.transpose()
mymatrix07.display()

print("matrix1+matrix5:")
mymatrix.add(mymatrix05)
print("matrix1-matrix5:")
mymatrix.sub(mymatrix05)
print("matrix1*matrix4:")
mymatrix.mul(mymatrix04)
