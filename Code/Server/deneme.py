"""from gpiozero import Servo
from time import sleep
servo = Servo(26)

try:
        while(True):
              servo.value=-1
              sleep(1)
              servo.value=-0.5
              sleep(1)
              servo.value=0
              sleep(1)
              servo.value=0.5
              sleep(1)
              servo.value=1
              sleep(1)

except KeyboardInterrupt:
        print("Stop")
        """
        
# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(33,GPIO.OUT)
servo1 = GPIO.PWM(33,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Define variable duty
duty = 2
degree = 0
# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty < 12:
    degree = (duty - 2) * 18
    print("degree: ", degree)
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.1)
    duty = duty + 0.5
    
degree = (duty - 2) * 18
print("degree: ", degree)
# Wait a couple of seconds
time.sleep(2)

#turn back to 0 degrees
while duty > 0:
    degree = (duty - 2) * 18
    print("degree: ", degree)
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.1)
    duty = duty - 0.5

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye") 
