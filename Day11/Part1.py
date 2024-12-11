data = [8069,87014,98,809367,525,0,9494914,5]
updater = []
base = False

def splitByMid(num: int):
    val = str(num)
    length = len(val)
    mid = length//2
    return [int(val[0:mid]),int(val[mid::])]

for i in range(75):
    print()
    if base == False:
        updater = []
        for i in range(len(data)):
            if data[i] == 0:
                updater.append(1)
                # print(1)
            elif len(str(data[i]))%2==0:
                split = splitByMid(data[i])
                updater.append(split[0])
                updater.append(split[1])
                # print(2)
            else:
                val = data[i]
                updater.append(val*2024)
                # print(3)
        base = True
    else:
        data = []
        for i in range(len(updater)):
            if updater[i] == 0:
                data.append(1)
                # print(11)
            elif len(str(updater[i]))%2==0:
                split = splitByMid(updater[i])
                data.append(split[0])
                data.append(split[1])
                # print(22)
            else:
                val = updater[i]
                data.append(val*2024)
                # print(33)
        base = False

print(len(updater))