x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))

#if (x < z) and (x < y):
#   print(x,"is the minimum number")
# elif (y < z) and (y < x):
#   print(y,"is the minimum number")
# else:
#   print(z,"is the minimum number")

min_num = x

if y < min_num:
  min_num = y
if z < min_num:
  min_num = z

print(min_num)
