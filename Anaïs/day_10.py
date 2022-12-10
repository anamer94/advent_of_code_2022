file = open('Anaïs\day_10.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
    
# puzzle 1

list_cycle = [20, 60, 100, 140, 180, 220]
x = 1
cycle = 0
sum_cycle = 0
for k in range (len(data)):
    cycle += 1
    if cycle in list_cycle:
        print(x, cycle)
        sum_cycle += x * cycle
    if data[k] != 'noop':
        cycle += 1
        if cycle in list_cycle:
            print(x, cycle)
            sum_cycle += x * cycle
        x = x + int(data[k].split(' ')[1])

print(sum_cycle)
        
# puzzle 2
        
list_cycle = [40, 80, 120, 160, 200, 240]
x = 1
cycle = 0
CRT =[]
line_CRT = ''
for k in range (len(data)):
    cycle += 1
    
    if len(line_CRT) in [x-1, x, x+1]:
        line_CRT += '#'
    else :
        line_CRT += '.'
    print(x, cycle)
    
    if cycle in list_cycle:
        CRT.append(line_CRT)
        line_CRT = ''
    if data[k] != 'noop':
        cycle += 1
        
        if len(line_CRT) in [x-1, x, x+1]:
            line_CRT += '#'
        else :
            line_CRT += '.'
        print(x, cycle)
        
        if cycle in list_cycle:
            CRT.append(line_CRT)
            line_CRT = ''
        
        x = x + int(data[k].split(' ')[1])

for line in CRT:
    print(line)      

        