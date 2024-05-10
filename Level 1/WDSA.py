class WDSA:
    def __init__(self):
        self.W: int = 0
        self.D: int = 0
        self.S: int = 0
        self.A: int = 0

    def AddW(self):
        self.W += 1
    
    def AddD(self):
        self.D += 1
    
    def AddS(self):
        self.S += 1
    
    def AddA(self):
        self.A += 1

    def TotalSum(self) -> int:
        return self.W + self.D + self.S + self.A 

    def GetResultString(self):
        return f"{self.W} {self.D} {self.S} {self.A}"