import pyautogui
import time
import tkinter as tk
import sys

def countDown():
    timeLeft = 5
    while timeLeft > 0:
        sys.stdout.write(str(timeLeft) + '    \r')
        timeLeft -= 1
        time.sleep(1)
    return

def run_hours():
    # this script runs hours, exports data, refreshes time commiments excel sheet, copy and pastes current data to OFW2
    pyautogui.click(x=810, y=1053, clicks=1, interval=0.5, button='right')
    time.sleep(0.5)
    pyautogui.click(x=775, y=585, clicks=1, interval=0.5, button='left')
    time.sleep(6)
    pyautogui.doubleClick(x=1749, y=478, interval=0.5, button='right')
    pyautogui.click(x=1786, y=605, clicks=1, interval=0.5, button='left')
    time.sleep(10)
    pyautogui.click(x=148, y=1000, clicks=1, interval=0.5, button='left')
    time.sleep(3)
    pyautogui.click(x=801, y=10, clicks=1, interval=0.5, button='left')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'space')
    pyautogui.click(x=47, y=101, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=810, y=1053, clicks=1, interval=0.5, button='right')
    time.sleep(0.5)
    pyautogui.click(x=769, y=551, clicks=1, interval=0.5, button='left')
    time.sleep(5)
    pyautogui.click(x=129, y=1004, clicks=1, interval=0.5, button='left')
    pyautogui.click(x=136, y=942, clicks=1, interval=0.5, button='left')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(x=246, y=1004, clicks=1, interval=0.5, button='left')
    return

def main():
    print('5 seconds, Hours script will run !')
    countDown()
    run_hours()
    return

main()
