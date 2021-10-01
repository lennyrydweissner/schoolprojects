import pygame
import math
import sys


class Intro:
    def __init__(self):
        pygame.init()
        # Using RGB values
        #              R  G   B
        black_color = (0, 0, 0)
        sc_x = 1550
        sc_y = 800

        # Make a surface there i can draw my pictures
        surface1 = pygame.display.set_mode((sc_x, sc_y))
        pygame.display.set_caption("Stavningsleken")

        logo_image = pygame.image.load("C:/python/different_tracks/bilder/stavningsleken.png")
        intro_image = pygame.image.load("C:/python/different_tracks/bilder/elefant_right_size.jpg")
        pygame.mixer.music.load("bensound-sunny.mp3")

        self.surface1 = surface1
        self.black_color = black_color
        self.intro_image = intro_image
        self.logo_image = logo_image

    def load_start_images(self):
        # Load the logo and the image to the screen.
        self.logo_image = pygame.image.load("C:/python/different_tracks/bilder/stavningsleken.png")
        self.intro_image = pygame.image.load("C:/python/different_tracks/bilder/elefant_right_size.jpg")

    def fill_the_screen(self):
        self.surface1.fill(self.black_color)
        self.surface1.blit(self.intro_image, (575, 150))
        self.surface1.blit(self.logo_image, (550, 0))

    @staticmethod
    def play_music():
        pygame.mixer.music.play()

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()

