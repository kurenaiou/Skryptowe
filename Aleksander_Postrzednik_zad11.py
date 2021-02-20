def utf8len(s):
    return len(s.encode('utf-8'))

string = "Desmond Thomas Doss (ur. 7 lutego 1919 w Lynchburgu, zm. 23 marca 2006 w Piedmont) – żołnierz Armii Stanów Zjednoczonych, pierwszy człowiek w historii Stanów Zjednoczonych odmawiający walki oraz dotykania broni (tzw. obdżektor), który jako sanitariusz otrzymał Medal Honoru. Podczas dokonywania heroicznych czynów, za które został odznaczony Medalem Honoru, miał stopień starszego szeregowego. Służbę pełnił w Medycznym Korpusie 307 Pułku, 77 Dywizji Piechoty." \
         "Traktował religię jako najważniejszą sprawę życia i był w pełni zaangażowanym chrześcijaninem regularnie czytającym Biblię i uważającym, że jest ona Słowem Bożym, szczególnie w odniesieniu do Dziesięciu Przykazań, ważnym niezależnie od okoliczności." \
         "W czasie walk miał przy sobie Biblię podarowaną mu po ślubie przez żonę Dorothy z oznaczonym przez nią wierszem 1 Listu do Koryntian 10,13, który stanowił niejako motto jego służby wojskowej: „Dotąd nie przyszło na was pokuszenie, które by przekraczało siły ludzkie; lecz Bóg jest wierny i nie dopuści, abyście byli kuszeni ponad siły wasze, ale z pokuszeniem da i wyjście, abyście je mogli znieść”. Ulubionymi fragmentami Desmonda były Psalmy 91 i 93."

zapisane_dane = 0
znacznik = 1
limit = 5
iteracja = 1
bufor = ""

while (iteracja < limit):
    num_of_bytes = 0
    if znacznik == 1:
        p1 = open("plik_1.txt", "w", encoding='utf-8')
        while (zapisane_dane < 100 * iteracja):
            bufor += string [zapisane_dane]
            zapisane_dane += 1
        p1.write(bufor)
        znacznik = 2
        print(utf8len(bufor))
        bufor = ""
        iteracja += 1
        p1.close()

    elif znacznik == 2:
        p2 = open("file2.txt", "w", encoding='utf-8')
        while (zapisane_dane < 100 * iteracja ):
            bufor += string [zapisane_dane]
            zapisane_dane += 1
        p2.write(bufor)
        znacznik = 3
        print(utf8len(bufor))
        bufor = ""
        iteracja += 1
        p2.close()

    elif znacznik == 3:
        p3 = open("file3.txt", "w", encoding='utf-8')
        while (zapisane_dane < 100 * iteracja ):
            bufor += string [zapisane_dane]
            zapisane_dane += 1
        p3.write(bufor)
        znacznik = 1
        print(utf8len(bufor))
        bufor = ""
        iteracja += 1
        p3.close()
