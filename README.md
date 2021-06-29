# Autorzy
* [Bogna Jaszczak](https://github.com/bognaj)
* [Szymon Krząstek](https://github.com/kszonsteg)
* [Piotr Rogula](https://github.com/rogulforce)

# Wstęp
Bazę tworzymy i wypełniamy skryptowo. 
Przed przystąpieniem do dalszych części należy przejść do pliku `user_manual.md` i zrealizować zawarte w niej polecenia.

# Część 1 - projekt i utworzenie schematu (10p)
* analiza potrzebnych danych
	* na zasadzie burzy mózgów i researchu	
* utworzenie potrzebnego schematu za pomocą narzędzia `ERD EDITOR` - dodatku do `Visual Studio Code`

![Schemat](resources/images/schema.png?raw=true)

* wygenerowanie potrzebnych tabel przu użyciu `main.py`, SQLowy kod znajduje się w `db_schema/db_creation.sql`

# Część 2 - skryptowe wypełnienie bazy (15p)

* wygenerowanie cząstkowej bazy użytkownikow Facebooka
	* oczyszczenie bazy
	* zrandomizowanie wartości (imiona, nazwiska, numery tel, pochodzenie)
	* zapisanie do `data/users_randomized.csv` przy pomocy `python pandas`

* zapisanie typoowych leków, sprzętów itd do plików `.xlsx` i `.csv`	
  
* tworzenie bazy przy użyciu `main.py`


* uzupełnianie bazy przy użyciu `main.py` (kod znajduje się w `tables_fulfill.py`)
	* employees
		* pracownicy
	  		* księgowa
	  		* recepcjonistka
	  		* szef
	  		* 3 weterynarzy
	 		* osoba sprzątająca
	 	* zarobki - na podstawie strony wynagrodzenia.pl
	 	* imiona i nazwiska na podstawie zrandomizowanych wartości z bazy użytkowników Facebooka
	* rooms
		* 2 gabinety weterynarzy
	  	* gabinet zabiegowy
	  	* recepcja
	  	* pomieszczenie socjalne
	  	* zaplecze
	* equipment
	  	
		* lista, z której bierzemy informacje znajduje się w pliku `meds.xlsx`
	  	
		* wygenerowano losowo dane liczbowe
	  	
		* pomieszczenie na podstawie informacji o pomieszczeniach
	* meds
	  	
		* lista, z której bierzemy informacje znajduje się w pliku `drugs.csv`
		* wygenerowane losowo dane liczbowe
	* owners
		* losowanie z zakresu, każdemu przypisujemy od 1 do kilku zwierząt wg prawdopodobiństwa
	
	* pets
	  	
		* psy: regresja liniowa na podstawie pliku `dogs.xlsx`
	  	
		* waga, wzrost oraz czas życia wszystkich zwierząt na podstawie informacji dostępnych w internecie
		* wygenerowana losowo data urodzenia
	
	* visits
		* po 20 dziennie, część odwołana, wg prawdopodobieństwa
	  	* za odwołaną wizytę płaci się opłatę manipulacyjną w wysokośći 50pln
	
		* **przypisanie zwierzęcia do lekarza prowadzącego**
		
	* meds_prescribed
		
		* na podstawie wizyty
	* cash flow
	  	
		* na podstawie wizyt i pracowników
		
	  
* przykładowe wyniki, dla poszczególnych tabel, przy użyciu zapytania:
  ```sql
  SELECT * FROM `nazwa_tabeli` LIMIT 10
  ```

* employees

![tabela1](resources/images/employees.png?raw=true)

* rooms

![tabela2](resources/images/rooms.png?raw=true)

* equipment

![tabela3](resources/images/equipment.png?raw=true)

* meds

![tabela3](resources/images/meds.png?raw=true)

* owners

![tabela3](resources/images/owners.png?raw=true)

* pets

![tabela3](resources/images/pets.png?raw=true)

* visits

![tabela3](resources/images/visits.png?raw=true)

* meds prescribed

![tabela3](resources/images/meds_perscribed.png?raw=true)

* cash flow

![tabela3](resources/images/cashflow2.png?raw=true)

![tabela3](resources/images/cashflow1.png?raw=true)


# Część 3 - analiza danych (20p)

* wykres przedstawiający liczbę wizyt każdego dnia.
* wykres przedstawiający bilans zysków i strat kliniki.
* lista zwierzaków najdłużej czekających na wizytę.
* rozkład wagi zwierząt
* zarobki lekarzy w stosunku do liczby wizyt
* najczęściej przypisywane leki
* procentowy podział strat

# Część 4 - raport (10p)

Po wypełnieniu poleceń z `user_manual.md` powinien pojawić się plik `final_code/analiza.html`,
czyli raport.

# Część 5 - dokumentacja (15p)

* spis użytych technologii
  * znajduje się w `user_manual.md`


* lista plików i ich zawartości
  * data
	* `dogs.xlsx` -> informacje o psach
	* `drugs.csv` ->  informacje o lekach
	* `users_randomized` -> zrandomizowana baza danych osobowych
  * db_schema
	* `db_creation.sql` -> kod tworzacy bazę danych
	* `schema.vuerd.json` -> schemat bazy danych
  * final_code
	* `analiza.html` -> notebook z analizą z `#3` i `#4` w formie `.html`
	* `main.py` -> skypt generujący i wypełniający bazę oraz tworzący raport
	* `schema_creaction.py` -> plik zawierający funkcje potrzebne do połączenia z bazą
	* `tables_fulfill.py` -> plik zawierający funkcje potrzebne do wypełnienia bazy
	* `report` -> folder zawierający wykresy do raportu  
  * generate
	* pliki z różnymi danymi dotyczącymi klinik weterynaryjnych
		* zarobki, zwierzęta, proste regresji, medykamenty, itd.
  * resources
	* notebooki do czyszczenia danych, wersje testowe, obrazki do `README.md`, itd.


* kolejność i sposób uruchamiania plików, aby uzyskać gotowy projekt
  * znajduje się w `user_manual.md`
	

* schemat projektu bazy danych
  
  * znajduje się w na początku `README.md`
	

* dla każdej relacji listę zależności funkcyjnych z wyjaśnieniem
  * meds
  	* klucze kandydujące: `drugID`, `name`
  	* klucz główny: `drugID`
  	* zależności funkcyjne: trywialne (np. `ordered` -> `ordered`), `drugID` -> pozostałe pozdbiory atrybutów relacji, `name` -> pozostałe podzbiory atrybutów relacji
  	* komentarz: `drugID` jest oczywiście unikatowym kluczem głównym. `name` jest unikatowym atrybutem. w naszej bazie danych leki określamy jako substancje czynne - stąd każda wartość jest unikatowa. 
  * meds_prescribed
  	* klucze kandydujące: `(drugID, name)` <- klucz kompozytowy
  	* klucz główny: `(drugID, name)`
  	* zależności funkcyjne: trywialne, `(drugID, name)` -> pozostałe pozdbiory atrybutów relacji
  	* komenatarz: klucz główny jest kluczem kompozytowym, gdyż w ciągu jednej wizyty możemy przypisać wiele leków, a jeden lek może być przypisany wielu wizytom
  * employees
 	* klucze kandydujące: `employeeID`
  	* klucz główny: `employeeID`
  	* zależności funkcyjne: trywialne, `employeeID` -> pozostałe pozdbiory atrybutów relacji
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym
  * pets
  	* klucze kandydujące: `petID`
  	* klucz główny: `petID`
  	* zależności funkcyjne: trywialne, `petID` -> pozostałe pozdbiory atrybutów relacji 
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym
  * owners
  	* klucze kandydujące: `ownerID`
  	* klucz główny: `ownerID`
  	* zależności funkcyjne: trywialne, `ownerID` -> pozostałe pozdbiory atrybutów relacji 
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym. adres email i numer telefonu nie są unikatowe, ponież są to tylko dane kontektowe, wartości te nie są wykorzystywane do logowania do systemu. przykładowo mąż i żona mogą posiadać ten sam numer telefonu (domowy) oraz podać tę samą skrzynkę mailową.
  * rooms
	* klucze kandydujące: `roomID`, `number`
  	* klucz główny: `roomID`
  	* zależności funkcyjne: trywialne, `roomID` -> pozostałe pozdbiory atrybutów relacji, `number` -> pozostałe pozdbiory atrybutów relacji
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym. każdy pokój posiada swój unikatowy numer (unikoatowy w ramach kliniki). nie użyliśmy numeru pokoju jako klucza głównego, ponieważ czasami numery pokojów zostają zmienione, a zmienienie kluczy głównych w całej bazie danych jest bardzo niepożądaną operacją.
  * equipment
	* klucze kandydujące: `eqID`, `(eqName, status, room_number)` 
  	* klucz główny: `eqID`
  	* zależności funkcyjne: trywialne, `eqID` -> pozostałe pozdbiory atrybutów relacji, `(eqName, status, room_number)` ->  pozostałe pozdbiory atrybutów relacji
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym. klucz kandydujący kompozytowy również jednoznacznie identyfikuje krotkę.
  * visits
  	* klucze kandydujące: `visitID`
  	* klucz główny: `visitID`
  	* zależności funkcyjne: trywialne, `visitID` -> pozostałe pozdbiory atrybutów relacji 
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym
  * cash_flow
  	* klucze kandydujące: `cfid`
  	* klucz główny: `cfid`
  	* zależności funkcyjne: trywialne, `cfid` -> pozostałe pozdbiory atrybutów relacji 
  	* komenatarz: klucz główny relacji jest atrybutem unikatowym
  	
* uzasadnienie, że baza jest w EKNF
  * jak wykazaliśmy w poprzednim podpunkcie, każda nietrywialna zależność funkcyjna albo zaczyna się od nadklucza albo kończy się na
atrybucie elementarnym. Oznacza to, że baza jest w EKNF. 
* opis, co było najtrudniejsze podczas realizacji projektu
	* uzasadnienie, że baza jest w EKNF
	* wyeliminowanie problemów technicznych związanych z generowaniem skryptowym i wypełnianiem bazy
