import time
import board
import keypad
import neopixel
from rainbowio import colorwheel
import board
from analogio import AnalogIn
import storage

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)


def get_voltage(pin):
    return (pin.value * 3.6) / 65536 * 2


battery_voltage = get_voltage(vbat_voltage)
print("VBat voltage: {:.2f}".format(battery_voltage))

storage.remount("/", False)
with open('x.txt', 'w') as f:
    f.write(b'abcdefg')

COLUMNS = 4
ROWS = 4

MATRIX_COLUMNS = 2
MATRIX_ROWS = 3

colorEffect = 0
color = 0
brightnessIncrease = -0.0005


def XYToNumber(y, x):
    return COLUMNS * y + x

TopFace = [73, 72, 70, 71, 75, 74, 69, 68, 77, 76, 66, 67, 79, 78, 65, 64]

NorthFace = [63, 56, 55, 48, 62, 57, 54, 49, 61, 58, 53, 50, 60, 59, 52, 51]

SouthFace = [3, 4, 11, 12, 2, 5, 10, 13, 1, 6, 9, 14, 0, 7, 8, 15]

EastFace = [28, 29, 30, 31, 27, 26, 25, 24, 20, 21, 22, 23, 19, 18, 17, 16]

WestFace = [44, 45, 46, 47, 43, 42, 41, 40, 36, 37, 38, 39, 35, 34, 33, 32]

StartSequence = [74, 69, 66, 76, 77, 75, 73, 72, 70, 71, 68, 67, 64, 65, 78, 79, 32, 39, 40, 47, 60, 59, 52, 51, 28, 27, 20, 19, 12, 11, 4, 3, 33, 38, 41, 46, 61, 58, 53, 50, 29, 26, 21, 18, 13, 10, 5, 2, 34, 37, 42, 45, 62, 57, 54, 49, 30, 25, 22, 17, 14, 9, 6, 1, 35, 36, 43, 44, 63, 56, 55, 48, 31, 24, 23, 16, 15, 8, 7, 0]

RaimbowPattern = [
    [TopFace[XYToNumber(1, 1)], TopFace[XYToNumber(1, 2)], TopFace[XYToNumber(2, 1)], TopFace[XYToNumber(2, 2)]],
    
    [TopFace[XYToNumber(0, 0)], TopFace[XYToNumber(0, 1)], TopFace[XYToNumber(0, 2)], TopFace[XYToNumber(0, 3)],
     TopFace[XYToNumber(1, 0)], TopFace[XYToNumber(1, 3)], TopFace[XYToNumber(2, 0)], TopFace[XYToNumber(2, 3)],
     TopFace[XYToNumber(3, 0)], TopFace[XYToNumber(3, 1)], TopFace[XYToNumber(3, 2)], TopFace[XYToNumber(3, 3)]],

    [NorthFace[XYToNumber(3, 0)], NorthFace[XYToNumber(3, 1)], NorthFace[XYToNumber(3, 2)], NorthFace[XYToNumber(3, 3)],
     SouthFace[XYToNumber(0, 0)], SouthFace[XYToNumber(0, 1)], SouthFace[XYToNumber(0, 2)], SouthFace[XYToNumber(0, 3)],
     EastFace[XYToNumber(0, 0)], EastFace[XYToNumber(1, 0)], EastFace[XYToNumber(2, 0)], EastFace[XYToNumber(3, 0)],
     WestFace[XYToNumber(0, 3)], WestFace[XYToNumber(1, 3)], WestFace[XYToNumber(2, 3)], WestFace[XYToNumber(3, 3)]],

    [NorthFace[XYToNumber(2, 0)], NorthFace[XYToNumber(2, 1)], NorthFace[XYToNumber(2, 2)], NorthFace[XYToNumber(2, 3)],
     SouthFace[XYToNumber(1, 0)], SouthFace[XYToNumber(1, 1)], SouthFace[XYToNumber(1, 2)], SouthFace[XYToNumber(1, 3)],
     EastFace[XYToNumber(0, 1)], EastFace[XYToNumber(1, 1)], EastFace[XYToNumber(2, 1)], EastFace[XYToNumber(3, 1)],
     WestFace[XYToNumber(0, 2)], WestFace[XYToNumber(1, 2)], WestFace[XYToNumber(2, 2)], WestFace[XYToNumber(3, 2)]],

    [NorthFace[XYToNumber(1, 0)], NorthFace[XYToNumber(1, 1)], NorthFace[XYToNumber(1, 2)], NorthFace[XYToNumber(1, 3)],
     SouthFace[XYToNumber(2, 0)], SouthFace[XYToNumber(2, 1)], SouthFace[XYToNumber(2, 2)], SouthFace[XYToNumber(2, 3)],
     EastFace[XYToNumber(0, 2)], EastFace[XYToNumber(1, 2)], EastFace[XYToNumber(2, 2)], EastFace[XYToNumber(3, 2)],
     WestFace[XYToNumber(0, 1)], WestFace[XYToNumber(1, 1)], WestFace[XYToNumber(2, 1)], WestFace[XYToNumber(3, 1)]],

    [NorthFace[XYToNumber(0, 0)], NorthFace[XYToNumber(0, 1)], NorthFace[XYToNumber(0, 2)], NorthFace[XYToNumber(0, 3)],
     SouthFace[XYToNumber(3, 0)], SouthFace[XYToNumber(3, 1)], SouthFace[XYToNumber(3, 2)], SouthFace[XYToNumber(3, 3)],
     EastFace[XYToNumber(0, 3)], EastFace[XYToNumber(1, 3)], EastFace[XYToNumber(2, 3)], EastFace[XYToNumber(3, 3)],
     WestFace[XYToNumber(0, 0)], WestFace[XYToNumber(1, 0)], WestFace[XYToNumber(2, 0)], WestFace[XYToNumber(3, 0)]],
]

special_key_matrix = {
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

def key_to_pixel_map(key_number):
    return special_key_matrix[key_number]

# warning keep brightness to 0.1, just in case the 80 LEDs draw too much current for the board to handle

pixels = neopixel.NeoPixel(board.SDA, 80, brightness=0.1, auto_write=False)

keys = keypad.KeyMatrix(

    row_pins=(board.A0, board.A1, board.A2, board.A3, board.A4, board.A5, board.SCK, board.MOSI, board.MISO, board.RX, board.TX, board.D2),
    column_pins=(board.D9, board.D6, board.D5, board.SCL, board.D13, board.D12, board.D11, board.D10),

    columns_to_anodes=False,
)

for i in range(0, len(StartSequence)):
    pixels[StartSequence[i]] = (255, 0, 0)
    if (i > 5) and (i < 80):
        pixels[StartSequence[i - 6]] = (0, 0, 0)
    pixels.show()
    time.sleep(0.05)

time.sleep(0.5)
pixels.fill((255, 0, 0))
pixels.show()
time.sleep(0.5)
pixels.fill((0, 255, 0))
pixels.show()
time.sleep(0.5)
pixels.fill((0, 0, 255))
pixels.show()
time.sleep(0.5)
pixels.fill((0, 0, 0))
pixels.show()
time.sleep(0.5)

while True:
    if colorEffect == 0:
        color = (color - 1) % 255
        for i in range(0, len(RaimbowPattern)):
            for j in range(0, len(RaimbowPattern[i])):
                pixels[RaimbowPattern[i][j]] = colorwheel(color + (i * 10))

    elif colorEffect == 1:
        color = (color + 1) % 255
        for i in range(0, len(RaimbowPattern)):
            for j in range(0, len(RaimbowPattern[i])):
                pixels[RaimbowPattern[i][j]] = colorwheel(color + (i * 10))
    
    elif colorEffect == 2:
        pixels.fill((255, 0, 0))
        pixels.brightness += brightnessIncrease
        if pixels.brightness <= 0 or pixels.brightness > 0.1:
            brightnessIncrease = -brightnessIncrease
          
    elif colorEffect == 3:
        pixels.fill((0, 255, 0))
        pixels.brightness += brightnessIncrease
        if pixels.brightness <= 0 or pixels.brightness > 0.1:
            brightnessIncrease = -brightnessIncrease
        
    elif colorEffect == 4:
        pixels.fill((0, 0, 255))
        pixels.brightness += brightnessIncrease
        if pixels.brightness <= 0 or pixels.brightness > 0.1:
            brightnessIncrease = -brightnessIncrease

    key_event = keys.events.get()
    if key_event:
        if key_event.pressed:
            if colorEffect == 5:
                pixels[key_to_pixel_map(key_event.key_number)] = (255, 0, 0)
            if (key_to_pixel_map(key_event.key_number) == 76):
                colorEffect = (colorEffect + 1) % 6
                pixels.fill((0, 0, 0))
                pixels.brightness = 0.1
                brightnessIncrease = -0.0005
        else:
            if colorEffect == 5:
                pixels[key_to_pixel_map(key_event.key_number)] = (0, 0, 0)

    pixels.show()