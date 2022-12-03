import string

file = open('Anaïs\day_3.txt','r')
data = file.read()
file.close()
data = data.split('\n')

priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# puzzle 1

total_priority = 0
for rucksack in data:
    size = len(rucksack)
    lettre = list(set(rucksack[:size//2]) & set(rucksack[size//2:]))
    total_priority += priority.index(lettre[0]) + 1

print(total_priority)
    
# puzzle 2

total_priority = 0
size = len(data)
for i in range (size // 3):
    lettre = list(set(data[3*i]) & set(data[3*i+1]) & set(data[3*i+2]))
    total_priority += priority.index(lettre[0]) + 1

print(total_priority)
