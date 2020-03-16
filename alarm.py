"""
Author : Mulla Mohammed
Description : This program demonstrates the working on stop watch,

Input : Ask the user in how much time should it buzz
output : buzz
working : takes the inputs from user , trigger the buzzer when its about time
"""

import time, os, winsound
def buzzer():
    for i in range(3): #REPEAT BUZZER
        for j in range(9):
            winsound.MessageBeep(-1)
            time.sleep(1)

def snooze(unit_sec):
    print("wait time in seconds :", unit_sec)
    time.sleep(unit_sec)
    buzzer()

if __name__ == '__main__':
    print("WELCOME TO STOP WATCH PROGRAM !")
    minutes = int(input("Please enter Minutes :"))
    sec = int(input("Please enter seconds:"))
    minutes = minutes * 60
    unit_sec = minutes + sec
    snooze(unit_sec)
