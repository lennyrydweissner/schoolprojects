import pygame
import math
import sys


class Intro:
    def __init__(self, surface1, black_color):
        pygame.init()

        # Setting up the name of the pygame window
        pygame.display.set_caption("Stavningsleken")

        logo_image = ""
        intro_image = ""

        # Load the music
        pygame.mixer.music.load("bensound-sunny.mp3")

        self.surface1 = surface1
        self.black_color = black_color
        self.intro_image = intro_image
        self.logo_image = logo_image

    def load_start_images(self):
        # Load the logo and the image to the screen.
        self.logo_image = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/stavningsleken.png")
        self.intro_image = pygame.image.load("C:\This is what i use to github stavningsleken/bilder/elefant.png")

    def fill_the_screen(self):
        self.surface1.fill(self.black_color)
        self.surface1.blit(self.intro_image, (575, 80))
        self.surface1.blit(self.logo_image, (550, 0))

    @staticmethod
    def play_music():
        pygame.mixer.music.play()

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()