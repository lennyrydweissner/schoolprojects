import pygame
import math
import sys
from class_intro import Intro

# create Intro object
intro_object = Intro()
intro_object.play_music()
game_running = True


def main():
    while game_running:
        intro_object.load_start_images()
        intro_object.fill_the_screen()

        # Pygame boiler code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # updates the screen
        pygame.display.update()


if __name__ == '__main__':
    main()
