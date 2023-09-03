import pygame
class Player:
    def __init__(self, x, y, vel, grav):
        self.x = x
        self.y = y
        self.vel = vel
        self.grav = grav
        self.dis=0
    def moved(self):
        self.dis+=0.1
    def mov(self):
        self.vel +=self.grav
        self.y += self.vel
    def jump(self):
        self.vel = -4
    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), 30)
