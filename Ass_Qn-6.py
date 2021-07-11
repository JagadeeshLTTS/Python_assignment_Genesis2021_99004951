def findLowestDiffNumber(first_list):
    first_list=sorted(first_list)
    return first_list[0]-first_list[1]


if __name__ == '__main__':
    size = int(input("Enter the size of the number list : "))
    first_list = [int(input("Enter elements: ")) for i in range(size)]
    res=findLowestDiffNumber(first_list)
    print("Difference b/w two lowest Numbers in a list  is: ",res)