def mean(l):
    sum=0
    m=0
    for ele in l:
        sum=sum+ele
        m=sum/(len(l))
    return m
def nearestNumber(l,m):
    templist=[]
    for i in range(len(l)):
        if ((m-l[i])==0):
            return l[i]
        templist.append(abs(m-l[i]))
    templist=sorted(templist)
    return m-templist[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s=int(input("Enter the size of list: "))
    l=[int(input("Enter the elements: ")) for i in range(s)]
    m=mean(l)
    print("Mean for the given list: ",m)
    m=round(m)
    num=nearestNumber(l,m)
    print("Number nearest to mean: ",num)

