def numPeople(onBoard,offBoard):
    return onBoard-offBoard

if __name__ == '__main__':
    onBoard=int(input("Enter the no. of people onboarded: "))
    offBoard = int(input("Enter the no. of people alighted: "))
    num=numPeople(onBoard,offBoard)
    if(num<0):
        print("Entered Wrong Values")
    print("No. of people in Bus: ",num)
