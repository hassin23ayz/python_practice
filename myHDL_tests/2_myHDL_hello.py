from myhdl import block, delay, always, now

# def LedDriver(): A hardware module is modeled by a function 
#                  The parameter list of the function is used to define the interface of the hardware block
# @block         : block decorator makes the function a hardware block  
@block
def LedDriver():
    # def blink(): local function inside the hw block defines desired behaviour of the hw block
    # @always    : decorator that has delay object param . behinf the curtain it is a geneartor(yield)
    #              the decorated function also becomes a generator 
    # delay(n)   : is a param, function will be executed whenever the specified delay interval has expired
    @always(delay(10))
    def blink():
        print("at time: %s Led Blinks!" % now())
    # returning a generator 
    return blink


inst = LedDriver()
# simulation : run the hardware block for 100 timesteps
inst.run_sim(100)