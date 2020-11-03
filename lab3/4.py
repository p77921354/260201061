age = int(input("what's your age? "))
discount = int() 
price = 3

if (age < 6) or (age > 60):
  discount = 1 #100%
  price = price - price*discount

elif (age >= 6) or (age <= 18):
  discount = 0.5 #50%
  price = price - price*discount

else:
  discount = 0 # 0%
  price = price - price*discount

print(price,"is the price")