file = open('Anaïs\day_4.txt','r')
data = file.read()
file.close()
data = data.split('\n')
data = [element.split(',') for element in data]

# puzzle 1

total_pair = 0
for pair in data:
    elf_1 = pair[0].split('-')
    elf_2 = pair[1].split('-')
    if ((int(elf_1[0])<=int(elf_2[0]) and int(elf_1[1])>=int(elf_2[1])) 
        or (int(elf_1[0])>=int(elf_2[0]) and int(elf_1[1])<=int(elf_2[1]))) :
        total_pair += 1

print(total_pair)

# puzzle 2

total_pair = 0
for pair in data:
    elf_1 = pair[0].split('-')
    elf_2 = pair[1].split('-')
    if ((int(elf_1[0])<=int(elf_2[0]) and int(elf_1[1])>=int(elf_2[0])) 
        or (int(elf_1[0])<=int(elf_2[1]) and int(elf_1[1])>=int(elf_2[1])) 
        or (int(elf_1[0])>=int(elf_2[0]) and int(elf_1[0])<=int(elf_2[1]))
        or (int(elf_1[1])>=int(elf_2[0]) and int(elf_1[1])<=int(elf_2[1]))):
        total_pair += 1

print(total_pair)
    