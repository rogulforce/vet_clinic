# Wstęp
Bazę tworzymy i wypełniamy skryptowo. 
Przed przystąpieniem do dalszych części należy przejść do pliku `user_manual.md` i zrealizować zawarte w niej polecenia.

# Część 1 - projekt i utworzenie schematu (10p)
* analiza potrzebnych danych
	* na zasadzie burzy mózgów i researchu	
* utworzenie potrzebnego schematu za pomocą narzędzia `ERD EDITOR` - dodatku do `Visual Studio Code`

**WSTAWIĆ TUTAJ ZDJĘCIE SCHEMATU**

* wygenerowanie potrzebnych tabel przu użyciu `nazwa_pliku.py`

# Część 2 - skryptowe wypełnienie bazy (15p)

* wygenerowanie cząstkowej bazy użytkownikow Facebooka
	* oczyszczenie bazy
	* zrandomizowanie wartości (imiona, nazwiska, numery tel, pochodzenie)
	* zapisanie do `data/users_randomized.csv` przy pomocy `python pandas`
	
* tworzenie bazy przy użyciu `schema_creation.py`


* uzupełnianie bazy
	* employees
	  * księgowa
	  * szef
	  * sekretarka
	  * 2-3 weterynarzy
	* rooms
	  * zależnie od liczby weterynarzy
    * equipment
	  * trzeba wymyśleć jaki
	  * przypisujemy do pokoju
  	* visits
		* dodać kilka zaplanowanych
	* meds_perscribed
	  * na podstawie wizyty
	* meds
	  * na pdostawie wszystkich meds_perscribed
	* pets
	  * na podstawie wizyty
	* owners
	  * na podstawie wizyty
	* costs
	  * na podstawie wszystkiego innego
  *  przykładowe wyniki, dla poszczególnych tabel, przy użyciu zapytania
  ```sql
  SELECT * FROM nazwa_tabeli LIMIT 10
  ```
