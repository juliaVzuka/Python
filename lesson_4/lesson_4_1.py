from sys import argv
script_name, working_hours, rate_per_hour, bonus = argv


def salary_calc(hours, rate, bonus):
    return float(hours) * float(rate) + float(bonus)


print("Зарплата равна: ", salary_calc(working_hours, rate_per_hour, bonus))



