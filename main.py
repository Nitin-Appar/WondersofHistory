import datetime
import random
from tkinter import * 
import tkinter as tk
from xmlrpc.client import Boolean

import about
import data_retrieve

calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

ordinalday = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4]) #lambda function to convert a given number to its ordinal value


def date_today():
    today = datetime.datetime.now() # datetime module allows the program to retrieve today's day and month values from the system
    day = today.day
    month = today.month
    
    day = str(day).zfill(2) # adding leading zeroes to the day and month values to create a two digit number
    month = str(month).zfill(2)
    print("it is the",ordinalday(int(day)),"of", calendar[int(month)-1])
    
    return month,day


def date_input():
    flag = 2
    month = 0
    day = 0
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]

    while(flag == 2): # getting a month as input from user and checking its validity
        month = int(input("enter month: "))
        if(month < 1 or month > 12):
            print("Invalid month^, please enter a valid month")
        else:
            flag = 1

    while(flag == 1): # getting a day as input from user and checking its validity against the month value using the month lists
        day = int(input("enter day: "))
        if(month == 2):
            if(day > 28):
                print("Invalid day^, please enter a valid day")
            else:
                flag = 0
        elif(month in months_with_31_days):
            if(day < 1 or day > 31):
                print("Invalid day^, please enter a valid day")
            else:
                flag = 0
        elif(month in months_with_30_days):
            if(day < 1 or day > 30):
                print("Invalid day^, please enter a valid day")
            else:
                flag = 0

    day = str(day).zfill(2)
    month = str(month).zfill(2)
    print("it is the",ordinalday(int(day)),"of", calendar[int(month)-1]) #printing month and day values in its verbal form
    
    return month,day


def date_random():
    flag = 1
    month = 0
    day = 0
    months_with_30_days = [4, 6, 9, 11]
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    month = random.randint(1, 12) # generating a random month value

    while(flag == 1):
        day = random.randint(1, 31) #generating a random day value and checking its validity
        if(month == 2):
            if(day > 28):
                continue
            else:
                flag = 0
        elif(month in months_with_31_days):
            if(day < 1 or day > 31):
                continue
            else:
                flag = 0
        elif(month in months_with_30_days):
            if(day < 1 or day > 30):
                continue
            else:
                flag = 0

    day = str(day).zfill(2)
    month = str(month).zfill(2)
    print("it is the",ordinalday(int(day)),"of", calendar[int(month)-1])
    
    return month,day


def date_preset():
    month=6
    day=2
    print("it is the",ordinalday(int(day)),"of", calendar[int(month)-1])

    return month,day



# menu
verify=0
while(verify==0):
    print("________Wonders Of History________")
    print("\--------------------------------/")
    print("1.Events that happened on this day\n2.Enter custom date\n3.Random date\n4.Preset date example\n5.Info\n0. =Exit= ") 
    choice = int(input())
    
    if choice == 1:
        m,d=date_today()
        data_retrieve.retrievefordm(m,d) #calling module data_retrieve to get the events from the day and month values given to it
    elif choice == 2:
        m,d=date_input()
        data_retrieve.retrievefordm(m,d)
    elif choice == 3:
        m,d=date_random()
        data_retrieve.retrievefordm(m,d)
    elif choice == 4:
        m,d=date_preset()
        data_retrieve.retrievefordm(m,d)
    elif choice == 5:
        about.aboutus()
    elif choice == 0:
        print("Exiting the program, thank you.")
    flag_b=1
    while(flag_b==1):
        verify=int(input("are you sure you want to procede? (1-yes,0-no):- "))
        if(verify==0):
            flag_b=0
            continue
        elif(verify==1):
            break
        else:
            print("invalid value, please enter a valid confirmation value") 


def text_change():
    global text
    text=text+1
    if text>len(data_retrieve.eventlist):
        text = 0
    print("changed to event number: ", text)

    btn.config(text=data_retrieve.eventlist[text])
    
def text_print():
    print("the year is:",data_retrieve.yearlist[text])


text=-1
root = tk.Tk()

btn = tk.Button(text="Click to see events", command=text_change, width=150, height=25)
btn.grid(row=1, column=1)

btn2 = tk.Button(text="year", command=text_print, width=10, height=2)
btn2.grid(row=2, column=1)

root.mainloop()


print("Exiting the program, thank you.")


