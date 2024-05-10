class WDSA:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0

    def AddW(self): # up
        self.Y += 1
        if self.Y > self.yMax:
            self.yMax = self.Y
    
    def AddD(self): # right
        self.X += 1
        if self.X > self.xMax:
            self.xMax = self.X
    
    def AddS(self): # down
        self.Y -= 1
        if self.Y < self.yMin:
            self.yMin = self.Y
    
    def AddA(self): # left
        self.X -= 1
        if self.X < self.xMin:
            self.xMin = self.X

    def TotalSum(self) -> int:
        if self.X == self.xMin == self.xMax and self.Y == self.yMin == self.yMax:
            return 0
        else:
            return 1

    def GetResultString(self):
        return f"{self.xMax - self.xMin + 1} {self.yMax - self.yMin + 1}"