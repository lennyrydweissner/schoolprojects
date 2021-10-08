import pygame
import math
import sys


class Intro:
    def __init__(self, surface1, black_color):
        pygame.init()

        # Make a surface there i can draw my pictures
        # surface1 = pygame.display.set_mode((sc_x, sc_y))
        pygame.display.set_caption("Stavningsleken alpha version 0.3 school project")

        logo_image = ""
        intro_image = ""
        pygame.mixer.music.load("bensound-sunny.mp3")

        self.surface1 = surface1
        self.black_color = black_color
        self.intro_image = intro_image
        self.logo_image = logo_image

    def load_start_images(self):
        # Load the start image to the screen.
        self.intro_image = pygame.image.load("C:/This is what i use to github stavningsleken/bilder/katt.png")

    def fill_the_screen(self):
        self.surface1.fill(self.black_color)
        self.surface1.blit(self.intro_image, (580, 320))


    @staticmethod
    def play_music():
        pygame.mixer.music.play()

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()
