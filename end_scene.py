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

        end_scene_font = pygame.font.SysFont('cambria', 24)
        big_text_font_end_scene = pygame.font.SysFont('cambria', 48)
        font_to_rend = ""
        big_text_font = ""
        saved_score = False
        text_one = "Stavningsleken"
        text_two = "SPELET ÄR NU SLUT: "
        text_three = "Din poäng var: "
        text_four = "VILL DU SPARA DIN POÄNG ? TRYCK (S)"
        text_five = "TRYCK (F) FÖR ATT SPELA IGEN."
        text_six = "ELLER TRYCK (A) FÖR ATT AVSLUTA SPELET HELT. "
        text_seven = "VISA HÖGSTA POÄNG LISTAN TRYCK (V)"

        text_rect = None

        pygame.display.set_caption("STAVNINGSLEKEN MY FIRST SCHOOL PROJECT.")
        self.end_scene_font = end_scene_font
        self.big_text_font_end_scene = big_text_font_end_scene
        self.font_to_rend = font_to_rend
        self.big_text_font = big_text_font
        self.text_rect = text_rect
        self.saved_score = saved_score
        self.text_one_output = text_one
        self.text_two_output = text_two
        self.text_three_output = text_three
        self.text_four_output = text_four
        self.text_five_output = text_five
        self.text_six_output = text_six
        self.text_seven_output = text_seven
        self.display_surface = display_surface

    def show_the_end(self, saved_score):

        if not saved_score:

            self.display_surface.fill(WHITE)
            self.put_big_text_to_screen(self.text_one_output, 710, 50)
            self.put_menu_text_to_screen(self.text_two_output, 700, 150)
            self.put_menu_text_to_screen(self.text_four_output, 690, 250)
            self.put_menu_text_to_screen(self.text_five_output, 690, 300)
            self.put_menu_text_to_screen(self.text_six_output, 690, 350)
            self.put_menu_text_to_screen(self.text_seven_output, 690, 400)

        else:

            self.display_surface.fill(WHITE)
            self.put_big_text_to_screen(self.text_one_output, 710, 50)
            self.put_menu_text_to_screen(self.text_two_output, 700, 150)
            self.put_menu_text_to_screen(self.text_five_output, 690, 300)
            self.put_menu_text_to_screen(self.text_six_output, 690, 350)
            self.put_menu_text_to_screen(self.text_seven_output, 690, 400)

    def put_menu_text_to_screen(self, output_text, text_pos_x, text_pos_y):
        self.font_to_rend = self.end_scene_font.render(output_text, True, PURPLE, WHITE)
        self.text_rect = self.font_to_rend.get_rect()
        self.text_rect.center = (text_pos_x, text_pos_y)
        self.display_surface.blit(self.font_to_rend, self.text_rect)

    def put_big_text_to_screen(self, output_text, text_pos_x, text_pos_y):
        self.big_text_font = self.big_text_font_end_scene.render(output_text, True, PURPLE, WHITE)
        self.text_rect = self.big_text_font.get_rect()
        self.text_rect.center = (text_pos_x, text_pos_y)
        self.display_surface.blit(self.big_text_font, self.text_rect)
