def binary_to_dec(number):
  d = 0
  rev = str(number)[::-1]
  for i in range(len(rev)):
    d += (2**i)*int(rev[i])
  return d

def dec_to_binary(number):
  a = ""
  while number > 0:
    a += str(number%2)
    number //= 2
  return a[::-1]

def main():
  binary_num = "1001"
  print(binary_to_dec(binary_num))
  dec_num = 18
  print(dec_to_binary(dec_num))
main() 