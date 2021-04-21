number = int(input("Сколько товаров вы хотите внести в структуру? "))
i = 0
key_1 = 'название'
key_2 = 'цена'
key_3 = 'количество'
key_4 = 'единицы'
dict_list = []
items_list = []
name_list = []
price_list = []
quantity_list = []
units_list = []
while i < number:
    i = i + 1
    name = input('Введите название товара: ')
    name_list.append(name)
    price = input('Введите цену товара:')
    price_list.append(price)
    quantity = input('Введите количество товара:')
    quantity_list.append(quantity)
    units = input('Введите единицы измерения товара:')
    units_list.append(units)
    items_list.append((i, dict(название=name, цена=price, количество=quantity, единицы=units)))
print('Товары.')
print(items_list)
analytics_dict = dict(название=name_list, цена=price_list, количество=quantity_list, единицы=units_list)
print('Аналитика.')
print(analytics_dict)



