import os

print("Enter the name: ")
name = input()
path = os.getcwd()
one = "1"

hashed_name = one + name

os.mkdir(os.path.join(path, hashed_name)) # make new directory
os.chdir(os.path.join(path, hashed_name)) # navigate into new directory

new_path = os.getcwd() # update working directory

print("Place media file and subtitle(optional) file in new folder named " + name)
input("Press Enter to continue...")

filenames =  os.listdir(new_path)


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


os.chdir(path)
os.rename(hashed_name,name)

print("The following files have been renamed:")
print(os.listdir())