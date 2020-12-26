while True:
  path = input("Enter a file path:")

  if path == "story1.txt":
    file = open("story1.txt", "r")
    user_letter = input("Enter a list of letters:")
    while user_letter.isalpha() == False:
      user_letter = input("Enter a list of letters:")
  
    user_letter = user_letter.islower()
    letters = list()
    for i in user_letter:
      letters.append(i)

    lines = file.readlines()

    for line in lines:
      line = line.replace('""',"")
      line = line.replace("'","")
      words = line.split(" ")
  
    outs = list()
    for word in words:
      for letter in letters:
        if letter in word:
          max_len = 0
          if len(word) > max_len:
            max_len = len(word)
          success_out = f"{letter}:{word}"
          outs.append(success_out)
        elif letter not in word:
          fail_out = f"{letter}:Letter not found!"
          outs.append(fail_out)




  elif path == "story2.txt":
    file = open("story2.txt", "r")
    user_letter = input("Enter a list of letters:")
    while user_letter.isalpha() == False:
      user_letter = input("Enter a list of letters:")
  
    user_letter = user_letter.islower()
    letters = list()
    for i in user_letter:
      letters.append(i)

    lines = file.readlines()

    for line in lines:
      line = line.replace('""',"")
      line = line.replace("'","")
      words = line.split(" ")
  
    outs = list() 

    for word in words:
      for letter in letters:
        if letter in word:
          max_len = 0
          if len(word) > max_len:
            max_len = len(word)
          success_out = f"{letter}:{word}"
        elif letter not in word:
          fail_out = f"{letter}:Letter not found!"

  outs.sort()

  print(outs)
      
user_input = input("Enter *path* for a new path, *list* for a new list of letters and *quit* to quit:")
if user_input == "quit:":
  print("Goodbye!")
  break
elif user_input == "list":
   user_letter = input("Enter a list of letters:")
  while user_letter.isalpha() == False:
    user_letter = input("Enter a list of letters:")
  
    user_letter = user_letter.islower()
    letters = list()
    for i in user_letter:
      letters.append(i)

    lines = file.readlines()

    for line in lines:
      line = line.replace('""',"")
      line = line.replace("'","")
      words = line.split(" ")
  
    outs = list()
    for word in words:
      for letter in letters:
        if letter in word:
          max_len = 0
          if len(word) > max_len:
            max_len = len(word)
          success_out = f"{letter}:{word}"
          outs.append(success_out)
        elif letter not in word:
          fail_out = f"{letter}:Letter not found!"
          outs.append(fail_out)
  outs.sort()

  print(outs)
      

elif user_input == "path":
  pass