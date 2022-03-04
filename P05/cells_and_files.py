from random import randint, randrange

class Cell():
    def __init__(self, address):
        self.size_left = 2100
        self.address = address
        self.files = []

    def __str__(self):
        files = " | ".join(self.files)
        return f"*Memory cell#{self.address} Free Space -> {self.size_left}kb\n{files}"


class File():
    def __init__(self, n_file):
        self.n_file = "file" + str(n_file) + ".txt"
        self.size = randrange(500, 2101, 100)
        self.saved = [False, None]

    def __str__(self):
        return f"{self.n_file} Size -> {self.size}kb"