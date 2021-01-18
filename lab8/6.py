def check_valid_pass(password):
  level1 = 0
  level2 = 0
  level3 = 0
  level = 0
  if len(password) >= 8:
    for i in password:
      if i == " ":
        level = 0
        return level
      else:
        if i.isalnum():
          level1, level2 = 1,1
        elif not i.isalnum():
          level3 = 1
  level = level1 +level2+level3
  return level
print(check_valid_pass("ab de12345--"))
