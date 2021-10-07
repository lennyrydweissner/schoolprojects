import random
import pygame


class RandomPictureGenerator:

    # Constructor
    def __init__(self, display_surface):

        # Class variables
        line_list = []      # This list is for all the words it can randomize from
        random_word = ""    # This is the variable who holds the random word later.
        f = ""              # The file object, used to open the txt file.
        full_path = ""      # Pathway variable, who will hold the path to the pictures
        random_image = ""   # Variable to hold the random image

        self.line_list = line_list
        self.display_surface = display_surface
        self.random_word = random_word
        self.f = f
        self.full_path = full_path
        self.random_image = random_image

    def display_screen(self, image2):
        self.display_surface.fill((255, 255, 255))
        self.display_surface.blit(image2, (575, 180))

    def random_image_generator(self):
        self.f = open("C:/This is what i use to github stavningsleken/bildfilen.txt", "r", encoding="utf-8")
        self.line_list = self.f.readlines()
        self.random_word = random.choice(self.line_list)
        self.random_word = self.random_word.strip()
        self.f.close()
        return self.random_word

    def display_next_image(self, random_word):
        self.full_path = "C:/This is what i use to github stavningsleken/bilder/" + random_word + ".png"
        self.random_image = pygame.image.load("C:/This is what i use to github stavningsleken/bilder/" + random_word + ".png")
        return self.random_image
