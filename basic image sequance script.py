#basic script that takes a folder of images and renames them to a number based on the order they are in the folder
#this is useful for when you have a bunch of images that you want to rename to a number so you can use them in a video
#made by pumpkin

import os
import sys

#get imput from user
folder = input("Enter the filepath: ")

#check if the folder exists
if os.path.exists(folder):
    #get the files in the folder
    files = os.listdir(folder)
    #sort the files
    files.sort()
    #set the starting number
    i = 1
    #loop through the files
    for file in files:
        #get the file extension
        ext = os.path.splitext(file)[1]
        #rename the file
        os.rename(os.path.join(folder, file), os.path.join(folder, str(i) + ext))
        #increment the number
        i += 1
else:
    print("That folder does not exist")
    sys.exit()
