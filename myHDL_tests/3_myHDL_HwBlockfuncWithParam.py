'''
this example shows a hardware block (function) with parameter 
clock generation using @instance decorator is used here 
'''

from myhdl import block, delay, instance, Signal, always, now

clk = Signal(0)
gap = ""
# in myHDL a function's parameter is way to model PORT 
@block
def clkDriver(clk, period=20):
	lowTime  = int(period/2)
	highTime = period - lowTime

	# this function is a geneartor function as it has yield 
	# @instance decorator is less sophisticated than @always decorator 
	# @instance decorator is used to return a generator function 
	@instance
	def drive_clk():
		while True:                # to make sure generator runs forever it is wrapped in while True loop
			yield delay(lowTime)   # yield is similar to VHDL: wait for 
			clk.next = 1
			yield delay(highTime)
			clk.next = 0
		
	@always(clk.posedge)
	def at_pos_clk():
		global gap
		print("T:%s %s__|````|__" %(now(), gap))
		gap +="          "

	@always(clk.negedge)
	def at_neg_clk():
		global gap
		print("T:%s %s``|____|``"  % (now(), gap))
		gap +="          "

	return drive_clk, at_pos_clk, at_neg_clk

inst1 = clkDriver(clk)
inst1.run_sim(100)


			