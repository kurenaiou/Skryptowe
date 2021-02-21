plik_one = open('plik.txt', 'r+')
plik_one.write('plik ma teraz wiecej tresci!')
plik_one.seek(0)
print(plik_one.readlines())

