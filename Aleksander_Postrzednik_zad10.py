import re

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

standard_pattern = re.compile(r'(\b\w{4,}\b)')
words_in_sentence = set(standard_pattern.findall(bridge_of_death))
print(words_in_sentence)