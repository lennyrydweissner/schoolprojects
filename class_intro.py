import pygame
from pygame.compat import geterror


class Intro:
    def __init__(self, surface1, black_color):
        pygame.init()
        pygame.mixer.init()
        working = 0

        # Naming the game window.
        pygame.display.set_caption("STAVNINGSLEKEN MY FIRST SCHOOL PROJECT.")

        logo_image = ""
        intro_image = ""
        music_file = "C:/this is what i use to github stavningsleken/bensound-sunny.mp3"
        stop_playing_music = pygame.mixer.music.stop()

        applauds_sound = pygame.mixer.Sound("C:/this is what i use to github stavningsleken/Sounds/"
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
        self.applauds = applauds_sound
        self.operation_sound = operation_sound
        self.type_writer_sound = type_writer_sound
        self.music_file = music_file
        self.stop_playing_music = stop_playing_music
        self.working = working

    def load_start_images(self):
        # Load the start image to the screen.
        try:
            self.intro_image = pygame.image.load("C:/This is what i use to github stavningsleken/bilder/katt.png")
            self.working = 1
        except pygame.error as message:
            self.working = 0
            print(f"Couldn't load the start image. {message}")
        return self.working

    def fill_the_screen(self):
        self.surface1.fill(self.black_color)
        self.surface1.blit(self.intro_image, (580, 320))

    def applauds_sound(self):
        try:
            pygame.mixer.Sound.play(self.applauds)
            self.working = 1
        except pygame.error:
            self.working = 0
            print(self.working)
            print('Cannot load sound: %s' % self.applauds)
            raise SystemExit(str(geterror()))
        return self.working

    def wrong_answer_sound(self):
        try:
            pygame.mixer.Sound.play(self.operation_sound)
            self.working = 1

        except pygame.error:
            self.working = 0
            print(self.working)
            print('Cannot load sound: %s' % self.operation_sound)
            raise SystemExit(str(geterror()))
        return self.working

    def sound_of_typewriter(self):

        pygame.mixer.Sound.play(self.type_writer_sound)

    def stop_sound_of_typewriter(self):

        pygame.mixer.Sound.stop(self.type_writer_sound)

    def play_music(self):
        try:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.working = 1

        except pygame.error:
            self.working = 0
            print(self.working)
            print('Cannot load sound: %s' % self.music_file)
            raise SystemExit(str(geterror()))

        return self.working

    def stop_music(self):
        try:
            self.stop_playing_music = pygame.mixer.music.stop()
            self.working = 1
        except pygame.error:
            self.working = 0
            print(self.working)
            print('Cannot stop music: %s')
            raise SystemExit(str(geterror()))
        return self.working
