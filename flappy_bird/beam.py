import random
import pygame
class Beam:

    def __init__(self,height,width,gap):
        self.gap = gap
        self.height=height
        self.top = random.randrange(0, height-self.gap)
        self.bot = self.top+self.gap
        self.x = width-20

    def mov(self, vel):
        self.x -= vel

    def hit(self, obj):
        if (obj.x > self.x and obj.x < self.x+30):
            if obj.y-30 < self.top or obj.y+30 > self.bot:
                return True
        return False
    def draw(self, window):

        pygame.draw.rect(window, (255, 255, 0), (self.x, 0, 30, self.top), 0)
        pygame.draw.rect(window, (255, 255, 0),
                         (self.x, self.bot, 30, self.height-self.bot), 0)
