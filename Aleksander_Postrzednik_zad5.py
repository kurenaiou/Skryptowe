import random

names_list = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
first_letter_list = []
for letter in names_list:
    first_letter_list.append(letter[0])
print(first_letter_list)


list_of_lists = []
for n in range(5):
    list=[]
    for n in range(4):
        list.append(random.randint(1, 10))
    list_of_lists.append(list)

print(list_of_lists)