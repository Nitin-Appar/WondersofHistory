import check_validity
import data_retrieve
import datetime
import random
import about

print("________Wonders Of History________")
print("\--------------------------------/")
print("1.Events that happened on this day\n2.Enter custom date\n3.Random date\n4.Preset date example\n5.Info\n0. =Exit= ")
choice=int(input())
while choice!=0:
    
    
    if choice==1:
        today=datetime.datetime.now()
        day_today=today.day
        month_today=today.month
        day_today=str(day_today).zfill(2)
        month_today=str(month_today).zfill(2)
        date_dm=str(day_today)+" "+str(month_today)
        print("month:",month_today,"\nday:",day_today)
        data_retrieve.retrievefordm(date_dm)
        

    elif choice==2:
        flag=2
        month=0
        day=0
        months_with_31_days=[1,3,5,7,8,10,12]
        months_with_30_days=[4,6,9,11]
        while(flag==2):
            month=int(input("enter month: "))
            if(month<1 or month>12):
                print("enter valid month...")
            else:
                flag=1
            
    
        while(flag==1):
            day=int(input("enter day: "))
            if(month==2):
                if(day>28):
                    print("enter a valid day...")
                else:
                    flag=0
            elif(month in months_with_31_days):
                if(day<1 or day>31):
                    print("enter a valid day...")
                else:
                    flag=0
            elif(month in months_with_30_days):
                if(day<1 or day>30):
                    print("enter a valid day...")
                else:
                    flag=0

        print("month:",month,"\nday:",day)
        day=str(day).zfill(2)
        month=str(month).zfill(2)
        date_dm=str(day)+" "+str(month)
        data_retrieve.retrievefordm(date_dm)
    

    elif choice==3:
        check_validity.randomdate()
    

    #elif choice==4:
    elif choice==5:
        about.aboutus()

    
    print("1.Events that happened on this day\n2.Enter custom date\n3.Random date\n4.Preset date example\n5.Info\n0. =Exit= ")
    choice=int(input())   

print("Exiting the program, thank you.")
