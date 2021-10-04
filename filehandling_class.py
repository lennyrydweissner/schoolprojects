class MyFileHandling:

    def __init__(self, filepath_from_main):
        animal_list = []
        self.filepath_from_main = filepath_from_main
        self.animal_list = animal_list

    def read_the_file_animal_list(self):
        tf = open(self.filepath_from_main, "r", encoding="utf-8")
        self.animal_list = tf.readlines()
        tf.close()
        return self.animal_list

    # This method is for development purpose
    # just want to se if i can print a word from the file.
    def print_content(self):
        random_word = (self.animal_list[2])
        return random_word