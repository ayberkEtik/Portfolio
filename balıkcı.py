#This Code for simple clicking

#İmporting package
import time
import pyautogui as pg
import keyboard

#Time between clicks
sleepTime = 7.6

while keyboard.is_pressed('q') != True:
    time.sleep(sleepTime)
    pg.leftClick()
    pg.leftClick()
