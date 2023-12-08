
![KeyCube Light Manager Module Logo](https://github.com/keycube/lightManager/blob/main/assets/Logo.png?raw=true)
# Introduction
LightManager is a light management module for all existing keycube models and sizes. It supports object-oriented programming and is fully modular to create any sequential effect or use effects such as rainbow, breathing or ripple, designed in the object-oriented paradigm to be as transparent as possible to the user.

# Attributes

### RAIMBOW_COLOR
This integer is a number between 0 and 255 which is incremented or decremented with the [RAIMBOW_INCREASE](https://github.com/keycube/lightManager/blob/main/README.md#raimbow_increase) variable and updated in the [updateRaimbowColor](https://github.com/keycube/lightManager/blob/main/README.md#updateraimbowcolorself) function.  

| Type | Default |
|--|--|
| [int]() | 0 |

### RAIMBOW_INCREASE
This integer is used in the [updateRaimbowColor](https://github.com/keycube/lightManager/blob/main/README.md#updateraimbowcolorself) function to update each [RAIMBOW_COLOR](https://github.com/keycube/lightManager/blob/main/README.md#raimbow_color) step (1 in one direction and -1 in the other).

| Type | Default |
|--|--|
| [int]() | 1 |

### BRIGHTNESS
This float is a number between 0 and 0,1 which is incremented or decremented with the [BRIGHTNESS_INCREASE](https://github.com/keycube/lightManager/blob/main/README.md#raimbow_direction) variable and updated in the [updateBrightness](https://github.com/keycube/lightManager/blob/main/README.md#updatebrightnessself) function.  

| Type | Default |
|--|--|
| [float]() | 0,1 |

### BRIGHTNESS_INCREASE
This integer is used in the [updateBrightness](https://github.com/keycube/lightManager/blob/main/README.md#updatebrightnessself) function to update [BRIGHTNESS](https://github.com/keycube/lightManager/blob/main/README.md#brightness) (-0,0005 in one direction and 0,0005 in the other).

| Type | Default |
|--|--|
| [float]() | -0,0005 |

### COLOR_EFFECT_NUMBER
Generate with the list of effects loaded on the cube, this integer corresponds to the number of light effects loaded on the cube.

| Type | Default |
|--|--|
| [int]() |  |

### COLOR_EFFECT_ACTUAL
Corresponds to the current ID of the lighting effect played on the cube and incremented when the button set to [COLOR_SWITCH](https://github.com/keycube/lightManager/blob/main/README.md#color_switch) is pressed.

| Type | Default |
|--|--|
| [int]() | 0 |

### COLOR_SWITCH
This is the button which, when pressed, modifies the lighting effect played on the cube.

| Type | Default |
|--|--|
| [int]() | TP[0][0] |

### SIZE
It corresponds to the size of the cube and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [int]() |  |

### P
It corresponds to neopixel pixels and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [neopixel.NeoPixel]() |  |

### K
It corresponds to the keyMatrix of keypad and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [keypad.KeyMatrix]() |  |

### TF
It corresponds to the top face matrix and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### NF
It corresponds to the north face matrix and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### SF
It corresponds to the south face matrix and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### EF
It corresponds to the east face matrix and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### WF
It corresponds to the east face matrix and is one of the parameters of the constructor.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### _CTV
It corresponds to the matrix of the cube's top view and is generated using the [createCubeWestView](https://github.com/keycube/lightManager/blob/main/README.md#createcubetopviewself) function.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### _CNV
It corresponds to the matrix of the cube's north view and is generated using the [createCubeNorthView](https://github.com/keycube/lightManager/blob/main/README.md#createcubenorthviewself) function.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### _CSV
It corresponds to the matrix of the cube's south view and is generated using the [createCubeSouthView](https://github.com/keycube/lightManager/blob/main/README.md#createcubesouthviewself) function.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### _CEV
It corresponds to the matrix of the cube's east view and is generated using the [createCubeEastView](https://github.com/keycube/lightManager/blob/main/README.md#createcubeeastviewself) function.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### _CWV
It corresponds to the matrix of the cube's west view and is generated using the [createCubeWestView](https://github.com/keycube/lightManager/blob/main/README.md#createcubewestviewself) function.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |

### _RP
It corresponds to the rainbow sequence matrix and is generated using the [createRaimbow](https://github.com/keycube/lightManager/blob/main/README.md#createraimbowself) function.

| Type | Default |
|--|--|
| [list[list[int]]]() |  |


# Methods

### matFlat(self, matrix)
Convert a matrix into a list.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| matrix | [list[list[Any]]]() |  |  | A matrix of integer |

returns : [list[Any]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_Size_Mat_Flat.png?raw=true)

### matDist(self, matrix)
Get the distance from the center of an even or odd matrix.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| matrix | [list[list[int]]]() |  |  | A matrix of integer |

returns : [list[list[int]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_Size_Mat_Dist.png?raw=true)

### matRot(self, matrix, n)
Convert a matrix into a list.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| matrix | [list[list[Any]]]() |  |  | A matrix of integer |
| n | [int]() |  |  | an integer corresponding to the number of rotations by 90 |

returns : [list[list[Any]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_Size_Mat_Rot.png?raw=true)

### createCubeTopView(self)
Create a cube centered on the top face using the [face attributes](https://github.com/keycube/lightManager/blob/main/README.md#tf) imported when the object was created.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [list[list[int]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_Top.png?raw=true)

### createCubeNorthView(self)
Create a cube centered on the north face using the [matRot](https://github.com/keycube/lightManager/blob/main/README.md#matrotself-matrix-n) function and the [face attributes](https://github.com/keycube/lightManager/blob/main/README.md#tf) imported when the object was created.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [list[list[int]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_North.png?raw=true)

### createCubeSouthView(self)
Create a cube centered on the south face using the [matRot](https://github.com/keycube/lightManager/blob/main/README.md#matrotself-matrix-n) function and the [face attributes](https://github.com/keycube/lightManager/blob/main/README.md#tf) imported when the object was created.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [list[list[int]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_South.png?raw=true)

### createCubeEastView(self)
Create a cube centered on the east face using the [matRot](https://github.com/keycube/lightManager/blob/main/README.md#matrotself-matrix-n) function and the [face attributes](https://github.com/keycube/lightManager/blob/main/README.md#tf) imported when the object was created.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [list[list[int]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_East.png?raw=true)

### createCubeWestView(self)
Create a cube centered on the west face using the [matRot](https://github.com/keycube/lightManager/blob/main/README.md#matrotself-matrix-n) function and the [face attributes](https://github.com/keycube/lightManager/blob/main/README.md#tf) imported when the object was created.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [list[list[int]]]()
![cube pattern centered on the top face](https://github.com/keycube/lightManager/blob/main/assets/Cube_West.png?raw=true)

### createRaimbow(self)
Create a rainbow sequence on the north face using the [matDist](https://github.com/keycube/lightManager/blob/main/README.md#matdistself-matrix) function and the [face attributes](https://github.com/keycube/lightManager/blob/main/README.md#tf) imported when the object was created.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [list[list[int]]]()

### updateRaimbowColor(self)
Update variable [RAIMBOW_COLOR](https://github.com/keycube/lightManager/blob/main/README.md#raimbow_color) using [RAIMBOW_DIRECTION](https://github.com/keycube/lightManager/blob/main/README.md#raimbow_direction) variable every tick.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| No Parameter |  |  |  |  |

returns : [None]()

### detectFace(self, key)
Returns the view centered on the face matrix and the (x, y) coordinates of a key.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| key | [int]() |  |  | the integer corresponding to a key value |

returns : [list[list[list[int]], tuple(int)]]()

### rippleEffect(self, tab, actual, previous, counter)
Recursive function to create the ripple effect.

| Parameter | Type | Optional | Default | Description |
|--|--|--|--|--|
| tab | [int]() |  |  | the view centered on a face matrix |
| actual | [list[tuple(int)]]() |  |  | list of coordinates pixel to update |
| previous | [list[list[tuple(int)]]]() | Yes | [] | sequence of all list of all steps of update |
| counter | [int]() | Yes | 0 | steps of the effect |

returns : [list[list[list[int]], tuple(int)]]()

## Credits
Thibaut Breton [Website](https://tbreton.fr) [Github](https://github.com/ayrozdzn)
OpenRGB [Website](https://openrgb.org) [Github](https://github.com/CalcProgrammer1/OpenRGB)
Light Effect List [Website](https://www.pc-100.com/mechanical-keyboard-features-parameters/back-light-effects-mechanical-keyboard/)
