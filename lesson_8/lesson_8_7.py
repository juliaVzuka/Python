class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        sum_a = self.a + other.a
        sum_b = self.b + other.b
        return ComplexNumber(sum_a, sum_b)

    def __mul__(self, other):
        mult_a = self.a * other.a - self.b * other.b
        mult_b = self.a * other.b + other.a * self.b
        return ComplexNumber(mult_a, mult_b)

    def __str__(self):
        if self.b >= 0:
            return f"{self.a}+{self.b}i"
        else:
            return f"{self.a}{self.b}i"


a1 = -4
b1 = 37
a2 = 11
b2 = -6
cn1 = ComplexNumber(a1, b1)
cn2 = ComplexNumber(a2, b2)
print(f"Первое число: {cn1}")
print(f"Второе число: {cn2}")
print(f"Сумма чисел: {cn1 + cn2}")
print(f"Произведение чисел: {cn1 * cn2}")

