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

def run_shiftTime():
    pyautogui.click(x=513, y=1060, clicks=1, interval=0, button='left')
    pyautogui.click(x=855, y=123, clicks=1, interval=0, button='left')
    time.sleep(6) #sleep to wait for query to run and finish
    pyautogui.click(x=1067, y=731, clicks=1, interval=0, button='right')
    pyautogui.click(x=1094, y=847, clicks=1, interval=1, button='left')
    pyautogui.click(x=925, y=401, clicks=1, interval=1, button='left')
    pyautogui.press('c')
    time.sleep(1)
    pyautogui.doubleClick(x=1007, y=531,interval=0, button='left')
    time.sleep(1)
    pyautogui.typewrite('shiftTimes.csv', interval=0)
    for _i in range(3):
        pyautogui.press('enter')
    time.sleep(5) #sleep to wait for data to fully export to excel sheet
    pyautogui.hotkey('alt', 'space')
    pyautogui.click(x=47, y=101, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=166, y=1061, clicks=1, interval=1, button='right')
    pyautogui.moveTo(x=184, y=605)
    pyautogui.click(x=184, y=605, clicks=1, interval=0.5, button='left')
    pyautogui.hotkey('win', 'up')
    pyautogui.doubleClick(x=459, y=91, interval=0.5, button='left')
    pyautogui.doubleClick(x=442, y=165, interval=0.5, button='left')
    time.sleep(3.5)
    pyautogui.press('down')
    pyautogui.click(x=381, y=44, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=593, y=86, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=265, y=418, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=386, y=461, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=282, y=585, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=390, y=486, clicks=1, interval=0.5, button='left')
    pyautogui.press('a')
    for _i in range(2):
        pyautogui.press('enter')
    pyautogui.doubleClick(x=50, y=253, interval=0.5, button='left')
    for _i in range(6):
        pyautogui.hotkey('ctrl','shift','right')
    pyautogui.press('ctrl','shift','down')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'space')
    pyautogui.click(x=47, y=101, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=810, y=1053, clicks=1, interval=0.5, button='right')
    time.sleep(0.5)
    pyautogui.click(x=769, y=551, clicks=1, interval=0.5, button='left')
    time.sleep(5)
    pyautogui.click(x=487, y=1004, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=56, y=253, clicks=1, interval=0.5, button='left')
    pyautogui.hotkey('ctrl', 'v')
    return
    
def main():
    print('5 seconds, Hours script will run !')
    countDown()
    run_shiftTime()
    return

main()
    
    
    