'''
"r"  mode : For reading only
"w"  mode : For writing only
"a"  mode : For appending only
"r+" mode : For both reading and writing 

f = open("myFile.txt", "r")

firstLine  = f.readline() #readline() adds the '\n' character to the end of each line 
secondLine = f.readline()

print(firstLine, end = "")
print(secondLine)

f.close()

def printFileContents():
    f = open("myFile.txt", "r")
    for eachLine in f:
        print(eachLine,end = "")
    f.close()
    print("")
    return None

printFileContents()

f = open("myFile.txt", "a")
f.write(" same line addon ")
f.write("\n Python is fun ")
f.close()

printFileContents()

inputFile  = open("myFile.txt", 'r')
outputFile = open("myOutputFile.txt", 'w')

msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)
inputFile.close()
outputFile.close()
'''

#binary files refer to any file that contains non text
inputFile = open("waveR.jpg",'rb')
outputFile = open("waveW.jpg", 'wb')

bStream = inputFile.read(10)
while len(bStream):
    outputFile.write(bStream)
    bStream = inputFile.read(10)
inputFile.close()
outputFile.close()

import os
os.rename("waveR.jpg", "waveR_converted.jpg")

    








