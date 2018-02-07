# eng ali gamal 

# ch02_01.py file
import wiringpi2 as wiringpi
import time
# initialize
wiringpi.wiringPiSetup()
# define GPIO pins
pin_a = 15
pin_b = 16
pin_c = 1
pin_dip = 4
pin_d = 5
pin_e = 6
pin_f = 10
pin_g = 11

LOW = 0
HIGH = 1
OUTPUT = 1
# define GPIO mode
wiringpi.pinMode(pin_a, OUTPUT)
wiringpi.pinMode(pin_b, OUTPUT)
wiringpi.pinMode(pin_c, OUTPUT)
wiringpi.pinMode(pin_dip, OUTPUT)
wiringpi.pinMode(pin_d, OUTPUT)
wiringpi.pinMode(pin_e, OUTPUT)
wiringpi.pinMode(pin_f, OUTPUT)
wiringpi.pinMode(pin_g, OUTPUT)
def showNumber(number, dip):
if dip:
wiringpi.digitalWrite(pin_dip, HIGH)
else:
wiringpi.digitalWrite(pin_dip, LOW)
if number == 0:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, HIGH)
wiringpi.digitalWrite(pin_f, HIGH)
wiringpi.digitalWrite(pin_g, LOW)
elif number == 1:
wiringpi.digitalWrite(pin_a, LOW)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, LOW)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, LOW)
wiringpi.digitalWrite(pin_g, LOW)
elif number == 2:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, LOW)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, HIGH)
wiringpi.digitalWrite(pin_f, LOW)
wiringpi.digitalWrite(pin_g, HIGH)
elif number == 3:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, LOW)
wiringpi.digitalWrite(pin_g, HIGH)
elif number == 4:
wiringpi.digitalWrite(pin_a, LOW)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, LOW)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, HIGH)
wiringpi.digitalWrite(pin_g, HIGH)
elif number == 5:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, LOW)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, HIGH)
wiringpi.digitalWrite(pin_g, HIGH)
elif number == 6:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, LOW)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, HIGH)
wiringpi.digitalWrite(pin_f, HIGH)
wiringpi.digitalWrite(pin_g, HIGH)
elif number == 7:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, LOW)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, LOW)
wiringpi.digitalWrite(pin_g, LOW)
elif number == 8:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, HIGH)
wiringpi.digitalWrite(pin_f, HIGH)
wiringpi.digitalWrite(pin_g, HIGH)
elif number == 9:
wiringpi.digitalWrite(pin_a, HIGH)
wiringpi.digitalWrite(pin_b, HIGH)
wiringpi.digitalWrite(pin_c, HIGH)
wiringpi.digitalWrite(pin_d, HIGH)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, HIGH)
wiringpi.digitalWrite(pin_g, HIGH)
def clear_all():
wiringpi.digitalWrite(pin_a, LOW)
wiringpi.digitalWrite(pin_b, LOW)
wiringpi.digitalWrite(pin_c, LOW)
wiringpi.digitalWrite(pin_d, LOW)
wiringpi.digitalWrite(pin_e, LOW)
wiringpi.digitalWrite(pin_f, LOW)
wiringpi.digitalWrite(pin_g, LOW)
wiringpi.digitalWrite(pin_dip, LOW)
try:
while 1:
print("display 0")
showNumber(0, HIGH)
time.sleep(2)
print("display 1")
showNumber(1, HIGH)
time.sleep(2)
print("display 2")
showNumber(2, HIGH)
time.sleep(2)
print("display 3")
showNumber(3, HIGH)
time.sleep(2)
print("display 4")
showNumber(4, HIGH)
time.sleep(2)
print("display 5")
showNumber(5, HIGH)
time.sleep(2)
print("display 6")
showNumber(6, HIGH)
time.sleep(2)
print("display 7")
showNumber(7, HIGH)
time.sleep(2)
print("display 8")
showNumber(8, HIGH)
time.sleep(2)
print("display 9")
showNumber(9, HIGH)
time.sleep(2)
clear_all()
except KeyboardInterrupt:
clear_all()
print("done")