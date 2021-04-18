inc = float(input("Enter your company's incom: "))
exp = float(input("Enter your company's expences: "))
if inc < exp:
    print("Your company is suffering losses.")
else:
    print("Your company's profitability is: ", round(((inc - exp) / inc), 3))
    num = int(input("Enter the number of your company's employees: "))
    print("Your company's profit per employee is: ", round(((inc - exp) / num), 3))

