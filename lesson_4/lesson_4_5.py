from functools import reduce


def product(el, next_el):
    return el * next_el


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(product, my_list))



