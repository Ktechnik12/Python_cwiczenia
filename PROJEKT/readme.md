# Dokumentacja programu: "Kółko i Krzyżyk"

## Wprowadzenie
Program jest implementacją gry "Kółko i Krzyżyk", w której użytkownik gra przeciwko komputerowi wyposażonemu w algorytm MiniMax. Gra jest zbudowana w Pythonie z wykorzystaniem biblioteki `tkinter` do stworzenia graficznego interfejsu użytkownika (GUI).

Gra polega na rywalizacji użytkownika z komputerem. Gracz wykonuje pierwszy ruch jako **"O"**, a następnie komputer jako **"X"**. Program analizuje możliwe ruchy i stosuje algorytm MiniMax, aby podejmować optymalne decyzje. Gra kończy się gdy program wykryje wygraną jednego z użytkowników lub zapełnienie się planszy.

### Algorytm MiniMax 

Algorytm MiniMax jest to rekurencyjny algorytm, który ocenia wszystkie możliwe ruchy w danej pozycji oraz wybiera ten który maksymalizuje jego szanse na zwycięstwo lub minimalizuje ryzyko przegranej.

**Zasada działania:**  
- Algorytm przegląda wszystkie możliwe ruchy w obecnym stanie gry.  
- Ocenia wartości ruchów na podstawie potencjalnych wyników.  
- Algorytm wybiera optymalny ruch.

---

## Opis interfejsu  

###  Interfejs użytkownika  

Graficzny interfejs użytkownika został zaimplementowany korzystając z biblioteki `tkinter`. Plansza gry składa się z siatki 3x3, w której umieszczone są przyciski reprezentujące pola.  

**Elementy interfejsu:**  
- **Siatka 3x3** – każde pole to przycisk, który zmienia swoją wartość po kliknięciu.  
- **Komunikaty końca gry** – używane do informowania użytkownika o wyniku.  
- **Automatyczny reset gry** po zamknieciu powiadomienia.  

---

## Struktura programu

### 1. **Moduły i funkcje**

#### **`SprawdzWygrana(tablica)`**
- **Opis**: sprawdza, czy któryś z graczy wygrał.
- **Parametry**:
  - `tablica`: dwuwymiarowa lista 3x3 reprezentująca planszę gry.
- **Zwracana wartość**: 
  - Symbol gracza (`"X"` lub `"O"`), jeśli jest wygrana.
  - `None`, jeśli nikt nie wygrał.

#### **`CzyPelna(tablica)`**
- **Opis**: sprawdza, czy plansza jest pełna (wszystkie pola są zajęte).
- **Parametry**:
  - `tablica`: dwuwymiarowa lista 3x3 reprezentująca planszę gry.
- **Zwracana wartość**: 
  - `True`, jeśli plansza jest pełna.
  - `False`, jeśli są wolne pola.

#### **`MiniMax(tablica, glebokosc, gracz)`**
- **Opis**: Implementacja algorytmu MiniMax do optymalnego wyznaczania ruchu dla komputera.
- **Parametry**:
  - `tablica`: Dwuwymiarowa lista 3x3 reprezentująca planszę gry.
  - `glebokosc`: Aktualna głębokość rekursji (ilość ruchów do przewidzenia w przód).
  - `gracz`: Boolean. `True`, jeśli ruch należy do komputera (`"X"`), `False`, jeśli do użytkownika (`"O"`).
- **Zwracana wartość**: Liczba całkowita reprezentująca wartość ruchu:
  - Wartość dodatnia: Korzystne dla komputera.
  - Wartość ujemna: Korzystne dla użytkownika.
  - `0`: Ruch neutralny (np. remis).

#### **`NajlepszyRuch(tablica)`**
- **Opis**: Wyznacza najlepszy ruch dla komputera na podstawie algorytmu MiniMax.
- **Parametry**:
  - `tablica`: Dwuwymiarowa lista 3x3 reprezentująca planszę gry.
- **Zwracana wartość**: 
  - Krotka `(i, j)` z indeksem najlepszego pola na planszy.

---

### 2. **Klasa: `KolkoIKrzyzyk`**
Kluczowa klasa programu, która implementuje logikę gry i obsługuje interfejs użytkownika.

#### **Konstruktor `__init__(self, root)`**
- **Opis**: Inicjalizuje okno aplikacji, planszę gry i przyciski GUI.
- **Parametry**:
  - `root`: Główne okno aplikacji (obiekt `tk.Tk`).

#### **Metody**:
1. **`StworzPlansze(self)`**
   - Tworzy graficzną planszę gry 3x3 jako zestaw przycisków.

2. **`RuchGracza(self, i, j)`**
   - Obsługuje ruch użytkownika:
     - Oznacza pole jako `"O"`.
     - Sprawdza, czy gra się zakończyła.
     - Uruchamia ruch komputera, jeśli gra trwa dalej.

3. **`RuchKomputera(self)`**
   - Wywołuje funkcję `NajlepszyRuch`, aby komputer wykonał optymalny ruch.
   - Aktualizuje planszę i GUI.

4. **`CzyKonieGry(self)`**
   - Sprawdza, czy gra zakończyła się wygraną, remisem lub powinna być kontynuowana.
   - Wyświetla odpowiedni komunikat w przypadku zakończenia gry i resetuje planszę.

5. **`ResetGry(self)`**
   - Resetuje stan gry do początkowego (czysta plansza).

---

### 3. **Główna funkcja programu**
```python
if __name__ == "__main__":
    root = tk.Tk()
    app = KolkoIKrzyzyk(root)
    root.mainloop()
```

---

## 4. Podsumowanie i wyniki testów  

### 4.1 Podsumowanie  

Program umożliwia rozgrywkę przeciwko komputerowi z wykorzystaniem algorytmu MiniMax, który sprawia, bardzo cieżko jest graczowi pokonać komputer. 

### 4.2 Wyniki testów  

Testy pokazały, że:  
- **Komputer nigdy nie przegrywa** – albo wygrywa, albo kończy grę remisem.  
- **Komputer potrafi rozpoznać najlepszy ruch** i natychmiast go wykonać.  
- **Interfejs jest intuicyjny i prosty w obsłudze.**  
