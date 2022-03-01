from random import choice

class Cell():
    def __init__(self, address):
        self.max_size = 2100
        self.size_left = 2100
        self.address = address


class File():
    def __init__(self, n_file):
        self.n_file = "file" + str(n_file) + ".txt"
        self.size = choice([500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100])
        self.saved = [False, None]