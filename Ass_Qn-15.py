def rmvDuplicate(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


def findWordFrequency(message):
    words=message.split()
    word_list=rmvDuplicate(words)
    for item in word_list:
        print("The Frequency of ",item,"is: ",message.count(item))


if __name__ == '__main__':
    message=input("Enter message: ");
    findWordFrequency(message)
