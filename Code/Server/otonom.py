from Control import *

def call_forward():
    self = Control()
    ultrasonic2 = Ultrasonic()
    while True:
        print(ultrasonic2.getDistance())
        if ultrasonic2.getDistance() < 15  and ultrasonic2.getDistance() != 0:
            break
            
        self.forWard()
            

#Control py        
if __name__=='__main__':
    call_forward()
        
        

   
