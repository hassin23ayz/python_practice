'''
#Functions
def checkIfPrime(num2chck):
    if(num2chck%2 == 0):
        return False
    else:
        return True

for eachNum in range(0,10,1):
    if checkIfPrime(eachNum):
        print(eachNum)

#local vs global vars
rawDataTopic = "rawData/"          #global var
def addCommonTopicPrefix(bcktStr): #string is immutable
    prefix = "Telemetry/"          #local var
    newStr = prefix + bcktStr       
    return newStr 

topic2Subscribe = rawDataTopic
topic2Subscribe = addCommonTopicPrefix(topic2Subscribe)
print(topic2Subscribe)


#import external module
import random as Mod_random
print(Mod_random.randrange(1,10))   
'''
#import external module made by me

import sys
if '.\\customModules' not in sys.path:
    sys.path.append('.\\customModules')

import PrimeChecker
for eachNum in range(0,10,1):
    if PrimeChecker.checkIfPrime(eachNum):
        print(eachNum)
