import tkinter as tk
import random

def rzut_kostka():
    wynik = random.randint(1, 6)
    wynik_label.config(text=f"Wynik rzutu: {wynik}")

root = tk.Tk()
root.title("Symulacja rzutu kostką")

wynik_label = tk.Label(root, text="Kliknij przycisk, aby rzucić kostką!", font=("Arial", 14))
wynik_label.pack(pady=20)

rzut_button = tk.Button(root, text="Rzuć kostką", command=rzut_kostka, font=("Arial", 12))
rzut_button.pack(pady=10)

root.mainloop()
