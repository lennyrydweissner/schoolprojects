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
GREEN2 = (10, 105, 14)
PURPLE = (107, 50, 168)


class EndScene:
    # Constructor goes here.
    def __init__(self, display_surface):
        pathway_to_logo = "C:/this is what i use to github stavningsleken/meny bilder/Stavningsleken.png"
        saved_score = False
        text_one = "Stavningsleken"
        text_two = "SPELET ÄR NU SLUT: "
        text_three = "Din poäng var: "
        text_four = "VILL DU SPARA DIN POÄNG ? TRYCK (S)"
        text_five = "TRYCK (F) FÖR ATT SPELA IGEN."
        text_six = "ELLER TRYCK (A) FÖR ATT AVSLUTA SPELET HELT. "
        text_seven = "VISA HÖGSTA POÄNG LISTAN TRYCK (V)"

        text_one_textrect = None
        text_two_textrect = None
        text_three_text_rect = None
        text_four_text_rect = None
        text_five_text_rect = None
        text_six_text_rect = None
        text_seven_text_rect = None

        pygame.display.set_caption("STAVNINGSLEKEN MY FIRST SCHOOL PROJECT.")

        self.text_one = ""
        self.text_two = ""
        self.text_three = ""
        self.text_four = ""
        self.text_five = ""
        self.text_six = ""
        self.text_seven = ""
        self.saved_score = saved_score
        self.text_one_output = text_one
        self.text_two_output = text_two
        self.text_three_output = text_three
        self.text_four_output = text_four
        self.text_five_output = text_five
        self.text_six_output = text_six
        self.text_seven_output = text_seven

        self.text_one_rect = text_one_textrect
        self.text_two_rect = text_two_textrect
        self.text_three_rect = text_three_text_rect
        self.text_four_rect = text_four_text_rect
        self.text_five_rect = text_five_text_rect
        self.text_six_rect = text_six_text_rect
        self.text_seven_rect = text_seven_text_rect

        self.display_surface = display_surface

    def show_the_end(self, saved_score):

        if not saved_score:

            font = pygame.font.SysFont('cambria', 48)
            font_two = pygame.font.SysFont('cambria', 24)
            font_four = pygame.font.SysFont('cambria', 24)
            self.display_surface.fill(WHITE)
            # self.display_surface.fill((255, 255, 255))
            self.text_one = font.render(self.text_one_output, True, PURPLE, WHITE)
            self.text_two = font_two.render(self.text_two_output, True, PURPLE, WHITE)
            self.text_four = font_four.render(self.text_four_output, True, PURPLE, WHITE)
            self.text_five = font_four.render(self.text_five_output, True, PURPLE, WHITE)
            self.text_six = font_four.render(self.text_six_output, True, PURPLE, WHITE)
            self.text_seven = font_four.render(self.text_seven_output, True, PURPLE, WHITE)

            self.text_one_rect = self.text_one.get_rect()
            self.text_two_rect = self.text_two.get_rect()
            self.text_four_rect = self.text_four.get_rect()
            self.text_five_rect = self.text_five.get_rect()
            self.text_six_rect = self.text_six.get_rect()
            self.text_seven_rect = self.text_seven.get_rect()

            self.text_one_rect.center = (710, 50)
            self.text_two_rect.center = (700, 150)
            self.text_four_rect.center = (690, 250)
            self.text_five_rect.center = (690, 300)
            self.text_six_rect.center = (690, 350)
            self.text_seven_rect.center = (690, 400)

            self.display_surface.blit(self.text_one, self.text_one_rect)
            self.display_surface.blit(self.text_two, self.text_two_rect)
            self.display_surface.blit(self.text_four, self.text_four_rect)
            self.display_surface.blit(self.text_five, self.text_five_rect)
            self.display_surface.blit(self.text_six, self.text_six_rect)
            self.display_surface.blit(self.text_seven, self.text_seven_rect)

        else:
            font = pygame.font.SysFont('cambria', 48)
            font_two = pygame.font.SysFont('cambria', 24)
            font_four = pygame.font.SysFont('cambria', 24)
            self.display_surface.fill(WHITE)

            self.text_one = font.render(self.text_one_output, True, PURPLE, WHITE)
            self.text_two = font_two.render(self.text_two_output, True, PURPLE, WHITE)
            # self.text_four = font_four.render(self.text_four_output, True, PURPLE, WHITE)
            self.text_five = font_four.render(self.text_five_output, True, PURPLE, WHITE)
            self.text_six = font_four.render(self.text_six_output, True, PURPLE, WHITE)
            self.text_seven = font_four.render(self.text_seven_output, True, PURPLE, WHITE)

            self.text_one_rect = self.text_one.get_rect()
            self.text_two_rect = self.text_two.get_rect()
            # self.text_four_rect = self.text_four.get_rect()
            self.text_five_rect = self.text_five.get_rect()
            self.text_six_rect = self.text_six.get_rect()
            self.text_seven_rect = self.text_seven.get_rect()

            self.text_one_rect.center = (710, 50)
            self.text_two_rect.center = (700, 150)
            # self.text_four_rect.center = (690, 250)
            self.text_five_rect.center = (690, 300)
            self.text_six_rect.center = (690, 350)
            self.text_seven_rect.center = (690, 400)

            self.display_surface.blit(self.text_one, self.text_one_rect)
            self.display_surface.blit(self.text_two, self.text_two_rect)
            # self.display_surface.blit(self.text_four, self.text_four_rect)
            self.display_surface.blit(self.text_five, self.text_five_rect)
            self.display_surface.blit(self.text_six, self.text_six_rect)
            self.display_surface.blit(self.text_seven, self.text_seven_rect)


