import quadrov6
"""
p1 >>>>>>>>>>>>>>>>GPIO(0)
p2 >>>>>>>>>>>>>>>>GPIO(2)
p3 >>>>>>>>>>>>>>>>GPIO(4)
p4 >>>>>>>>>>>>>>>>GPIO(5)
p5 >>>>>>>>>>>>>>>>GPIO(12)
p6 >>>>>>>>>>>>>>>>GPIO(13)
p7 >>>>>>>>>>>>>>>>GPIO(14)
p8 >>>>>>>>>>>>>>>>GPIO(15)
"""
print("v3")
def FL(pos):
	if pos=="UP":
		quadrov6.PWM_SET(quadrov6.p2,70)
	elif pos=="DOWN":
		quadrov6.PWM_SET(quadrov6.p2,40)
def FR(pos):
	if pos=="UP":
		quadrov6.PWM_SET(quadrov6.p1,40)
	elif pos=="DOWN":
		quadrov6.PWM_SET(quadrov6.p1,70)
def BL(pos):
	if pos=="UP":
		quadrov6.PWM_SET(quadrov6.p4,40)
	elif pos=="DOWN":
		quadrov6.PWM_SET(quadrov6.p4,60)
def BR(pos):
	if pos=="UP":
		quadrov6.PWM_SET(quadrov6.p3,70)
	elif pos=="DOWN":
		quadrov6.PWM_SET(quadrov6.p3,45)


def FLS(pos):
	if pos=="FOR":
		quadrov6.PWM_SET(quadrov6.p5,80)
	elif pos=="BACK":
		quadrov6.PWM_SET(quadrov6.p5,40)
	elif pos=="MID":
		quadrov6.PWM_SET(quadrov6.p5,60)

def FRS(pos):
	if pos=="FOR":
		quadrov6.PWM_SET(quadrov6.p6,40)
	elif pos=="BACK":
		quadrov6.PWM_SET(quadrov6.p6,80)
	elif pos=="MID":
		quadrov6.PWM_SET(quadrov6.p6,60)
def BLS(pos):
	if pos=="FOR":
		quadrov6.PWM_SET(quadrov6.p7,70)
	elif pos=="BACK":
		quadrov6.PWM_SET(quadrov6.p7,30)
	elif pos=="MID":
		quadrov6.PWM_SET(quadrov6.p7,50)
def BRS(pos):
	if pos=="FOR":
		quadrov6.PWM_SET(quadrov6.p8,40)
	elif pos=="BACK":
		quadrov6.PWM_SET(quadrov6.p8,85)
	elif pos=="MID":
		quadrov6.PWM_SET(quadrov6.p8,60)

def shoulders_reset():
	FLS("MID")
	FRS("MID")
	BLS("MID")
	BRS("MID")







def motors_off():
	quadrov6.PWM_SET(quadrov6.p1,0)
	quadrov6.PWM_SET(quadrov6.p2,0)
	quadrov6.PWM_SET(quadrov6.p3,0)
	quadrov6.PWM_SET(quadrov6.p4,0)
	quadrov6.PWM_SET(quadrov6.p5,0)
	quadrov6.PWM_SET(quadrov6.p6,0)
	quadrov6.PWM_SET(quadrov6.p7,0)
	quadrov6.PWM_SET(quadrov6.p8,0)

def motor_check():
	import time
	FL("UP")
	time.sleep(0.5)
	FLS("FOR")
	time.sleep(0.5)
	FLS("BACK")
	time.sleep(0.5)
	FLS("MID")
	time.sleep(0.5)
	FL("DOWN")
	time.sleep(0.5)
	FR("UP")
	time.sleep(0.5)
	FRS("FOR")
	time.sleep(0.5)
	FRS("BACK")
	time.sleep(0.5)
	FRS("MID")
	time.sleep(0.5)
	FR("DOWN")
	time.sleep(0.5)
	BR("UP")
	time.sleep(0.5)
	BR("DOWN")
	time.sleep(0.5)
	BL("UP")
	time.sleep(0.5)
	BL("DOWN")
	time.sleep(0.5)
	motors_off()


motor_check()