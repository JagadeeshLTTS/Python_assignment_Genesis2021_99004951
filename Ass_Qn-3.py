def findAvgSpeed(speed_list):
    sum=0
    for item in speed_list:
        sum=sum+item
    return sum/len(speed_list)


if __name__ == '__main__':
    size = int(input("Enter the size of the speeds list : "))
    speed_list = [int(input("Enter speed at fixed time intervals: ")) for i in range(size)]
    avgSpeed=findAvgSpeed(speed_list)
    print("Average Speed is: ",avgSpeed)
