import pygame
import sys


class Score:
    def __init__(self, display_surface):
        pathway_to_good_sp = "C:/this is what i use to github stavningsleken/meny bilder/bra_rätt_stavat.png"
        pathway_to_bad_sp = "C:/this is what i use to github stavningsleken/meny bilder/tyvärr_det_var_fel_stavat.png"
        load_good = ""
        load_bad = ""
        good_image = ""
        bad_image = ""

        self.display_surface = display_surface
        # self.answer = answer
        self.pathway_to_good_sp = pathway_to_good_sp
        self.pathway_to_bad_sp = pathway_to_bad_sp
        self.load_good = load_good
        self.load_bad = load_bad
        self.good_image = good_image
        self.bad_image = bad_image
        self.user_input_word = ""
        self.random_word = ""

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
        # self.answer = user_answer_num
        self.user_input_word = user_input_word
        self.random_word = random_word

        if self.user_input_word == self.random_word:
            # 1 Load the good answer image
            lgi = self.load_good_answer_image()
            self.show_good_answer(lgi)

        if self.user_input_word == "":
            pass
        else:
            if not self.user_input_word == self.random_word:
                # Load the bad answer image
                lbi = self.load_bad_answer_image()
                self.show_bad_answer(lbi)

