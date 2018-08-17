import os
import sys

print("Enter the name: ")
name = input()
path = os.getcwd()

try:
    os.mkdir(os.path.join(path, name)) # make new directory
    os.chdir(os.path.join(path, name)) # navigate into new directory
except FileExistsError as err:
    print('This file exists already... Error Message:', err)
    print("Exiting...")
    sys.exit(1)

path = os.getcwd() # update working directory

filenames = os.listdir(path)

print("Place media file and subtitle(optional) file in new folder named " + name)
input("Press Enter to continue...")

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

print("The following files have been renamed:")
print(os.listdir())