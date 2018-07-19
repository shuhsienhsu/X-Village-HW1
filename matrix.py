import random

from copy import deepcopy

class Matrix:
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        #self.matrix = nrows*[ncols*[0]]
        self.rows = int(nrows)
        self.cols = int(ncols)
        self.matrix = [[None] * self.cols for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.randint(0,9)

    def add(self, m):
        if(self.rows != m.rows or self.cols != m.cols):
            print("Matrixs' size should be in the same size")
            print()
            return None
        else:
            matrix_temp = Matrix(self.rows, self.cols)            
            for i in range(self.rows):
                for j in range(self.cols):
                    matrix_temp.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
            return matrix_temp

    def sub(self, m):
        if(self.rows != m.rows or self.cols != m.cols):
            print("Matrixs' size should be in the same size")
            print()
            return None
        else:
            matrix_temp = Matrix(self.rows, self.cols)            
            for i in range(self.rows):
                for j in range(self.cols):
                    matrix_temp.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
            return matrix_temp

    def mul(self, m):
        if(self.cols != m.rows):
            print("Invalid action")
            print()
            return None
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
        matrix_temp = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                matrix_temp.matrix[i][j] = self.matrix[j][i]
        return matrix_temp
    
    def display(self):
        for k in range(self.rows):
            for l in range(self.cols):
                print('{:^5}'.format(self.matrix[k][l]), end='')
            print()
        print()

i = input("Enter A matrix's rows:")
j = input("Enter A matrix's columns:")
print("Matrix A(", i, ",", j, "):", sep='')
matrix_a = Matrix(i,j)
matrix_a.display()

i = input("Enter B matrix's rows:")
j = input("Enter B matrix's columns:")
print("Matrix B(", i, ",", j, "):", sep='')
matrix_b = Matrix(i,j)
matrix_b.display()

print('=' * 10 + 'A + B' + '=' * 10)
matrix_add = matrix_a.add(matrix_b)
if(matrix_add):
    matrix_add.display()

print('=' * 10 + 'A - B' + '=' * 10)
matrix_sub = matrix_a.sub(matrix_b)
if(matrix_sub):
    matrix_sub.display()

print('=' * 10 + 'A * B' + '=' * 10)
matrix_mul = matrix_a.mul(matrix_b)
if(matrix_mul):
    matrix_mul.display()

print('=' * 5 + 'the transpose of A*B' + '=' * 5)
if(matrix_mul):
    matrix_transpose = matrix_mul.transpose()
    matrix_transpose.display()
else:
    print('Invalid action')