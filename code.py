import time
import board
import keypad
import neopixel
import asyncio
from rainbowio import colorwheel
import board
from analogio import AnalogIn
from LightManager import LightManager

pixels = neopixel.NeoPixel(board.SDA, 80, brightness=0.1, auto_write=False)
keys = keypad.KeyMatrix(
    row_pins=(board.A0, board.A1, board.A2, board.A3, board.A4, board.A5, board.SCK, board.MOSI, board.MISO, board.RX, board.TX, board.D2),
    column_pins=(board.D9, board.D6, board.D5, board.SCL, board.D13, board.D12, board.D11, board.D10),

    columns_to_anodes=False,
)

kMat = {
    0:48,
    8:55,
    16:56,
    24:63,
    1:49,
    9:54,
    17:57,
    25:62,
    2:50,
    10:53,
    18:58,
    26:61,
    3:51,
    11:52,
    19:59,
    27:60,

    36:0,
    44:7,
    52:8,
    60:15,
    37:1,
    45:6,
    53:9,
    61:14,
    38:2,
    46:5,
    54:10,
    62:13,
    39:3,
    47:4,
    55:11,
    63:12,

    35:35,
    34:34,
    33:33,
    32:32,
    40:39,
    41:38,
    42:37,
    43:36,
    48:40,
    49:41,
    50:42,
    51:43,
    56:47,
    57:46,
    58:45,
    59:44,

    28:31,
    29:30,
    30:29,
    31:28,
    20:24,
    21:25,
    22:26,
    23:27,
    12:23,
    13:22,
    14:21,
    15:20,
    7:19,
    6:18,
    5:17,
    4:16,

    68:64,
    69:65,
    77:66,
    76:67,
    84:68,
    85:69,
    93:70,
    92:71,
    94:72,
    95:73,
    86:74,
    87:75,
    78:76,
    79:77,
    70:78,
    71:79
}
def kToP(key_number):
    return kMat[key_number]

SIZE = 4
TF = [
        [73, 72, 70, 71], 
        [75, 74, 69, 68], 
        [77, 76, 66, 67], 
        [79, 78, 65, 64]
    ] # Top Face Pattern
NF = [
        [63, 56, 55, 48], 
        [62, 57, 54, 49], 
        [61, 58, 53, 50], 
        [60, 59, 52, 51]
    ] # North Face Pattern
SF = [
        [ 3,  4, 11, 12], 
        [ 2,  5, 10, 13], 
        [ 1,  6,  9, 14], 
        [ 0,  7,  8, 15]
    ] # South Face Pattern
EF = [
        [28, 29, 30, 31], 
        [27, 26, 25, 24], 
        [20, 21, 22, 23], 
        [19, 18, 17, 16]
    ] # East Face Pattern
WF = [
        [44, 45, 46, 47], 
        [43, 42, 41, 40], 
        [36, 37, 38, 39], 
        [35, 34, 33, 32]
    ] # West Face Pattern

cube = LightManager(SIZE, pixels, keys, TF, NF, SF, EF, WF)

cube.p.fill((0, 0, 0))

async def main():
    interpolateColor = cube.interpolate_color((255, 0, 0), (0, 0, 255), 254)
    while True:
        if cube.color == 0: # Raimbow Effect 1
            cube.RAIMBOWDIRECTION = 1
            for i in range(0, len(cube.RP)):
                for j in range(0, len(cube.RP[i])):
                    cube.p[cube.RP[i][j]] = colorwheel((cube.RAIMBOWCOLOR + (i * 10)) % 255)

        elif cube.color == 1: # Raimbow Effect 2
            cube.RAIMBOWDIRECTION = -1
            for i in range(0, len(cube.RP)):
                for j in range(0, len(cube.RP[i])):
                    cube.p[cube.RP[i][j]] = colorwheel((cube.RAIMBOWCOLOR + (i * 10)) % 255)

        elif cube.color == 2: # Raimbow Custom Effect
            cube.RAIMBOWDIRECTION = -1
            for i in range(0, len(cube.RP)):
                for j in range(0, len(cube.RP[i])):
                    cube.p[cube.RP[i][j]] = interpolateColor[(cube.CUSTOMRAIMBOWSTEP + (i * 10)) % len(interpolateColor)]

        elif cube.color == 3: # Respiration Effect Red
            cube.p.fill((255, 0, 0))
            cube.p.brightness = cube.BRIGHTNESS

        elif cube.color == 4: # Respiration Effect Blue
            cube.p.fill((0, 255, 0))
            cube.p.brightness = cube.BRIGHTNESS

        elif cube.color == 5: # Respiration Effect Green
            cube.p.fill((0, 0, 255))
            cube.p.brightness = cube.BRIGHTNESS

        key_event = keys.events.get()
        if key_event:
            if key_event.pressed:
                # Switch light effect
                if (kToP(key_event.key_number) == cube.colorSwitch):
                    cube.color = (cube.color + 1) % (cube.colorEffect + 1)
                    cube.p.fill((0, 0, 0))
                    cube.BRIGHTNESS = 0.1

                # Click effect Press
                if cube.color == 6: 
                    cube.p[kToP(key_event.key_number)] = (255, 0, 0)

                # Ripple effect
                if cube.color == 7:
                    info = cube.detectFace(kToP(key_event.key_number))
                    await cube.rippleInit(info[0], info[1])
            else:
                # Click effect Release
                if cube.color == 6:
                    cube.p[kToP(key_event.key_number)] = (0, 0, 0)

        cube.brightnessUpdate()
        cube.raimbowColorUpdate()
        cube.p.show()

asyncio.run(main())