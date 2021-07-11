if __name__ == '__main__':
    RGB= list(map(int, input("Enter a multiple value: ").split()))
    str="0x"
    for i in RGB:
        str=str+hex(i)[2:]
    print(str)
