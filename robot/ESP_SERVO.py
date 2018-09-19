import ESP_PWM	
import time
print("v1")						
ESP_PWM.PWM_INIT(50)
for i in range(100):

	PWM_SET(p2,i)
	time.sleep_ms(20)
