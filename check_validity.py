import random


def randomdate():
    flag=2
    month=0
    day=0
    months_with_30_days=[4,6,9,11]
    months_with_31_days=[1,3,5,7,8,10,12]
    
    while(flag==2):
        month=random.randint(1,12)
        if(month<1 or month>12):
            continue
        else:
            flag=1
        
    while(flag==1):
        day=random.randint(1,31)
        if(month==2):
            if(day>28):
                continue
            else:
                flag=0
        elif(month in months_with_31_days):
            if(day<1 or day>31):
                continue
            else:
                flag=0
        elif(month in months_with_30_days):
            if(day<1 or day>30):
                continue
            else:
                flag=0
    
    day=str(day).zfill(2)
    month=str(month).zfill(2)
    print("month:",month,"\nday:",day)
    date_dm=str(day)+" "+str(month)   


