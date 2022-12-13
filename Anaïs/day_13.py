import string

file = open('Anaïs\day_13.txt','r')
data = file.read()
file.close()

data = data.split('\n')
data = [eval(element) for element in data if element != '']

# puzzle 1 

def compare_left_right(right, left):
    good = None
    # print(left, right)
    for k in range (min(len(right), len(left))):
        good = None
        if type(right[k]) is int and type(left[k]) is int :
            if int(left[k]) > int(right[k]):
                return False
            elif int(left[k]) < int(right[k]):
                return True
        elif type(right[k]) is list and type(left[k]) is list:
            good =  compare_left_right(right[k], left[k])
        elif  type(right[k]) is list and type(left[k]) is int:
            list_int = [left[k]]
            good =  compare_left_right(right[k], list_int)
        elif  type(right[k]) is int and type(left[k]) is list:
            list_int = [right[k]]
            good =  compare_left_right(list_int, left[k])
        
        if good == False or good == True:
            return good
    
    if len(left) > len(right):
        return False
    
    if len(left) < len(right):
        return True

    return None
    
# puzzle 1 

sum_tot = 0
for k in range (len(data)//2):
    left = data[2*k]
    right = data[2*k+1]
    good = compare_left_right(right, left)
    if good == True:
        sum_tot += k+1

print(sum_tot)

# puzzle 2

data.insert(0, [[2]])
data.insert(0, [[6]])

def tri_insertion(L):
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and compare_left_right(L[j], cle):
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle


tri_insertion(data)
print((data.index([[2]])+1)*(data.index([[6]])+1))
    
    
    