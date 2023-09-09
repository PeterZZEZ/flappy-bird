import pygame
from flappy_bird import Game
import neat
import pickle
import os
class FlappyGame:
    def __init__(self,window,width,height) -> None:
        self.game=Game(window,width,height,0.3,0.2)
        self.player = self.game.player
    def test_ai(self,genome,config):
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    break
            output = net.activate((self.player.y, abs(self.game.closest_pipe().top-self.player.y),abs(self.game.closest_pipe().bot-self.player.y), abs(self.game.closest_pipe().x-self.player.x) ))
            dec = output.index(max(output))
            if dec==0:
                pass
            else:
                self.player.jump()
            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()
            if not game_info.alive:
                run = False
        pygame.quit()
    def train_ai(self,genome,config):
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        run = True 
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
            output = net.activate((self.player.y, abs(self.game.closest_pipe().top-self.player.y),abs(self.game.closest_pipe().bot-self.player.y), abs(self.game.closest_pipe().x-self.player.x) ))
            dec = output.index(max(output))
            if dec==0:
                pass
            else:
                self.player.jump()
            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()
            if not game_info.alive or game_info.score >=100:
                self.calculate_fit(genome,game_info)
                break
    def calculate_fit(self,genome,game_info):
        genome.fitness += game_info.score*10+game_info.player_moved         
    
    
def eval_genomes(genomes,config):
    width,height = 700,700
    window = pygame.display.set_mode((width,height))
    for i, (genome_id1,genome) in enumerate(genomes):
        genome.fitness=0
        game = FlappyGame(window,width,height)
        game.train_ai(genome,config)
            

def run_neat(config):
    #p =  neat.Checkpointer.restore_checkpoint('neat-checkpoint-447')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5,filename_prefix='checkpoint/neat-checkpoint-'))
    
    winner=p.run(eval_genomes,500)
    with open("best.pickle","wb") as f:
        pickle.dump(winner,f)
def test_ai(config):
    width, height = 700,700
    window = pygame.display.set_mode((width,height))
    with open('best.pickle','rb') as f:
        winner = pickle.load(f)
    game = FlappyGame(window,width,height)
    game.test_ai(winner,config)
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
    #test_ai(config)