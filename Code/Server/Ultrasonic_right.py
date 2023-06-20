import time
import RPi.GPIO as GPIO
class Ultrasonic_right:
    def __init__(self):
        GPIO.setwarnings(False)
        self.trigger_pin = 25
        self.echo_pin = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)
    def send_trigger_pulse(self):
        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin,False)

    def pulseIn(self,pin,level,timeOut): # obtain pulse time of a pin under timeOut
        t0 = time.time()
        while(GPIO.input(pin) != level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        pulseTime = (time.time() - t0)*1000000
        return pulseTime
        
    def getDistance(self):
        distance_cm=[0,0,0]
        for i in range(3):
            self.send_trigger_pulse()
            pingTime = self.pulseIn(self.echo_pin,GPIO.HIGH,300*60)
            distance_cm[i] = pingTime * 340.0 / 2.0 /10000.0
        distance_cm=sorted(distance_cm)
        return int(distance_cm[1])
        
# Main program logic follows:
"""
if __name__ == '__main__':
    ultrasonic_otonom = Ultrasonic_right()

    try:
        while True:
            data= ultrasonic_otonom.getDistance()   #Get the value
            f = open("distance.txt" , "w")    
            f.write(str(data))
            f.close()
            if(data < 15 and data != 0):
                break
            time.sleep(1)
            
    except KeyboardInterrupt:
        print ("\nEnd of program")
"""
