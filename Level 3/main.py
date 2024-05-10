from WDSA import *
from Field import *

inPath: str = "C:\\Users\\pichu\\OneDrive\\Рабочий стол\\Ausbildung\\2ndSemester\\contest\\Level3\\in\\"
fileName: str = "level3_5"
resultMessage: str = ""

with open(inPath + fileName + ".in", 'r') as file:
    content = file.read()

strArray: list[str] = content.split("\n")
pathNum: int = int(strArray[0]) # 3

row: int = 1
for path in range(pathNum):
    field: str = strArray[row]
    fieldSize: list[str] = field.split(" ")
    field: Field = Field(int(fieldSize[0]), int(fieldSize[1]))
    row += 1
    
    for r in range(field.Height):
        fieldRow = strArray[row]
        row += 1 

        Xindex: int = fieldRow.find("X")
        if Xindex != -1:
            field.TreeX = Xindex
            field.TreeY = r          
    
    wdsa: WDSA = WDSA()
    commandString: str = strArray[row]
    for i in commandString:
        if i == "W":
            wdsa.AddW() 
        elif i == "D":
            wdsa.AddD()
        elif i == "S":
            wdsa.AddS()
        elif i == "A":
            wdsa.AddA()

    if wdsa.CheckCrossing():
        resultMessage += "INVALID\n"
        row += 1
        continue

    if wdsa.CheckTree(field.TreeX, field.TreeY):
        resultMessage += "INVALID\n"
        row += 1
        continue

    if wdsa.CheckCount(field.Count):
        resultMessage += "INVALID\n"
        row += 1
        continue

    resultMessage += "VALID\n"
    row += 1

# generalMessage = resultMessage.rstrip('\n')
outPath: str = "C:\\Users\\pichu\\OneDrive\\Рабочий стол\\Ausbildung\\2ndSemester\\contest\\Level3\\out\\"
with open(outPath + fileName + ".out", 'w') as file:
    file.write(resultMessage)
        

