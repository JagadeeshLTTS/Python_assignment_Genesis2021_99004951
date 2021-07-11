def mean(l):
    sum=0
    m=0
    for ele in l:
        sum=sum+ele
        m=sum/(len(l))
    return m
def smallerMeanNumbersCount(l,m):
    count=0
    for i in l:
        if(i<m):
            count=count+1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size=int(input("Enter the size of list: "))
    l=[int(input("Enter the elements: ")) for i in range(size)]
    mean_value=mean(l)
    print("Mean for the given list: ",mean_value)
    count=smallerMeanNumbersCount(l,mean_value)
    print("Count of Numbers smaller than mean: ",count)

