import time
import random

long_list = [random.randint(0, 3000) for element in range(1000000)]

czas_poczatkowy = time.time()
proba_1 = -1 in long_list
czas_koncowy = time.time()
czas_wykonania = czas_koncowy - czas_poczatkowy

print('Sposób 1 time(): ', czas_wykonania, 'secoonds\n')

#2
timer_start = time.time()
for i in range(len(long_list)):
    if list[i] == -1:
        print ("jest")
        break
timer_stop = time.time()
print('Sposób 2 time(): ', timer_stop - timer_start, 'secoonds\n')








#true or false
