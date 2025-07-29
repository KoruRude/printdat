import random
import os
from PIL import Image
printFileType = input("Print File Extension: ")
printFileName = input("Print File Name: ")
im = Image.open(printFileName + "." + printFileType)
px = im.load()
imgWidth = int(input("Print Image Width (32-480): "))
scaleFactor = im.size[0]/(imgWidth)
calibration = 51/42 #width divided by height

#inputs 0-64
def matrixValue(brightness, position=0):
    if(random.randrange(1, 64) < brightness): #Random Engine
    #if(32 < brightness): #fall-off
        return False
    else:
        return True

def brightNes(xs, ys):
    try:
        return int((px[xs,ys][0] + px[xs,ys][1] + px[xs,ys][2])/3/4)
    except:
        print("ERROR DUMP:")
        print("xs: " + str(xs))
        print("ys: " + str(ys))
        print("Size: " + str(im.size))
        print("Scale factor: " + str(scaleFactor))
        print("Range: " + str(int(im.size[1] * scaleFactor)))

print("size/scaleFactor: " + str(int(im.size[1] / scaleFactor)))
arrayOutput = []

#generate array 
#arrayOutput[Line][Character]
for y in range(int((im.size[1] / scaleFactor) * calibration)):
    arrayOutput.append([])
    for x in range(imgWidth):
        brt =  brightNes(int(x * scaleFactor), int(y * scaleFactor / calibration))
        if (matrixValue(brt, x + y)):
            brt = True ## -dot
        else:
            brt = False # -no dot
        #print(brt, end="")
        arrayOutput[y].append(brt)


#output array as termina image
def outputArrayImage():
    outputArrCali = .40
    for y in range(int(len(arrayOutput)*outputArrCali)):
        for x in range(len(arrayOutput[y])):
            if(arrayOutput[int(y/outputArrCali)][x]):
                print("#", end="")
            else:
                print(" ", end="")
        print("")
outputArrayImage()


#Build Data file
#set filename
fileName = printFileName + str(imgWidth) + ".dat"
try:
    os.remove(fileName)
except Exception as e:
    print(f"An error occurred: {e}")
def append(input):
    with open(fileName, "a") as myfile:
        myfile.write(input)
        myfile.write("\n")

#removes existing file to prevent program overlap
try:
    os.remove(fileName)
except Exception as e:
    print(f"An error occurred: {e}")

#sets first number to img width for PrintDat program
append(str(imgWidth) + ",")
lineFileArray = []
endReached = False
for y in range(0, len(arrayOutput), 7):

    #output basic program
    
    #data run
    dataLineStr = ""
    exceptionOutput = False
    for x in range(len(arrayOutput[y])):
        #determine number code:
        numberCode = 0
        try:
            if (arrayOutput[y][x]):
                numberCode = numberCode + 64
        except:
            exceptionOutput = True
        try:
            if (arrayOutput[y + 1][x]):
                numberCode = numberCode + 32
        except:
            exceptionOutput = True
        try:
            if (arrayOutput[y + 2][x]):
                numberCode = numberCode + 16
        except:
            exceptionOutput = True
        try:
            if (arrayOutput[y + 3][x]):
                numberCode = numberCode + 8
        except:
            exceptionOutput = True
        try:
            if (arrayOutput[y + 4][x]):
                numberCode = numberCode + 4
        except:
            exceptionOutput = True
        try:
            if (arrayOutput[y + 5][x]):
                numberCode = numberCode + 2
        except:
            exceptionOutput = True
        try:
            if (arrayOutput[y + 6][x]):
                numberCode = numberCode + 1
        except:
            exceptionOutput = True
        
        dataLineStr = dataLineStr + str(numberCode)
        dataLineStr = dataLineStr + ","
        if(len(dataLineStr) >= 75):
            append(dataLineStr)
            dataLineStr = ""
        else:
            continue #dataLineStr = dataLineStr + ","
        #make new data line
    
    
    
    #this needs fix
    if not endReached:
        if (y != len(arrayOutput[y])-1):
            if exceptionOutput:
                print("Exception output reached for line")
                dataLineStr = dataLineStr + "129"
                append(dataLineStr)
                endReached = True
            else:
                dataLineStr = dataLineStr + "128,"
                append(dataLineStr)
        else:
            dataLineStr = dataLineStr + "129"
            append(dataLineStr)
    
