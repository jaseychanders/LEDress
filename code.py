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
rainbowFade = [[0,0,0,0,0,0,0,0,0,0],
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

for i in range(0,10):
    rainbowFade[0][i] = (166, 5, 5)
    rainbowFade[01][i] = (171,19, 4)
    rainbowFade[2][i] = (176, 33, 3)
    rainbowFade[3][i] = (181, 47,3)
    rainbowFade[4][i] = (186, 61, 1)
    rainbowFade[5][i] = (191, 77, 1)
    rainbowFade[6][i] = (196, 99, 6)
    rainbowFade[7][i] = (201, 121, 11)
    rainbowFade[8][i] = (206, 142, 16)
    rainbowFade[9][i] = (211, 164,21)
    rainbowFade[10][i] = (217, 185, 26)
    rainbowFade[11][i] = (186, 181, 34)
    rainbowFade[12][i] = (155, 177, 42)
    rainbowFade[13][i] = (124, 173, 50)
    rainbowFade[14][i] = (92, 169, 58)
    rainbowFade[15][i] = (60, 166, 67)
    rainbowFade[16][i] = (64, 158, 97)
    rainbowFade[17][i] = (66, 154, 110)
    rainbowFade[18][i] = (68,150, 121)
    rainbowFade[19][i] = (72,142,145)
    rainbowFade[20][i] = (76,134,169)
    rainbowFade[21][i] = (78, 124, 217)
    rainbowFade[22][i] = (91,112,217)
    rainbowFade[23][i] = (104,100,217)
    rainbowFade[24][i] = (117,88,217)
    rainbowFade[25][i] = (130,76,217)
    rainbowFade[26][i] = (141, 65, 217)
    rainbowFade[27][i] = (147,50,164)
    rainbowFade[28][i] = (153,35,110)
    rainbowFade[29][i] = (159,20,56)

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
twoSpirial = [[0,0,0,0,0,0,0,0,0,0],
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
spiralNewRow = [(76, 23, 191),0,0,0,0,0,0,0,0,0]
twoSpiralNewRow = [(76, 23, 191),0,0,0,0,(97, 186, 230),0,0,0,0]

rainbowFadeColor = (166, 5, 5)
rainbowFadeColors = [(166, 5, 5), (191, 77, 11), (217, 185, 26), (60, 166, 67), (78, 124, 217), (141, 65, 217)]
rainbowFadePosition = 0
rainbowCount = 0
down = True
blueVal = 0
mode = 0
prevButton = True
alienStripesCount = 0
photos = False
display = True
displayTimer = 0
while True:
    if display:
        displayTimer += 1
        if displayTimer % 50 == 0:
            mode +=2
            if mode > 13:
                mode = 0
    else:
        if Button.value == False and prevButton == True:
            if photos:
                mode += 1
            else:
                mode += 2
            if mode >13:
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
    elif mode == 9:
        x=x
    elif mode == 10:
        newMatrix = []
        newRow = []
        newRow.append(twoSpiralNewRow[8])
        newRow.append(twoSpiralNewRow[9])
        for i in range(0,9):
            newRow.append(twoSpiralNewRow[i])
        newMatrix.append(newRow)
        twoSpiralNewRow = newRow
        for j in range(0,29):
            shifted = []
            shifted.append(twoSpirial[j][9])
            for i in range(0,9):
                shifted.append(twoSpirial[j][i])
            newMatrix.append(shifted)
        twoSpirial = newMatrix
        x = remap_fatten(twoSpirial)
    elif mode == 11:
        x = x
    elif mode == 12:
        B = [0] * 10
        for i in range(0, 10):
            B[i] = rainbowFade[29][i]
        for row in range(0, 30):
            rowReversed = 30 - row -1
            if rowReversed > 0:
                for i in range(0, 10):
                    rainbowFade[rowReversed][i] = rainbowFade[rowReversed - 1][i]
            elif rowReversed == 0:
                for i in range(0, 10):
                    rainbowFade[rowReversed][i] = B[i]
        time.sleep(0.25)
        x = remap_fatten(rainbowFade)
    elif mode == 13:
        x=x
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
