def make_ruler(n):
    miarka = '|' + '|'.join(['....'] * n) + '|\n'
    numeracja = ''.join([f"{i:<5}" for i in range(n + 1)])
    return miarka + numeracja

def make_grid(rows, cols):
    pozioma_krawedz = ('+---' * cols) + '+\n'
    wiersz = ('|   ' * cols) + '|\n'
    prostokat = (pozioma_krawedz + wiersz) * rows + pozioma_krawedz
    return prostokat


ruler = make_ruler(12)
print(ruler)


grid = make_grid(3, 5)
print(grid)
