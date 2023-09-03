import pygame
import os
import copy
from .player import Player
from .beam import Beam
pygame.init()
class GameInfo:
    def __init__(self,score,alive,moved) -> None:
        self.score=score
        self.alive=alive
        self.player_moved=moved

class Game:
    cooldown = 0
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    def __init__(self, window, window_width, window_height, grav, vel):
        self.window_width = window_width
        self.window_height = window_height
        self.player = Player(60,window_height/2,vel,grav)
        self.window=window
        self.score=0
        self.beamvel = 2
        pipe = Beam(self.window_height,self.window_width,gap=200)
        self.beams = []
        self.beams.append(pipe)
        self.count=150
        self.alive=True
    def _draw_score(self):
        cur_score_text= self.SCORE_FONT.render(f"{self.score}",1,self.WHITE)
        self.window.blit(cur_score_text,(self.window_width//4- cur_score_text.get_width()//2,20))
    
    def _collision(self):
        for i in self.beams:
            if i.hit(self.player):
                return True
        if(self.player.y>=self.window_height):
            return True
        return False
    def move(self):
        self.player.jump()
    def loop(self):
        for i in self.beams:
            i.mov(self.beamvel)
        self.player.moved()
        for i in self.beams[:]:
            if i.x < -60:
                self.beams.remove(i)
                self.score += 1
        if self.count <= 0:
            pipe = Beam(self.window_height,self.window_width,gap=150)
            self.beams.append(pipe)
            self.count = 150
        else:
            self.count -= 1
        self.player.mov()
        if self.alive==True:
            self.alive=not self._collision()
        game_info = GameInfo(self.score,self.alive,self.player.dis)
        return game_info
    def closest_pipe(self):
        pipe=None
        closest =10000000000000
        for i in self.beams:
            if i.x <= closest:
                closest=i.x
                pipe=copy.deepcopy(i)
        return pipe
    def draw(self):
        self.window.fill(self.BLACK)
        for i in self.beams:
            i.draw(self.window)
        self._draw_score()
        self.player.draw(self.window)
'''
    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if lost:
            if lostCount > FPS * 3:
                lost = False
                lostCount = 0
                player = Player(50, HEIGHT/2, vel, grav)
                beams = []
                score1 = 0
            else:
                lostCount += 1
                continue
        for i in beams:
            lost = i.hit(player)
            break

        if player.y+5 >= HEIGHT:
            lost = True
            lostCount += 1
        if count <= 0:
            pipe = Beam()
            beams.append(pipe)
            count = 150
        else:
            count -= 1

        keys = pygame.key.get_pressed()
        if cooldown == 0:
            if keys[pygame.K_SPACE]:
                player.mov()
                cooldown = 10
        else:
            cooldown -= 1

        for i in beams:
            i.mov(beamvel)

        
        for i in beams[:]:
            if i.x < -60:
                beams.remove(i)
                score1 += 1
'''