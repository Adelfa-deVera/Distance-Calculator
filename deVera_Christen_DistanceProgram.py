import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

distance = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))

print(f"The distance between the two points is: {distance:.2f}")