import random
import pygame
import os
from pygame.locals import *


class RandomPictureGenerator:

    # Constructor
    def __init__(self, display_surface):
        # Class variables
        line_list = []     # This list is for all the words it can randomize from
        random_word = ""   # This is the variable who holds the random word later.
        f = ""             # The file object, used to open the txt file.
        full_path = ""     # Pathway variable, who will hold the path to the pictures
        random_image = ""  # Variable to hold the random image
        time_to_go = False
        check = False
        working = 0

        self.line_list = line_list
        self.display_surface = display_surface
        self.random_word = random_word
        self.f = f
        self.full_path = full_path
        self.random_image = random_image
        self.time_to_go = time_to_go
        self.check = check
        self.working = working

    def display_screen(self, image2):
        image2 = pygame.transform.scale(image2, (200, 200))
        my_rect = image2.get_rect()
        my_rect.center = (630, 400)

        self.display_surface.blit(image2, my_rect)

    def load_list_to_pick_random_word_from(self):
        try:
            self.f = open("C:/This is what i use to github stavningsleken/bildfilen.txt", "r", encoding="utf-8")
        except FileNotFoundError as e:
            print(f'There was an error while loading the file. {e}')
        try:
            self.line_list = self.f.readlines()
        except BaseException as e:
            print(f'Something went wrong then trying to populate the list. {e}')
        finally:
            self.f.close()
        return self.line_list

    def get_computer_randomized_word_from_list(self):
        self.check_if_list_is_empty()
        self.random_word = random.choice(self.line_list)
        self.line_list.remove(self.random_word)
        self.random_word = self.random_word.strip()
        return self.random_word

    def display_next_image(self, random_word):
        try:
            self.full_path = "C:/This is what i use to github stavningsleken/bilder/" + random_word + ".png"
            self.random_image = pygame.image.load(
                "C:/This is what i use to github stavningsleken/bilder/" + random_word + ".png")
            self.working = 1

        except pygame.error as message:
            self.working = 0
            print(self.working)
            print(f'Cant load the image file. {message} ')

        return self.random_image

    def check_if_list_is_empty(self):
        if len(self.line_list) == 1:
            self.time_to_go = True

    def check_the_list_status(self):
        return self.time_to_go
