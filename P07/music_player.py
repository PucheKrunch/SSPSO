from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import pygame
from random import shuffle
import time
from mutagen.mp3 import MP3

global playlist
playlist = []
global paused
paused = False
global stopped
stopped = False

root = Tk()
root.title("Music Player")
root.geometry("500x375")
root.resizable(False, False)
root.configure(background='#2a2a2a')

#Pygame mixer
pygame.mixer.init()

#Functions

#Slide bar
def slide(x):
    song = song_box.get(ACTIVE)
    song = f"music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))

#Song playing time
def play_time():
    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000

    format_time = time.strftime("%M:%S", time.gmtime(current_time))

    current_song = song_box.curselection()
    song = song_box.get(current_song)
    song_mut = MP3(f"music/{song}.mp3")
    global total_time
    total_time = song_mut.info.length
    format_total_time = time.strftime("%M:%S", time.gmtime(total_time))
    current_time += 1

    if int(slider.get()) == int(total_time):
        next_song()
    elif paused:
        pass
    elif int(slider.get()) == int(current_time):
        slider.configure(to=total_time, value=int(current_time))
    else:
        slider.configure(to=total_time, value=int(slider.get()))
        format_time = time.strftime("%M:%S", time.gmtime(int(slider.get())))
        status_bar.configure(text=f"{format_time}/{format_total_time}")
        next_time = int(slider.get()) + 1
        slider.configure(value=next_time)

    #update
    status_bar.after(1000, play_time)

#Add song
def add_song():
    song = filedialog.askopenfilename(initialdir="music/", title="Seleccionar canción", filetypes=(("mp3 files", "*.mp3"), ))
    playlist.append(song)
    song = song.split("/")[-1].split(".")[0]
    song_box.insert(END, song)

#Add many songs
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="music/", title="Seleccionar canción", filetypes=(("mp3 files", "*.mp3"), ))
    for song in songs:
        playlist.append(song)
        song = song.split("/")[-1].split(".")[0]
        song_box.insert(END, song)

#Delete selected song
def delete_song():
    song = song_box.get(ACTIVE)
    index = song_box.curselection()[0]
    song_box.delete(ACTIVE)
    playlist.pop(index)

#Delete all songs
def delete_all_songs():
    song_box.delete(0, END)
    playlist.clear()
    pygame.mixer.music.stop()

#Play selected song
def play_song(is_paused):
    global stopped
    global paused
    stopped = False
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        stopped = False
        pause_button['state'] = 'normal'
    else:
        song = song_box.curselection()
        song = song_box.get(song)
        pygame.mixer.music.load(f"music/{song}.mp3")
        pygame.mixer.music.play(loops=0)
    play_button['state'] = 'disabled'
    play_time()

#Play the previous song
def prev_song():
    previous_index = song_box.curselection()[0] - 1
    song_box.selection_clear(ACTIVE)
    if previous_index == -1:
        previous_index = len(playlist) - 1
    song = playlist[previous_index]
    song_box.activate(previous_index)
    song_box.selection_set(previous_index)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    slider.configure(to=total_time, value=0)

#Play the next song
def next_song():
    next_index = song_box.curselection()[0] + 1
    song_box.selection_clear(ACTIVE)
    if next_index == len(playlist):
        next_index = 0
    song = playlist[next_index]
    song_box.activate(next_index)
    song_box.selection_set(next_index)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    slider.configure(to=total_time, value=0)

#Shuffle playlist
def shuffle_playlist():
    shuffle(playlist)
    song_box.delete(0, END)
    for song in playlist:
        song = song.split("/")[-1].split(".")[0]
        song_box.insert(END, song)
    song_box.activate(0)
    song_box.selection_set(0)
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(f"music/{song}.mp3")
    pygame.mixer.music.play(loops=0)
    slider.configure(to=MP3(f"music/{song}.mp3").info.length, value=0)
    play_button['state'] = 'disabled'
    play_time()

#Stop playing song
def stop_song():
    global stopped
    stopped = True
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar.configure(text="")
    slider.configure(value=0)
    play_button['state'] = 'normal'

#Pause playing song
def pause_song(is_paused):
    global stopped
    global paused
    paused = is_paused
    stopped = True
    pygame.mixer.music.pause()
    paused = True
    play_button['state'] = 'normal'
    pause_button['state'] = 'disabled'

#Playlist box
song_box = Listbox(root, bg="black", fg="white", width=70, selectbackground="grey", selectforeground="white")
song_box.configure(border=0)
song_box.pack(pady=20)

#Player control buttons icons
back_button_img = PhotoImage(file="icons/back.png")
forward_button_img = PhotoImage(file="icons/next.png")
play_button_img = PhotoImage(file="icons/play.png")
pause_button_img = PhotoImage(file="icons/pause.png")
stop_button_img = PhotoImage(file="icons/stop.png")
shuffle_button_img = PhotoImage(file="icons/shuffle.png")

#Progress bar
style = ttk.Style()
style.configure("TScale", background="#0f111a")
slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360, style="TScale")
slider.pack(pady=20)

#Create Player control frame
controls_frame = Frame(root)
controls_frame.configure(background='#5f5f5f')
controls_frame.pack()

#Player control buttons
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, background='#5f5f5f', command=prev_song)
forward_button = Button(controls_frame, image=forward_button_img, borderwidth=0, background='#5f5f5f', command=next_song)
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, background='#5f5f5f', command=lambda:play_song(paused))
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0, background='#5f5f5f', command=lambda: pause_song(paused))
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, background='#5f5f5f', command=stop_song)
shuffle_button = Button(controls_frame, image=shuffle_button_img, borderwidth=0, background='#5f5f5f', command=shuffle_playlist)

back_button.grid(row=0, column=0, padx=5)
forward_button.grid(row=0, column=1, padx=5)
play_button.grid(row=0, column=2, padx=5)
pause_button.grid(row=0, column=3, padx=5)
stop_button.grid(row=0, column=4, padx=5)
shuffle_button.grid(row=0, column=5, padx=5)

#Status bar
status_bar = Label(root, text="", bd=1, relief=SUNKEN, anchor=W, background='#0c0e15', foreground='white')
status_bar.pack(side=BOTTOM, fill=X, ipady=2)

#Create menu bar
my_menu = Menu(root)
root.config(menu=my_menu)

#Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Agregar Canciones", menu=add_song_menu)
add_song_menu.add_command(label="Agregar 1 Cancion", command=add_song)

#Add many songs menu
add_song_menu.add_command(label="Agregar varias Canciones", command=add_many_songs)

#Delete song menu
delete_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Eliminar Canciones", menu=delete_song_menu)
delete_song_menu.add_command(label="Eliminar 1 Cancion", command=delete_song)
delete_song_menu.add_command(label="Eliminar todas las Canciones", command=delete_all_songs)

root.mainloop()