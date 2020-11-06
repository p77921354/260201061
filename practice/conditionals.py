kilo = int(input("kilonuz? "))
boy = float(input("boyunuz? "))

bki = kilo / boy * boy #beden kitle endeksi

if bki < 18.5:
  print("çok zayıf")

elif bki >= 18.5 and bki < 25:
  print("normal")

elif bki >= 25 and bki < 30:
  print("fazla kilolu")

elif bki > 30:
  print("obez")
  