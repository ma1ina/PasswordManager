import pynput.mouse
import time
import sys
from threading import Thread
def getMousePos():
    global thread_running
    global pozycja
    pozycja=[]
    thread_running=True
    t1 = Thread(target=mousePos)
    t2 = Thread(target=waitTillInput)

    t1.start()
    t2.start()

    t2.join()
    thread_running = False
def mousePos():
    while thread_running:
        mouse=pynput.mouse.Controller()
        pozycja.extend(list(mouse.position))
        print(mouse.position)
        time.sleep(0.1)
        

def waitTillInput():
    input("Press enter when you done")

def getChars():
    getMousePos()
    key="".join([str(abs(i)) for i in pozycja])
    try:
        return key
    except:
        print("Error")


print(getChars())