import pyautogui
import time
import sys

print(pyautogui.position())

def countDown():
    timeLeft = 5
    while timeLeft > 0:
        sys.stdout.write(str(timeLeft) + '    \r')
        timeLeft -= 1
        time.sleep(1)
    return

def run_forecast():
    pyautogui.click(x=810, y=1053, clicks=1, interval=0.5, button='right')
    time.sleep(0.5)
    pyautogui.click(x=769, y=551, clicks=1, interval=0.5, button='left')
    time.sleep(5)
    pyautogui.click(x=377, y=50, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=461, y=79, clicks=1, interval=0.5, button='left')
    pyautogui.doubleClick(x=1771, y=336, interval=0.5, button='right')
    pyautogui.click(x=1792, y=468, clicks=1, interval=0.5, button='left')
    time.sleep(3)
    pyautogui.doubleClick(x=1803, y=385, interval=0.5, button='right')
    pyautogui.click(x=1786, y=521, clicks=1, interval=0.5, button='left')
    time.sleep(3)
    pyautogui.click(x=1897, y=228, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=183, y=995, clicks=1, interval=0.5, button='left')
    
def main():
    print('5 seconds, Forecast script will run !')
    countDown()
    run_forecast()
    return

main()