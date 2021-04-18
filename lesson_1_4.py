s = input("Enter any positive integer number: ")
i = 0
max = int(s[0])
while i < len(s):
    n = int(s[i])
    if n >= max:
         max = n
    i = i + 1
print('The largest digit in this number is: ', max)
