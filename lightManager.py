import keypad
import neopixel

class LightEffect:
    # Type: 1 = Sequence
    def __init__(self, type: int = 0, color = (0, 0, 0), sequence: list[list[int]] = []) -> None:
        self.type = type
        self.color = color
        self.sequence = sequence

class LightManager:
    # Return distance of a point from the center of a matrix
    def matriceDist(self, matrice):
        centre = (len(matrice) // 2) - (len(matrice)+1)%2*0.5
        
        distances = []
        for i in range(len(matrice)):
            for j in range(len(matrice)):
                distance = max(abs(i - centre), abs(j - centre))
                distances.append(int(distance)) 

        matriceUp = [[] for _ in range(distances[0]+1)]
        for y in range(len(matrice)):
            for x in range(len(matrice)):
                matriceUp[distances[len(matrice)*y + x]].append(matrice[y][x])

        return matriceUp

    # Rotate a matrix by 90 degrees, n: 0 = 0°, 1 = 90°, 2 = 180°, 3 = 270°/-90°
    def matRot(self, matrix, n):
        rotMatrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        if (n <= 0):
            return matrix

        for _ in range(n):
            for y in range(len(matrix)):
                for x in range(len(matrix[0])):
                    rotMatrix[x][len(matrix) - 1 - y] = matrix[y][x]

        if (n == 1):
            return rotMatrix

        return self.matRot(rotMatrix, n - 1)
    
    # Create a cube pattern centered on the top face of the cube with all connected faces
    def createCubeTopView(self) -> list[list[int]]:
        cubeTopView = [[-1] * (self.size * 3) for _ in range(self.size * 3)]

        for y in range(self.size):
            for x in range(self.size):
                cubeTopView[y + self.size * 0][x + self.size * 1] = self.matRot(self.NF, 0)[y][x]
                cubeTopView[y + self.size * 1][x + self.size * 1] = self.matRot(self.TF, 0)[y][x]
                cubeTopView[y + self.size * 1][x + self.size * 0] = self.matRot(self.WF, 0)[y][x]
                cubeTopView[y + self.size * 1][x + self.size * 2] = self.matRot(self.EF, 0)[y][x]
                cubeTopView[y + self.size * 2][x + self.size * 1] = self.matRot(self.SF, 0)[y][x]

        return cubeTopView
    
    # Create a cube pattern centered on the north face of the cube with all connected faces
    def createCubeNorthView(self) -> list[list[int]]:
        cubeNorthView = [[-1] * (self.size * 5) for _ in range(self.size * 3)]

        for y in range(self.size):
            for x in range(self.size):
                cubeNorthView[y + self.size * 0][x + self.size * 0] = self.matRot(self.SF, 2)[y][x]
                cubeNorthView[y + self.size * 0][x + self.size * 1] = self.matRot(self.WF, 1)[y][x]
                cubeNorthView[y + self.size * 0][x + self.size * 2] = self.matRot(self.NF, 0)[y][x]
                cubeNorthView[y + self.size * 0][x + self.size * 3] = self.matRot(self.EF, 3)[y][x]
                cubeNorthView[y + self.size * 0][x + self.size * 4] = self.matRot(self.SF, 2)[y][x]
                cubeNorthView[y + self.size * 1][x + self.size * 2] = self.matRot(self.TF, 0)[y][x]
                cubeNorthView[y + self.size * 2][x + self.size * 2] = self.matRot(self.SF, 0)[y][x]

        return cubeNorthView
    
    # Create a cube pattern centered on the south face of the cube with all connected faces
    def createCubeSouthView(self) -> list[list[int]]:
        cubeSouthView = [[-1] * (self.size * 5) for _ in range(self.size * 3)]

        for y in range(self.size):
            for x in range(self.size):
                cubeSouthView[y + self.size * 0][x + self.size * 2] = self.matRot(self.NF, 0)[y][x]
                cubeSouthView[y + self.size * 1][x + self.size * 2] = self.matRot(self.TF, 0)[y][x]
                cubeSouthView[y + self.size * 2][x + self.size * 0] = self.matRot(self.NF, 2)[y][x]
                cubeSouthView[y + self.size * 2][x + self.size * 1] = self.matRot(self.WF, 1)[y][x]
                cubeSouthView[y + self.size * 2][x + self.size * 2] = self.matRot(self.SF, 0)[y][x]
                cubeSouthView[y + self.size * 2][x + self.size * 3] = self.matRot(self.EF, 3)[y][x]
                cubeSouthView[y + self.size * 2][x + self.size * 4] = self.matRot(self.NF, 2)[y][x]

        return cubeSouthView
    
    # Create a cube pattern centered on the east east of the cube with all connected faces
    def createCubeEastView(self) -> list[list[int]]:
        cubeEastView = [[-1] * (self.size * 3) for _ in range(self.size * 5)]

        for y in range(self.size):
            for x in range(self.size):
                cubeEastView[y + self.size * 0][x + self.size * 0] = self.matRot(self.EF, 2)[y][x]
                cubeEastView[y + self.size * 1][x + self.size * 0] = self.matRot(self.NF, 3)[y][x]
                cubeEastView[y + self.size * 2][x + self.size * 0] = self.matRot(self.WF, 0)[y][x]
                cubeEastView[y + self.size * 2][x + self.size * 1] = self.matRot(self.TF, 0)[y][x]
                cubeEastView[y + self.size * 2][x + self.size * 2] = self.matRot(self.EF, 0)[y][x]
                cubeEastView[y + self.size * 3][x + self.size * 0] = self.matRot(self.SF, 1)[y][x]
                cubeEastView[y + self.size * 4][x + self.size * 0] = self.matRot(self.EF, 2)[y][x]

        return cubeEastView
    
    # Create a cube pattern centered on the west face of the cube with all connected faces
    def createCubeWestView(self) -> list[list[int]]:
        cubeWestView = [[-1] * (self.size * 3) for _ in range(self.size * 5)]

        for y in range(self.size):
            for x in range(self.size):
                cubeWestView[y + self.size * 0][x + self.size * 2] = self.matRot(self.WF, 2)[y][x]
                cubeWestView[y + self.size * 1][x + self.size * 2] = self.matRot(self.NF, 1)[y][x]
                cubeWestView[y + self.size * 2][x + self.size * 0] = self.matRot(self.WF, 0)[y][x]
                cubeWestView[y + self.size * 2][x + self.size * 1] = self.matRot(self.TF, 0)[y][x]
                cubeWestView[y + self.size * 2][x + self.size * 2] = self.matRot(self.EF, 0)[y][x]
                cubeWestView[y + self.size * 3][x + self.size * 2] = self.matRot(self.SF, 3)[y][x]
                cubeWestView[y + self.size * 4][x + self.size * 2] = self.matRot(self.WF, 2)[y][x]

        return cubeWestView

    # Create a raimbow pattern with all steps and gestion of top face step by distance
    def createRaimbow(self) -> list[list[int]]:
        raimbowPattern = []
        raimbowTop = self.matriceDist(self.TF)
        for i in range(len(raimbowTop)):
            raimbowPattern.append(raimbowTop[i])
        
        for y in range(self.size):
            step = []
            for x in range(self.size):
                step.append(self.SF[y][x])
                step.append(self.matRot(self.EF, 1)[y][x])
                step.append(self.matRot(self.NF, 2)[y][x])
                step.append(self.matRot(self.WF, 3)[y][x])

            raimbowPattern.append(step)

        return raimbowPattern
    
    # Update the raimbow color
    def raimbowColorUpdate(self) -> None:
        self.RAIMBOWCOLOR = (self.RAIMBOWCOLOR - 1) % 255

    # Update the brightness
    def brightnessUpdate(self) -> None:
        self.BRIGHTNESS = self.BRIGHTNESS + self.BRIGHTNESS_INCREASE

        if self.BRIGHTNESS >= 0.1 or self.BRIGHTNESS <= 0.01:
            self.BRIGHTNESS_INCREASE = -self.BRIGHTNESS_INCREASE

    def __init__(self, size: int, pixels: neopixel.NeoPixel, keys: keypad.KeyMatrix, TF: list[list[int]], NF: list[list[int]], SF: list[list[int]], EF: list[list[int]], WF: list[list[int]]):
        self.RAIMBOWCOLOR: int = 0
        self.BRIGHTNESS: int = 0.1
        self.BRIGHTNESS_INCREASE: int = -0.0005

        self.colorEffect: int = 5
        self.color: int = 0
        self.colorSwitch: int = TF[0][0]

        self.size: int = size
        self.p: neopixel.NeoPixel = pixels
        self.k: keypad.KeyMatrix = keys

        self.TF: list[list[int]] = TF
        self.NF: list[list[int]] = NF
        self.SF: list[list[int]] = SF
        self.EF: list[list[int]] = EF
        self.WF: list[list[int]] = WF

        self._CTV: list[list[int]] = self.createCubeTopView() # Cube Top View
        self._CNV: list[list[int]] = self.createCubeNorthView() # Cube North View
        self._CSV: list[list[int]] = self.createCubeSouthView() # Cube South View
        self._CEV: list[list[int]] = self.createCubeEastView() # Cube East View
        self._CWV: list[list[int]] = self.createCubeWestView() # Cube West View

        self.RP: list[list[int]] = self.createRaimbow() # Raimbow Pattern
