file = open('Anaïs\day_8.txt','r')
data = file.read()
file.close()

data = data.split('\n')
data = [[int(element[k]) for k in range (len(element))] for element in data]

# puzzle 1

def tree_visible_up (data, tree_visible):
    visible = data[0]
    k = 1
    tree_visible[0] = [1]*len(data[0])
    for i in range (len(data)-1):
        k = i + 1
        for j in range(len(data[0])):
            if visible[j] < data[k][j]:
                tree_visible[k][j] = 1
                visible[j] = data[k][j]
    return tree_visible


def tree_visible_down (data, tree_visible):
    visible = data[-1]
    k = len(data) - 1
    tree_visible[len(data) - 1] = [1]*len(data[0])
    for i in range (len(data)):
        for j in range(len(data[0])):
            if visible[j] < data[k-1][j]:
                tree_visible[k-1][j] = 1
                visible[j] = data[k-1][j]
        k = k - 1
    return tree_visible

def tree_visible_left (data, tree_visible):
    visible = []
    for k in range(len(data)):
        tree_visible[k][0] = 1
        visible.append(data[k][0])
    for i in range (len(data[0])-1):
        k = i + 1
        for j in range(len(data)):
            if visible[j] < data[j][k]:
                tree_visible[j][k] = 1
                visible[j] = data[j][k]
    return tree_visible

def tree_visible_right (data, tree_visible):
    visible = []
    for k in range(len(data)):
        tree_visible[k][-1] = 1
        visible.append(data[k][-1])
    k = len(data) - 1
    for i in range (len(data[0])):
        for j in range(len(data)):
            if visible[j] < data[j][k-1]:
                tree_visible[j][k-1] = 1
                visible[j] = data[j][k-1]
        k = k - 1
    return tree_visible


tree_visible = [[0 for k in range(len(data[0]))] for j in range(len(data))]
tree_visible = tree_visible_up (data, tree_visible)
tree_visible = tree_visible_down (data, tree_visible)
tree_visible = tree_visible_left (data, tree_visible)
tree_visible = tree_visible_right (data, tree_visible)

tree_sum = 0
for line in tree_visible:
    for element in line:
        if element == 1:
            tree_sum += 1
print(tree_sum)



#puzzle 2

def look (data, number_line, number_colonne):
    #up
    up = 1
    down = 1
    right = 1
    left = 1
    
    # up
    for k in range(number_line - 1):
        
        if data[number_line][number_colonne] <= data[number_line - k -1][number_colonne]:
            break
        up += 1
    
    # down
    for k in range(len(data) - number_line - 2):
        if data[number_line][number_colonne] <= data[number_line + k + 1][number_colonne]:
            break
        down += 1
        
    # left
    for k in range(number_colonne - 1):
        if data[number_line][number_colonne] <= data[number_line][number_colonne - k - 1]:
            break
        left += 1
    
    # right 
    for k in range(len(data[0]) - number_colonne - 2):
        if data[number_line][number_colonne] <= data[number_line ][number_colonne + k + 1]:
            break
        right +=1
    
    return up*down*left*right

max_scenic = 0
for k in range(len(data) - 2):
    k += 1
    for j in range(len(data[0]) - 2):
        j += 1
        max_scenic = max(max_scenic, look (data, k, j))
print(max_scenic)      
        
        