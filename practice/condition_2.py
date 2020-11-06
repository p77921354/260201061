x = int(input("enter num: "))
y = int(input("enter num: "))
z = int(input("enter num: "))

minimum = x

if x < y and x < z:
  minimum = x

if y < x and y < z:
  minimum = y

if z < x and z < y:
  minimum = z

print(minimum)
 
