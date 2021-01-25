import board
from time import sleep
from adafruit_ht16k33.matrix import Matrix8x8
from PIL import Image

#Setup i2c connection and matrix object
i2c = board.I2C()
matrix = Matrix8x8(i2c)

#Take user input and loop through the individual characters and display
#correlating png
while True:
    string = input("what would you like to say?")
    for letter in string: 
        if letter == ' ': #if space pause
            sleep(.25)
        else:
            image = Image.open(r"{}.png".format(letter.lower()))
            matrix.image(image)
            for i in range(8):
                matrix.shift_right()
                sleep(.1)

    matrix.fill(1)
