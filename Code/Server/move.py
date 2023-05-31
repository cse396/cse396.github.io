import time
import os
read_path =  "/tmp/pythonread_fifo"

def forward():
    while True:
        f = open("distance.txt", "r")
        data = int(f.read())
        if(data < 15 and data != 0):
            break
        print("yürüyor!!");
        time.sleep(1)
    print("durdu!!")
            
def right():
    print("saga donuyor!!")

def left():
    print("sola donuyor!!")
    
def tenStep():
    for i in range(10):
        f = open("distance", "r")
        if(f < 15 and f != 0):
            break
        print(str(i) +". adim!!")

def switch(data):
    if data == "forward":
        forward()
    elif data == "right":
        right()
    elif data == "left":
        left();
    elif data == "tenStep":
        tenStep()
    elif data == "quit":
        quit()
    
if __name__=='__main__':
    try:
        os.mkfifo(read_path)
    except:
        pass

    fd = os.open(read_path, os.O_RDONLY | os.O_NONBLOCK)
    
    data = os.read(fd, 20)
    data = data.decode('utf-8')
    if len(data) == 0:
        print("Writer closed")
    switch(data)