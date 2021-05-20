class MyError(Exception):

    def __init__(self, text):
        self.text = text


a = int(input(f"Ведите делимое: "))
b = int(input(f"Ведите делитель: "))
try:
    if b == 0:
        raise MyError("Делить на ноль нельзя!")
except MyError as err:
    print(err)
else:
    print(f"{a} разделить на {b} равно {round(a / b, 2)}.")



