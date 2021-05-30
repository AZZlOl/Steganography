"""

    Py Program for the Steganography Implimentation (naive Approach)

"""
import os
from PIL import Image
import msvcrt as m


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
            # Opens and displays stats for the img
            self.img = Image.open(self.fileLoc)
            # print("Image was opened successfully...\n")
            # print(":-: Image Stats :-:\n")

            # print("Size: {:.2f}".format( os.stat(self.fileLoc).st_size / (1024*1024) ) + "MBs")
            # print("Format: " + self.img.format)

            # print("Resolution: " + str(self.img.size[0]) + " x " + str(self.img.size[1]))

            # print("\n\nPress any key to continue:\n")
            # m.getch()

        except:
            print("The file cannot be opened\n")
            exit()

    # End of __init__() -----------------------------------------------------------------------------------

    def encode(self, msg = "Sample Message"):
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
        # print(msgBi)
        for i in range(len(msgAscii)):
            binaryVal = bin(msgAscii[i]).replace("0b","")       # Gets Binary of the numbers

            if len(binaryVal) < 8:
                binaryVal = "0"*(8 - len(binaryVal)) + binaryVal    # padds to make 8 bits
            msgBi.append(binaryVal)
        # print(msgBi)


        # Divides the binary into 3 parts of 2:3:3 and stores in 3 different list
        r = list()
        g = list()
        b = list()
        i = 0

        for y in range(self.img.size[1]):
            # Exit when the Original message length have been inserted
            if i == len(msg):
                break
            # New List for every row of the img
            r.append([])
            g.append([])
            b.append([])

            for x in range(self.img.size[0]):
                # Exit when the Original message length have been inserted
                if i == len(msg):
                    break

                # Append the bits into the specific sublists
                r[y].append(msgBi[i][:2])
                g[y].append(msgBi[i][2:5])
                b[y].append(msgBi[i][5:])
                i += 1



        print(msgBi)
        # print(r)
        # print(g)
        # print(b)


        # Inserting the Bits into the pixels
        i = 0
        for y in range(self.img.size[1]):
            # Exit when the Original message length have been inserted
            if i == len(msg):
                break

            for x in range(self.img.size[0]):
                # Exit when the Original message length have been inserted
                if i == len(msg):
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


        self.img.save(os.path.dirname(__file__)+"\\"+"file.png")
        print("Image was saved at: "+str(os.path.dirname(__file__)+"\\"+"file.png"))
        # self.img.show()
        m.getch()


    def decode(self):
        # self.img.show()

        # Get the length of the message
        msgLen = ""
        for i in range(5):
            temp = self.img.getpixel((i,0))
            msgLen = msgLen + bin(temp[0]).replace("0b","")[6:] + bin(temp[1]).replace("0b","")[5:] + bin(temp[2]).replace("0b","")[5:]
        length = int(msgLen,2)
        # print(length)

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
        
        

        # Converts the 8 bits to Characters
        charAscii = [ chr(int(x,2)) for x in msg ]

        # Output String
        op = ""
        for i in range(len(charAscii)):
            if i < 5:
                continue
            op = op + charAscii[i]

        print(op)

            



s = Steganography("test.png")
s.encode("Hellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo ThereHellqo Yoyoyoyoyoyo There")

s = Steganography("file.png")
s.decode()
