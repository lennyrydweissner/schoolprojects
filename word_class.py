import random


class RandomWords:

    def __init__(self, words):
        self.words = words

    # Create a random word from the list
    def random_word(self):
        for start_image in range(22):
            randomized_word = random.choice(self.words)
            return randomized_word
