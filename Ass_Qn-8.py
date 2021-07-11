def actualTime(hour, minute, second):
    while(hour>=24 or minute>=60 or second>=60):
        if(hour>=24):
            hour=hour%24
        if(minute>=60):
            hour = hour + (minute // 60)
            minute=minute%60
        if(second>=60):
            minute = minute + (second // 60)
            second=second%60
    time=[hour,minute,second]
    return time


if __name__ == '__main__':
    hour=int(input("Enter Hour's Time: "))
    minute=int(input("Enter minute's time: "))
    second = int(input("Enter second's time: "))
    correct_time=[]
    correct_time=actualTime(hour,minute,second)
    print("Actual Time is:",end=" ")
    print(correct_time[0],":",correct_time[1],":",correct_time[2])
