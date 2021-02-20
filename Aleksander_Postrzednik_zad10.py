def string_k(k, bridge_of_death):
    string = []

    text = bridge_of_death.split(' ')

    for x in text:
        if len(x) >= k:
            string.append(x)
    return string


k = 4
bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

bad_chars = ['.', '-', '!', "?"]

for i in bad_chars:
    bridge_of_death = bridge_of_death.replace(i, '')

bridge_of_death = bridge_of_death.replace("\n", " ")

print(string_k(k, bridge_of_death))