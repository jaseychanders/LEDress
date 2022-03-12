"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from ulab import numpy as np
import random
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
for j in range(0,30, 5):
    for i in range(0,10):
        RainbowChaseDown[j][i] = (204, 84, 129)
        RainbowChaseDown[j+1][i] = (252, 142, 78)
        RainbowChaseDown[j+2][i] = (106, 202, 137)
        RainbowChaseDown[j+3][i] = (85, 147, 182)
        RainbowChaseDown[j+4][i] = (136, 101, 229)
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
twinkle = [[0,0,0,0,0,0,0,0,0,0],
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
alienAbduction = [[0,0,0,0,0,0,0,0,0,0],
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
spiral = [[0,0,0,0,0,0,0,0,0,0],
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

staticSpiral = [[(76, 23, 191),0,0,0,0,(97, 186, 230),0,0,0,0],
    [0,(76, 23, 191),0,0,0,0,(97, 186, 230),0,0,0,],
    [0,0,(76, 23, 191),0,0,0, 0,(97, 186, 230),0,0],
    [0,0,0,(76, 23, 191),0,0,0,0,(97, 186, 230),0],
    [0,0,0,0,(76, 23, 191),0,0,0,0,(97, 186, 230)],
    [(97, 186, 230),0,0,0,0,(76, 23, 191),0,0,0,0],
    [0,(97, 186, 230),0,0,0,0,(76, 23, 191),0,0,0],
    [0,0,(97, 186, 230),0,0,0,0,(76, 23, 191),0,0],
    [0,0,0,(97, 186, 230),0,0,0,0,(76, 23, 191),0],
    [0,0,0,0,(97, 186, 230),0,0,0,0,(76, 23, 191)],
    [(76, 23, 191),0,0,0,0,(97, 186, 230),0,0,0,0],
    [0,(76, 23, 191),0,0, 0,0,(97, 186, 230),0,0,0,],
    [0,0,(76, 23, 191),0,0,0, 0,(97, 186, 230),0,0],
    [0,0,0,(76, 23, 191),0,0,0,0,(97, 186, 230),0],
    [0,0,0,0,(76, 23, 191),0,0,0,0,(97, 186, 230)],
    [(97, 186, 230),0,0,0,0,(76, 23, 191),0,0,0,0],
    [0,(97, 186, 230),0,0,0,0,(76, 23, 191),0,0,0],
    [0,0,(97, 186, 230),0,0,0,0,(76, 23, 191),0,0],
    [0,0,0,(97, 186, 230),0,0,0,0,(76, 23, 191),0],
    [0,0,0,0,(97, 186, 230),0,0,0,0,(76, 23, 191)],
    [(76, 23, 191),0,0,0,0,(97, 186, 230),0,0,0,0],
    [0,(76, 23, 191),0,0, 0,0,(97, 186, 230),0,0,0,],
    [0,0,(76, 23, 191),0,0,0, 0,(97, 186, 230),0,0],
    [0,0,0,(76, 23, 191),0,0,0,0,(97, 186, 230),0],
    [0,0,0,0,(76, 23, 191),0,0,0,0,(97, 186, 230)],
    [(97, 186, 230),0,0,0,0,(76, 23, 191),0,0,0,0],
    [0,(97, 186, 230),0,0,0,0,(76, 23, 191),0,0,0],
    [0,0,(97, 186, 230),0,0,0,0,(76, 23, 191),0,0],
    [0,0,0,(97, 186, 230),0,0,0,0,(76, 23, 191),0],
    [0,0,0,0,(97, 186, 230),0,0,0,0,(76, 23, 191)]]
spiralNewRow = [(76, 23, 191),0,0,0,0,0,0,0,0,0]
down = True
blueVal = 0
mode = 0
prevButton = True
alienStripesCount = 0
while True:
    if Button.value == False and prevButton == True:
        mode += 1
        if mode >9:
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
        x = x
    elif mode == 2:
        newMatrix = []

        if blueVal < 10:
            down = True
        elif blueVal > 245:
            down = False
        if down:
            blueVal = BlueWhiteFade[0][0][2] + 10
        else:
            blueVal = BlueWhiteFade[0][0][2] - 10
        newRow = [(0, 0, blueVal)] * 10
        newMatrix.append(newRow)
        for i in range(0,29):
            newMatrix.append(BlueWhiteFade[i])
        BlueWhiteFade = newMatrix
        x = remap_fatten(BlueWhiteFade)
    elif mode == 3:
        x=x
    elif mode == 4:
        col = random.randint(0, 9)
        row = random.randint(0, 29)
        twinkle[row][col] = (5,5,5)
        col = random.randint(0, 9)
        row = random.randint(0, 29)
        twinkle[row][col] = (5,5,5)
        for j in range(0,30):
            for i in range(0,10):
                current = twinkle[j][i]
                if not current == 0 and current[0] <=180:
                    new = current[0] + 10
                    twinkle[j][i] = twinkle[j][i] = (new, new, new)
                elif not current == 0 and current[0] > 180:
                    twinkle[j][i] = (0,0,0)
        x = remap_fatten(twinkle)
    elif mode == 5:
        x=x
    elif mode == 6:
        newMatrix = []
        color = (0,0,0)
        if alienStripesCount > 17:
            alienStripesCount = 0
        if alienStripesCount == 0:
            color = (12, 242, 93)
            alienStripesCount += 1
        elif alienStripesCount == 4:
            color = (3, 140, 62)
            alienStripesCount += 1
        elif alienStripesCount == 8:
            color = (2, 115, 94)
            alienStripesCount += 1
        elif alienStripesCount == 12:
            color = (2, 89, 81)
            alienStripesCount += 1
        elif alienStripesCount == 16:
            color = (3, 65, 89)
            alienStripesCount += 1
        else:
            color = (0, 0, 0)
            alienStripesCount += 1
        newRow = [color] * 10
        newMatrix.append(newRow)
        for i in range(0,29):
            newMatrix.append(alienAbduction[i])
        alienAbduction = newMatrix
        x = remap_fatten(alienAbduction)
    elif mode == 7:
        x=x
    elif mode == 8:
        newMatrix = []
        newRow = []
        newRow.append(spiralNewRow[8])
        newRow.append(spiralNewRow[9])
        for i in range(0,9):
            newRow.append(spiralNewRow[i])
        newMatrix.append(newRow)
        spiralNewRow = newRow
        for j in range(0,29):
            shifted = []
            shifted.append(spiral[j][9])
            for i in range(0,9):
                shifted.append(spiral[j][i])
            newMatrix.append(shifted)
        spiral = newMatrix
        x = remap_fatten(spiral)

    elif mode == 9:
        x = remap_fatten(staticSpiral)
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
