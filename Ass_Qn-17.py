def accumulatedString(str):
    res=""
    for i in range(1,len(str)+1):
        res=res+str[i-1].upper()+(i-1)*str[i-1]+"-"
    return res[:len(res)-1]
if __name__ == '__main__':
    str=input("Enter string: ")
    res=accumulatedString(str)
    print("Accumulated string of ",str,"==> ",res)