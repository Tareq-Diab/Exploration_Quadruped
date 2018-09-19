
import machine
import time
"""
The way to connect your board to the external world, and control other components,
 is through the GPIO pins. Not all pins are available to use, in most cases only pins 0, 2, 4, 5, 12, 13, 14, 15, and 16 can be used.

The pins are available in the machine module, so make sure you import that first
"""

print ("pwm module imported") #informing
p1 =  machine.Pin(0)
p2 =  machine.Pin(2)
p3 =  machine.Pin(4)
p4 =  machine.Pin(5)
p5 =  machine.Pin(12)
p6 =  machine.Pin(13)
p7 =  machine.Pin(14)
p8 =  machine.Pin(15)


"""
Pulse width modulation (PWM) is a way to get an artificial analog output on a
 digital pin. It achieves this by rapidly toggling the pin from low to high.
  There are two parameters associated with this: the frequency of the toggling, 
  and the duty cycle. The duty cycle is defined to be how long the pin is high 
  compared with the length of a single period (low plus high time). Maximum duty 
  cycle is when the pin is high all of the time, and minimum is when it is low all of the time.

On the ESP8266 the pins 0, 2, 4, 5, 12, 13, 14 and 15 all support PWM. The limitation
 is that they must all be at the same frequency, and the frequency must be between 1Hz and 1kHz.

 Hobby servo motors can be controlled using PWM. They require a frequency of 50Hz and then 
 a duty between about 40 and 115, with 77 being the centre value.
 CHECK :"https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/pwm.html" for mor information.

"""
def PWM_INIT(freqin):
	global p1,p2,p3,p4,p5,p6,p7,p8
	p1 =  machine.PWM(machine.Pin(0),freq=freqin)
	p2 =  machine.PWM(machine.Pin(2),freq=freqin)
	p3 =  machine.PWM(machine.Pin(4),freq=freqin)
	p4 =  machine.PWM(machine.Pin(5),freq=freqin)
	p5 =  machine.PWM(machine.Pin(12),freq=freqin)
	p6 =  machine.PWM(machine.Pin(13),freq=freqin)
	p7 =  machine.PWM(machine.Pin(14),freq=freqin)
	p8 =  machine.PWM(machine.Pin(15),freq=freqin)

def PWM_SET(servoPin,Duty):
	servoPin.duty(Duty)
