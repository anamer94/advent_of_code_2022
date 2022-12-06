from collections import Counter

file = open('Anaïs\day_6.txt','r')
data = file.read()
file.close()

# puzzle 1

for k in range(len(data)-3):
    L = [i for i,j in Counter(data[k:k+4]).items() if j>1]
    if L == []:
        print(k+4)
        break

# puzzle 2

for k in range(len(data)-13):
    L = [i for i,j in Counter(data[k:k+14]).items() if j>1]
    if L == []:
        print(k+14)
        break