from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

x = 0
y = 90
ck = 0
while (1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    
    while ck != 0 :
        if (x < 800 and y < 90):
            x = x+2
        elif (x == 800 and y < 600):
            y = y + 2
        elif (x > 0 and y == 600):
            x = x - 2
        else :
            y = y - 2

        ck = ck + 1
        delay(0.01)
    
close_canvas()
