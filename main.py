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

# Variables that i need goes here:
mx = 0  # This is the mouse tracker start coordinate x
my = 0  # This is the mouse tracker start coordinate y
black_color = (255, 255, 255)  # Black background color
sc_x = 1550  # Screen size in x
sc_y = 800  # Screen size in y
path_to_word_file = "bildfilen.txt"  # Filepath to the file with all words.

# Make the pygame screen
surface1 = pygame.display.set_mode((sc_x, sc_y))

# Loading up my buttons to the game:
start_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Starta.png")
stopp_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Avsluta.png")
main_meny_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Huvud meny.png")
turn_off_music_img = pygame.image.load(
    "C:\This is what i use to github stavningsleken/meny bilder/Stäng av musiken.png")
turn_on_music_img = pygame.image.load("C:\This is what i use to github stavningsleken/meny bilder/Sätt på musiken.png")

# Loading start screen images here.
main_logo_start_screen_img = pygame.image.load(
    "C:\This is what i use to github stavningsleken/start_bilder/Stavningsleken_logo.png")
start_the_game_img = pygame.image.load("C:\This is what i use to github stavningsleken/start_bilder/Starta spelet.png")
end_the_game_img = pygame.image.load("C:\This is what i use to github stavningsleken/start_bilder/Avsluta spelet.png")

# Button instances goes here
stopp_music_button = Button(30, 65, turn_off_music_img)
turn_on_music_button = Button(30, 120, turn_on_music_img)
main_meny_button = Button(30, 15, main_meny_img)
stopp_button = Button(30, 180, stopp_img)
start_button = Button(570, 385, start_img)

# Start Screen button instances goes here
main_logo_button = Button(460, 30, main_logo_start_screen_img)
start_the_game_button = Button(460, 150, start_the_game_img)
end_the_game_button = Button(460, 250, end_the_game_img)

# creates all my instances here
intro_object = Intro(surface1, black_color)
mouse_cords_tracker = MouseCords(mx, my)  # Not gonna use this then the game is done. just in development phase
read_my_file = MyFileHandling(path_to_word_file)

game_running = True


def the_start_screen():
    start_screen_running = True

    # intro_object.play_music()

    while start_screen_running:
        surface1.fill((255, 255, 255))

        if main_logo_button.draw_button_to_screen(surface1):
            pass

        if start_the_game_button.draw_button_to_screen(surface1):
            main_game_loop()
            # print("Nu skall du starta spelet")

        if end_the_game_button.draw_button_to_screen(surface1):
            # Ends the whole game here
            start_screen_running = False

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


def main_game_loop():
    global game_running
    game_running = True
    # Starts playing the music here.
    intro_object.play_music()

    # Start the intro scene on screen
    intro_object.load_start_images()
    intro_object.fill_the_screen()

    # Creating an instance off random picture class
    rnd_obj = RandomPictureGenerator(surface1)

    chosen_random_word = rnd_obj.random_image_generator()

    # Getting the list of all words
    collected_list = read_my_file.read_the_file_animal_list()

    # Getting a random word from the collected_list
    selected_word = RandomWords(collected_list)


    while game_running:

        if main_meny_button.draw_button_to_screen(surface1):
            pass

        if stopp_music_button.draw_button_to_screen(surface1):
            intro_object.stop_music()

        if turn_on_music_button.draw_button_to_screen(surface1):
            intro_object.play_music()

        if stopp_button.draw_button_to_screen(surface1):
            game_running = False

        if start_button.draw_button_to_screen(surface1):
            # Gets a random word from the line_list in class method random_image_generator
            random_word = rnd_obj.random_image_generator()

            # Load upp the image who is corresponding to the random word we got above
            random_image = rnd_obj.display_next_image(random_word)

            # Show the image on the screen.
            rnd_obj.display_screen(random_image)

        # Pygame boiler code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Hunting the mouse cords. (need this for placing the buttons on the screen)
            # mouse_cords_tracker.hunt_cords()
            # mouse_cords_tracker.write_out_cords()

            # Prints out the word i selected.
            collected_word = read_my_file.print_content()
            choosen_random_word = selected_word.random_word()

        # updates the screen
        pygame.display.update()


def main():
    the_start_screen()


if __name__ == '__main__':
    main()
