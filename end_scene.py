import pygame
import sys

# Constants in RGB Colors (Red, Green, Blue)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)
YELLOW = (186, 184, 43)
DARKER_YELLOW = (153, 153, 0)
PINK = (243, 132, 245)
NAVY_MARIN_BLUE = (102, 233, 242)


class EndScene:
    # Constructor goes here.
    def __init__(self, display_surface):
        text_one = "Stavningsleken"
        text_two = "Spelet har slutat: tryck (a) för att spela igen. eller tryck (e) för att avsluta."
        text_one_textrect = None
        text_two_textrect = None
        pygame.display.set_caption("Stavningsleken: Gjort för mina två barn Felicia och Emilia.")

        self.text_one = ""
        self.text_two = ""
        self.text_one_output = text_one
        self.text_two_output = text_two
        self.text_one_rect = text_one_textrect
        self.text_two_rect = text_two_textrect
        self.display_surface = display_surface

    def show_the_end(self):
        font = pygame.font.SysFont('cambria', 48)
        font_two = pygame.font.SysFont('cambria', 24)
        self.display_surface.fill((255, 255, 255))
        self.text_one = font.render(self.text_one_output, True, DARKER_YELLOW, WHITE)
        self.text_two = font_two.render(self.text_two_output, True, DARKER_YELLOW, WHITE)

        self.text_one_rect = self.text_one.get_rect()
        self.text_two_rect = self.text_two.get_rect()

        self.text_one_rect.center = (710, 50)
        self.text_two_rect.center = (700, 200)

        self.display_surface.blit(self.text_one, self.text_one_rect)
        self.display_surface.blit(self.text_two, self.text_two_rect)
