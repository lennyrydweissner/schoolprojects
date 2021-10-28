import pygame

import end_scene
from end_scene import EndScene


# Make this class inherit from end_scene class so i can use
# show_the_end class method, dont wanna write almost the same code again. :)
# and i want to use the constants which are the colors.

class HighScoreClass(EndScene):
    def __init__(self, read_score, display_surface):
        super().__init__(display_surface)
        pygame.init()
        high_score_font = pygame.font.SysFont('cambria', 24)
        f = ""
        score_list = []
        the_line = ""
        cleaning_from_whitespaces = ""
        counter = 0
        temp_name = ""
        temp_points = 0
        sorted_list = []
        hp0, hp1, hp2, hp3, hp4 = "", "", "", "", ""
        hn0, hn1, hn2, hn3, hn4 = "", "", "", "", ""
        text_one = "HÖGSTA POÄNG LISTAN"
        text_two = ""
        text_three = ""
        text_four = ""
        text_five = ""
        text_six = ""
        text_one_textrect = None
        text_two_textrect = None

        # Self outputs here
        self.text_one_output = text_one
        self.text_two_output = text_two

        # Self rects here
        self.text_one_rect = text_one_textrect
        self.text_two_rect = text_two_textrect

        # Self fonts i want to use goes here
        self.high_score_font = high_score_font

        self.surface1 = display_surface
        self.user_score_to_save_to_the_high_score_list = read_score
        self.user_name_to_save = ""
        self.file = f
        self.score_list = score_list
        self.the_line = the_line
        self.cleaning_from_whitespaces = cleaning_from_whitespaces
        self.counter = counter
        self.temp_name = temp_name
        self.temp_points = temp_points
        self.sorted_list = sorted_list
        self.hp0 = hp0
        self.hp1 = hp1
        self.hp2 = hp2
        self.hp3 = hp3
        self.hp4 = hp4
        self.hn0 = hn0
        self.hn1 = hn1
        self.hn2 = hn2
        self.hn3 = hn3
        self.hn4 = hn4

    def save_to_high_score_list(self, user_input_word):
        self.user_name_to_save = user_input_word
        self.file = open("Highscore.txt", "a", encoding="utf-8")
        self.file.write(self.user_score_to_save_to_the_high_score_list)
        self.file.write(",")
        self.file.write(self.user_name_to_save)
        self.file.write("\n")
        self.file.close()
        print("Highscore.txt was saved")

    def sort_high_score_list(self):
        self.file = open("Highscore.txt", "r", encoding="utf-8")
        self.the_line = self.file.readlines()

        for items in self.the_line:
            if self.counter <= 4:
                self.cleaning_from_whitespaces = items.strip()
                self.score_list.append(self.cleaning_from_whitespaces)
                self.counter += 1
        self.counter = 0

        # Sort the items we got after the highest value.
        self.score_list = sorted(self.score_list, key=lambda x: int(x.split(',')[0]))
        self.score_list.reverse()
        return self.score_list

    def show_high_score_on_screen(self):
        self.counter = 0
        for items in self.score_list:

            # Disperse the highest scores and names.
            if self.counter == 0:
                self.hp0, self.hn0 = items.split(',')
            if self.counter == 1:
                self.hp1, self.hn1 = items.split(',')
            if self.counter == 2:
                self.hp2, self.hn2 = items.split(',')
            if self.counter == 3:
                self.hp3, self.hn3 = items.split(',')
            if self.counter == 4:
                self.hp4, self.hn4 = items.split(',')
            self.counter += 1

        # Putting the score out on the screen
        # Here we present the High score text on screen
        self.text_one = self.high_score_font.render(self.text_one_output, True, end_scene.PURPLE, end_scene.WHITE)
        self.text_one_rect = self.text_one.get_rect()
        self.text_one_rect.center = (710, 50)
        self.display_surface.blit(self.text_one, self.text_one_rect)

        # Here we present the highest score user.
        self.text_two = self.high_score_font.render(self.hn0, True, end_scene.PURPLE, end_scene.WHITE)
        self.text_three = self.high_score_font.render(self.hp0, True, end_scene.PURPLE, end_scene.WHITE)

        self.text_two_rect = self.text_two.get_rect()
        self.text_three_rect = self.text_three.get_rect()

        self.text_two_rect.center = (710, 150)
        self.text_three_rect.center = (820, 150)

        self.display_surface.blit(self.text_two, self.text_two_rect)
        self.display_surface.blit(self.text_three, self.text_three_rect)

        # Here comes the second highest score user
        