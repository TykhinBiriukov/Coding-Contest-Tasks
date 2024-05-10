import itertools


class Field:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.Count = self.Height*self.Width - 1
    
    def TreeXY(self, x: int, y: int):
        self.TreeX = x
        self.TreeY = y
    
    def PointCount(self):
        zeros = {0, 0}
        coords = {self.Width, self.Height}
        numberOfPoint = list(itertools.product(zeros, coords))
        self.Count = len(numberOfPoint) - 1