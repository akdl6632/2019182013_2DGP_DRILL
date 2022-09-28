from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('penguin.png')

frame = 0
ck = 0
for x in range(0, 800, 5):
    if(ck == 0):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 128, 1900, 128, 140, x, 90, 200, 200)
        update_canvas()
        if(frame + 1 == 16):
            ck = 1
        frame = (frame + 1) % 16
        delay(0.1)
        get_events()
    elif ck >= 1 and ck <= 3:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 128, 1800 - 140*(ck - 1), 128, 127, x, 90, 200, 200)
        update_canvas()
        if(frame + 1 == 12):
            if(ck == 3):
                ck = 0
            else:
                ck += 1
        frame = (frame + 1) % 12
        delay(0.1)
        get_events()

close_canvas()

