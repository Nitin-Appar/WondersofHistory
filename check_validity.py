import random


# function randomdate creates a random date between the given constraints and checks its validity to return a fully random and valid date
def randomdate():
    flag = 1
    month = 0
    day = 0
    months_with_30_days = [4, 6, 9, 11]
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

    # creating a random month between 1 and 12
    month = random.randint(1, 12)

    # createing a random day between the constraints 1 and 31 and checking its validity against the random month created
    while(flag == 1):
        day = random.randint(1, 31)
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

    # adding a leading 0 to the final random day and month to return a 2 digit number
    day = str(day).zfill(2)
    month = str(month).zfill(2)
    date_dm = str(day)+" "+str(month)
    print("the month is:", month, "\nthe day is:", day)
    return date_dm
