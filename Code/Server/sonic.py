from Ultrasonic import *

if __name__ == '__main__':
    ultrasonic_otonom = Ultrasonic()

    try:
        while True:
            data= ultrasonic_otonom.getDistance()   #Get the value
            
                
            f = open("distance.txt" , "w")    
            f.write(str(data))
            f.close()
            if(data < 15):
                break
            time.sleep(1)
            
    except KeyboardInterrupt:
        print ("\nEnd of program")
        
