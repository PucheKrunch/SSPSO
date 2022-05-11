import threading
import time
from tkinter import *
from random import choice

# Shared Memory variables
CAPACITY = 12
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0

# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

# entry Thread Class


class Entry(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full, items_produced

        items_produced = 0
        counter = 0

        while items_produced < 20:
            empty.acquire()
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY

            mutex.release()
            full.release()

            time.sleep(1)

            items_produced += 1
            print("Capacity:", items_produced)

# exit Thread Class


class Exit(threading.Thread):
    def run(self):

        global CAPACITY, buffer, in_index, out_index, counter
        global mutex, empty, full, items_produced

        items_consumed = 0

        while items_consumed < 20:
            full.acquire()
            mutex.acquire()

            item = buffer[out_index]
            out_index = (out_index + 1) % CAPACITY

            mutex.release()
            empty.release()

            time.sleep(1)

            items_produced -= 1
            print("Capacity:", items_produced)


# Creating Threads
entry = Entry()
exit = Exit()

# Starting Threads
exit.start()
entry.start()

# Waiting for threads to complete
entry.join()
exit.join()
