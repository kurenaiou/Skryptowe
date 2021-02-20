import copy

di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
copy = copy.deepcopy(di)
di['four'][0] = 'cztery'

print("Orginal :\n", di)
print("Kopia : \n", copy)