import os
import argparse
from PIL import Image

def image_stats():
    parser = argparse.ArgumentParser(description=" This script will display image stats.")
    parser.add_argument('file_location', type=str, help="Takes location of the image as input.")

    args = parser.parse_args()

    file_location = os.path.dirname(__file__) + "\\" + args.file_location

    try:
        # Opens and displays stats for the img
        img = Image.open(file_location)
        print("Image was opened successfully...\n")
        print("Size: {:.2f}".format( os.stat(file_location).st_size / (1024*1024) ) + "MBs")
        print("Format: " + img.format)
        print("Resolution: " + str(img.size[0]) + " x " + str(img.size[1]))
        print("Total Characters that can be encoded: " + str((img.size[0]*img.size[1])-5))

    except:
        print("The file cannot be opened\n")
        exit()


image_stats()