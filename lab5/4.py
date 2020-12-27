import time

user_pass = "asdfg"

password = input("enter your password, if you can't remember it type help: ")

trial = 0

while True:
  if password == user_pass:
    print("welcome")
    break
  
  elif password == "help":
    print(user_pass[0], "maybe this help you to remember your pass...")

  else:
    password = input("wrong, try again ")
    trial += 1
    if trial == 2:
      print("wait 10 seconds to try again")
      time.sleep(10)
      password = input("your pass")
      if password != user_pass:
        print("password try no longer accepted")
        break