def is_isogram(st):
    strlen=len(st)
    count=0
    for i in range(strlen):
        for j in range(i+1,strlen):
            if(st[i]==st[j]):
                count=count+1
                return False
    if count==0:
        return True

if __name__ == '__main__':
    st=input("Enter a string: ")
    if(is_isogram(st)):
        print("Given String",st,"is isogram")
    else:
        print("Given String",st,"is NOT isogram")
