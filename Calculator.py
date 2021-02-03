# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:28:56 2021

@author: mrbar
"""
import tkinter
import tkinter.font as font
from math import sin, cos, tan, pi, log10, log

class Calculate:
    def __init__(self, master):
        self.DisplayAnswer = tkinter.Label(master)
        self.DisplayAnswer.grid(row = 1, column = 4, padx = 5, pady = 5)
        
        self.TextFont = font.Font(size = 60)
        self.Enter = tkinter.Entry(master, width = 5, bg = 'white', fg = 'black', justify = 'right', relief = 'flat', font = self.TextFont)
        self.Enter.grid(row = 2, columnspan = 10, padx = 5, pady = 5, ipadx = 90, ipady = 40)
        self.Enter.insert('end', 0)
        
        self.AddButtonFont = font.Font(size = 15)
        self.SubtractButtonFont = font.Font(size = 15)
        self.MultiplyButtonFont = font.Font(size = 15)
        self.DivideButtonFont = font.Font(size = 15)
        self.ZeroButtonFont = font.Font(size = 15)
        self.OneButtonFont = font.Font(size = 15)
        self.TwoButtonFont = font.Font(size = 15)
        self.ThreeButtonFont = font.Font(size = 15)
        self.FourButtonFont = font.Font(size = 15)
        self.FiveButtonFont = font.Font(size = 15)
        self.SixButtonFont = font.Font(size = 15)
        self.SevenButtonFont = font.Font(size = 15)
        self.EightButtonFont = font.Font(size = 15)
        self.NineButtonFont = font.Font(size = 15)
        self.SinButtonFont = font.Font(size = 15)
        self.CosButtonFont = font.Font(size = 15)
        self.TanButtonFont = font.Font(size = 15)
        self.PiButtonFont = font.Font(size = 15)
        self.SquareRootFont = font.Font(size = 15)
        self.SquaredFont = font.Font(size = 15)
        self.EqualsFont = font.Font(size = 15)
        self.ClearFont = font.Font(size = 15)
        self.NaturalLogFont = font.Font(size = 15)
        self.LogFont = font.Font(size = 15)
        self.DotFont = font.Font(size = 15)
        
        self.AddButton = tkinter.Button(master, text = "+", width = 7, height = 2, bg = "black", fg = "white", command = self.Add)
        self.SubtractButton = tkinter.Button(master, text = "-", width = 7, height = 2, bg = "black", fg = "white", command = self.Subtract)
        self.MultiplyButton = tkinter.Button(master, text = "x", width = 7, height = 2, bg = "black", fg = "white", command = self.Multiply)
        self.DivideButton = tkinter.Button(master, text = "/", width = 7, height = 2, bg = "black", fg = "white", command = self.Divide)
        self.ZeroButton = tkinter.Button(master, text = "0", width = 7, height = 2, bg = "black", fg = "white", command = self.Zero)
        self.OneButton = tkinter.Button(master, text = "1", width = 7, height = 2, bg = "black", fg = "white", command = self.One)
        self.TwoButton = tkinter.Button(master, text = "2", width = 7, height = 2, bg = "black", fg = "white", command = self.Two)
        self.ThreeButton = tkinter.Button(master, text = "3", width = 7, height = 2, bg = "black", fg = "white", command = self.Three)
        self.FourButton = tkinter.Button(master, text = "4", width = 7, height = 2, bg = "black", fg = "white", command = self.Four)
        self.FiveButton = tkinter.Button(master, text = "5", width = 7, height = 2, bg = "black", fg = "white", command = self.Five)
        self.SixButton = tkinter.Button(master, text = "6", width = 7, height = 2, bg = "black", fg = "white", command = self.Six)
        self.SevenButton = tkinter.Button(master, text = "7", width = 7, height = 2, bg = "black", fg = "white", command = self.Seven)
        self.EightButton = tkinter.Button(master, text = "8", width = 7, height = 2, bg = "black", fg = "white", command = self.Eight)
        self.NineButton = tkinter.Button(master, text = "9", width = 7, height = 2, bg = "black", fg = "white", command = self.Nine)
        self.SinButton = tkinter.Button(master, text = "sin", width = 7, height = 2, bg = "black", fg = "white", command = self.Sin)
        self.CosButton = tkinter.Button(master, text = "cos", width = 7, height = 2, bg = "black", fg = "white", command = self.Cos)
        self.TanButton = tkinter.Button(master, text = "tan", width = 7, height = 2, bg = "black", fg = "white", command = self.Tan)
        self.PiButton = tkinter.Button(master, text = "Π", width = 7, height = 2, bg = "black", fg = "white", command = self.Pi)
        self.SquareRootButton = tkinter.Button(master, text = "√x", width = 7, height = 2, bg = "black", fg = "white", command = self.SquareRoot)
        self.SquaredButton = tkinter.Button(master, text = "x²", width = 7, height = 2, bg = "black", fg = "white", command = self.Squared)
        self.EqualsButton = tkinter.Button(master, text = "=", width = 7, height = 2, bg = "blue", fg = "white", command = self.Equals)
        self.ClearButton = tkinter.Button(master, text = "C", width = 7, height = 2, bg = "black", fg = "white", command = self.Clear)
        self.NaturalLogButton = tkinter.Button(master, text = "ln", width = 7, height = 2, bg = "black", fg = "white", command = self.NaturalLog)
        self.LogButton = tkinter.Button(master, text = "log", width = 7, height = 2, bg = "black", fg = "white", command = self.Log)
        self.DotButton = tkinter.Button(master, text = ".", width = 7, height = 2, bg = "black", fg = "white", command = self.Dot)
        
        self.AddButton['font'] = self.AddButtonFont
        self.SubtractButton['font'] = self.SubtractButtonFont
        self.MultiplyButton['font'] = self.MultiplyButtonFont
        self.DivideButton['font'] = self.DivideButtonFont
        self.ZeroButton['font'] = self.ZeroButtonFont
        self.OneButton['font'] = self.OneButtonFont
        self.TwoButton['font'] = self.TwoButtonFont
        self.ThreeButton['font'] = self.ThreeButtonFont
        self.FourButton['font'] = self.FourButtonFont
        self.FiveButton['font'] = self.FiveButtonFont
        self.SixButton['font'] = self.SixButtonFont
        self.SevenButton['font'] = self.SevenButtonFont
        self.EightButton['font'] = self.EightButtonFont
        self.NineButton['font'] = self.NineButtonFont
        self.SinButton['font'] = self.SinButtonFont
        self.CosButton['font'] = self.CosButtonFont
        self.TanButton['font'] = self.TanButtonFont
        self.PiButton['font'] = self.PiButtonFont
        self.SquareRootButton['font'] = self.SquareRootFont
        self.SquaredButton['font'] = self.SquaredFont
        self.EqualsButton['font'] = self.EqualsFont
        self.ClearButton['font'] = self.ClearFont  
        self.NaturalLogButton['font'] = self.NaturalLogFont
        self.LogButton['font'] = self.LogFont
        self.DotButton['font'] = self.DotFont

        self.AddButton.grid(row = 9, column = 0)
        self.SubtractButton.grid(row = 8, column = 0)
        self.MultiplyButton.grid(row = 7, column = 0)
        self.DivideButton.grid(row = 6, column = 0)
        self.ZeroButton.grid(row = 9, column = 2)
        self.OneButton.grid(row = 8, column = 1)
        self.TwoButton.grid(row = 8, column = 2)
        self.ThreeButton.grid(row = 8, column = 3)
        self.FourButton.grid(row = 7, column = 1)
        self.FiveButton.grid(row = 7, column = 2)
        self.SixButton.grid(row = 7, column = 3)
        self.SevenButton.grid(row = 6, column = 1)
        self.EightButton.grid(row = 6, column = 2)
        self.NineButton.grid(row = 6, column = 3)
        self.SinButton.grid(row = 7, column = 4)
        self.CosButton.grid(row = 8, column = 4)
        self.TanButton.grid(row = 9, column = 4)
        self.PiButton.grid(row = 3, column = 3)
        self.SquareRootButton.grid(row = 3, column = 4)
        self.SquaredButton.grid(row = 6, column = 4)
        self.EqualsButton.grid(row = 9, column = 3)
        self.ClearButton.grid(row = 3, column = 0)
        self.NaturalLogButton.grid(row = 3, column = 1)
        self.LogButton.grid(row = 3, column = 2)
        self.DotButton.grid(row = 9, column = 1)
        
        tkinter.mainloop()
        
    def Zero(self):
        zero = self.ZeroButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', zero)
        global result
        result += '0'
    
    def One(self):
        one = self.OneButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', one)
        global result
        result += '1'
    
    def Two(self):
        two = self.TwoButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', two)
        global result
        result += '2'
    
    def Three(self):
        three = self.ThreeButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', three)
        global result
        result += '3'
        
    def Four(self):
        four = self.FourButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', four)
        global result
        result += '4'
    
    def Five(self):
        five = self.FiveButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', five)
        global result
        result += '5'
    
    def Six(self):
        six = self.SixButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', six)
        global result
        result += '6'
    
    def Seven(self):
        seven = self.SevenButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', seven)
        global result
        result += '7'
    
    def Eight(self):
        eight = self.EightButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', eight)
        global result
        result += '8'
    
    def Nine(self):
        nine = self.NineButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', nine)
        global result
        result += '9'
    
    def Add(self):
        self.Enter.delete(0, 'end')
        global result
        result += '+'

    def Subtract(self):
        self.Enter.delete(0, 'end')
        global result
        result += '-'
        
    def Multiply(self):
        self.Enter.delete(0, 'end')
        global result
        result += '*'
        
    def Divide(self):
        self.Enter.delete(0, 'end')
        global result
        result += '/'
    
    def SquareRoot(self):
        global result
        result += '**0.5'

    def Squared(self):
        global result 
        result += '**2'
        
    def Sin(self):
        global result
        result = 'sin({})'.format(self.Enter.get())
    
    def Cos(self):
        global result
        result = 'cos({})'.format(self.Enter.get())
    
    def Tan(self):
        global result
        result = 'tan({})'.format(self.Enter.get())
    
    def Pi(self):
        self.Enter.delete(0, 'end')
        global result
        result += "pi"
    
    def NaturalLog(self):
        global result
        result = 'log({})'.format(self.Enter.get())
    
    def Log(self):
        global result
        result = 'log10({})'.format(self.Enter.get())
        
    def Dot(self):
        self.Enter.insert('end', '.')
        global result
        result += '.'
    
    def Equals(self):
        global total, result
        total = round(eval(result), 4)
        self.Enter.delete(0, 'end')
        self.Enter.insert('end', total)
        self.DisplayAnswer["text"] = result + " = "
        result = self.Enter.get()
        
    def Clear(self):
        self.Enter.delete(0, 'end')
        self.Enter.insert('end', 0)
        self.DisplayAnswer['text'] = ""
        global result, total
        result, total = '', ''
   
result, total = "", ""  
window = tkinter.Tk()
window.title("Calculator")
window.geometry("435x529")
Calculate(window)