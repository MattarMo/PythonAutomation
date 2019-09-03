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

def run_opaBlocks():
    pyautogui.click(x=513, y=1060, clicks=1, interval=0, button='left')
    pyautogui.click(x=1381, y=123, clicks=1, interval=0, button='left')
    time.sleep(3) #sleep to wait for query to run and finish
    pyautogui.click(x=1622, y=705, clicks=1, interval=0, button='right')
    pyautogui.click(x=1625, y=818, clicks=1, interval=1, button='left')
    pyautogui.click(x=925, y=401, clicks=1, interval=1, button='left')
    pyautogui.press('c')
    time.sleep(1)
    pyautogui.doubleClick(x=1007, y=531,interval=0, button='left')
    time.sleep(1)
    pyautogui.typewrite('opa.csv', interval=0)
    for _i in range(3):
        pyautogui.press('enter')
    time.sleep(3) #sleep to wait for data to fully export to excel sheet
    pyautogui.hotkey('alt', 'space')
    pyautogui.click(x=47, y=101, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=166, y=1061, clicks=1, interval=1, button='right')
    pyautogui.moveTo(x=184, y=605)
    pyautogui.click(x=184, y=605, clicks=1, interval=0.5, button='left')
    pyautogui.hotkey('win', 'up')
    pyautogui.doubleClick(x=459, y=91, interval=0.5, button='left')
    pyautogui.doubleClick(x=479, y=185, interval=0.5, button='left')
    time.sleep(3.5)
    pyautogui.press('down')
    pyautogui.hotkey('ctrl','shift','right')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'space')
    pyautogui.click(x=47, y=101, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=810, y=1053, clicks=1, interval=0.5, button='right')
    time.sleep(0.5)
    pyautogui.click(x=769, y=551, clicks=1, interval=0.5, button='left')
    time.sleep(5)
    pyautogui.click(x=574, y=1002, clicks=1, interval=0.5, button='left')
    pyautogui.hotkey('ctrl', 'v')
    return
    
def main():
    print('5 seconds, Opa blocks script will run !')
    countDown()
    run_opaBlocks()
    return

main()
    