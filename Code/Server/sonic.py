import RPi.GPIO as GPIO
import time # right
GPIO.setmode(GPIO.BCM)

TRIG = 25 #6
ECHO = 24 #5

#GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        
        GPIO.output(TRIG, False)

        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if distance > 1 and distance < 400:
            f = open("distanceSonicRight.txt" , "w") 
            f.write(str(distance))
            print(distance)
            f.close()

except KeyboardInterrupt: 
	print("ctrl-c geldi")
	GPIO.cleanup()

finally:
    GPIO.cleanup()
	


