from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global vertical
    global ck
    global look
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                ck = 1
                look = 0
            elif event.key == SDLK_LEFT:
                dir -= 1
                ck = 2
                look = 1
            elif event.key == SDLK_UP:
                vertical += 1
                if(look == 0):
                    ck = 5
                elif(look == 1):
                    ck = 6
            elif event.key == SDLK_DOWN:
                vertical -= 1
                if(look == 0):
                    ck = 5
                elif(look == 1):
                    ck = 6
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                ck = 0
            elif event.key == SDLK_LEFT:
                dir += 1
                ck = 4
            elif event.key == SDLK_UP:
                vertical -= 1
                if(look == 0):
                    ck = 0
                elif(look == 1):
                    ck = 4
            elif event.key == SDLK_DOWN:
                vertical += 1
                if(look == 0):
                    ck = 0
                elif(look == 1):
                    ck = 4

open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
vertical = 0
ck = 0
look = 0

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if(ck == 0):
        character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif(ck == 1 or ck == 5):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif(ck == 2 or ck == 6):
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif (ck == 4):
        character.clip_draw(frame * 100, 200, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if (x + dir * 5 < 1280 and x + dir * 5 > 0):
        x += dir * 5
    if (y + vertical * 5 < 1024 and y + vertical * 5 > 0):
        y += vertical * 5
    delay(0.01)

close_canvas()

