books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
dict_ = {}
for book in books:
  count_unique = 0
  char_dict = {}
  for book_char in book:
    if book_char not in char_dict:
      char_dict[book_char] = 1
      count_unique += 1
    else:
      char_dict[book_char] += 1
  dict_[book] = (len(book),count_unique)
print(dict_)