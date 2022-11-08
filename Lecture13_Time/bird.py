from pico2d import *
import random

import game_framework

# Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 40.0 # 20.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5   # 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


# class Fly:
#     def enter(self):
#         print('ENTER Fly')
#         self.dir = 0
#         self.timer = 1000
#
#     def draw(self):



class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.frame = 0
        self.ystate = 0
        self.dir = 1
        self.image = load_image('bird_animation.png')


    def update(self):
        if self.ystate == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            # print(f'in y = 0 and frame is ={int(self.frame)}, yframe is ={self.ystate}')
            if int(self.frame) == 3:
                self.ystate += 1
                self.frame = 0
        else: # ystate -> 1 or 2
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            # print(f'in y = not 0 and frame is ={int(self.frame)}, yframe is ={self.ystate}')
            if int(self.frame) == 4:
                self.ystate += 1
                self.frame = 0

        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time

        self.ystate = self.ystate % 3 # ystate range 0 ~ 2

        # self.frame = (self.frame + 1) % 14
        # self.x += self.dir * 1
        if self.x > 800 - 90:
            self.x = 800 - 90
            self.dir = -1
        elif self.x < 0 + 90:
            self.x = 0 + 90
            self.dir = 1

    def draw(self):
        if self.dir == 1: # 오른쪽으로 비행
            self.image.clip_draw(int(self.frame) * 181, 168 * (2 - self.ystate), 181, 166, self.x, self.y)
        elif self.dir == -1: # 왼쪽으로 비행
            self.image.clip_composite_draw(int(self.frame) * 181, 168 * (2 - self.ystate), 181, 166, 0, 'h', self.x, self.y, 181, 166)

