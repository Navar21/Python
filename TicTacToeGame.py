# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:53:08 2020

@author: Navar21
"""
import sys

alist = [1, 2, 3]
blist = [4, 5, 6]
clist = [7, 8, 9] 

def printboard(): 
    print(" ", alist)    
    print(" ", blist)
    print(" ", clist)
    
def check_for_tie():
    tielist = []
    tielist.append(alist + blist + clist)
    
    count = 0
    for d in tielist:
        for f in d:
            if f == 'X' or f == 'O':
                count += 1
                if count == 9:
                    print("It's a tie")
                    sys.exit()
                    
def check_for_win():
    # Checks for win in list [1, 2, 3]
    if alist[0] == 'X' and alist[1] == 'X' and alist[2] == 'X':
        print("You Win")
        sys.exit()
    elif alist[0] == 'O' and alist[1] == 'O' and alist[2] == 'O':
        print("You Win")
        sys.exit()
                
    # Checks for win in list [4, 5, 6]  
    elif blist[0] == 'X' and blist[1] == 'X' and blist[2] == 'X': 
        print("You Win")
        sys.exit()    
    elif blist[0] == 'O' and blist[1] == 'O' and blist[2] == 'O':
        print("You Win")
        sys.exit()
                
    # Checks for win in list [7, 8, 9]  
    elif clist[0] == 'X' and clist[1] == 'X' and clist[2] == 'X': 
        print("You Win")
        sys.exit()    
    elif clist[0] == 'O' and clist[1] == 'O' and clist[2] == 'O':
        print("You Win")
        sys.exit()
                
    # Checks for win in [1] [4] [7]
    elif alist[0] == 'X' and blist[0] == 'X' and clist[0] == 'X':
        print("You Win")
        sys.exit()
    elif alist[0] == 'O' and blist[0] == 'O' and clist[0] == 'O':
        print("You Win")
        sys.exit()
        
    # Checks for win in [2] [5] [8]
    elif alist[1] == 'X' and blist[1] == 'X' and clist[1] == 'X':
        print("You Win")
        sys.exit()
    elif alist[1] == 'O' and blist[1] == 'O' and clist[1] == 'O':
        print("You Win")
        sys.exit()
    
    # Checks for win in [3] [6] [9]
    elif alist[2] == 'X' and blist[2] == 'X' and clist[2] == 'X':
        print("You Win")
        sys.exit()             
    elif alist[2] == 'O' and blist[2] == 'O' and clist[2] == 'O':
        print("You Win")
        sys.exit()
        
    # Checks for win in [1] [5] [9]
    elif alist[0] == 'X' and blist[1] == 'X' and clist[2] == 'X':
        print("You Win")
        sys.exit()             
    elif alist[0] == 'O' and blist[1] == 'O' and clist[2] == 'O':
        print("You Win")
        sys.exit()
       
    # Checks for win in [3] [5] [7]
    elif alist[2] == 'X' and blist[1] == 'X' and clist[0] == 'X':
        print("You Win")
        sys.exit()             
    elif alist[2] == 'O' and blist[1] == 'O' and clist[0] == 'O':
        print("You Win")
        sys.exit()
        
print("\n", ("TIC-TAC-TOE"), "\n")
printboard()

n = input("Player 1, select 'X' or 'O': ")
if n == 'X':
    while True:
        x = int(input("Player 1 choose a number: "))
        if x == 1:
            alist[0] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2 choose a number: "))
            if y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
                
        elif x == 2:
            alist[1] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
    
        elif x == 3:
            alist[2] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()   
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
        
        elif x == 4:
            blist[0] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
          
        elif x == 5:
            blist[1] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
            
        elif x == 6:
            blist[2] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            else:
                clist[2] = 'O'
                printboard()
                check_for_tie()
                
        elif x == 7:
            clist[0] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
        
        elif x == 8:
            clist[1] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'O'
                printboard()
                check_for_tie()
                
        elif x == 9:
            clist[2] = 'X'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'O'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'O'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'O'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'O'
                printboard()
                check_for_tie()

elif n == 'O':
    while True:
        x = int(input("Player 1 choose a number: "))
        if x == 1:
            alist[0] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2 choose a number: "))
            if y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
                
        elif x == 2:
            alist[1] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
    
        elif x == 3:
            alist[2] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()   
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
        
        elif x == 4:
            blist[0] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
          
        elif x == 5:
            blist[1] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
            
        elif x == 6:
            blist[2] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            else:
                clist[2] = 'X'
                printboard()
                check_for_tie()
                
        elif x == 7:
            clist[0] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
        
        elif x == 8:
            clist[1] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 9:
                clist[2] = 'X'
                printboard()
                check_for_tie()
                
        elif x == 9:
            clist[2] = 'O'
            printboard()
            check_for_tie()
            check_for_win()
            y = int(input("Player 2, choose a number: "))
            if y == 1:
                alist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 2:
                alist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 3:
                alist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 4:
                blist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 5:
                blist[1] = 'X'
                printboard()
                check_for_tie()
            elif y == 6:
                blist[2] = 'X'
                printboard()
                check_for_tie()
            elif y == 7:
                clist[0] = 'X'
                printboard()
                check_for_tie()
            elif y == 8:
                clist[1] = 'X'
                printboard()
                check_for_tie()