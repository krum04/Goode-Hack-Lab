import board #import the GPIO library
from time import sleep 
from adafruit_ht16k33.matrix import Matrix8x8 #import the matrix module

i2c = board.I2C() #define the i2c connection
matrix = Matrix8x8(i2c) #create our matrix instance 

matrix.fill(1) #All LEDs on
matrix.fill(0) #All LEDs off

while True: #Loop through all rows & columns 

    for i in range(8):
        for n in range(8):
            matrix[i,n] = 1
            sleep(.01)

    for i in range(8):
        for n in range(8):
            matrix[i,n] = 0
            sleep(.01)