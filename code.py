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


num_pixels = 298

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def remap_fatten(A):
    C = [row[:] for row in A]
    x = [0] * 298
    for i in range(0,10):
        if not i % 2 == 0:
                flip = [0] * 30
                for j in range(0, 30):
                    flip[j] = C[j][i]
                fliped = flip[::-1]
                for j in range(0, 30):
                    C[j][i] = fliped[j]
        else:

            for j in range(0, 30):
                C[j][i] = A[j][i]

    for i in range(0,10):
            for j in range(0,30):
                index = i * 30 + j
                if index < 209:
                    x[index] = C[j][i]
                elif index > 209 and index < 269:
                    x[index-1] = C[j][i]
                elif index > 269 and index < 300:
                    x[index-2] = C[j][i]
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
RainbowChaseDown = [[0,0,0,0,0,0,0,0,0,0],
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
for j in range(0,30, 3):
    for i in range(0,10):
        RainbowChaseDown[j][i] = RED
        RainbowChaseDown[j+1][i] = GREEN
        RainbowChaseDown[j+2][i] = BLUE
BlueWhiteFade = [[0,0,0,0,0,0,0,0,0,0],
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
for j in range(0, 30):
    j2 = j*5
    if j2 > 255: j2 =255
    for i in range(0,10):
        BlueWhiteFade[j][i] = (0, 0, j2)

down = True
blueVal = 0
mode = 0
prevButton = True
while True:
    if Button.value == False and prevButton == True:
        mode += 1
        if mode >2:
            mode = 0
        prevButton = False
    elif Button.value == True and prevButton == False:
        prevButton = True

    if mode == 0:
        B = [0] * 10
        for i in range(0, 10):
            B[i] = RainbowChaseDown[29][i]
        for row in range(0, 30):
            rowReversed = 30 - row -1
            if rowReversed > 0:
                for i in range(0, 10):
                    RainbowChaseDown[rowReversed][i] = RainbowChaseDown[rowReversed - 1][i]
            elif rowReversed == 0:
                for i in range(0, 10):
                    RainbowChaseDown[rowReversed][i] = B[i]
        time.sleep(0.25)
        x = remap_fatten(RainbowChaseDown)
    elif mode == 1:
        newMatrix = []

        if blueVal < 10:
            down = True
        elif blueVal > 245:
            down = False
        if down:
            blueVal = BlueWhiteFade[0][0][2] + 10
        else:
            blueVal = BlueWhiteFade[0][0][2] - 10
        print(blueVal)
        newRow = [(0, 0, blueVal)] * 10
        newMatrix.append(newRow)
        for i in range(0,29):
            newMatrix.append(BlueWhiteFade[i])
        BlueWhiteFade = newMatrix
        x = remap_fatten(BlueWhiteFade)
    elif mode == 2:
       pixels[269] = WHITE
       print("f")


    for i in range(0, 298):
        pixels[i] = x[i]
    pixels.show()

    time.sleep(0.15)

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
