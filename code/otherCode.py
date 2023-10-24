# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
NeoKey 5x6 Ortho Snap-Apart simple key press NeoPixel demo.
"""


# KEYPRESS COLOR test

import board
import keypad
import neopixel
from rainbowio import colorwheel

COLUMNS = 4
ROWS = 4

MATRIX_COLUMNS = 2
MATRIX_ROWS = 3

color = 0

def XYToNumber(y, x):
    return COLUMNS * y + x

TopFace = [73, 72, 70, 71, 75, 74, 69, 68, 77, 76, 66, 67, 79, 78, 65, 64]

NorthFace = [63, 56, 55, 48, 62, 57, 54, 49, 61, 58, 53, 50, 60, 59, 52, 51]

SouthFace = [3, 4, 11, 12, 2, 5, 10, 13, 1, 6, 9, 14, 0, 7, 8, 15]

EastFace = [28, 29, 30, 31, 27, 26, 25, 24, 20, 21, 22, 23, 19, 18, 17, 16]

WestFace = [44, 45, 46, 47, 43, 42, 41, 40, 36, 37, 38, 39, 35, 34, 33, 32]

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

# warning keep brightness to 0.1, just in case the 80 LEDs draw too much current for the board to handle
pixels = neopixel.NeoPixel(board.SDA, 80, brightness=0.1)

keys = keypad.KeyMatrix(
    #row_pins=(board.D2, board.TX, board.RX, board.MISO, board.MOSI, board.SCK, board.A5, board.A4, board.A3, board.A2, board.A1, board.A0),

    row_pins=(board.A0, board.A1, board.A2, board.A3, board.A4, board.A5, board.SCK, board.MOSI, board.MISO, board.RX, board.TX, board.D2),
    column_pins=(board.D9, board.D6, board.D5, board.SCL, board.D13, board.D12, board.D11, board.D10),
    #column_pins=(board.SCL, board.D5, board.D6, board.D9, board.D10, board.D11, board.D12, board.D13),

    #row_pins=(board.A4, board.A5, board.SCK, board.MOSI, board.A0, board.A1, board.A2, board.A3, board.D2, board.TX, board.RX, board.MISO),
    #column_pins=(board.D13, board.D12, board.D11, board.D10, board.D9, board.D6, board.D5, board.SCL),

    #row_pins=(board.A4, board.A5, board.SCK, board.MOSI, board.A0, board.A1, board.A2, board.A3),
    #column_pins=(board.D13, board.D12, board.D11, board.D10, board.D9, board.D6, board.D5, board.SCL),

    #row_pins=(board.D2, board.TX, board.RX, board.MISO, board.MOSI, board.SCK, board.A5, board.A4),
    #column_pins=(board.SCL, board.D5, board.D6, board.D9, board.D10, board.D11, board.D12, board.D13),
    #row_pins=(board.D2, board.TX, board.RX, board.MISO),

    #column_pins=(board.SCL, board.D5, board.D6, board.D9, board.D10, board.D11, board.D12, board.D13),

    columns_to_anodes=False,
)

# ugly but working...
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
    """
    if key_number > 64:
        return special_key_matrix[key_number]
    row = key_number // (COLUMNS * MATRIX_COLUMNS)
    column = key_number % (COLUMNS * MATRIX_COLUMNS)

    matrix_row = row // ROWS
    matrix_column = column // COLUMNS

    #print('key', key_number, 'row', row, 'column', column, 'matrixRow', matrix_row, 'matrixColumn', matrix_column)

    row = row % ROWS
    column = column % COLUMNS

    if row % 2 == 1:
        column = COLUMNS - column - 1
    pixel_number = row * COLUMNS + column + 16 * (matrix_column + matrix_row * MATRIX_COLUMNS)
    print('key', key_number, 'pixel', pixel_number)
    return pixel_number
    """

pixels.fill((0, 0, 0))  # Begin with pixels off.

while True:
    color = (color + 10) % 255

    for pixel in RaimbowPattern[0]:
        pixels[pixel] = colorwheel(color)

    for pixel in RaimbowPattern[1]:
        pixels[pixel] = colorwheel(color + 15)

    for pixel in RaimbowPattern[2]:
        pixels[pixel] = colorwheel(color + 25)

    for pixel in RaimbowPattern[3]:
        pixels[pixel] = colorwheel(color + 35)

    for pixel in RaimbowPattern[4]:
        pixels[pixel] = colorwheel(color + 45)

    for pixel in RaimbowPattern[5]:
        pixels[pixel] = colorwheel(color + 55)

    pixels.show()

    key_event = keys.events.get()
    if key_event:
        #print(key_event)
        if key_event.pressed:
            print(key_to_pixel_map(key_event.key_number), key_event.key_number)
            pixels[key_to_pixel_map(key_event.key_number)] = (255, 0, 0)
            #key_to_pixel_map(key_event.key_number)
        else:
            pixels[key_to_pixel_map(key_event.key_number)] = (0, 0, 0)

# end keypress color

# RAINBOW test
"""
import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.SDA

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 80

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

# warning keep brightness to 0.1, just in case the 80 LEDs draw too much current for the board to handle
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

"""
# end rainbow test


# VOLTAGE test
"""

import board
from analogio import AnalogIn

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)

def get_voltage(pin):
    return (pin.value * 3.6) / 65536 * 2

battery_voltage = get_voltage(vbat_voltage)

print("VBat voltage: {:.2f}".format(battery_voltage))

"""
# end voltage
