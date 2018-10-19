from Tkinter import *
from time import sleep
import tkMessageBox

sleep(3)

Tk().wm_withdraw()

result = tkMessageBox.askyesno("Python", "Would you like to save the data?")
print result
