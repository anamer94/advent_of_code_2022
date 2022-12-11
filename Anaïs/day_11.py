from math import *

file = open('Anaïs\day_11.txt','r')
data = file.read()
file.close()

data = data.split('\n')

    
data_bis = []
for element in data:
    data_bis.append(element.split(':')[-1])
    
list_monkey = []    
print(len(data))
for k in range(len(data)//7):
    dict_monkey ={}
    dict_monkey['items'] = data_bis[7*k+1].split(',')
    dict_monkey['operation'] = data_bis[7*k+2].split('=')[-1]
    dict_monkey['test'] = data_bis[7*k+3].split(' ')[-1]
    dict_monkey['true'] = data_bis[7*k+4].split(' ')[-1]
    dict_monkey['false'] = data_bis[7*k+5].split(' ')[-1]
    list_monkey.append(dict_monkey)
    
print(list_monkey)

# puzzle 1

list_inspected_items = [0] * len(list_monkey)
print(list_inspected_items)
mul_com = prod([int(monkey['test']) for monkey in list_monkey])

for k in range (10000): 
    for monkey in list_monkey:
        for item in monkey['items']:
            list_inspected_items[list_monkey.index(monkey)] += 1
            operation = ''.join(list(map(lambda x: x.replace('old', item), monkey['operation'].split(' '))))
            item = floor(eval(operation)%mul_com)
            if item % int(monkey['test']) == 0:
                number_monkey = int(monkey['true'])
            else:
                number_monkey = int(monkey['false'])
            n_monkey = list_monkey[number_monkey]
            n_monkey['items'].append(str(item))
            list_monkey[number_monkey] = n_monkey
            
        monkey['items'] = []
        

print(list_inspected_items)
print(prod(sorted(list_inspected_items, reverse=True)[:2]))