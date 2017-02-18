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
