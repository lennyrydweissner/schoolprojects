import random
import pygame
from pygame.locals import *


class RandomPictureGenerator:

    # Constructor
    def __init__(self, display_surface):
        # Class variables
        line_list = []  # This list is for all the words it can randomize from
        random_word = ""  # This is the variable who holds the random word later.
        f = ""  # The file object, used to open the txt file.
        full_path = ""  # Pathway variable, who will hold the path to the pictures
        random_image = ""  # Variable to hold the random image
        time_to_go = False
        check = False

        self.line_list = line_list
        self.display_surface = display_surface
        self.random_word = random_word
        self.f = f
        self.full_path = full_path
        self.random_image = random_image
        self.time_to_go = time_to_go
        self.check = check

    def display_screen(self, image2):
        image2 = pygame.transform.scale(image2, (200, 200))
        my_rect = image2.get_rect()
        my_rect.center = (630, 400)
        # screen.blit(my_image, my_rect)
        self.display_surface.blit(image2, my_rect)

    def load_list_to_pick_random_word_from(self):
        self.f = open("C:/This is what i use to github stavningsleken/bildfilen.txt", "r", encoding="utf-8")
        self.line_list = self.f.readlines()
        self.f.close()
        return self.line_list

    def get_computer_randomized_word_from_list(self):
        self.check_if_list_is_empty()
        self.random_word = random.choice(self.line_list)
        self.line_list.remove(self.random_word)
        self.random_word = self.random_word.strip()
        return self.random_word

    def display_next_image(self, random_word):
        self.full_path = "C:/This is what i use to github stavningsleken/bilder/" + random_word + ".png"
        self.random_image = pygame.image.load(
            "C:/This is what i use to github stavningsleken/bilder/" + random_word + ".png")
        return self.random_image

    def check_if_list_is_empty(self):
        if len(self.line_list) == 1:
            print(len(self.line_list))
            self.time_to_go = True

    def check_the_list_status(self):
        return self.time_to_go
