import pygame
from end_scene import EndScene


# Make this class inherit from end_scene class so i can use
# the_end_scene class methods, dont wanna write almost the same code again. :)
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
        texture = ""
        hp0, hp1, hp2, hp3, hp4 = "", "", "", "", ""
        hn0, hn1, hn2, hn3, hn4 = "", "", "", "", ""
        t1 = pygame.image.load("C:/This is what i use to github stavningsleken/meny bilder/highscore2.png")
        t2 = "TRYCK (G) FÖR ATT GÅ TILLBAKA."
        path_to_high_score_file = "C:/this is what i use to github stavningsleken/Highscore.txt"
        working = False

        self.texture = texture
        self.path_to_high_score_file = path_to_high_score_file
        self.working = working
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

    def save_to_high_score_list(self, user_input_word, path_to_high_score_file):
        try:
            self.path_to_high_score_file = path_to_high_score_file
            self.user_name_to_save = user_input_word
            self.file = open(self.path_to_high_score_file, "a", encoding="utf-8")
            self.working = True
        except FileNotFoundError as e:
            self.working = False
            print(f'There was an error while opening the file. {e}')

        try:
            self.file.write(self.user_score_to_save_to_the_high_score_list)
            self.file.write(",")
            self.file.write(self.user_name_to_save)
            self.file.write("\n")
            self.file.close()
            print("Highscore.txt was saved")
            self.working = True
        except BaseException as e:
            self.working = False
            print(f'Something went wrong then trying to save Highscore.txt {e}')

        finally:
            self.working = True
            self.file.close()
        return self.working

    def sort_high_score_list(self, path_to_high_score_file):
        try:
            self.file = open(self.path_to_high_score_file, "r", encoding="utf-8")
            self.working = True
        except FileNotFoundError as e:
            self.working = False
            print(f"Something went wrong. Couldn't open the file.  {e}")
        try:
            self.the_line = self.file.readlines()
            self.working = True
        except BaseException as e:
            self.working = False
            print(f'Something went wrong then trying to read lines from the file. {e}')

        finally:
            self.file.close()

        for items in self.the_line:
            self.cleaning_from_whitespaces = items.strip()
            self.score_list.append(self.cleaning_from_whitespaces)
            self.counter += 1

        # Sort the items we got after the highest value.
        self.score_list = sorted(self.score_list, key=lambda x: int(x.split(',')[0]))
        self.score_list.reverse()

        return self.score_list, self.working

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

        # Here no.1 score user.
        self.put_menu_text_to_screen(self.hn0, 550, 150)
        self.put_menu_text_to_screen(self.hp0, 720, 150)

        # Here no.2 score user
        self.put_menu_text_to_screen(self.hn1, 550, 200)
        self.put_menu_text_to_screen(self.hp1, 720, 200)

        # Here no.3 score user
        self.put_menu_text_to_screen(self.hn2, 550, 250)
        self.put_menu_text_to_screen(self.hp2, 720, 250)

        # Here no.4 score user
        self.put_menu_text_to_screen(self.hn3, 550, 300)
        self.put_menu_text_to_screen(self.hp3, 720, 300)

        # Here no.5 score user
        self.put_menu_text_to_screen(self.hn4, 550, 350)
        self.put_menu_text_to_screen(self.hp4, 720, 350)

        # Go back alternative goes here
        self.put_menu_text_to_screen(self.t2, 650, 550)
