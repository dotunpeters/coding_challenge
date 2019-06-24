from datetime import datetime

dt = datetime.strptime("12-July-1990", "%d-%B-%Y")
x = dt.strftime("%A")
print(x)

dt2 = datetime.strptime("12-July-2019", "%d-%B-%Y")
y = dt2.strftime("%A")
print(y)

print(x < y)