password = input("enter your password: ")
count_dict = {"count_upper":0, "count_lower":0,"count_number":0}
count = 0
is_valid = True
if len(password) >= 8:
  for i in password:
    if "A" <= i <= "Z":
      count_dict["count_upper"] += 1
    elif "a" <= i <= "z":
      count_dict["count_lower"] += 1
    elif "0" <= i <= "9":
      count_dict["count_number"] += 1
  for i in count_dict:
    if count_dict[i] >= 1:
      count += 1
  if count == 3:
    is_valid = True
  else:
    is_valid = False
else:
  is_valid = False
  
print(is_valid)