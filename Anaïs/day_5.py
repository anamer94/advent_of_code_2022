import queue

file = open('Anaïs\day_5.txt','r')
data = file.read()
file.close()
data = data.split('\n')

index = data.index('')

data_stack = data[:index-1]
number = data[index-1:index]
data_procedure = data[index+1:]

# nomber of stack
number = number[0].split(' ')
number = int(number[-2])

# data formatting for crate stack
data_int = [queue.LifoQueue() for k in range(number)]
data_stack.reverse()
for line in data_stack:
    for k in range(number):
        print([line[1 + 4*(number-1-k)]])
        if line[1 + 4*k] != ' ':
            data_int[k].put(line[1 + 4*k])
data_stack = data_int

# data formatting for procedure
data_procedure = [element.split(' ') for element in data_procedure]

# puzzle 1

# for line in data_procedure:
#     List_int = []
#     for k in range(int(line[1])):
#         List_int.append(data_stack[int(line[3])-1].get())
#     for k in range(int(line[1])):
#         data_stack[int(line[5])-1].put(List_int[k])

# print(''.join([q.get() for q in data_stack]))
    
#puzzle 2

for line in data_procedure:
    List_int = []
    for k in range(int(line[1])):
        List_int.append(data_stack[int(line[3])-1].get())
    List_int.reverse()
    for k in range(int(line[1])):
        data_stack[int(line[5])-1].put(List_int[k])

print(''.join([q.get() for q in data_stack]))

