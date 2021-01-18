def is_prime(num):
  count = 0
  for i in range(2,num):
    if num % i == 0:
      return "not prime"
    else:
      count += 1
  if count >= 1:
    return "is prime"
print(is_prime(11))

def print_primes_between(a,b):
  prime_list = list()
  for i in range(a,b):
    b = is_prime(i)
    if b == "is prime":
      prime_list.append(i)
  print(prime_list)

print_primes_between(2,13)