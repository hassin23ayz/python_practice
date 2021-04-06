'''
#use of while loop
counter = 5
while counter > 0:
    print(counter)
    counter = counter - 1
    
noOfItems = 8
for i in range(0,noOfItems,1):
    print(i)

noOfItems = 8
for i in range(0,noOfItems,1):
    print(i)
    if(i == 5):
        break;

#continue skips loop statements after it 
for i in range(10):
    i = i+1 
    if i==5:
        continue
    print(i)
'''

#try Except
try:
    answer = 12/0
    print(answer)
except Exception as e:
    print("An error occured", e)
    
