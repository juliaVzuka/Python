a = float(input("Enter the first day's distance: "))
b = float(input("Enter the desired distance a day: "))
i = 1
d = a
while d < b:
    d = d * 1.1
    i = i + 1
    print(round(d,2))
print("The runner will make at least", b,"km a day on his", i, "day of training.")

