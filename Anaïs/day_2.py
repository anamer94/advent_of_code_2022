file = open('Anaïs\day_2.txt','r')
data = file.read()
file.close()

# data formatting

data = data.split('\n')

# puzzle 1

dict_score = {}
dict_score['A Y'] = 2 + 6
dict_score['A X'] = 1 + 3
dict_score['A Z'] = 3 + 0
dict_score['B Y'] = 2 + 3
dict_score['B X'] = 1 + 0
dict_score['B Z'] = 3 + 6
dict_score['C Y'] = 2 + 0
dict_score['C X'] = 1 + 6
dict_score['C Z'] = 3 + 3

total_score = 0

for round in data:
    total_score += dict_score[round]
    
print(total_score)
    
# puzzle 2

dict_score = {}
dict_score['A Y'] = 1 + 3   
dict_score['A X'] = 3+ 0
dict_score['A Z'] = 2 + 6
dict_score['B Y'] = 2 + 3
dict_score['B X'] = 1 + 0
dict_score['B Z'] = 3 + 6
dict_score['C Y'] = 3 + 3
dict_score['C X'] = 2 + 0
dict_score['C Z'] = 1 + 6

total_score = 0

for round in data:
    total_score += dict_score[round]
    
print(total_score)