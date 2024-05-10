from WDSA import *

inPath: str = "C:\\Users\\pichu\\OneDrive\\Рабочий стол\\Ausbildung\\2ndSemester\\contest\\Level2\\in\\"
fileName: str = "level2_5"

with open(inPath + fileName + ".in", 'r') as file:
    content = file.read()

strArray: list[str] = content.split("\n")


iteration: int = int(strArray[0]) # 3
del strArray[0] # delete number
generalString: str = ""


for i in strArray:
    wdsa: WDSA = WDSA()
    for j in i:
        if j == "W":
            wdsa.AddW() 
        elif j == "D":
            wdsa.AddD()
        elif j == "S":
            wdsa.AddS()
        elif j == "A":
            wdsa.AddA()
    if wdsa.TotalSum() != 0:
        generalString += wdsa.GetResultString() + '\n'

outPath: str = "C:\\Users\\pichu\\OneDrive\\Рабочий стол\\Ausbildung\\2ndSemester\\contest\\Level2\\out\\"
with open(outPath + fileName + ".out", 'w') as file:
    file.write(generalString)
        

