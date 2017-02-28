from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()



add_edge(matrix,0,0,0,500,500,0)
add_edge(matrix,0,500,0,500,0,0)

add_edge(matrix,0,100,0,500,400,0)
add_edge(matrix,0,400,0,500,100,0)

add_edge(matrix,100,0,0,400,500,0)
add_edge(matrix,100,500,0,400,0,0)

add_edge(matrix,250,0,0,250,500,0)
add_edge(matrix,0,250,0,500,250,0)


draw_lines( matrix, screen, color )
display(screen)

print "These are all the points in format x y z 1.0. Every 2 points is a edge"
print_matrix(matrix)


print "--------------------\nMatrix Multiplication:"
m1 = [[1,8,3,4],[2,9,6,5]]
m2 = [[1,2,3],[4,5,66],[7,8,9],[10,-3,0]]
print_matrix(m1)
print
print_matrix(m2)
print "\nMultiplying the above two should result in \n[94 54 558]\n[130 82 654]"
matrix_mult(m1,m2)
print "\nResult:"
print_matrix( m2 )

print "-------------------------\nScalar Multiplication:"
print_matrix(m1)
scalar_mult(m1,10)
print "\nMultiplying the above matrix by 10 should result in\n[10,80,30,40]\n[20,90,60,50]"
print "\nResult:"
print_matrix(m1)

print "-------------------------\nIdent:\nmatrix is now:"
matrix = new_matrix()
ident(matrix)
print_matrix(matrix)

# need matrix examples (multiplication, etc.)
