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
import io
import os
import time
import fcntl
import socket
import struct
from threading import Condition
import threading
import lidar_servo

factory = PiGPIOFactory()
servo=Servo(13,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000, pin_factory=factory)

def get_sonic_mapping_rotation(deg):
	i = deg
	servo.value = math.sin(math.radians(i))

def get_sonic_mapping(deg, back_servo, forw_servo):
	print(deg)
	distrad = []
	i = deg
	servo.value = math.sin(math.radians(i))
	sleep(0.5)

	for j in range(2):
		if j == 0:
			GPIO.setmode(GPIO.BCM)
			TRIG = 6 #6
			ECHO = 5 #5

			#GPIO.setwarnings(False)
			GPIO.setup(TRIG, GPIO.OUT)
			GPIO.setup(ECHO, GPIO.IN)
			i=back_servo
		else:
			GPIO.setmode(GPIO.BCM)
			TRIG = 25 #6
			ECHO = 24 #5

			#GPIO.setwarnings(False)
			GPIO.setup(TRIG, GPIO.OUT)
			GPIO.setup(ECHO, GPIO.IN)
			i=forw_servo
	  

		time.sleep(0.7)

		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)==0:
			print('test' + str(j))
			pulse_start = time.time()

		while GPIO.input(ECHO)==1:
			print('test2')
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150
		distance = round(distance, 2)
		print(distance)
		distrad.append((distance,i))
		GPIO.cleanup()
	return distrad
  
def send_data(self,connect,data):
	try:
		connect.send(data.encode('utf-8'))
		#print("send",data)
	except Exception as e:
		print(e)
		
def get_interface_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
										0x8915,
										struct.pack('256s',b'wlan0'[:15])
										)[20:24])

HOST=get_interface_ip()
server_socket2 = socket.socket()
server_socket2.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
server_socket2.bind((HOST, 9001))
server_socket2.listen(1)

try:
	connection2,client_address2 = server_socket2.accept()
	print ("Client connection successful !")
except:
	print ("Client connect failed")
i = 0
while True:
	command='#'+str(get_sonic_mapping(i))+"\n"
	print(command)
	#send_data(connection2, command)
	i += 15
	i=i%360

