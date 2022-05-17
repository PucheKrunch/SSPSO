import threading as Thread
from random import choice
from time import sleep

frecuencies = [0.5, 1, 2]
lock = Thread.Lock()

class Writer(Thread.Thread):
    def run(self):
        while True:
            lock.acquire()
            frequency = choice(frecuencies)
            print("Writer {} is writing - Frequency: {}".format(Thread.current_thread().getName(), frequency))
            with open("data.txt", "r+") as data:
                number = int(data.read())
                print("Old data: {}".format(number))
                data.seek(0)
                data.write(str(number + 1))
                print("New data: {}".format(number + 1))                
                sleep(frequency)
                lock.release()

class Reader(Thread.Thread):
    def run(self):
        while True:
            frecuency = choice(frecuencies)
            lock.acquire()
            print("Reader {} is reading - Frecuency {}".format(Thread.current_thread().getName(), frecuency))
            with open("data.txt", "r") as data:
                number = int(data.read())
                print("Data: {}".format(number))
                lock.release()
                sleep(frecuency)

writer = Writer(name = 1)
writer2 = Writer(name = 2)
reader = Reader(name = 1)
reader2 = Reader(name = 2)
writer.start()
writer2.start()
reader.start()
reader2.start()