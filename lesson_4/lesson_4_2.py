from random import randint


start_list = []
for i in range(0, 10):
    start_list.append(randint(0, 500))
print(start_list)
new_list = [start_list[i] for i in range(1, len(start_list)-1) if start_list[i] > start_list[i-1]]
print(new_list)
