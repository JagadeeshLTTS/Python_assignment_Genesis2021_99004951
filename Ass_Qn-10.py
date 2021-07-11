def convertToDecimal(hexa_number):
    res=""
    for item in hexa_number:
        if item=='a':
            res=res.__add__("10.")
        if item=='b':
            res = res.__add__("11.")
        if item=='c':
            res = res.__add__("12.")
        if item=='d':
            res = res.__add__("13.")
        if item=='e':
            res = res.__add__("14.")
        if item=='f':
            res=res.__add__("15.")
    return res
def convertToHexa(decimal_number):
    res=""
    for item in decimal_number:
        if item==10:
            res=res.__add__("a.")
        if item==11:
            res=res.__add__("b.")
        if item==12:
            res = res.__add__("c.")
        if item==13:
            res = res.__add__("d.")
        if item==14:
            res=res.__add__("e.")
        if item==15:
            res=res.__add__("f.")
    return res
if __name__ == '__main__':
    hexa_number=input("Enter the ipv6 address: ")
    decimal_number=list(map(int, input("Enter a multiple value: ").split()))
    number1=convertToDecimal(hexa_number)
    print(hexa_number,"Converted to ",number1)
    number2=convertToHexa(decimal_number)
    print(decimal_number, "Converted to ", number2)
