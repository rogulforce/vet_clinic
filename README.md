# vet_clinic

Projekt

Projekt zaliczeniowy składa się z 5 części. Przeczytaj całość projektu, aby wiedzieć, jaki schemat bazy będzie optymalny do rozwiązania poszczególnych zadań.

Podczas realizacji raportu możesz pracować na lokalnej bazie danych. Jeśli chcesz pracować na serwerze do zajęć (giniewicz.it), zgłoś się po indywidualny login/hasło oraz bazę danych na projekt.

## Część 1 - projekt i utworzenie schematu (10p)

Zaprojektuj i zaimplementuj schemat bazy danych kliniki weterynaryjnej. Baza powinna przynajmniej posiadać informacje o:

    pracownikach,
    posiadanym sprzęcie,
    pacjentach kliniki,
    zaplanowanych wizytach,
    kosztach i zyskach.

Schemat możesz utworzyć ręcznie (CREATE TABLE itp) albo automatycznie przez połączenie z jakimś pakietem statystycznym lub językiem programowania.

## Część 2 - skryptowe wypełnienie bazy (15p)

Połącz bazę danych z wybranym narzędziem (Python/R/Excel/Matlab/Mathematica/…).

W oparciu o losowanie wygeneruj dane do tabel. Wylosowane dane powinny mieć sens. Zadbaj między innymi o to, żeby:

    imiona i nazwiska były realistycznej długości, na przykład losując pary popularnych imion i nazwisk na podstawie danych GUS,
    daty były uporządkowane, czyli na przykład data wyleczenia nie była wcześniejsza niż data rejestracji na wizytę,
    informacje o pacjentach miały sens, nie leczymy psów mających 300 lat i ważących 973 kilogramy, ani kotów mających 23 metry długości,
    pensje pracowników powinny spełniać wymogi minimalnej krajowej, a jeszcze lepiej zapoznać się ze średnimi danymi znajdującymi się w Internecie,
    zwierzęta powinny być legalne, nadające się do leczenia i nie powinny należeć do wyginiętych gatunków — nie leczy się gupików, nie przychodzi się do kliniki z tygrysem bengalskim a z mamutem nie da się przyjść, nawet gdyby były legalne.

Rozmiar bazy powinien być rozsądny (porównywalny z tym, co może zebrać rzeczywista klinika). Załóż, że klinika działa minimum od 3 miesięcy. Użyj wyszukiwarki a znajdziesz dużo informacji o klinikach weterynaryjnych.

## Część 3 - analiza danych (20p)

Połącz bazę danych z wybranym narzędziem (może być inne niż w poprzedniej części!).

    Przygotuj wykres przedstawiający liczbę wizyt każdego dnia.
    Przygotuj wykres przedstawiający bilans zysków i strat kliniki.
    Stwórz listę zwierzaków najdłużej czekających na wizytę.
    Postaw i odpowiedz analizą na minimum cztery dodatkowe pytania.

## Część 4 - raport (10p)

Połącz bazę danych z wybranym narzędziem (może być inne niż w poprzedniej części!). Jeśli wykonujesz zadanie w tym samym narzędziu (na przykład KnitR), raport może od razu wykonywać analizę z części 3.

Przedstaw wykonaną analizę w formie raportu PDF lub HTML — całość procedury powinna dać się zautomatyzować, za pomocą wykorzystanego narzędzia lub jakiegoś skryptu uruchamiającego różne narzędzia w konkretnej kolejności.

## Część 5 - dokumentacja (15p)

Do projektu dołącz dokumentację a w niej:

    spis użytych technologii,
    listę plików i ich zawartości,
    kolejność i sposób uruchamiania plików, aby uzyskać gotowy projekt,
    schemat projektu bazy danych,
    dla każdej relacji listę zależności funkcyjnych z wyjaśnieniem,
    uzasadnienie, że baza jest w EKNF,
    opis, co było najtrudniejsze podczas realizacji projektu.

