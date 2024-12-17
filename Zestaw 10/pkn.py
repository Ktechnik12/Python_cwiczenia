import tkinter as tk
import random

def wybor_komputera():
    return random.choice(["Papier", "Kamień", "Nożyce"])

def sprawdz_wynik(wybor_uzytkownika):
    komputer = wybor_komputera()
    
    etykieta_wybor.config(text=f"Twój wybór: {wybor_uzytkownika}\nWybór komputera: {komputer}")
    
    if wybor_uzytkownika == komputer:
        wynik = "Remis!"
    elif (wybor_uzytkownika == "Papier" and komputer == "Kamień") or \
         (wybor_uzytkownika == "Kamień" and komputer == "Nożyce") or \
         (wybor_uzytkownika == "Nożyce" and komputer == "Papier"):
        wynik = "Wygrałeś!"
    else:
        wynik = "Przegrałeś!"
    
    etykieta_wynik.config(text=f"Wynik gry: {wynik}")

root = tk.Tk()
root.title("Papier-Kamień-Nożyce")
root.geometry("400x300")

etykieta_naglowek = tk.Label(root, text="Wybierz Papier, Kamień lub Nożyce", font=("Arial", 14))
etykieta_naglowek.pack(pady=10)

etykieta_wybor = tk.Label(root, text="Twój wybór: ---\nWybór komputera: ---", font=("Arial", 12))
etykieta_wybor.pack(pady=10)

etykieta_wynik = tk.Label(root, text="Wynik gry: ---", font=("Arial", 14, "bold"))
etykieta_wynik.pack(pady=10)

przycisk_papier = tk.Button(root, text="Papier", font=("Arial", 12), width=10, command=lambda: sprawdz_wynik("Papier"))
przycisk_papier.pack(pady=5)

przycisk_kamien = tk.Button(root, text="Kamień", font=("Arial", 12), width=10, command=lambda: sprawdz_wynik("Kamień"))
przycisk_kamien.pack(pady=5)

przycisk_nozyce = tk.Button(root, text="Nożyce", font=("Arial", 12), width=10, command=lambda: sprawdz_wynik("Nożyce"))
przycisk_nozyce.pack(pady=5)

root.mainloop()
