from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x = 400
        self.y = 30

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


