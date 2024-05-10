class WDSA:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0
        self.coordList: list[tuple[int, int]] = []
        self.coordList.append((0,0))

    def AddW(self): # up
        self.Y += 1
        if self.Y > self.yMax:
            self.yMax = self.Y
        self.coordList.append((self.X, self.Y))
    
    def AddD(self): # right
        self.X += 1
        if self.X > self.xMax:
            self.xMax = self.X
        self.coordList.append((self.X, self.Y))
    
    def AddS(self): # down
        self.Y -= 1
        if self.Y < self.yMin:
            self.yMin = self.Y
        self.coordList.append((self.X, self.Y))
    
    def AddA(self): # left
        self.X -= 1
        if self.X < self.xMin:
            self.xMin = self.X
        self.coordList.append((self.X, self.Y))

    def TotalSum(self) -> int:
        if self.X == self.xMin == self.xMax and self.Y == self.yMin == self.yMax:
            return 0
        else:
            return 1

    def CheckCrossing(self) -> bool:
        self.seen: set = set()
        for t in self.coordList:
            if t in self.seen:
                return True
            self.seen.add(t)
        return False
    
    def CheckTree(self, x: int, y: int) -> bool:
        treeX: int = self.xMin + x
        treeY: int = self.yMax - y
        self.Tree = (treeX, treeY)
        if self.Tree in self.seen:
            return True
        else:
            return False
        
    def CheckCount(self, fieldCount):
        if len(self.coordList) != fieldCount:
            return True
        else:
            return False

    def GetResultString(self):
        return f"{self.xMax - self.xMin + 1} {self.yMax - self.yMin + 1}"