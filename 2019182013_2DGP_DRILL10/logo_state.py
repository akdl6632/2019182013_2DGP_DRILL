import game_framework
import play_state
import title_state
from pico2d import *

# running = True
image = True
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    # logo_time 1초넘으면 running = False
    global logo_time
    #global running
    delay(0.01)
    logo_time += 0.01
    if logo_time >= 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





