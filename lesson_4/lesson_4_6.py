from itertools import count
from itertools import cycle


for el in count(3):
    if el > 10:
        break
    else:
        print(el)
my_list = [i for i in range(1, 4)]
i = 0
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1


