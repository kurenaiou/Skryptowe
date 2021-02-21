slowo_klucz = "truskawka"

print("Mały czerwony owoc o słodkim smaku. Co to za owoc?")

ilosc_prob = 3

for i in range(ilosc_prob):
    if i < ilosc_prob:
        if input().lower() == slowo_klucz:
            print("gratulacje!")
            break
        else:
            print("sprobuj ponownie")
    else:
        print("Niestety nie udalo ci sie zgadnac")
        break
