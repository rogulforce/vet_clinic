import random as r

# trzeba ustalić pracowników
# to klinika, więc musi być z 4-5 weterynarzy
# https://wynagrodzenia.pl/moja-placa/ile-zarabia-lekarz-weterynarii

# szefu całej kliniki
pensja_szef = r.randint(5361, 10000)

# ze dwóch weterynarzy z dłuższym stażem
pensja_starszy1 = r.randint(4500, 5360)
pensja_starszy2 = r.randint(4500, 5360)

# i ze dwóch z krótszym stażem
pensja_mlodszy1 = r.randint(3670, 4500)
pensja_mlodszy2 = r.randint(3670, 4500)

# przyda nam się też księgowa, która te pensje ogarnie
# https://wynagrodzenia.pl/moja-placa/ile-zarabia-ksiegowy
ksiegowa = r.randint(3920, 5990)

# no i może jedna osoba w recepcji
# https://wynagrodzenia.pl/moja-placa/ile-zarabia-recepcjonista
recepcjonista = r.randint(3080, 4240)

# i jedna osoba do sprzątania
# https://wynagrodzenia.pl/moja-placa/ile-zarabia-pracownik-sprzatajacy
sprzatacz = r.randint(2600, 3220)
