import string

file = open('Anaïs\day_12.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]   
    
def find_letter(data, letter):
    for k in range(len(data)):
        for j in range (len(data[0])):
            if letter == data[k][j]:
                return [k, j]
    return False

data = [[letter for letter in element] for element in data]
S = find_letter(data, 'S')
data[S[0]][S[1]]= 'a'
E = find_letter(data, 'E')
data[E[0]][E[1]]= 'z'
priority = list(string.ascii_lowercase)
data = [[priority.index(element) for element in line] for line in data]

def where_can_move(data, seen, x, y):
    xy = []
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    for element in move:
        x1 = x + element[0]
        y1 = y + element[1]
        if (x1>=0 and x1<len(data) and y1>=0 and y1<len(data[0]) and [x1,y1] not in seen):
            if 1 >= data[x1][y1]-data[x][y]:
                xy.append([x1, y1])
    return xy


seen = [S]
study = [S]
sum_tot = 0

while study != []:
    sum_tot += 1
    new_study = []
    for element in study:        
        list_int = where_can_move(data, seen, element[0], element[1])
        new_study += list_int
        seen += list_int
    if E in seen:
        print(sum_tot) 
        break   
    elif new_study == []:
        print('problem')
        break
    else:
        study = new_study[:]

# puzzle 2

def find_all_letter(data, letter):
    position = []
    for k in range(len(data)):
        for j in range (len(data[0])):
            if letter == data[k][j]:
                position.append([k, j])
    return position

a = find_all_letter(data, 0)
list_sum_tot = []

for S in a:
    seen = [S]
    study = [S]
    sum_tot = 0

    while study != []:
        sum_tot += 1
        new_study = []
        for element in study:        
            list_int = where_can_move(data, seen, element[0], element[1])
            new_study += list_int
            seen += list_int
        if E in seen:
            list_sum_tot.append(sum_tot)
            break   
        elif new_study == []:
            break
        else:
            study = new_study[:]
            
print(min(list_sum_tot))