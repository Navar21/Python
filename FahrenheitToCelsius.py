# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:18:52 2019

@author: Navar21
"""

import tkinter

class Convert:
    def __init__(self, master):
        
        self.CelsiusLabel = tkinter.Label(master, text = "Celsius")
        self.FarenheitLabel = tkinter.Label(master, text = "Farenheit")
        self.DisplayFarenheitLabel = tkinter.Label(master)
        self.DegreeCelsiusLabel = tkinter.Label(master, text = "\u00b0C")
        self.DegreeFarenheitLabel = tkinter.Label(master, text = "\u00b0F")
        
        self.CelsiusLabel.grid(row = 0)
        self.FarenheitLabel.grid(row = 1)
        self.DisplayFarenheitLabel.grid(row = 1, column = 1)
        self.DegreeCelsiusLabel.grid(row = 0, column = 2)
        self.DegreeFarenheitLabel.grid(row = 1, column = 2)
        
        self.EnterCelsius = tkinter.Entry(master, width = 10, justify = "center")
        
        self.EnterCelsius.grid(row = 0, column = 1)
        
        self.Calculate = tkinter.Button(master, text = "Convert", bg = "red", \
                                        fg = "white", command = self.Data) 
        
        self.Calculate.grid(row = 2, column = 1)
        
        tkinter.mainloop()
    
    def Data(self):
        Celsius = float(self.EnterCelsius.get())
        Farenheit = (9/5 * Celsius) + 32
        self.DisplayFarenheitLabel["text"] = str(Farenheit)

Window = tkinter.Tk()
Window.geometry("160x70")
Convert(Window)