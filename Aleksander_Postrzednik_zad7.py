def person_print(name, last_name, age, *others, **kwargs):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age,)
    others_str = '   '
    for arg in others:
        others_str += arg + '  '
    print(formatted_data + others_str)


person_print('alek', 'post', '18',  'koszykowka', 'pilka_nozna', first="Geeks",mid="for",last="Geeks")

#Nie można było użyc tej funkcji bez modyfikowania
#Najpierw trzeba podac pojedyncze argumenty, pozniej mozna uzyc gwiazdka *args
#na końcu dopiero **kwargs