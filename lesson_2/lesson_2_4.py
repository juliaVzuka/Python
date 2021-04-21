my_string = input('Ведите строку, состоящую из нескольких слов, разделенных пробелом: ')
my_list = my_string.split()
for ind, el in enumerate(my_list, 1):
    print(ind, el[0:10])



