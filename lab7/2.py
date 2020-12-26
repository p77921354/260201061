books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {}
letter_num = 0
for book_name in books:
  book_name.replace(" ","")
  letter_num = 0
  for letter in book_name:
    letter_num += len(letter)
  book_dict[book_name] = letter_num
    if book_name.count(letter) > 1:
      
