def removeDigit(number):
    values=[]
    for i in range(len(number)):
        new_number=number[:i]+number[i+1:]
        values.append(new_number)
    return values

def findLargerNumber(values):
    values=sorted(values)
    return values[len(values)-1]



if __name__ == '__main__':
    number=input("Enter number: ")
    values=removeDigit(number)
    print("List of number after removing one digit",values)
    largest_number=findLargerNumber(values)
    print("Largest Number among the list",largest_number)