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

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    new_matrix = []
    for row in range(len(m1)):
        matrix_row = []
        for col in range(len(m2[0])):
            #row is the row to check in m1
            #col is the col to check in m2
            total = 0
            #loop through the cols in m1 or rows in m2
            for r in range(len(m2)):
                total += m1[row][r]*m2[r][col]
            matrix_row.append(total)
            
        new_matrix.append(matrix_row)
    return new_matrix
            

'''
2 x 4

A B C D
E F G H


4 x 3

a b c 
d e f
g h i
j k l


Result 2x3

Aa+Bd+Cg+Dj  Ab+Be+Fh+Dk Ac+Bf+Ci+Dl
x   x   x
'''


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
