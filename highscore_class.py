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
        t1 = pygame.image.load("C:/This is what i use to github stavningsleken/meny bilder/highscore2.png")
        t2 = "TRYCK (G) FÖR ATT GÅ TILLBAKA."
        # t1 = "HÖGSTA POÄNG LISTAN"
        self.t1 = t1
        self.t2 = t2
        # Self outputs here
        self.t1_output = t1

        # Self fonts i want to use goes here
        self.high_score_font = high_score_font

        self.surface = display_surface
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
            # if self.counter <= 4:
            self.cleaning_from_whitespaces = items.strip()
            self.score_list.append(self.cleaning_from_whitespaces)
            self.counter += 1
        # self.counter = 0

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

        # Here we put the Highest score text in middle of screen
        self.surface.blit(self.t1, (300, 25))
        # self.blitz(self.t1_output, 700, 50)

        # Here no.1 score user.
        self.blitz(self.hn0, 550, 150)
        self.blitz(self.hp0, 720, 150)

        # Here no.2 score user
        self.blitz(self.hn1, 550, 200)
        self.blitz(self.hp1, 720, 200)

        # Here no.3 score user
        self.blitz(self.hn2, 550, 250)
        self.blitz(self.hp2, 720, 250)

        # Here no.4 score user
        self.blitz(self.hn3, 550, 300)
        self.blitz(self.hp3, 720, 300)

        # Here no.5 score user
        self.blitz(self.hn4, 550, 350)
        self.blitz(self.hp4, 720, 350)

        # Go back alternative goes here
        self.blitz(self.t2, 650, 550)

    def blitz(self, output_text, text_pos_x, text_pos_y):
        text_font_rend = self.high_score_font.render(output_text, True, end_scene.PURPLE, end_scene.WHITE)
        text_rect = text_font_rend.get_rect()
        text_rect.center = (text_pos_x, text_pos_y)
        self.display_surface.blit(text_font_rend, text_rect)
