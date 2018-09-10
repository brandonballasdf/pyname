import os, imp
import subprocess
from tkinter import *
import tkinter.simpledialog as simpledialog


def make_folder():
    name_of_movie = movie.get()
    path = os.getcwd()

    os.mkdir(os.path.join(path, name_of_movie)) # make new directory
    os.chdir(os.path.join(path, name_of_movie)) # navigate into new directory

    path = os.getcwd()
    os.startfile(path)

def rename_files():
    path = os.getcwd()
    filenames =  os.listdir(path)
    name = movie.get()

    for filename in filenames: # for loop searches for key file extensions and renames according to user input

        if filename.endswith('.srt'):
            dst = name + '.srt'
            os.rename(filename, dst)

        elif filename.endswith('.mp4'):
            dst = name + '.mp4'
            os.rename(filename, dst)

        elif filename.endswith('.avi'):
            dst = name + '.avi'
            os.rename(filename, dst)

        elif filename.endswith('.mkv'):
            dst = name + '.mkv'
            os.rename(filename, dst)

    os.chdir('..')


root = Tk()

root.title("pyname")
root.geometry("300x100")

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='Quit', command=sys.exit)


label1 = Label(root, text = "Enter the name of the movie:")
movie = Entry(root)
createfolderbutton = Button(root, text = "Create Folder and Open", command=make_folder)
label2 = Label(root, text = "Move media and select")
renamebutton = Button(root, text = "This Button", command=rename_files)
label1.grid(row=0,column=0)
movie.grid(row=0,column=1)
createfolderbutton.grid(row=1,column=0)

label2.grid(row=5,column=0)
renamebutton.grid(row=5,column=1)
root.mainloop()