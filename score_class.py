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


class Score:
    def __init__(self, display_surface, player_score):

        pathway_to_good_sp = "C:/this is what i use to github stavningsleken/meny bilder/bra_rätt_stavat.png"
        pathway_to_bad_sp = "C:/this is what i use to github stavningsleken/meny bilder/tyvärr_det_var_fel_stavat.png"
        load_good = None
        load_bad = None
        good_image = None
        bad_image = None
        your_score_text = None
        score_text = None
        your_score_textrect = None
        score_textrect = None

        self.display_surface = display_surface
        self.pathway_to_good_sp = pathway_to_good_sp
        self.pathway_to_bad_sp = pathway_to_bad_sp

        self.load_good = load_good
        self.load_bad = load_bad

        self.good_image = good_image
        self.bad_image = bad_image
        self.user_input_word = ""
        self.random_word = ""

        self.your_score_text = your_score_text
        self.score_text = score_text
        self.your_score_text_rect = your_score_textrect
        self.score_text_rect = score_textrect

        self.player_score = player_score
        self.value = self.player_score

    def load_good_answer_image(self):
        self.good_image = pygame.image.load(self.pathway_to_good_sp)
        return self.good_image

    def load_bad_answer_image(self):
        self.load_bad = pygame.image.load(self.pathway_to_bad_sp)
        return self.load_bad

    def show_good_answer(self, g_image):
        self.good_image = pygame.transform.scale(g_image, (450, 50))
        my_good_image_rect = self.good_image.get_rect()
        my_good_image_rect.center = (1040, 720)
        self.display_surface.blit(self.good_image, my_good_image_rect)

    def show_bad_answer(self, b_image):
        self.bad_image = pygame.transform.scale(b_image, (450, 50))
        my_bad_image_rect = self.bad_image.get_rect()
        my_bad_image_rect.center = (1040, 720)
        self.display_surface.blit(self.bad_image, my_bad_image_rect)

    def check_the_user_answer(self, user_input_word, random_word):
        self.user_input_word = user_input_word
        self.random_word = random_word

        if self.user_input_word == self.random_word:
            # 1 Load the good answer image
            lgi = self.load_good_answer_image()
            self.show_good_answer(lgi)
            self.adding_score()
            self.showing_score()
            self.value = self.player_score
            print(self.value)
        if self.user_input_word == "":
            pass
        else:
            if not self.user_input_word == self.random_word:
                # Load the bad answer image
                lbi = self.load_bad_answer_image()
                self.show_bad_answer(lbi)
                self.showing_score()

    def showing_score(self):

        # 1 Load up the font i want to use
        font = pygame.font.SysFont('cambria', 32)
        # 2 Create 2 text surfaces that i can put on the screen.
        self.your_score_text = font.render('Your Score: ', True, DARKER_YELLOW, WHITE)
        self.score_text = font.render(str(self.player_score), True, DARKER_YELLOW, WHITE)

        # 3 Create rects around the text surfaces
        self.your_score_text_rect = self.your_score_text.get_rect()
        self.score_text_rect = self.score_text.get_rect()

        # 4 telling where i want this to show up
        self.your_score_text_rect.center = (1000, 450)
        self.score_text_rect.center = (1000, 480)

        # Blit the 2 texts to the screen
        self.display_surface.blit(self.your_score_text, self.your_score_text_rect)
        self.display_surface.blit(self.score_text, self.score_text_rect)
        pygame.display.flip()

    def adding_score(self):
        self.player_score = self.player_score + 10
        self.value = self.player_score

    def show_value(self):
        value = self.value
        return value
