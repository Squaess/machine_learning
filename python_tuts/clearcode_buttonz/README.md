# Buttonz counter
W folderze znajdują się 4 pliki:
1. `buttonz-counter.py`
2. `test_buttonz-counter.py`
2. `websites`
3. `out.csv`

### `buttonz-counter.py`
Jest to główny plik wykonujący całe obliczenia. Przyjmuje dwa CLI argumenty. Pierwszy to plik ze stronami, które ma on analizować. Drugi to plik wyjściowy, w którym mają być umieszczone dane wynikowe. Skrypt zapisuje do drugiego pliku dane w formacie **csv**.
Jeśli skrypt będzie miał problem z pobraniem pewnej strony, to poinformuje o tym, lecz nie zatrzyma to jego wykonywania. Zamiast ilości przycisków, dla problematycznej strony, w pliku pojawi się słowo `Error`.
### `test_buttonz-counter.py`
Jest to plik testujący klasę parser, która znajduje się w pliku `buttonz-counter.py`
Przykład użycia testu:
`python test_buttonz-counter.py`
### `websites`
Plik zawierający strony **www** rozdzielone znakiem `\n`.
### `out.csv`
Plik z danymi wynikowymi pochodzącymi ze skryptu `byttonz-counter.py`
