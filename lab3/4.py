age = int(input("what's your age? "))
price = 0

if not(age > 18 and  age <= 60):
  if age < 6 and age > 60:
    price = 0
  elif age >= 6 and age <= 18:
    price = 1.5
else:
  price = 3
print(price)