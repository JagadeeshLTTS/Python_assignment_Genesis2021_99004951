def findOddNumber(num_list):
    size=len(num_list)
    count=0
    for i in range(size):
        for j in range(size):
            if(j==i):
                continue
            if(num_list[i]==num_list[j]):
                count=1
                break
            else:
                count=0
        if(count==0):
            return num_list[i]

if __name__ == '__main__':
    size=int(input("Enter the size of the list as odd number : "))
    if((size%2)!=0):
        num_list = [int(input("Enter elements: ")) for i in range(size)]
        num = findOddNumber(num_list)
        print("Stray Number is: ", num)
    else:
        print("Wrong size entered")