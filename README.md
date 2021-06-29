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
  
  * Pycharm 2020.1.3
  * dbdiagram.io

  * Windows 10

  * MariaDB server 10.5

  * Python 3.9 with packages:

	* argon2-cffi         20.1.0
	* async-generator     1.10
	* attrs               20.3.0
	* backcall            0.2.0
	* bleach              3.3.0
	* cffi                1.14.5
	* colorama            0.4.4
	* cycler              0.10.0
	* decorator           5.0.7
	* defusedxml          0.7.1
	* entrypoints         0.3
	* et-xmlfile          1.1.0
	* ipykernel           5.5.3
	* ipython             7.22.0
	* ipython-genutils    0.2.0
	* ipywidgets          7.6.3
	* jedi                0.18.0
	* Jinja2              2.11.3
	* joblib              1.0.1
	* jsonschema          3.2.0
	* jupyter             1.0.0
	* jupyter-client      6.1.12
	* jupyter-console     6.4.0
	* jupyter-core        4.7.1
	* jupyterlab-pygments 0.1.2
	* jupyterlab-widgets  1.0.0
	* kiwisolver          1.3.1
	* mariadb             1.0.6
	* MarkupSafe          1.1.1
	* matplotlib          3.4.1
	* mistune             0.8.4
	* nbclient            0.5.3
	* nbconvert           6.0.7
	* nbformat            5.1.3
	* nest-asyncio        1.5.1
	* notebook            6.3.0
	* numpy               1.20.2
	* openpyxl            3.0.7
	* packaging           20.9
	* pandas              1.2.4
	* pandocfilters       1.4.3
	* parso               0.8.2
	* pickleshare         0.7.5
	* Pillow              8.2.0
	* pip                 21.1.3
	* plotly              4.14.3
	* prometheus-client   0.10.1
	* prompt-toolkit      3.0.18
	* pycparser           2.20
	* Pygments            2.8.1
	* pyparsing           2.4.7
	* pyrsistent          0.17.3
	* python-dateutil     2.8.1
	* pytz                2021.1
	* pywin32             300
	* pywinpty            0.5.7
	* pyzmq               22.0.3
	* qtconsole           5.0.3
	* QtPy                1.9.0
	* scikit-learn        0.24.2
	* scipy               1.6.2
	* seaborn             0.11.1
	* Send2Trash          1.5.0
	* setuptools          49.2.1
	* six                 1.15.0
	* sklearn             0.0
	* terminado           0.9.4
	* testpath            0.4.4
	* threadpoolctl       2.1.0
	* tornado             6.1
	* traitlets           5.0.5
	* wcwidth             0.2.5
	* webencodings        0.5.1
	* widgetsnbextension  3.5.1
	* xlrd                2.0.1
	* plotly			  5.1.0
	* tenacity			  6.2.0
	

  
* lista plików i ich zawartości
  * `main.py` -> skypt generujący i wypełniający bazę oraz tworzący raport
  * `analiza.html` -> notebook z analizą z `#3` i `#4` w formie `.html`  
  * `user_manual.md` -> instrukcja
  * `polecenie.md` -> polecenie prof. Giniewicza
  * data
	* `dogs.xlsx` -> informacje o psach
	* `drugs.csv` ->  informacje o lekach
	* `users_randomized` -> zrandomizowana baza danych osobowych
  * db_schema
	* `db_creation.sql` -> kod tworzacy bazę danych
	* `schema.vuerd.json` -> schemat bazy danych
  * final_code
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
	
* uzasadnienie, że baza jest w EKNF
  * BRAK PÓKI CO (?)
* opis, co było najtrudniejsze podczas realizacji projektu
	* uzasadnienie, że baza jest w EKNF
	* wyeliminowanie problemów technicznych związanych z generowaniem skryptowym i wypełnianiem bazy
