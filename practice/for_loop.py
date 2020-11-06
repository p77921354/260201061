numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = list()
odd_numbers = list()
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
  else:
    odd_numbers.append(number)
print("number of even numbers: ", len(even_numbers))
print("number of odd numbers: ", len(odd_numbers))