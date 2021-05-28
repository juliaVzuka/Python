from abc import ABC, abstractmethod


class Dress(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def fabric(self):
        pass


class Coat(Dress):

    def __init__(self, size):
        super().__init__(size)

    @property
    def fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Dress):

    def __init__(self, size):
        super().__init__(size)

    @property
    def fabric(self):
        return 2 * self.size + 0.3


'''Словари, содержащие размеры и количества одежды, которую нужно сшить'''

coats_sizes_quantity = {165: 1, 170: 2, 175: 3, 180: 4}
suits_sizes_quantity = {46: 1, 48: 2, 50: 3, 52: 4}
coats_sum = 0
suits_sum = 0
for key in coats_sizes_quantity:
    coats_sum += Coat(key).fabric * coats_sizes_quantity[key]
for key in suits_sizes_quantity:
    suits_sum += Suit(key).fabric * suits_sizes_quantity[key]
print(f"Всего на одежду потратили {round(coats_sum + suits_sum, 2)} метров ткани.")
