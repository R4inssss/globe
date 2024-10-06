import pygame
from sprites import *
from config import *
from protocols import *
import sys
from dialogue import MainText
from dialogue import *



class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 30)
        self.running = True

        # Map Calls
        self.bg = pygame.image.load(r"./assets/bg.png")



    def new(self):
        # New game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()            # Object that contains all of our sprites && updates
        self.blocks = pygame.sprite.LayeredUpdates()                 # walls

    def events(self):
        # Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.blit(self.bg,(0,0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            #self.carbon()
        self.running = False

    def game_over(self):
        pass

    def intro(self):
        pass


if __name__ == "__main__":
    g = Game()
    g.intro()
    g.new()
    while g.running:
        g.main()
        g.game_over()

    pygame.quit()
    sys.exit()
