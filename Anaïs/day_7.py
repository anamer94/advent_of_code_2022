file = open('Anaïs\day_7.txt','r')
data = file.read()
file.close()

data = data.split('\n')

# puzzle 1

arborences = {}
arborences['/'] = []
directory = '/'

for line in data[1:]:
    if "$ cd" in line:
        if '..' in line:
            directory = directory.split("/")
            directory = "/".join(directory[:-1])
        else:
            list_int = line.split(" ")
            directory = directory + '/' + list_int[-1]
    elif "$ ls" == line:
        do_nothing = 1
    else:
        list_int = line.split(" ")
        if "dir" in line:
            arborences[directory].append(directory + '/' + list_int[-1])
            arborences[directory + '/' + list_int[-1]] = []
        else: 
            arborences[directory].append(directory + '/' + list_int[-1])
            arborences[directory + '/' + list_int[-1]] = int(list_int[0])

dict_size = {}

def calcul_size(arborences, dict_size, directory):
    if isinstance(arborences[directory], (int)):
        return dict_size, arborences[directory]
    else :
        size = 0
        for element in arborences[directory]:
            if element in dict_size:
                size += dict_size[element]
            else:
                dict_size, size_element = calcul_size(arborences, dict_size, element)
                size += size_element
        dict_size[directory] = size
        return dict_size, size

dict_size, size = calcul_size(arborences, dict_size, '/')
size_sum = 0

for element in list(dict_size.keys()):
    if dict_size[element]<=100000:
        size_sum += dict_size[element]
print(size_sum)
        
size_max = 30000000 - 70000000 + size  
size_del = 70000000

for element in list(dict_size.keys()):
    if dict_size[element]>= size_max:
        size_del = min(size_del, dict_size[element])

print(size_del)
        
