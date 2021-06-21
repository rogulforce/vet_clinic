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

_In progress..._

# Część 4 - raport (10p)

_In progress..._

# Część 5 - dokumentacja (15p)

_In progress..._
