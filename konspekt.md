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

* wygenerowanie potrzebnych tabel przu użyciu `nazwa_pliku.py`

# Część 2 - skryptowe wypełnienie bazy (15p)

* wygenerowanie cząstkowej bazy użytkownikow Facebooka
	* oczyszczenie bazy
	* zrandomizowanie wartości (imiona, nazwiska, numery tel, pochodzenie)
	* zapisanie do `data/users_randomized.csv` przy pomocy `python pandas`
	
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
	  	* wygenerowan losowo dane liczbowe
	  	* pomieszczenie na podstawie informacji o pomieszczeniach
	* meds
	  	* lista, z której bierzemy informacje znajduje się w pliku `drugs.csv`
	  	* wygenerowane losowo dane liczbowe
	* visits
	  
	* pets
	  	* psy: regresja liniowa na podstawie pliku `dogs.xlsx`
	  	* waga, wzrost oraz czas życia wszystkich zwierząt na podstawie informacji dostępnych w internecie
	  	* wygenerowana losowo data urodzenia
	* owners
	  	* na podstawie wizyty
	* meds_perscribed
	  	* na podstawie wizyty
	* costs
	  	* na podstawie wszystkiego innego
* przykładowe wyniki, dla poszczególnych tabel, przy użyciu zapytania:
  ```sql
  SELECT * FROM `nazwa_tabeli` LIMIT 10
  ```
![tabela1](resources/images/sample.jpg?raw=true)
![tabela2](resources/images/sample.jpg?raw=true)
![tabela3](resources/images/sample.jpg?raw=true)
