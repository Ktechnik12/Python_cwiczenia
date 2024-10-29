L = [3, 5, 4] ; L = L.sort() – L.sort() sortuje listę w miejscu i zwraca None, więc L będzie przypisane do None, a nie posortowanej listy.

x, y = 1, 2, 3 – nieprawidłowe przypisanie, ponieważ liczba wartości po lewej stronie (2) nie odpowiada liczbie wartości po prawej stronie (3).

X = 1, 2, 3 ; X[1] = 4 – X jest krotką, która jest niemodyfikowalna, więc przypisanie X[1] = 4 spowoduje błąd.

X = [1, 2, 3] ; X[3] = 4 – lista X ma indeksy 0, 1, 2, więc próba przypisania X[3] = 4 spowoduje błąd indeksu.

X = "abc" ; X.append("d") – str jest niemodyfikowalnym typem i nie ma metody append.

L = list(map(pow, range(8))) – funkcja pow wymaga dwóch argumentów