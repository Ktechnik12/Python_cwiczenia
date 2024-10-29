while True:
    user_input = input("Podaj liczbę lub wpisz 'stop' aby zakończyć: ")
    if user_input.lower() == 'stop':
        break
    try:
        x = float(user_input)
        print(f"Liczba: {x}, Trzecia potęga: {x ** 3}")
    except ValueError:
        print("Błąd: Proszę podać prawidłową liczbę.")
