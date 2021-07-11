def splitToDigits(number):
    d=[int(i) for i in number]
    return d
def findLargestNumber(digits_list):
    digits_list.sort(reverse=True)
    num=digits_list[0]
    for i in range(1,len(digits_list)):
        num=num*10+digits_list[i]
    return num


if __name__ == '__main__':
    number=input("Enter number: ")
    digits_list=splitToDigits(number)
    largest_num=findLargestNumber(digits_list)
    print("Largest number by shuffling digits in the",number,"is:",largest_num)