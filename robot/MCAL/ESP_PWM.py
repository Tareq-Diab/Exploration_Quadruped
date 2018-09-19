import machine
print ("pwm module imported")
#identifing the pwm pins
def PWM_INIT(freqin):
	p1 =  machine.PWM(machine.Pin(0),freq(freqin))
	p2 =  machine.PWM(machine.Pin(2),freq(freqin))
	p3 =  machine.PWM(machine.Pin(4),freq(freqin))
	p4 =  machine.PWM(machine.Pin(5),freq(freqin))
	p5 =  machine.PWM(machine.Pin(12),freq(freqin))
	p6 =  machine.PWM(machine.Pin(13),freq(freqin))
	p7 =  machine.PWM(machine.Pin(14),freq(freqin))
	p8 =  machine.PWM(machine.Pin(15),freq(freqin))
"""
def pem_feq(freqin):
	p1.freq(freqin)
	p2.freq(freqin)
	p3.freq(freqin)
	p4.freq(freqin)
	p5.freq(freqin)
	p6.freq(freqin)
	p7.freq(freqin)
	p8.freq(freqin)
"""
def PWM_SET(servoPin,Duty):
	servoPin.duty(Duty)