import tkinter as tk
from tkinter import filedialog
import webbrowser as wb
import os
import subprocess
def f1():
    filename = filedialog.askopenfilename()
    print(filename)
    subprocess.Popen([filename  ,"sudo /usr/bin/open Preview"],shell=True)
    

def f2():  
    wb.open('https://meet.google.com/pnh-wttc-ahh')

def f3():
    wb.open('https://us02web.zoom.us/j/2320221486?pwd=SWJYMjl0aVZRNW1rMUoxcElwaW1hUT09#success')

root = tk.Tk()
root.title("Day Routine Manager")
root.geometry("500x500")
menubar=tk.Menu(root)
#FILE BAR
filemenu=tk.Menu(menubar,background="#A5D0FD", activebackground="#F59C9C")
filemenu.add_command(label="Open File", command=f1)
menubar.add_cascade(label="File",menu=filemenu)

#CLASSES BAR
classmenu=tk.Menu(menubar)
classmenu.add_command(label="Coding Class",command=f2)
classmenu.add_command(label="Piano Class",command=f3)
menubar.add_cascade(label="Classes",menu=classmenu)
#CONFIG
root.config(menu=menubar, background="#D4F3FC")
root.mainloop()
 