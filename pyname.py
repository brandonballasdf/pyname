import os
from tkinter import *
from tkinter.messagebox import showerror

def make_folder():
    error = "This directory already exists"
    name_of_movie = movie.get() # gets value from tkinter entry box
    path = os.getcwd() # saves current working directory

    try:
        os.mkdir(os.path.join(path, name_of_movie)) # make new directory
    except:
        showerror("D'Oh", message=str(error))

    os.chdir(os.path.join(path, name_of_movie)) # navigate into new directory

    path = os.getcwd() # update working directory
    os.startfile(path) # opens folder created

def rename_files():
    path = os.getcwd() # saves current working directory
    filenames =  os.listdir(path) #saves filenames in directory as tuple
    name = movie.get() # gets value from tkinter entry box

    for filename in filenames: # for loop searches for key file extensions and renames according to user input

        if filename.endswith('.srt'): # renames subtitle file
            dst = name + '.srt'
            os.rename(filename, dst)

        elif filename.endswith('.mp4'): # renames .mp4 file
            dst = name + '.mp4'
            os.rename(filename, dst)

        elif filename.endswith('.avi'): # renames .avi file
            dst = name + '.avi'
            os.rename(filename, dst)

        elif filename.endswith('.mkv'): # renames .mkv file
            dst = name + '.mkv'
            os.rename(filename, dst)

    os.chdir('..') # backs out to root media folder, back to back folders made become nested if this is taken out

root = Tk() # init tkinter

root.title("pyname") # title bar name
root.geometry("300x100") # window size

menubar = Menu(root) # init tkinter menubar
root.config(menu=menubar) # set as menubar

filemenu = Menu(menubar) # init file menu cascade from menubar
menubar.add_cascade(label='File', menu=filemenu) #  file menu

filemenu.add_command(label='Quit', command=sys.exit) # file menu quit command


label1 = Label(root, text = "Enter the name of the movie:")
movie = Entry(root)
movie.focus()
createfolderbutton = Button(root, text = "Create Folder and Open", command=make_folder)
label2 = Label(root, text = "Move media and select")
renamebutton = Button(root, text = "This Button", command=rename_files)
label1.grid(row=0,column=0)
movie.grid(row=0,column=1)
createfolderbutton.grid(row=1,column=0)

label2.grid(row=5,column=0)
renamebutton.grid(row=5,column=1)
root.mainloop()
