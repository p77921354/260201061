liste = [5,91,55,20,69,19,5,20,69,78,78]
for i in liste:
  if liste.count(i) > 1:
    liste.remove(i)
print(liste)