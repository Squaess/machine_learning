
# Sprint plannig helper
W folderze znajdują się 3 pliki:
1.  `sprint-plannning-helper.py`
2.  `data_preparation.py`
3.  `data.csv`

### `sprint-planning-helper.py`

Jest to główny plik wykonujący całe obliczenia. Przyjmuje dwa CLI argumenty. Pierwszy to plik **csv** z danymi. Drugi to **velocity** naszego zespołu. Skrypt wypisuje na standardowe wyjście odpowiednią kolejność *ticket'ów*.

### `data_preparation.py`

Skrypt generuje plik **data.csv**, w którym znajduje się 10000 *ticket'ów*. Wartości *story points* są z zakresu [1,7),a punkty KSP z zakresu [1,20). Oba to typy całkowite.

### `data.txt`

Plik **csv** zawierający odpowiednie dane
