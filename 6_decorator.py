'''
> python decorator allows one to extend and modify the behaviour of a callable [ functions, methods, classes]
without permanently modifying the callable itself

> A decorator is a callable that takes a callable as input and returns another callable 

'''

def null_decorator(func):
	return func

def upperCase_decorator(func):
	def wrapper():
		original_result = func()
		modified_result = original_result.upper()
		return modified_result
	return wrapper

@upperCase_decorator
def greet():
	return "hello"

# funcObj = null_decorator(greet)
# print(greet())
# print(funcObj())

print(greet())
