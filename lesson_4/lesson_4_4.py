user_list = [12, 12, 45, 56, 7, 7, 7, 0, 45, 21, 17, 0, 8, 1, 2, 3, 4, 5, 6, 7, 8]
print(user_list)
print([user_list[i] for i in range(0, len(user_list)) if user_list.count(user_list[i]) == 1])
