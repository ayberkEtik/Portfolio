import time
import pyautogui as pg
import keyboard
import win32api, win32con
counter = 0
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
time.sleep(5)
while keyboard.is_pressed('q') != True:
    mx,my = pg.position()
    time.sleep(0.35)
    click(mx,my)