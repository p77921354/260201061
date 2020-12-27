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

# int1 = input("Enter number 1: ")
# int2 = input("Enter number 2: ") alternative
# count_match = 0                   solution 1
# min_digit = 0
# if len(int1) < len(int2):
#   min_digit = len(int1)
# elif len(int2) < len(int1):
#   min_digit = len(int2)
# else:
#   min_digit = len(int1)
# int1 = int(int1)
# int2 = int(int2)

# for i in range(min_digit):
#   digit_of_1 = int1 % 10
#   digit_of_2 = int2 % 10
#   if digit_of_1 == digit_of_2:
#     count_match += 1
#   int1 = int1 // 10
#   int2 = int2 // 10
# print(count_match)

# min_len = min(len(int1),len(int2))
# count_match = 0                     alternative
# int1,int2 = int1[::-1],int2[::-1]   solution 2 
# for i in range(min_len):            
#   if int1[i] == int2[i]:                
#     count_match += 1                
# print(count_match)


