N = int(input("How many numbers? "))
count_even = 0
for i in range(N):
  num = int(input("Enter an integer: "))
  if num % 2 == 0:
    count_even += 1
print((count_even / N) * 100 , "%")
