from tkinter import *
from PIL import ImageTk, Image
from os import *
from random import *
from time import sleep

root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(500, 500))
root.title("Wubi Practice")

def choose_shape():
    chdir("wubi_shapes")
    # Get list of letters
    letter_list = listdir()
    if ".DS_Store" in letter_list: letter_list.remove(".DS_Store")
    # Choose a letter
    letter = choice(letter_list)
    chdir(letter)
    # Get a list of shapes
    shape_list = listdir()
    if ".DS_Store" in shape_list: shape_list.remove(".DS_Store")
    # Choose a shape
    shape = choice(shape_list)
    # Exit directory twice
    chdir(pardir)
    chdir(pardir)

    return f'wubi_shapes/{letter}/{shape}'

shape_path = choose_shape()
shape_name = shape_path.split("/")[-1][0]
open_img = ImageTk.PhotoImage(Image.open(shape_path))
disp_img = Label(root, image = open_img)
disp_img.pack(side="top", fill="both", expand="yes")

def callback(event):
    global shape_name
    if event.keysym == shape_name:
        shape_path = choose_shape()
        shape_name = shape_path.split("/")[-1][0]
        new_img = ImageTk.PhotoImage(Image.open(shape_path))
        disp_img.configure(image = new_img)
        disp_img.image = new_img

root.bind('<Key>', callback)

root.mainloop()
