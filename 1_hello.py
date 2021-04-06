#Single Line comment
'''
this
is
multiple line comment 
'''
'''
print("hello world")

userAge, userName = 30, "Peter"
print(userAge)
print(userName)

x = 5
y  = 2
print(x/y)   #division
print(x//y)  #floor_division
print(x%y)   #remainder
print(x**y)  #exponent

mobileNo = 121212121 #integer type data
balance  = -0.023    #float type data
customerName = "tom hanks" #string type data
customerGender = " IS MALE"
customerInfo = customerName.upper() + customerGender.lower()
#print(customerInfo)

info = "the customer %s %s \nhave cell no %d with balance %4.2f" %(customerName,customerGender,mobileNo,balance)
info2 = "the customer {0:s} {1:s} \nhave cell no {2:d} with balance {3:4.2f}".format(customerName,customerGender,mobileNo,balance)
info3 = "the customer {} {} \nhave cell no {} with balance {}".format(customerName,customerGender,mobileNo,balance)
#print(info3)

#-------------------------------------type casting
#type casting to int
print(int(2.45))          #float to int
print(int("245"))         #string to int

#type casting to float
print(float(2))           #int to float
print(float("2.45"))      #strint to float

#type casting to string
print(str(2))             #int to string
print(str(2.45))          #float to string

#-------------------------------------List []
myList = [1,2,3,4,5,"hello"]
print(myList)
print(myList[2])
print(myList[-1])
myList2 = []
myList2 = myList
print(myList2)
myList2 = myList[1:5]
print(myList2)
myList[1] = 20
print(myList)
myList.append("how are you")
print(myList)
del myList[5]
print(myList)

#-------------------------------------tuple ()
monthsOfyear = ("jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(monthsOfyear)

monthsOfyear[1] = "leapFeb" #cannot alter element

monthsOfyear = monthsOfyear + ("vodro", "ashin", "shit")
print(monthsOfyear)

#-------------------------------------Dictionary {} 
userNameAndAge = {"peter":38, "john":25, "alvin":"not given"}
print(userNameAndAge)
print(userNameAndAge["john"])
userNameAndAge["Tom"]=56
print(userNameAndAge)
del userNameAndAge["alvin"]
print(userNameAndAge)
'''

#dictionary key and data types can be of different data types
myDict = {"One":1.35, 2.5:"two point five", 3:"+", 7.9:2 }
print(myDict)
myDict["newItem"] = "I am new"
print(myDict)








