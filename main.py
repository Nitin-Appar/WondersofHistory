import datetime
import random

import about
import check_validity
import data_retrieve

# menu
print("________Wonders Of History________")
print("\--------------------------------/")
print("1.Events that happened on this day\n2.Enter custom date\n3.Random date\n4.Preset date example\n5.Info\n0. =Exit= ")
choice = int(input())

# users option to change ways to enter date
while choice != 0:
    3

   # using datetime module to retrieve current day and month values from the system
    if choice == 1:
        today = datetime.datetime.now()
        day_today = today.day
        month_today = today.month
        # adding leading zeroes to the day and month values to create a two digit number
        day_today = str(day_today).zfill(2)
        month_today = str(month_today).zfill(2)
        print("month:", month_today, "\nday:", day_today)
        data_retrieve.retrievefordm(month_today, day_today)

    #
    elif choice == 2:
        flag = 2
        month = 0
        day = 0
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_with_30_days = [4, 6, 9, 11]

        # getting a month as input from user and checking its validity
        while(flag == 2):
            month = int(input("enter month: "))
            if(month < 1 or month > 12):
                print("enter valid month...")
            else:
                flag = 1

        # getting a day as input from user and checking its validity against the month value
        while(flag == 1):
            day = int(input("enter day: "))
            if(month == 2):
                if(day > 28):
                    print("enter a valid day...")
                else:
                    flag = 0
            elif(month in months_with_31_days):
                if(day < 1 or day > 31):
                    print("enter a valid day...")
                else:
                    flag = 0
            elif(month in months_with_30_days):
                if(day < 1 or day > 30):
                    print("enter a valid day...")
                else:
                    flag = 0

        print("month:", month, "\nday:", day)
        day = str(day).zfill(2)
        month = str(month).zfill(2)
        data_retrieve.retrievefordm(month, day)

    elif choice == 3:
        # calling randomdate module
        date = []
        date = check_validity.randomdate()
        day = date[0]
        month = date[1]
        data_retrieve.retrievefordm(month, day)

    elif choice == 4:
        data_retrieve.retrievefordm(6, 2)

    elif choice == 5:
        about.aboutus()

    print("1.Events that happened on this day\n2.Enter custom date\n3.Random date\n4.Preset date example\n5.Info\n0. =Exit= ")
    choice = int(input())

print("Exiting the program, thank you.")
