import math


def print_matrix( matrix ):
    for y in range(len(matrix)):
        row = "["
        for x in range(len(matrix[y])):
            if x == len(matrix[y])-1:
                row += str(matrix[y][x]) + "]"
            else:
                row += str(matrix[y][x]) + " "
        print row

def ident( matrix ):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x == y:
                matrix[y][x] = 1
            else:
                matrix[y][x] = 0
                

def scalar_mult( matrix, s ):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] *= s

import copy
#m1 is m * n
#m2 is n * o
def matrix_mult( m1, m2 ):
    m2_copy = copy.deepcopy(m2)
    del m2[:]
    for row in range(len(m1)):
        matrix_row = []
        for col in range(len(m2_copy[0])):
            total = 0
            for r in range(len(m2_copy)):
                total += m1[row][r]*m2_copy[r][col]
            matrix_row.append(total)
        m2.append(matrix_row)

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
