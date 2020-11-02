number = int(input("enter a number: "))
num_abs = 0
if number > 0:
  num_abs = number
else:
  num_abs = -1*number
  print(number,"is negative, absolute value of it is:", num_abs)