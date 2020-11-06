şekil = input("üçgen için 1 yazınız, dörtgen için 2 yazınız ")

if şekil == "1":
  üçgen1 = int(input("kenar girin: "))
  üçgen2 = int(input("kenar girin: "))
  üçgen3 = int(input("kenar girin: "))

  if not((abs(üçgen1 - üçgen2) < üçgen3 < üçgen1 + üçgen2) or (abs(üçgen1 - üçgen3) < üçgen2 < üçgen1 + üçgen3) or (abs(üçgen2 - üçgen3) < üçgen1 < üçgen2 + üçgen3)):
    print("üçgen belirtmiyor")
  else:
  
    if üçgen1 == üçgen2 and üçgen2 == üçgen3:
      print("eşkenar üçgen")

    elif (üçgen1 == üçgen2 and üçgen2 != üçgen3) or (üçgen1 == üçgen3 and üçgen3 != üçgen2) or (üçgen2 == üçgen3 and üçgen3 != üçgen1):
      print("ikizkenar üçgen")
  
    elif üçgen1 != üçgen2 and üçgen2 != üçgen3 and üçgen1 != üçgen3:
      print("sıradan üçgen")
  
  
elif şekil == "2":
  a = int(input("kenar girin: "))
  b = int(input("kenar girin: "))
  c = int(input("kenar girin: "))
  d = int(input("kenar girin: "))

  if (a == b) and (b == c) and (c == d):
    print("kare")

  elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
    print("dikdörtgen")
  
  elif a != b and c != d and a != c:
    print("dörtgen")

