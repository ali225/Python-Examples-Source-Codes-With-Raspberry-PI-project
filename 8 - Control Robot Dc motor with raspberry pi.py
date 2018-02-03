#by eng ali gamal 
import RPi.GPIO as io
import time 

io.setmode(io.BCM)
in1_pin1 = 27 
in2_pin1 = 22 
in1_pin2 = 20 
in2_pin2 = 21 

io.setup(in1_pin1, io.OUT)
io.setup(in2_pin1, io.OUT)
io.setup(in1_pin2, io.OUT)
io.setup(in2_pin2, io.OUT)

def forward(): 
    io.output(in1_pin1, True)
    io.output(in1_pin2, False) 
    io.output(in2_pin1, True)
    io.output(in2_pin2, False)
	
def reverse():	
    io.output(in1_pin1, False)
    io.output(in1_pin2, True)
    io.output(in2_pin1, False) 
    io.output(in2_pin2, True)
	
def stop() : 
    io.output(in1_pin1, False)
    io.output(in1_pin2, False)
    io.output(in2_pin1, False)
    io.output(in2_pin2, False)

while True:
    cmd = raw_input("Enter f (forward) or r (reverse) or s (stop) :")
    direction = cmd[0]
    if direction == "f":
        forward()
    if direction == "r":
         reverse()
    if direction == "s":
       stop()
	   
	
		
