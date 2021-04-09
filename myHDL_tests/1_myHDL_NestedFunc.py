from myhdl import block, delay, always, now
from inspect import currentframe

def showLineNo(decision):
	if decision == True:
	    cf = currentframe()
	    return "L"+ str(cf.f_back.f_lineno) + ":"
	else:
		return None 

# <----- example to showcase nested function behaviour ----->
def parent_func():
	def child_func():
		print(showLineNo(True), "I am a func defined in another function ")
	return child_func

#>1
parent_func()
print(showLineNo(True), parent_func())

#>2
try:
	child_func()
	print(child_func())
except Exception as e:
	print(showLineNo(False),"An error occured = ", e)

#>3
funcObj = parent_func()
funcObj()
funcObj()
# <----------------------------------------------->

