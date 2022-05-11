import time
from tkinter import *
from random import choice
from threading import Thread

#Button control for increasing input time
def input_time_add():
    global speeds
    try:
        time = speeds[speeds.index(float(label_input.cget("text"))) + 1]
    except IndexError:
        time = speeds[0]
    label_input.config(text=time)

#Button control for decreasing input time
def input_time_sub():
    global speeds
    if speeds.index(float(label_input.cget("text"))) == 0:
        time = speeds[-1]
    else:
        time = speeds[speeds.index(float(label_input.cget("text"))) - 1]
    label_input.config(text=time)

#Button control for increasing output time
def output_time_add():
    global speeds
    try:
        time = speeds[speeds.index(float(label_output.cget("text"))) + 1]
    except IndexError:
        time = speeds[0]
    label_output.config(text=time)

#Button control for decreasing output time
def output_time_sub():
    global speeds
    if speeds.index(float(label_output.cget("text"))) == 0:
        time = speeds[-1]
    else:
        time = speeds[speeds.index(float(label_output.cget("text"))) - 1]
    label_output.config(text=time)

#Car entry Thread
class Entry_thread(Thread):
    def run(self):
        while True:
            if int(counter.cget("text")) < 12:
                print("Carro entra")
                counter.config(text=str(int(counter.cget("text")) + 1))
                print(float(label_input.cget("text")))
                time.sleep(float(label_input.cget("text")))
            else:
                print("Carro no lugar")
                time.sleep(float(label_input.cget("text")))

#Car exit Thread
class Exit_thread(Thread):
    def run(self):
        while True:
            if int(counter.cget("text")) > 0:
                print("Carro sale")
                counter.config(text=str(int(counter.cget("text")) - 1))
                print(float(label_output.cget("text")))
                time.sleep(float(label_output.cget("text")))
            else:
                time.sleep(float(label_output.cget("text")))

#Main function
def main():
    entry = Entry_thread()
    exit = Exit_thread()
    entry.start()
    exit.start()

#Initializing speeds
speeds = [0.5,1,2]
input_speed = choice(speeds)
output_speed = choice(speeds)

#Configure window
root = Tk()
root.title("Parking lot")
root.geometry("300x400")
root.resizable(False, False)

#Ifo labels
Label(root, text="Input speed:", font=("Arial", 20)).pack()
div1 = Frame(root, pady=15)
div1.pack()
Label(root, text="Output speed:", font=("Arial", 20)).pack()
div2 = Frame(root, pady=15)
div2.pack()
Label(root, text="Parking lot:", font=("Arial", 20)).pack()
counter = Label(root, text="0", font=("Arial", 20))
counter.pack()

#Input and output time labels
label_input = Label(div1, text=input_speed, font=("Arial", 20), width=5)
label_input.grid(row=0, column=1)
label_output = Label(div2, text=output_speed, font=("Arial", 20), width=5)
label_output.grid(row=0, column=1)

#Input time buttons
input_add = Button(div1, text="+", command=input_time_add, font=("Arial", 20))
input_add.grid(row=0, column=2)
input_sub = Button(div1, text="-", command=input_time_sub, font=("Arial", 20))
input_sub.grid(row=0, column=0)

#Output time buttons
output_add = Button(div2, text="+", command=output_time_add, font=("Arial", 20))
output_add.grid(row=0, column=2)
output_sub = Button(div2, text="-", command=output_time_sub, font=("Arial", 20))
output_sub.grid(row=0, column=0)

#Execute main function (Threads)
root.after(1000, main)
root.mainloop()