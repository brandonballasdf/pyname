import os
import msvcrt as keypress

name = input("Enter the name: ")
path = os.getcwd()

os.mkdir(os.path.join(path, name)) # make new directory
os.chdir(os.path.join(path, name)) # navigate into new directory

path = os.getcwd() # update working directory

print("Place media file and subtitle(optional) file in new folder folder\n")
input("Press Enter to continue...")

filenames = os.listdir(path)

for filename in filenames:
    if filename[-4] == '.srt'
        dst = name + '.srt'
        os.rename(filename, dst)

    if filename[-4] == '.mp4'
        dst = name + '.mp4'
        os.rename(filename, dst)

    if filename[-4] == '.avi'
        dst = name + '.avi'
        os.rename(filename, dst)

print("The following files have been renamed:\n\n")
os.listdir()
    