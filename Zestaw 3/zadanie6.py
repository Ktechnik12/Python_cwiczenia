def rysuj_prostokat(wysokosc, szerokosc):
    pozioma_krawedz = ('+---' * szerokosc) + '+\n'
    wiersz = ('|   ' * szerokosc) + '|\n'
    prostokat = (pozioma_krawedz + wiersz) * wysokosc + pozioma_krawedz
    return prostokat

print(rysuj_prostokat(3, 5))
