from inspect import currentframe

def Ln(decision):
	if decision == True:
	    cf = currentframe()
	    return "L"+ str(cf.f_back.f_lineno) + ":"
	else:
		return None 