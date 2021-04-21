out = '0'
rating = []
while out != 'n':
    i = 0
    upd_rating = rating.copy()
    num = int(input('Введите число, которое хотите разместить в рейтинге:'))
    if rating == []:
        upd_rating = [num]
    elif num in rating:
        upd_rating.insert(rating.index(num) + rating.count(num), num)
    else:
        while num <= rating[i]:
            i = i + 1
            if i == len(rating):
                break
        upd_rating.insert(i, num)
    print('Обновленный рейтинг: ', upd_rating)
    rating = upd_rating.copy()
    out = input('Для прекращения ввода новых чисел в рейтинг нажмите N. Чтобы продолжить, нажмите любую другую кнопку.')
