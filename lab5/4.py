x = input("number: ")
y = input("number: ")

i = 1
matched_digit = 0
dig_1 = len(x)
dig_2 = len(y)

while dig_1 >= i and dig_2 >= i:
  x = int(x)
  y = int(y)
  if (x % (dig_1 * 10)) == (y % (dig_2 * 10)):
    matched_digit += 1
  dig_1 -= 1
  dig_2 -= 1
print(matched_digit)