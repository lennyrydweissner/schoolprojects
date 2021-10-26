import unittest
import pygame
from class_intro import Intro
from random_picture_class import RandomPictureGenerator
from score_class import Score


def dry_function():
    sc_x = 1450  # Screen size in x
    sc_y = 800  # Screen size in y
    black_color = (255, 255, 255)
    surface1 = pygame.display.set_mode((sc_x, sc_y))
    return sc_x, sc_y, surface1


class MyTestCase(unittest.TestCase):

    def test_is_music_playing(self):
        surface1 = dry_function()
        black_color = (255, 255, 255)
        check_status = 100
        self.check_status = check_status
        self.i1_obj = Intro(surface1, black_color)
        self.check_status = self.i1_obj.play_music()

        self.assertEqual(1, self.check_status)  # add assertion here
        self.i1_obj.stop_music()  # Stops music, so i dont have to listen through the other tests.

    def test_has_music_stopped(self):
        surface1 = dry_function()
        black_color = (255, 255, 255)
        check_status = 10  # rnd start value, so we know if the method is working by getting the right value
        self.check_status = check_status
        self.i1_obj = Intro(surface1, black_color)
        self.check_status = self.i1_obj.stop_music()
        self.assertEqual(1, self.check_status)

    def testing_if_applauds_sounds_working(self):
        surface1 = dry_function()
        black_color = (255, 255, 255)
        check_status = 0
        self.check_status = check_status
        self.i1_obj = Intro(surface1, black_color)
        self.check_status = self.i1_obj.applauds_sound()
        self.assertEqual(1, self.check_status)

    def testing_wrong_answer_sound(self):
        surface1 = dry_function()
        black_color = (255, 255, 255)
        check_status = 0
        self.check_status = check_status
        self.i1_obj = Intro(surface1, black_color)
        self.check_status = self.i1_obj.wrong_answer_sound()
        self.assertEqual(1, self.check_status)

    def testing_if_the_start_image_is_working(self):
        surface1 = dry_function()
        black_color = (255, 255, 255)
        check_status = 0
        self.check_status = check_status
        self.i1_obj = Intro(surface1, black_color)
        self.check_status = self.i1_obj.load_start_images()
        self.assertEqual(1, self.check_status)

    def testing_that_list_is_populated_from_random_picture_class(self):
        surface1 = dry_function()
        test_list = []
        check_status = []
        list_status = False

        self.test_list = test_list
        self.check_status = check_status
        self.list_status = list_status

        self.rnd_test_obj = RandomPictureGenerator(surface1)
        self.check_status = self.rnd_test_obj.load_list_to_pick_random_word_from()
        self.test_list = self.check_status

        if not self.test_list == []:
            self.list_status = True
        else:
            self.list_status = False

        self.assertEqual(True, self.list_status)  # add assertion here

    def testing_that_it_works_to_get_a_random_word(self):
        surface1 = dry_function()
        random_word = ""
        status = False

        self.status = status
        self.random_word = random_word
        self.rnd_test_obj = RandomPictureGenerator(surface1)
        self.rnd_test_obj.load_list_to_pick_random_word_from()
        self.rnd_test_obj.get_computer_randomized_word_from_list()
        self.random_word = self.rnd_test_obj.get_computer_randomized_word_from_list()

        if not self.random_word == "":
            self.status = True
            # print(self.random_word)
        else:
            self.status = False

        self.assertEqual(True, self.status)  # add assertion here

    def testing_check_so_it_load_next_random_image(self):
        surface1 = dry_function()
        random_word = ""
        random_picture_value = 0
        status = False

        self.random_word = random_word
        self.random_picture_value = random_picture_value
        self.status = status

        self.rnd_test_obj = RandomPictureGenerator(surface1)
        self.rnd_test_obj.load_list_to_pick_random_word_from()

        self.random_word = self.rnd_test_obj.get_computer_randomized_word_from_list()
        self.random_picture_value = self.rnd_test_obj.display_next_image(self.random_word)

        if not self.random_picture_value == "":
            self.status = True

        else:
            self.status = False

        self.assertEqual(True, self.status)

    def testing_to_add_score_from_score_class(self):
        surface1 = dry_function()
        player_score = 100
        fetched_score = 0

        self.player_score = player_score
        self.fetched_score = fetched_score
        self.test_score_obj = Score(surface1, player_score)
        self.player_score = self.test_score_obj.show_value()
        self.fetched_score = self.test_score_obj.adding_score()
        self.assertNotEqual(self.player_score, self.fetched_score)

    def testing_to_show_value_class(self):
        surface1 = dry_function()
        value = 0
        player_score = 0
        fetched_value = 0

        self.value = value
        self.player_score = player_score
        self.fetched_value = fetched_value

        self.test_score_obj = Score(surface1, player_score)
        self.test_score_obj.adding_score()
        self.fetched_value = self.test_score_obj.show_value()
        self.assertNotEqual(0, self.fetched_value)


if __name__ == '__main__':
    unittest.main()
