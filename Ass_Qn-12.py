def mexicanWave(st):
    wave=[];
    for i in range(len(st)):
        uppercase=st[i].upper()
        new_str=st[:i]+uppercase+st[i+1:]
        wave.append(new_str)
    return wave



if __name__ == '__main__':
    st=input("Enter a String: ")
    wave=mexicanWave(st)
    print(wave)
