from tkinter import *
import tkinter.ttk as ttk
import csv
from tkinter import *
import tkinter

root = Tk()
root.title('Flight Planner')
root.geometry("300x400")

def openflights():

    flights = Tk()
    flights.title("Flight Recorder")
    width = 900
    height = 900

    flights.mainloop()
    
def createflight():
    print("In Creation")
    
    

        
   
        

   
ofb = Button(root, text="Open Flights", command=openflights, fg="blue" )

ofb.pack()

cfb = Button(root, text="Create Flight", command=createflight, fg="blue" )

cfb.pack()


root.mainloop()

