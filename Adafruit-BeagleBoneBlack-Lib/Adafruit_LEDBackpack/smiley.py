#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight


grid = EightByEight(address=0x70)

smile_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11010010,0b11001100,0b00100001,0b00011110]
neutral_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11011110,0b11000000,0b00100001,0b00011110]
frown_bmp = [0b00011110,0b00100001,0b11010010,0b11000000,0b11001100,0b11010010,0b00100001,0b00011110]


# Write a smiley face
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
