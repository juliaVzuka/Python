time = int(input("Enter time in seconds: "))
hours = time // 3600
time = time - hours*3600
minutes = time // 60
seconds = time - minutes*60
print("hh : mm : ss  ", hours, ":", minutes, ":", seconds)