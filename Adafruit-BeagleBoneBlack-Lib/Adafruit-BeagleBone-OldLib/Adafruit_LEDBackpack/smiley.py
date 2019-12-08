#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import ColorEightByEight


grid = ColorEightByEight(address=0x70)

#smile_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11010010,0b11001100,0b00100001,0b00011110]
neutral_bmp = [ 0b1000000,0b0000000,0b0100100,0b0000000,0b0000000,0b0111100,0b0000000,0b0000000]
frown_bmp = [ 0b1000000,0b0000000,0b0100100,0b0000000,0b0000000,0b0111100,0b1000010,0b0000000]
smile_bmp = [0b1000000,0b0000000,0b0100100,0b0000000,0b1000010,0b1111110,0b0000000,0b0000000]



while True :
# Write a smiley face)


	for i in range(0,8):
       		grid.writeRowRaw(i, smile_bmp[i])
	time.sleep(.33)


     
# Write a neutral face
	for i in range(0,8):
     		grid.writeRowRaw(i, neutral_bmp[i])
	time.sleep(.33)
       
# Write a frown face
	for i in range(0,8):
 		grid.writeRowRaw(i, frown_bmp[i])
	time.sleep(.33)


