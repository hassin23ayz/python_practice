'''
this example shows a hardware block (function) without parameter 
'''

from myhdl import block, Signal, delay, always, now

# def LedDriver(): A hardware module is modeled by a function 
#                  The parameter list of the function is used to define the interface of the hardware block
# @block         : block decorator makes the function a hardware block  
@block
def LedDriver():
    # Signal     : Signal object is like VHDL Signal
    # def blink(): local function inside the hw block defines desired behaviour of the hw block
    # @always    : decorator that has delay object param . behind the curtain it is a geneartor(yield)
    #              the decorated function also becomes a generator 
    # delay(n)   : is a param, function will be executed whenever the specified delay interval has expired
    clk = Signal(0)
    # print(dir(clk))

    @always(delay(10))
    def drive_clk():
    	clk.next = not clk

    @always(clk.posedge)
    def at_pos_clk():
    	print("T:%s __|````|__" % now(), end = "")

    @always(clk.negedge)
    def at_neg_clk():
    	print("T:%s ``|____|``"  % now())

    @always(clk.posedge)
    def blink():
        print("T:%s Led Blinks!" % now())
    # returning a generator 
    return drive_clk, at_pos_clk, at_neg_clk, blink


inst = LedDriver()
# simulation : run the hardware block for 100 timesteps
inst.run_sim(100)

