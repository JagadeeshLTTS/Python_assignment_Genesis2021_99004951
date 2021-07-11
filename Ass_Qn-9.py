def actualDate(date, month, year):
    while(month>12 or date>31 or (month==2 and date>29 and year%400==0) or (month==2 and date>28 and year%400!=0)):
        year=year+(month//12)
        month=month%12
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            if(date>31):
                month=month+(date//31)
                date=date%31
        if (month == 4 or month == 6 or month == 9 or month == 11):
            if (date > 30):
                month = month + (date // 30)
                date = date % 30
        if(month==2 and (year%400==0)):
            if(date>29):
                month = month + (date // 29)
                date = date % 29
        else:
            if(date>28):
                month = month + (date // 28)
                date = date % 28


    date=[date,month,year]
    return date


if __name__ == '__main__':
    date=int(input("Enter date: "))
    month=int(input("Enter month "))
    year = int(input("Enter year: "))
    correct_date=[]
    correct_date=actualDate(date,month,year)
    print("Entered date is:", end=" ")
    print(date, ":", month, ":", year)
    print("Actual date is:",end=" ")
    print(correct_date[0],":",correct_date[1],":",correct_date[2])