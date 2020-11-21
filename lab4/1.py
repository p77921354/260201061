num = int(input("num? "))

if num >= 10:
  second_digit = (num // 10) % 10
  last_digit = num % 10
  summation = second_digit + last_digit
  print("sum: ",summation)

elif num < 10:
  second_digit = num // 10
  last_digit = num % 10
  summation = second_digit + last_digit
  print("sum: ",summation)

else:
  print("choose another number")
