"""
from gpiozero import Servo
from time import sleep
servo1 = Servo(13)

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

"""        
# Import libraries
import RPi.GPIO as GPIO
import time
import math
# Set GPIO numbering mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(33,GPIO.OUT)
servo1 = GPIO.PWM(33,50) # Note 11 is pin, 50 = 50Hz pulse

servo1.start(0)

# Define variable duty

duty = 2
degree = 0
# Loop for duty values from 2 to 12 (0 to 180 degrees)
print("servo")

while True:
    while duty < 12:
      degree = (duty - 2) * 18
      degree = math.floor(degree)
      f = open("degree.txt" , "w")  
      f.write(str(degree))
      f.close()
      servo1.ChangeDutyCycle(duty)
      time.sleep(0.1)
      duty = duty + 2/18
      time.sleep(0.1)
        
    degree = (duty - 2) * 18

    # Wait a couple of seconds

    #turn back to 0 degrees
    while duty > 0:
      degree = (duty - 2) * 18
      degree = math.floor(degree)
      f = open("degree.txt" , "w")    
      f.write(str(degree))
      f.close()
      servo1.ChangeDutyCycle(duty)
      time.sleep(0.1)
      duty = duty - 2/18
      time.sleep(0.1)
    duty = 2

"""
from gpiozero import Servo
import RPi.GPIO as GPIO
import time
import math
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
factory = PiGPIOFactory()
servo=Servo(13,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000, pin_factory=factory)

def get_sonic_mapping(deg):
  print(deg)
  distrad = []
  i = deg
  servo.value = math.sin(math.radians(i))
  sleep(2)
  return distrad
  """
  for j in range(2):
    if j == 0:
      GPIO.setmode(GPIO.BCM)
      TRIG = 6 #6
      ECHO = 5 #5

      #GPIO.setwarnings(False)
      GPIO.setup(TRIG, GPIO.OUT)
      GPIO.setup(ECHO, GPIO.IN)
    else:
      GPIO.setmode(GPIO.BCM)
      TRIG = 25 #6
      ECHO = 24 #5

      #GPIO.setwarnings(False)
      GPIO.setup(TRIG, GPIO.OUT)
      GPIO.setup(ECHO, GPIO.IN)
      i-=180
      

    time.sleep(0.3)

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
    print(distance)
    distrad.append((distance,i))
    GPIO.cleanup()
  """
  return distrad
