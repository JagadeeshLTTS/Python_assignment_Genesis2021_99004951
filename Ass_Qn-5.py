def findMissingNumber(original_list, modified_list):
    size=len(original_list)
    count=0
    for i in range(size):
        for j in range(size):
            if(original_list[i]==modified_list[j]):
                count=1
                break
            else:
                count=0
        if(count==0):
            return original_list[i]


if __name__ == '__main__':
    size = int(input("Enter the size of the number list : "))
    original_list = [int(input("Enter elements: ")) for i in range(size)]
    modified_list=[int(input("Enter modified elements from above list: ")) for i in range(size)]
    miss_num=findMissingNumber(original_list,modified_list)
    print("Missing Number is: ",miss_num)