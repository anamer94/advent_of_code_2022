import math

file = open('Anaïs\day_9.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]

# puzzle 1

def calcul_position_H (deplacement, position_H):
    direction = deplacement[0]
    if direction == 'R':
        position_H[1] = position_H[1] + 1
    elif direction == 'L':
        position_H[1] = position_H[1] - 1
    elif direction == 'D':
        position_H[0] = position_H[0] + 1
    elif direction == 'U':
        position_H[0] = position_H[0] - 1
    return position_H

def calcul_position_T (position_H, position_T):
    if position_H == position_T:
        return position_T
    if position_H[0] == position_T[0]:
        if abs(position_H[1] - position_T[1]) != 1:
            signe = int(math.copysign(1,position_H[1] - position_T[1]))
            position_T[1] = position_T[1] + signe
    elif position_H[1] == position_T[1]:
        if abs(position_H[0] - position_T[0]) != 1:
            signe = int(math.copysign(1,position_H[0] - position_T[0]))
            position_T[0] = position_T[0] + signe
    else:
        if (abs(position_H[0] - position_T[0]) != 1) or (abs(position_H[1] - position_T[1]) != 1):
            signe = int(math.copysign(1,position_H[0] - position_T[0]))
            position_T[0] = position_T[0] + signe
            signe = int(math.copysign(1,position_H[1] - position_T[1]))
            position_T[1] = position_T[1] + signe
    return position_T

position_H = [4,0]
position_T = [4,0]
Liste_position_T = [position_T[:]]

for deplacement in data:
    nombre_deplacement = int(deplacement[2:])
    for k in range(nombre_deplacement):
        position_H = calcul_position_H (deplacement, position_H)
        position_T = calcul_position_T (position_H, position_T)
        Liste_position_T.append(position_T[:])

unique_Liste_position_T = []
[unique_Liste_position_T.append(Liste_position_T) for Liste_position_T in Liste_position_T if Liste_position_T not in unique_Liste_position_T]

print(len(unique_Liste_position_T))

# puzzle 2

position_H = [0,0]
position_1_9 = [[0,0] for k in range(9)]
Liste_position_T = [position_1_9[-1][:]]

for deplacement in data:
    nombre_deplacement = int(deplacement[2:])
    for k in range(nombre_deplacement):
        position_H = calcul_position_H (deplacement, position_H)
        position_1_9[0] = calcul_position_T (position_H, position_1_9[0])
        for k in range(len(position_1_9)-1):
            position_1_9[k+1] = calcul_position_T (position_1_9[k], position_1_9[k+1])
        Liste_position_T.append(position_1_9[-1][:])

unique_Liste_position_T = []
[unique_Liste_position_T.append(Liste_position_T) for Liste_position_T in Liste_position_T if Liste_position_T not in unique_Liste_position_T]

print(len(unique_Liste_position_T))
        