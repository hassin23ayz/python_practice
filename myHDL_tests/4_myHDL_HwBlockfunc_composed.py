'''
in this example we will create a higher level function with four instances of lower level function
'''
from myhdl import block, delay, instance, Signal, always, now


@block
def clkDriver(clk, period=20):
	lowTime  = int(period/2)
	highTime = period - lowTime

	@instance
	def drive_clk():
		while True:               
			yield delay(lowTime)   
			clk.next = 1
			yield delay(highTime)
			clk.next = 0

	return drive_clk

@block
def LedDriver(clk, ledNo):
    @always(clk.posedge)
    def at_pos_clk():
    	print("T:%s LedNo %d Blinks" % (now(), ledNo))

    return at_pos_clk

@block
def myFancyLedCkt():
	clk1 = Signal(0)
	clk2 = Signal(0)

	mClkDriver1 = clkDriver(clk1)
	mClkDriver2 = clkDriver(clk2, 10)

	mLed1 = LedDriver(clk1, 1)
	mLed2 = LedDriver(clk2, 2)

	return mClkDriver1, mClkDriver2, mLed1, mLed2

inst = myFancyLedCkt()
inst.run_sim(50)