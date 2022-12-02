file = open('day_1.txt','r')
data = file.read()
file.close()

# data formatting

data = data.split('\n\n')
data = [element.split('\n') for element in data]

print(data)

for index_1 in range(len(data)):
    for index_2 in range (len(data[index_1])):
        data[index_1][index_2] = int(data[index_1][index_2])


# puzzle 1

list_calories = []

for Elf_inventory in data:
    calories = 0
    for item in Elf_inventory:
        calories += item
    list_calories.append(calories)

print(max(list_calories))

# puzzle 2

list_calories = sorted(list_calories)
print(list_calories[-1] + list_calories[-2] + list_calories[-3])