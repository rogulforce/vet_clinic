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
  * meds / drugID - meds_prescribed / drugID
	* połączenie przypisanego leku z bazą leków
  * meds_prescribed / visitID - visits / visitID
	* połączenie przypisanego leku z wizytą
  * employees / employeeID - visits / employeeID
	* połączenie pracownika z wizytą
	
  * pets / petID - visits / petID
	* połączenie zwirzaka z wizytą
  * pets / ownerID - owners / ownerID
	* połączenie zwierzaka z właścicielem
	
  * visits / number - rooms / number
	* połączenie wizyty z pokojem
	
  * equipment / number - rooms / number
	* połączenie pokoju ze sprzętem 
	
* uzasadnienie, że baza jest w EKNF
  * BRAK PÓKI CO (?)
* opis, co było najtrudniejsze podczas realizacji projektu
	* uzasadnienie, że baza jest w EKNF
	* wyeliminowanie problemów technicznych związanych z generowaniem skryptowym i wypełnianiem bazy