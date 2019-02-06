import numpy as np 
import arcade
from core import Brain
    

ROWS = 8
COLS = 8
INITIAL_X = 60
INITIAL_Y = 60
HEIGHT = 30
WIDTH = 30
TRANSFORM = 80
brain = Brain(ROWS, COLS)


def draw_cell_text(i,j,brain):
    pos_text_x = ((INITIAL_X*j) - WIDTH/2) + TRANSFORM
    pos_text_y = (INITIAL_Y*i) + TRANSFORM
    data = brain[i][j].data
    text = "%.2f" % data
    arcade.draw_text(text, pos_text_x, pos_text_y, (0,0,0), font_size=10)
def draw_cell(i,j,brain):
    arcade.draw_rectangle_outline((INITIAL_X*j)+TRANSFORM, (INITIAL_Y*i)+TRANSFORM, HEIGHT, WIDTH, (0,0,0))
def draw_cell_connections(i,j,brain):
    connections = brain[i-1][j-1].connections
    for connection in connections:
        start_x = (INITIAL_X*j)+TRANSFORM
        start_y = (INITIAL_Y*i)+TRANSFORM
        if connection == "w":
            if (j-1)<0:
                continue
            end_x = (INITIAL_X*(j-1))+TRANSFORM
            end_y = (INITIAL_Y*i)+TRANSFORM
            arcade.draw_line(start_x, start_y, end_x, end_y,(0,255,0))
        if connection == "e":
            if (j+1)>=COLS:
                continue
            end_x = (INITIAL_X*(j+1))+TRANSFORM
            end_y = (INITIAL_Y*i)+TRANSFORM
            arcade.draw_line(start_x, start_y, end_x, end_y,(255,0,0))
        if connection == "s":
            if (i-1)<0:
                continue
            end_x = (INITIAL_X*j)+TRANSFORM
            end_y = (INITIAL_Y*(i-1))+TRANSFORM
            arcade.draw_line(start_x, start_y, end_x, end_y,(0,0,255))
        if connection == "n":
            if (i+1)>=ROWS:
                continue
            end_x = (INITIAL_X*j)+TRANSFORM
            end_y = (INITIAL_Y*(i+1))+TRANSFORM
            arcade.draw_line(start_x, start_y, end_x, end_y,(0,0,0))
def update(delta_time):
    arcade.start_render()
    for i in range(ROWS):
        for j in range(COLS):    
            draw_cell_text(i,j,brain)
            draw_cell(i,j,brain)
            draw_cell_connections(i,j,brain)
            brain[i][j].set_random_data()
            brain[i][j].set_random_connections()

## DRAWING CODE START
arcade.open_window(600,600, "Brain")
arcade.set_background_color(arcade.color.WHITE)

arcade.schedule(update, 1/3)
arcade.run()
## DRAWING CODE END