file = open('Anaïs\day_14.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]  
data = [[eval(element) for element in (line.split(" -> "))] for line in data]
print(data)

def print_grid(list_path, list_sand):
    max_x = max(max([element[0] for element in list_path]), max([element[0] for element in list_sand]))
    min_x = min(min([element[0] for element in list_path]), min([element[0] for element in list_sand]))
    for k in range(max_y +1):
        unit_print=''
        for j in range( max_x - min_x +1):
            if [min_x + j,k] in list_sand:
                unit_print += 'o'  
            elif [min_x + j,k] in list_path:
                unit_print += '#'
            else:
                unit_print += '.'
        print(unit_print)
    print(max_x, min_x)

def path (data):
    path = []
    for line in data:
        for k in range(len(line)-1):
            x,y = line[k]
            x1,y1 = line[k+1]
            if x1 == x:
                for j in range(abs(y1-y)+1):
                    if [x,min(y,y1)+j] not in path:
                        path.append([x,min(y,y1)+j])
            elif y1 == y:
                for j in range(abs(x1-x)+1):
                    if [min(x,x1)+j,y] not in path:
                        path.append([min(x,x1)+j,y])
    return path

def can_move(xy,list_sand, list_path, max_y):
    if xy[1]+1> max_y:
        return "max_atteint"
    if [xy[0],xy[1]+1] not in list_path and [xy[0],xy[1]+1] not in list_sand:
        return [xy[0],xy[1]+1]
    elif [xy[0]-1,xy[1]+1] not in list_path and [xy[0]-1,xy[1]+1] not in list_sand:
        return [xy[0]-1,xy[1]+1]
    elif [xy[0]+1,xy[1]+1] not in list_path and [xy[0]+1,xy[1]+1] not in list_sand:
        return [xy[0]+1,xy[1]+1]
    return False

def sand(sand_begin, list_sand, list_path, max_y):
    xy = sand_begin
    while xy  not in [False, "max_atteint"]:
        unit_sand = xy
        xy = can_move(xy,list_sand, list_path, max_y)
        
    if xy == "max_atteint":
        return False
    list_sand.append(unit_sand)
    return True


#puzzle 1
# list_path = path(data)
# max_y = max([element[1] for element in list_path])
# print(max_y)
# sand_begin = [500,0]
# list_sand = []
# unit_sand = 0


# while sand(sand_begin, list_sand, list_path, max_y) != False:
#     unit_sand += 1
# print_grid(list_path, list_sand)
# print(unit_sand)

#puzzle 2

def can_move_2(xy,list_sand, list_path, max_y):
    if xy[1]+1 == max_y:
        return "max_atteint"
    if [xy[0],xy[1]+1] not in list_path and [xy[0],xy[1]+1] not in list_sand:
        return [xy[0],xy[1]+1]
    elif [xy[0]-1,xy[1]+1] not in list_path and [xy[0]-1,xy[1]+1] not in list_sand:
        return [xy[0]-1,xy[1]+1]
    elif [xy[0]+1,xy[1]+1] not in list_path and [xy[0]+1,xy[1]+1] not in list_sand:
        return [xy[0]+1,xy[1]+1]
    return False

def sand_2(sand_begin, list_sand, list_path, max_y):
    xy = sand_begin
    while xy  not in [False, "max_atteint"]:
        unit_sand = xy
        xy = can_move_2(xy,list_sand, list_path, max_y)
   
    if unit_sand == [500,0]:
        return False
    list_sand.append(unit_sand)
    return unit_sand

list_path = path(data)
max_y = max([element[1] for element in list_path]) + 2
sand_begin = [500,0]
list_sand = [[500,0]]
unit_sand = 0


while sand_2(sand_begin, list_sand, list_path, max_y) != False and unit_sand < 40000:
    unit_sand += 1
    print(unit_sand+1)

print_grid(list_path, list_sand)
print(max_y)
print(unit_sand+1)

    
    
