print("ax^2 + bx + c")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("{}x^2 + {}x + {}".format(a,b,c))

root_1 = 0
root_2 = 0


discrimant = b**2 - 4*a*c

if discrimant > 0:
  root_1 = (-1*b + (discrimant)**0.5) / (2*a)
  root_2 = (-1*b - (discrimant)**0.5) / (2*a)
  print("root 1:",root_1)
  print("root 2:",root_2)

elif discrimant == 0:
  root_1 = -1*b / (2*a)
  print("root",root_1)
  
elif discrimant < 0:
  print("there are not real roots")