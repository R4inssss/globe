import pygame
from sprites import *
from config import *
from protocols import *
from protocols import GlobalWarming
import sys
from dialogue import MainText
from dialogue import *


class Game():
    def __init__(self):
        # Gamplay Loop
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 30)
        self.running = True

        # Map Calls
        self.bg = pygame.image.load(r"./assets/bg.png")

        # Player reactives
        self.meter = 100
        self.border_size = 50

        # Answer key methods | protocols.py | can change as array
        self.GlobalWarming = GlobalWarming()
        self.key1 = 'A'

    # Story Loop /TODO: Modify and add border loop for game

    def ask_question(self, question_set):
        choice = None

        while choice is None:
            # Draw background and options
            self.screen.blit(self.bg, (0, 0))  # Draw background

            question_text = "Please select an option:"
            question_surface = self.font.render(question_text, True, BLACK)
            self.screen.blit(question_surface, (50, 50))

            # Render options on the screen
            y_offset = 300
            option_rects = []
            for option in question_set:
                for key, value in option.items():
                    option_text = f"{key}: {value}"
                    option_surface = self.font.render(option_text, True, BLACK)
                    option_rect = option_surface.get_rect(topleft=(50, y_offset))
                    pygame.draw.rect(self.screen, WHITE, option_rect.inflate(10, 10), 40)  # TODO: Adjust Layers
                    option_rects.append((key, option_rect))  # Store rect for mouse click detection <-sometimes works
                    self.screen.blit(option_surface, option_rect.topleft)
                    y_offset += 50

            pygame.display.update()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        choice = 'A'
                    elif event.key == pygame.K_b:
                        choice = 'B'
                    elif event.key == pygame.K_c:
                        choice = 'C'
                    elif event.key == pygame.K_d:
                        choice = 'D'

                # Detect mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for key, rect in option_rects:
                        if rect.collidepoint(mouse_pos):
                            choice = key

                if choice is not None:
                    pass
        return choice

    def air_dialogue(self):
        print("""\n MOST efficient of ways to reduce transportation emissions 
        Why is this important?: Most transportation methods involve
        non-renewable resources that contribute to global warming """)
        choice1 = self.ask_question(self.dialogue.A1text)
        print(f"\nYou selected: {choice1}\n")

        print("""\nIdentify the largest activity that contributes to air pollution
        Why is this important?: Understanding the primary sources of air pollution 
        can increase awareness and decrease the effects of such activities""")

        choice2 = self.ask_question(self.dialogue.A2text)
        print(f"\nYou selected: {choice2}\n")

    def water_dialogue(self):
        print("""\nFind the typical range of water temperature to support healthy aquatic ecosystems 
        Why is it important?: To analyze the impact of climate change, its beneficial to monitor 
        the water temperature to view how organisms adapt to their environment over a period of time""")
        choice1 = self.ask_question(self.dialogue.B1text)
        print(f"\nYou selected: {choice1}\n")

        print("""\nDescribe how an increase in water temperature will impact salmon populations
        Why is it important?: To analyze the impact of climate change, its beneficial to monitor 
        the water temperature to view how organisms adapt to their environment over a period of time""")
        choice2 = self.ask_question(self.dialogue.B2text)
        print(f"\nYou selected: {choice2}\n")

    # def carbon_dialogue(self):
    #     print("""\nAdjust your diet to decrease carbon-footprint 
    #     Why is it important? Livestock farming are one of the main contributors for methane emissions
    #     in the atmosphere""")
    #     choice1 = self.ask_question(self.dialogue.C1text)
    #     print(f"\nYou selected: {choice1}\n")

    #     print("""Identify what contributes most to an individual's carbon-footprint
    #     Why is it important?: Carbon footprint indicates the total amount of greenhouse gasses generated 
    #     by human action""")

    #     choice2 = self.ask_question(self.dialogue.C2text)
    #     print(f"\nYou selected: {choice2}\n")

    def carbon_dialogue(self):
        print("""\nAdjust your diet to decrease carbon-footprint 
        Why is it important? Livestock farming are one of the main contributors for methane emissions
        in the atmosphere""")
        choice1 = self.ask_question(self.dialogue.C1text)
        print(f"\nYou selected: {choice1}\n")

        print("""Identify what contributes most to an individual's carbon-footprint
        Why is it important?: Carbon footprint indicates the total amount of greenhouse gasses generated 
        by human action""")

        choice2 = self.ask_question(self.dialogue.C2text)
        print(f"\nYou selected: {choice2}\n")

    # New Game loop

    def new(self):
        # New game starts
        self.playing = True
        self.dialogue = MainText()
        self.dialogue.AirDialogue()
        self.dialogue.WaterDialogue()
        self.dialogue.CarbonDialogue()

        self.all_sprites = pygame.sprite.Group()

    def events(self):
        # Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                sys.exit()

    def update(self):
        self.all_sprites.update()

    # Event Draws
    def adjust_meter(self, correct):
        if correct:
            self.meter += 5
        else:
            self.meter -= 10
            self.border_size += 10

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.draw_border()
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def draw_border(self):
        pygame.draw.rect(self.screen, RED, (0, 0, WIN_WIDTH, WIN_HEIGHT), self.border_size)

    def intro(self):
        self.screen.fill(WHITE)
        intro_text = self.font.render('Welcome to Globel Games!', True, BLACK)
        self.screen.blit(intro_text, (WIN_WIDTH // 2 - intro_text.get_width() // 2, WIN_HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)

    def intro_banner(self):
        intro = True
        while intro:
            self.screen.fill(BLACK)
            title_text = self.font.render('Globel Games', True, WHITE)
            play_button_text = self.font.render('Play', True, WHITE)
            play_button_rect = play_button_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))

            self.screen.blit(title_text, (WIN_WIDTH // 2 - title_text.get_width() // 2, WIN_HEIGHT // 2 - 100))
            self.screen.blit(play_button_text, play_button_rect.topleft)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro_banner = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        intro = False

    def game_over(self):
        pass

    def main(self):
        # game loop
        self.intro_banner()
        #self.intro()
        self.new()

        # Question Sequences
        self.air_dialogue()
        self.water_dialogue()
        self.carbon_dialogue()

        while self.playing:
            self.events()
            self.update()
            self.draw()
            #self.carbon()
        self.running = False


if __name__ == "__main__":
    g = Game()
    g.intro()
    g.main()
    pygame.quit()
    sys.exit()
