filename = 'log_channels_105.txt'
elementList = []

with open(filename) as file:
    for line in file.readlines():
        elementList.append(line.rstrip('\n'))

print(elementList)
