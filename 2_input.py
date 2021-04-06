#use of input 
#myName = input("please input your name: ")
#print('''you have set your name
#as %s '''%(myName))

'''
control flow
[if] [for] [while] [try] [except] 

[==] [!=] [<] [>] [<=] [>=]

[and] [or] [not]

userInput = input("Enter 1 or 2")
if userInput == "1":
    print("hello world")
    print("how are you")
elif userInput == "2":
    print("python rocks")
else:
    print("you have not input any valid number") 

#inline if 

userChoice = int(input("choice [1:3]"))
userDecsn  = 0 if userChoice > 3 or userChoice < 1 else userChoice
print("valid Decision %d" %(userDecsn))


#for loop
#looping through an iterable
#iterables : [string] [list] [tuple]

books = ["chemistry", "physics", "math"]
for eachBook in books:
    print (eachBook)

for index, eachBook in enumerate(books):
    print (index, eachBook)

message = "Hello"
for eachCh in message:
    print(eachCh) 

bytesRecvd = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07]
print(bytesRecvd[0:7]) #print upto 0x06
print(bytesRecvd[0:8]) #print upto 0x07
'''

#range(start,end,step)
for i in range(0,8,1):
    print (i)
