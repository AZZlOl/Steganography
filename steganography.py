"""

    Py Program for the Steganography Implimentation (naive Approach)

"""
import os
from PIL import Image
import msvcrt as m
import argparse


class Steganography:
    def __init__(self, fileName = "sample.jpeg"):
        
        os.system('cls')

        self.fileName = fileName
        
        # If No File name is given, then take sample.jpg
        if self.fileName == "sample.jpeg":
            print("Sample file is being used. File Name: \"sample.jpeg\"")
        
        # Makes absolute URL for the file
        self.fileLoc = os.path.dirname(__file__) + "\\" + self.fileName

        try:
            # print(self.fileLoc)
            # Opens and displays stats for the img
            self.img = Image.open(self.fileLoc)
            # print("Image was opened successfully...\n")
            # print(":-: Image Stats :-:\n")

            # print("Size: {:.2f}".format( os.stat(self.fileLoc).st_size / (1024*1024) ) + "MBs")
            # print("Format: " + self.img.format)
            # print("Resolution: " + str(self.img.size[0]) + " x " + str(self.img.size[1]))
            # print("Total Characters that can be encoded: " + str((self.img.size[0]*self.img.size[1])-5))

            # print("\n\nPress any key to continue:")
            # m.getch()

        except:
            print("Python Script Exception: The file cannot be opened\n")
            exit()

    # End of __init__() -----------------------------------------------------------------------------------

    def encode(self, msg = "Sample Message", output_file_name="encoded_image.png"):
        # Converts pixels in RGB VALS || use self.imgRGB.getpixel((x,y))
        # self.imgRGB = self.img.convert("RGB")


        msg = list(msg)
        # print(msg)

        # If the message is larger than img pixel count - 5
        if len(msg) > (self.img.size[0] * self.img.size[1])-5:
            print("Message is too long for this image")
            exit()


        
        # Message Length to binary 5 chars
        msgLen = bin(len(msg)).replace("0b","")     # Gets binary number
        if len(msgLen) < 40:
            msgLen = "0"*(40-len(msgLen)) + msgLen      # adds padding bits to make 40 chars
        msgLen = " ".join(msgLen[i:i + 8] for i in range(0, len(msgLen), 8))        # Divides into 8 bits
        msgLen = msgLen.split()
        # print(msgLen)



        # Converts the message to ASCII and stores in msgAscii list
        msgAscii = [ord(i) for i in msg]


        # Converts the ASCII to Binary and appends to msgBi list
        msgBi = list(msgLen)
        # print(len(msgBi))
        for i in range(len(msgAscii)):
            binaryVal = bin(msgAscii[i]).replace("0b","")       # Gets Binary of the numbers

            if len(binaryVal) < 8:
                binaryVal = "0"*(8 - len(binaryVal)) + binaryVal    # padds to make 8 bits
            msgBi.append(binaryVal)
        # print(len(msgBi))


        # Divides the binary into 3 parts of 2:3:3 and stores in 3 different list
        r = list()
        g = list()
        b = list()
        i = 0

        for y in range(self.img.size[1]):
            # Exit when the Original message length have been inserted
            if i == len(msgBi):
                break
            # New List for every row of the img
            r.append([])
            g.append([])
            b.append([])

            for x in range(self.img.size[0]):
                # Exit when the Original message length have been inserted
                if i == len(msgBi):
                    break

                # Append the bits into the specific sublists
                r[y].append(msgBi[i][:2])
                g[y].append(msgBi[i][2:5])
                b[y].append(msgBi[i][5:])
                i += 1


        # Inserting the Bits into the pixels
        i = 0
        for y in range(self.img.size[1]):
            # Exit when the Original message length have been inserted
            if i == len(msgBi):
                break

            for x in range(self.img.size[0]):
                # Exit when the Original message length have been inserted
                if i == len(msgBi):
                    break
                

                # Takes Pixel value, converts into binary
                rgb = list(self.img.getpixel((x,y)))
                rgbBi = [ bin(rgb[0]).replace("0b",""), bin(rgb[1]).replace("0b",""), bin(rgb[2]).replace("0b","") ]

                # New Values are put in and converted into decimal
                newR = int(rgbBi[0][:6] + r[y][x], 2)
                newG = int(rgbBi[1][:5] + g[y][x], 2)
                newB = int(rgbBi[2][:5] + b[y][x], 2)

                self.img.putpixel((x,y),(newR, newG, newB))

                # Append the bits into the specific sublists
                i += 1

        output_file_location = os.path.dirname(__file__)+"\\encoded_images\\"

        if not os.path.exists(output_file_location):
            os.makedirs(output_file_location)

        self.img.save(output_file_location + output_file_name)
        # print("Image was saved at: " + output_file_location + output_file_name)
        # self.img.show()
        # m.getch()

    
    # End of encode() -----------------------------------------------------------------------------------

    
    def decode(self):
        # self.img.show()

        # Get the length of the message
        msgLen = ""
        for i in range(5):
            temp = self.img.getpixel((i,0))
            msgLen = msgLen + bin(temp[0]).replace("0b","")[6:] + bin(temp[1]).replace("0b","")[5:] + bin(temp[2]).replace("0b","")[5:]
        length = int(msgLen,2)
        length += 5
        # print("Message Length is "+str(length-5)+" chars")

        i = 0
        msg = list()
        for y in range(self.img.size[1]):
            if i == length:
                break
            for x in range(self.img.size[0]):
                if i == length:
                    break
                pixel = self.img.getpixel((x,y))
                msg.append(bin(pixel[0]).replace("0b","")[6:] + bin(pixel[1]).replace("0b","")[5:] + bin(pixel[2]).replace("0b","")[5:])
                i+=1
        # print(msg)
        print("here")
        
        

        # Converts the 8 bits to Characters
        charAscii = [ chr(int(x,2)) for x in msg ]
        # print(charAscii)
        
        print("here")
        # Output String
        op = ""
        for i in range(len(charAscii)):
            if i < 5:
                continue
            op = op + charAscii[i]
            
        print("here")

        print("Message: " + op)

            

# s = Steganography(input("Enter file name (with extension): "))
# s.encode(input("Enter a Message to Encode: "))

# s = Steganography(input("Enter File name (with Extension): "))
# s.decode()

def cla_handler():
    parser = argparse.ArgumentParser(description=" This script will embed data in an image")
    parser.add_argument('mode', type=str, help="Takes 'e'ncode or 'd'ecode as input.")
    parser.add_argument('file_location', type=str, help="Takes location of the image as input.")
    parser.add_argument('--output_file_name', type=str, help="Takes the name of the output file.")
    parser.add_argument('--msg', type=str, help="Only used when mode is 'e'.")

    args = parser.parse_args()

    mode = args.mode
    msg = args.msg
    file_location = args.file_location
    output_file_name = args.output_file_name

    if mode == 'e' or mode == 'd':
        if mode == 'e':
            s = Steganography(file_location)
            s.encode(msg, output_file_name)
        else:
            s = Steganography(file_location)
            s.decode()

    else:
        print("Invalid 'mode' selected. mode only takes 'e'ncode or 'd'ecode as input.")




cla_handler()