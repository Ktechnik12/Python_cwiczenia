import random

class RandomQueue:
    def __init__(self):
        self._data = []

    # def __init__(self, size=10): z ograniczeniem rozmiaru
    #     self._data = []
    #     self._max_size = size

    def insert(self, item):
        """Wstawia element do kolejki w czasie O(1)."""
        self._data.append(item)

        # Dla wersji z ograniczeniem rozmiaru:
        # if len(self._data) >= self._max_size:
        #     raise OverflowError("Queue is full")
        # self._data.append(item)

    def remove(self):
        """Zwraca losowy element z kolejki i usuwa go w czasie O(1)."""
        if self.is_empty():
            raise IndexError("Remove from empty queue")

        idx = random.randint(0, len(self._data) - 1)
        self._data[idx], self._data[-1] = self._data[-1], self._data[idx]

        return self._data.pop()

    def is_empty(self):
        """Sprawdza, czy kolejka jest pusta."""
        return len(self._data) == 0

    def is_full(self):
        """Sprawdza, czy kolejka jest pełna (wersja z ograniczeniem rozmiaru)."""
        # Dla wersji bez ograniczenia rozmiaru zawsze zwraca False
        return False  # len(self._data) >= self._max_size w wersji z ograniczeniem

    def clear(self):
        """Czyści kolejkę."""
        self._data = []
