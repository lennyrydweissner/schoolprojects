"""

credits goes to "Music: www.bensound.com"
for the music in this application.

"""
import pygame
import sys

# importing my classes
from class_intro import Intro
from mouse_cord_class import MouseCords
from word_class import RandomWords
from filehandling_class import MyFileHandling
from button import Button
from random_picture_class import RandomPictureGenerator
from rewritten_textbox_class import RewrittenTextbox
from score_class import Score
from end_scene import EndScene
from highscore_class import HighScoreClass

# init pygame
pygame.init()

# Variables that i need goes here:
mx = 0  # This is the mouse tracker start coordinate x
my = 0  # This is the mouse tracker start coordinate y
black_color = (255, 255, 255)  # Black background color
sc_x = 1450  # Screen size in x
sc_y = 800  # Screen size in y

# Make the pygame screen
surface1 = pygame.display.set_mode((sc_x, sc_y))

# Textbox variables.
# color_passive = pygame.Color('green')
# color_active = pygame.Color('black')

# font = pygame.font.SysFont("verdana", 32)
font = pygame.font.Font(None, 32)
path_to_word_file = "bildfilen.txt"  # Filepath to the file with all words.

# Loading up my button pictures to the game:
start_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Starta.png")
stopp_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Avsluta.png")
main_meny_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Huvud meny.png")
turn_off_music_img = pygame.image.load(
    "C:\This is what i use to github stavningsleken/meny bilder/Stäng av musiken.png")
turn_on_music_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Sätt på musiken.png")
next_picture_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Nästa bild.png.")
huge_logo_img = pygame.image.load("C:\This is what i use to github stavningsleken/start_bilder/Stavningsleken_huge.png")

# Loading start screen images here.

main_logo_start_screen_img = pygame.image.load(
    "C:\This is what i use to github stavningsleken/start_bilder/Stavningsleken_huge.png")
start_the_game_img = pygame.image.load("C:\This is what i use to github stavningsleken/start_bilder/Starta spelet.png")
end_the_game_img = pygame.image.load("C:\This is what i use to github stavningsleken/start_bilder/Avsluta spelet.png")

# Button instances goes here
stopp_music_button = Button(30, 555, turn_off_music_img)
turn_on_music_button = Button(30, 620, turn_on_music_img)
main_meny_button = Button(30, 15, main_meny_img)
stopp_button = Button(30, 680, stopp_img)
start_button = Button(570, 385, start_img)
next_random_picture_button = Button(570, 555, next_picture_img)
main_logo_button2 = Button(275, 30, huge_logo_img)

# Start Screen button instances goes here
main_logo_button = Button(275, 30, main_logo_start_screen_img)
start_the_game_button = Button(460, 180, start_the_game_img)
end_the_game_button = Button(460, 280, end_the_game_img)

# creates all my instances here
intro_object = Intro(surface1, black_color)
mouse_cords_tracker = MouseCords(mx, my)  # Not gonna use this then the game is done. just in development phase
read_my_file = MyFileHandling(path_to_word_file)

# Testing new stuff here
base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

my_text_box = RewrittenTextbox(570, 700, 140, 32, color_passive, color_active, base_font, surface1, active)
my_text_box.draw()
control = False
player_score = 0
game_running = True


def the_start_screen():
    start_screen_running = True

    while start_screen_running:

        surface1.fill((255, 255, 255))

        if main_logo_button.draw_button_to_screen(surface1):
            pass

        if start_the_game_button.draw_button_to_screen(surface1):
            # Start the game then user click on the button
            surface1.fill((255, 255, 255))

            main_game_loop()

        if end_the_game_button.draw_button_to_screen(surface1):
            # Ends the whole game here
            start_screen_running = False
            quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_screen_running = False

            # Coordinate tracker system, using it to place buttons on the screen.
            # mouse_cords_tracker.hunt_cords()
            # mouse_cords_tracker.write_out_cords()

        pygame.display.update()
    return start_screen_running


def end_screen():
    clock = pygame.time.Clock()
    end_obj = EndScene(surface1)
    end_running = True
    saved_score = False

    while end_running:

        # Pygame boiler code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    the_start_screen()

                if event.key == pygame.K_s:
                    save_sceen()

                if event.key == pygame.K_v:
                    high_score_screen()

                if event.key == pygame.K_a:
                    end_running = False
                    quit()

        end_obj.show_the_end(saved_score)

        pygame.display.update()

        clock.tick(60)


def main_game_loop():
    game_running = True

    # Starts playing the music here.
    # intro_object.play_music()

    # Start the intro scene on screen
    intro_object.load_start_images()
    intro_object.fill_the_screen()

    # Creating an instance off random picture class
    rnd_obj = RandomPictureGenerator(surface1)

    # Creating an score object
    real_score = 0
    score_obj = Score(surface1, player_score)

    # gets the player score for the first time.
    real_score = score_obj.showing_score()

    # Setting up the clock who controls the fps
    clock = pygame.time.Clock()

    # This is the block that loads in the gaming picture
    # first image you should spell right on.
    rnd_obj.load_list_to_pick_random_word_from()
    random_word = rnd_obj.get_computer_randomized_word_from_list()
    random_image = rnd_obj.display_next_image(random_word)
    rnd_obj.display_screen(random_image)
    soundcheck = None
    typewriter_sound = None

    while game_running:

        # Clear what was written in the user_input_word
        # every time the loop turns around
        user_input_word = my_text_box.clear_written_word()
        soundcheck = None

        # Pygame boiler code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            my_text_box.catch_user_events(event)
            user_input_word = my_text_box.what_user_wrote()

            score_obj.check_the_user_answer(user_input_word, random_word)
            soundcheck = score_obj.check_sound_state()
            # typewriter_sound = my_text_box.check_type_sound()

            if soundcheck == 1:
                intro_object.applauds_sound()
                soundcheck = 0

            if soundcheck == 2:
                intro_object.wrong_answer_sound()
                soundcheck = 0

        my_text_box.draw()

        my_text_box.update()

        if main_logo_button2.draw_button_to_screen(surface1):
            pass

        if stopp_music_button.draw_button_to_screen(surface1):
            intro_object.stop_music()

        if turn_on_music_button.draw_button_to_screen(surface1):
            intro_object.play_music()

        if stopp_button.draw_button_to_screen(surface1):
            game_running = False

        if next_random_picture_button.draw_button_to_screen(surface1):
            # Do a check if the word list is empty
            check_list_index = rnd_obj.check_the_list_status()
            rnd_obj.check_if_list_is_empty()
            if check_list_index:
                get_the_score_before_going_to_end_screen = score_obj.show_value()
                score_obj.save_the_score_before_we_go_to_end_sceen(get_the_score_before_going_to_end_screen)
                end_screen()

            surface1.fill((255, 255, 255))

            # user_player_score.adding_score()
            score_obj.showing_score()
            my_text_box.reset_mouseclick()

            # Gets a random word from the line_list in class method random_image_generator
            random_word = rnd_obj.get_computer_randomized_word_from_list()

            # Load upp the image who is corresponding to the random word we got above
            random_image = rnd_obj.display_next_image(random_word)

            # Show the image on the screen.
            rnd_obj.display_screen(random_image)

        pygame.display.update()

        clock.tick(60)


def save_sceen():
    surface1.fill((255, 255, 255))
    score_obj = Score(surface1, player_score)

    my_text_box2 = RewrittenTextbox(600, 80, 140, 32, color_passive, color_active, base_font, surface1, active)
    my_text_box2.draw()
    save_sceen_running = True
    clock = pygame.time.Clock()
    read_score = score_obj.load_file_score()
    hgh_obj = HighScoreClass(read_score, surface1)

    while save_sceen_running:

        # Pygame boiler code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    my_text_box2.catch_user_events(event)
                    user_input_word = my_text_box2.what_user_wrote()
                    hgh_obj.save_to_high_score_list(user_input_word)
                    very_last_sceen()

            my_text_box2.catch_user_events(event)

        my_text_box2.draw()

        my_text_box2.update()
        score_obj.show_value()
        score_obj.showing_score_save_sceen(read_score)
        pygame.display.update()

        clock.tick(60)


def very_last_sceen():
    surface1.fill((255, 255, 255))
    clock = pygame.time.Clock()
    score_obj = Score(surface1, player_score)
    read_score = score_obj.load_file_score()
    hgh2_obj = HighScoreClass(read_score, surface1)
    saved_score = True
    last_sceen_running = True

    while last_sceen_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    the_start_screen()

                if event.key == pygame.K_v:
                    # save_sceen()
                    high_score_screen()

                if event.key == pygame.K_a:
                    end_running = False
                    quit()

        hgh2_obj.show_the_end(saved_score)

        pygame.display.update()

        clock.tick(60)


def high_score_screen():
    surface1.fill((255, 255, 255))
    clock = pygame.time.Clock()
    score_obj = Score(surface1, player_score)
    read_score = score_obj.load_file_score()
    hgh2_obj = HighScoreClass(read_score, surface1)
    saved_score = True
    hgh2_obj.sort_high_score_list()
    hgh2_obj.show_high_score_on_screen()
    high_score_screen_running = True

    while high_score_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

        clock.tick(60)


def main():
    # Load up the start screen for the user.
    the_start_screen()


if __name__ == '__main__':
    main()
