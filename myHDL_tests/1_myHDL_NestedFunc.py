import sys
if '..\\customModules' not in sys.path:
    sys.path.append('..\\customModules')
from ShowLine import Ln 

# <----- example to showcase nested function behaviour ----->
def parent_func():
	def child_func():
		print(Ln(True), "I am a func defined in another function ")
	return child_func

#>1
parent_func()
print(Ln(True), parent_func())

#>2
try:
	child_func()
	print(child_func())
except Exception as e:
	print(Ln(True),"An error occured = ", e)

#>3
funcObj = parent_func()
funcObj()
funcObj()
# <----------------------------------------------->

