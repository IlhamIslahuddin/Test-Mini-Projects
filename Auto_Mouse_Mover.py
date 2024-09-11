import pyautogui as pag
#you may need to run "pip install pyautogui"
import random
import time

def Mouse_Mover():
    while True:
        x = random.randint(600,700)
        y = random.randint(200,600)
        pag.moveTo(x,y,0.5)
        sleep = random.randint(10,20)
        time.sleep(sleep)

if __name__ == "__main__":
    Mouse_Mover()
