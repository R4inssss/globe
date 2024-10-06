import pygame
from sprites import *
from config import *
from protocols import *
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 30)
        self.running = True

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

            #print(i, row)

    def new(self):
        # New game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # Object that contains all of our sprites && updates
        self.blocks = pygame.sprite.LayeredUpdates()  # walls
        #self.enemies = pygame.sprite.LayeredUpdates()               # enemies
        #self.attacks = pygame.sprite.LayeredUpdates()               # attack animation
        self.createTilemap()

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
        self.screen.fill(BLACK)
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
        text = ("Welcome to the Game! (Press enter to start)", True, BLACK)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Press Enter to continue
                        return  # Exit the banner screen

            screen.fill(WHITE)

            text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            screen.blit(text, text_rect)


# g = Game()
# g.intro()
# g.new()
# while g.running:
#     g.main()
#     g.game_over()

# pygame.quit()
# sys.exit()

if __name__ == "__main__":
    g = Game()
    g.intro()
    g.new()
    while g.running:
        g.main()
        g.game_over()

    pygame.quit()
    sys.exit()
