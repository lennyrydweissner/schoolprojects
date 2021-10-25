import pygame
import math
import sys


class Intro:
    def __init__(self, surface1, black_color):
        pygame.init()

        # Naming the game window.
        pygame.display.set_caption("STAVNINGSLEKEN MY FIRST SCHOOL PROJECT.")

        logo_image = ""
        intro_image = ""
        pygame.mixer.music.load("C:/this is what i use to github stavningsleken/bensound-sunny.mp3")
        applauds = pygame.mixer.Sound("C:/this is what i use to github stavningsleken/Sounds/"
                                      "CRWDApls_Applause 1 (ID 2363)_BSB.wav")

        operation_sound = pygame.mixer.Sound("C:/this is what i use to github stavningsleken/Sounds/"
                                             "TOYElec_Operation game 4 (ID 1685)_BSB.wav")

        type_writer_sound = pygame.mixer.Sound("C:/this is what i use to github stavningsleken/Sounds/"
                                               "COMType_Typewriter (ID 1065)_BSB.wav")

        laugh_sound = pygame.mixer.Sound("C:/this is what i use to github stavningsleken/Sounds/"
                                         "VOXLaff_Laugh (ID 0475)_BSB.wav")

        self.surface1 = surface1
        self.black_color = black_color
        self.intro_image = intro_image
        self.logo_image = logo_image
        self.applauds = applauds
        self.operation_sound = operation_sound
        self.type_writer_sound = type_writer_sound

    def load_start_images(self):
        # Load the start image to the screen.
        self.intro_image = pygame.image.load("C:/This is what i use to github stavningsleken/bilder/katt.png")
        working = 1
        return working

    def fill_the_screen(self):
        self.surface1.fill(self.black_color)
        self.surface1.blit(self.intro_image, (580, 320))

    def applauds_sound(self):
        pygame.mixer.Sound.play(self.applauds)
        check_that_sound_is_there = pygame.mixer.Sound.play(self.applauds)
        if not check_that_sound_is_there == "":
            working = 1
        else:
            working = 0
        return working

    def wrong_answer_sound(self):
        pygame.mixer.Sound.play(self.operation_sound)
        check_that_sound_is_there = pygame.mixer.Sound.play(self.operation_sound)
        if not check_that_sound_is_there == "":
            working = 1
        else:
            working = 0
        return working

    def sound_of_typewriter(self):
        pygame.mixer.Sound.play(self.type_writer_sound)

    def stop_sound_of_typewriter(self):
        pygame.mixer.Sound.stop(self.type_writer_sound)

    @staticmethod
    def play_music():
        pygame.mixer.music.play()

        if pygame.mixer.music.play() is None:
            working = 1
        else:
            working = 0

        return working

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()
        stop_sound_check = pygame.mixer.music.stop()

        if stop_sound_check is None:
            working = 0
        else:
            working = 1

        return working
