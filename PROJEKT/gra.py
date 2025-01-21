import math
import tkinter as tk
from tkinter import messagebox

def SprawdzWygrana(tablica):
    for i in range(3):
        if tablica[i][0] == tablica[i][1] == tablica[i][2] and tablica[i][0] != " ":
            return tablica[i][0]
        if tablica[0][i] == tablica[1][i] == tablica[2][i] and tablica[0][i] != " ":
            return tablica[0][i]

    if tablica[0][0] == tablica[1][1] == tablica[2][2] and tablica[0][0] != " ":
        return tablica[0][0]
    if tablica[0][2] == tablica[1][1] == tablica[2][0] and tablica[0][2] != " ":
        return tablica[0][2]

    return None

def CzyPelna(tablica):
    return all(i != " " for row in tablica for i in row)

def MiniMax(tablica, glebokosc, gracz):
    wygrany = SprawdzWygrana(tablica)
    
    if wygrany == "X":
        return 10 - glebokosc
    if wygrany == "O":
        return -10 + glebokosc
    if CzyPelna(tablica):
        return 0

    if gracz:
        najlepszyWynik = -math.inf
        for i in range(3):
            for j in range(3):
                if tablica[i][j] == " ":
                    tablica[i][j] = "X"
                    wynik = MiniMax(tablica, glebokosc + 1, False)
                    tablica[i][j] = " "
                    najlepszyWynik = max(najlepszyWynik, wynik)
        return najlepszyWynik
    else:
        najlepszyWynik = math.inf
        for i in range(3):
            for j in range(3):
                if tablica[i][j] == " ":
                    tablica[i][j] = "O"
                    wynik = MiniMax(tablica, glebokosc + 1, True)
                    tablica[i][j] = " "
                    najlepszyWynik = min(najlepszyWynik, wynik)
        return najlepszyWynik


def NajlepszyRuch(tablica):
    NajlepszyWynik = -math.inf
    ruch = None
    
    for i in range(3):
        for j in range(3):
            if tablica[i][j] == " ":
                tablica[i][j] = "X"
                wynik = MiniMax(tablica, 0, False)
                tablica[i][j] = " "
                print(wynik,"i", i, "j", j)
                if wynik > NajlepszyWynik:
                    NajlepszyWynik = wynik
                    ruch = (i, j)
                    
    return ruch

class KolkoIKrzyzyk:
    def __init__(self, root):
        self.root = root
        self.root.title("Kółko i krzyżyk")
        self.tablica = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.StworzPlansze()

    def StworzPlansze(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,command=lambda i=i, j=j: self.RuchGracza(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def RuchGracza(self, i, j):
        if self.tablica[i][j] == " ":
            self.tablica[i][j] = "O"
            self.buttons[i][j].config(text="O")
            
            if self.CzyKonieGry():
                return
            
            self.RuchKomputera()

    def RuchKomputera(self):
        move = NajlepszyRuch(self.tablica)
        
        if move:
            self.tablica[move[0]][move[1]] = "X"
            self.buttons[move[0]][move[1]].config(text="X")
            
        self.CzyKonieGry()

    def CzyKonieGry(self):
        winner = SprawdzWygrana(self.tablica)
        
        if winner:
            if winner == "X":
                messagebox.showinfo("Koniec Gry", "Komputer wygrał!")
            else:
                messagebox.showinfo("Koniec Gry", "Użytkownik wygrał!")
            self.ResetGry()
            return True
        
        if CzyPelna(self.tablica):
            messagebox.showinfo("Koniec Gry", "Remis!")
            self.ResetGry()
            return True
        
        return False

    def ResetGry(self):
        self.tablica = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    app = KolkoIKrzyzyk(root)
    root.mainloop()
