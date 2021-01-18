# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:57:13 2020

@author: mrbar
"""
import tkinter
import tkinter.font as font
import math

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
        
    result = 0
    
    def Zero(self):
        zero = self.ZeroButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', zero)
    
    def One(self):
        one = self.OneButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', one)
    
    def Two(self):
        two = self.TwoButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', two)
    
    def Three(self):
        three = self.ThreeButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', three)
    
    def Four(self):
        four = self.FourButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', four)
    
    def Five(self):
        five = self.FiveButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', five)
    
    def Six(self):
        six = self.SixButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', six)
    
    def Seven(self):
        seven = self.SevenButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', seven)
    
    def Eight(self):
        eight = self.EightButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', eight)
    
    def Nine(self):
        nine = self.NineButton['text']
        if self.Enter.get() == '0' or not self.Enter.get():    
            self.Enter.delete(0, 'end')
        self.Enter.insert('end', nine)
    
    def Add(self):
        stack.append(self.Enter.get())
        stack.append("+")
        #self.DisplayAnswer["text"] = x + ' ' + '+'
        self.Enter.delete(0, 'end')
        print(stack)

    def Subtract(self):
        stack.append(self.Enter.get())
        stack.append("-")
        #self.DisplayAnswer["text"] = x + ' ' + '+'
        self.Enter.delete(0, 'end')
        print(stack)
        
    def Multiply(self):
        stack.append(self.Enter.get())
        stack.append("x")
        self.Enter.delete(0, 'end')
        print(stack)
        
    def Divide(self):
        stack.append(self.Enter.get())
        stack.append("/")
        self.Enter.delete(0, 'end')
        print(stack)
    
    def SquareRoot(self):
        stack.append("√".format(self.Enter.get()))
        self.Enter.delete(0, 'end')
        print(stack)
    
    def Squared(self):
        stack.append(self.Enter.get())
        stack.append("^2")
        self.Enter.delete(0, 'end')
        print(stack)
        
    def Sin(self):
        stack.append("sin()")
        self.Enter.delete(0, 'end')
        print(stack)    
    
    def Cos(self):
        stack.append("cos()")
        self.Enter.delete(0, 'end')
        print(stack)
    
    def Tan(self):
        stack.append("tan()")
        self.Enter.delete(0, 'end')
        print(stack)
    
    def Pi(self):
        stack.append("Π")
        self.Enter.delete(0, 'end')
        print(stack)
    
    def NaturalLog(self):
        stack.append("ln")
        self.Enter.delete(0, 'end')
        print(stack)
    
    def Log(self):
        stack.append("log")
        self.Enter.delete(0, 'end')
        print(stack)
        
    def Dot(self):
        stack.append(".")
        self.Enter.delete(0, 'end')
        print(stack)
    
    def Equals(self):
        stack.append(self.Enter.get())
        print(stack)
        reversed_stack = stack[::-1]
        print(reversed_stack)
        while reversed_stack:
            if len(reversed_stack) == 1:
                stack.append(reversed_stack.pop())
                print(stack[-1])
                break
            num2, sign = reversed_stack.pop(), reversed_stack.pop()
            print("num2", num2)
            print("sign", sign)
            if sign == "+":
                num1 = reversed_stack.pop()
                print("num1", num1)
                if num1 == "log":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.log10(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num1 == "ln":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.log(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num2 == "sin()":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.sin(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num1 == "sin()":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.sin(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num2 == "cos()":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.cos(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num1 == "cos()":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.cos(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num2 == "tan()":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.tan(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num1 == "tan()":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.tan(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num2.isdigit() and num1.isdigit():
                    if int(num1):
                        result = int(num2) + int(num1)
                        print(result)
                        reversed_stack.append(str(result))
                        print(reversed_stack)
            if sign == "-":
                num1 = reversed_stack.pop()
                print(num1)
                if num1 == "log":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = abs(math.log10(float(num3)) - float(num2))
                    reversed_stack.append(result)
                    print(reversed_stack)
                elif num1 == "ln":
                    num3 = reversed_stack.pop()
                    print("num3", num3)
                    result = math.log(float(num3)) + float(num2)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
                else:
                    num3 = reversed_stack.pop()
                    result = int(num3) - int(num1)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
            if sign == "x":
                num1 = reversed_stack.pop()
                print(num1)
                if num1 == "Π":
                    reversed_stack.pop()
                    result = float(num2) * 3.14159
                    reversed_stack.append(result)
                    print(reversed_stack)
                else:
                    result = int(num2) * int(num1)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
            if sign == "/":
                num1 = reversed_stack.pop()
                print(num1)
                if num1 == '0':
                    self.Enter.insert("end", 0)
                    result = 0
                    break
                else:
                    result = int(num2) // int(num1)
                    print(result)
                    reversed_stack.append(result)
                    print(reversed_stack)
            if num2 == "√":
                print("after == sqrt", reversed_stack)
                result = (math.sqrt(int(sign)))
                print(result)
                reversed_stack.append(str(result))
                print(reversed_stack)
            if sign == "^2":
                reversed_stack.pop()
                print(reversed_stack)
                result = int(num2)**2
                print(result)
                reversed_stack.append(str(result))
                print(reversed(stack))
            if num2 == "sin()":
                num = sign
                result = math.sin(float(num))
                reversed_stack.append(str(result))
                print("hi", reversed_stack)
            if num2 == "cos()":
                num = sign
                result = math.cos(float(num))
                reversed_stack.append(str(result))
                print(reversed_stack)
            if num2 == "tan()":
                num = sign
                result = math.tan(float(num))
                reversed_stack.append(str(result))
                print(reversed_stack)
            if num2 == "ln":
                num = sign
                result = math.log(float(num))
                reversed_stack.append(str(result))
                print(reversed_stack)
            if num2 == "log":
                num = sign
                result = math.log10(float(num))
                reversed_stack.append(str(result))
                print(reversed_stack)
        self.Enter.delete(0, 'end')
        self.Enter.insert('end', result)
        #self.DisplayAnswer["text"] = x + ' ' + '+' + ' ' + y + ' ' + '='
        
    def Clear(self):
        self.Enter.delete(0, 'end')
        self.Enter.insert('end', 0)
        self.DisplayAnswer['text'] = ""
        stack.clear()
        print(stack)
        
stack = []       
window = tkinter.Tk()
window.title("Calculator")
window.geometry("435x529")
Calculate(window)