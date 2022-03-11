"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from ulab import numpy as np
pixel_pin = board.A0

Button = DigitalInOut(board.A1)
Button.direction = Direction.INPUT
Button.pull = Pull.UP


num_pixels = 398

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def remap_fatten(A):
    x = [0] * 298
    for i in range(0,10):
        if not i % 2 == 0:
            flip = [0] * 30
            for j in range(0, 30):
                flip[j] = A[j][i]
            fliped = flip[::-1]
            for j in range(0, 30):
                A[j][i] = fliped[j]

    for i in range(0,10):
            for j in range(0,30):
                if (i * 30 + j) < 209:
                    print(i * 30 + j, i, j)
                    x[i * 30 + j] = A[j][i]
                elif (i * 30 + j) > 209 and (i * 30 + j) < 299:
                    x[i * 30 + j-1] = A[j][i]

    return x

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (200, 0, 0)
YELLOW = (200, 100, 0)
GREEN = (0, 200, 0)
CYAN = (0, 200, 200)
BLUE = (0, 0, 200)
PURPLE = (120, 0, 200)
WHITE = (180, 180, 180)
A = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

for i in range(0,30, 10):
    for j in range(0,10):
        A[i][j] = (255, 0, 0)
        A[i+1][j] = (255, 0, 0)
        A[i+2][j] = (255, 0, 0)
        A[i+3][j] = (255, 0, 0)
        A[i+4][j] = (0, 255, 0)
        A[i+5][j] = (0, 255, 0)
        A[i+6][j] = (0, 255, 0)
        A[i+7][j] = (0, 255, 0)
        A[i+8][j] = (0, 0, 255)
        A[i+9][j] = (0, 0, 255)
x = remap_fatten(A)
while True:
    for i in range(0, 298):
        pixels[i] = x[i]
    pixels.show()

    time.sleep(1)

    # Increase or decrease to change the speed of the solid color change.
    # time.sleep(1)
   # pixels.fill(GREEN)
   # pixels.show()
    #time.sleep(1)
    #pixels.fill(BLUE)
    #pixels.show()
    #time.sleep(1)
    #color_chase(RED, 0.01)  # Increase the number to slow down the color chase
    #color_chase(YELLOW, 0.01)
    #color_chase(GREEN, 0.01)
    #color_chase(CYAN, 0.01)
    #color_chase(BLUE, 0.01)
    #color_chase(PURPLE, 0.01)
    #rainbow_cycle(0)  # Increase the number to slow down the rainbow
