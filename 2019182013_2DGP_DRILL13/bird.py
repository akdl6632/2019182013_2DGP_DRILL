from pico2d import *

import game_framework

import random

PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 40.0 # 사람의 2배의 속도로 이동하도록 설정
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), 500 # 1600, 600의 게임화면
        self.frame = 0
        self.ystate = 0
        self.dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        if self.ystate == 0: # y가 0일 때 4개의 이미지가 그려짐
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if int(self.frame) == 3:
                self.ystate += 1
                self.frame = 0
        else: # y가 1 or 2일 때 5개의 이미지가 그려짐
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            if int(self.frame) == 4:
                self.ystate += 1
                self.frame = 0

        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time

        self.ystate = self.ystate % 3

        # x 범위 설정
        if self.x > 1600 - 90:
            self.x = 1600 - 90
            self.dir = -1
        elif self.x < 0 + 90:
            self.x = 0 + 90
            self.dir = 1

    def draw(self):
        if self.dir == 1: # 오른쪽 이동
            self.image.clip_draw(int(self.frame) * 181, 166 * (2 - self.ystate), 181, 166, self.x, self.y)
        else: # 왼쪽 이동
            self.image.clip_composite_draw(int(self.frame) * 181, 166 * (2 - self.ystate), 181, 166, -3.141592, 'v', self.x, self.y, 181, 166)
