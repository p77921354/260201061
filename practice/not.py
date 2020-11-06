vize1 = int(input("birinci vize: "))
vize2 = int(input("ikinci vize: "))
final = int(input("final notu: "))

toplam_not = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

if toplam_not >= 90:
  harf_notu = "AA"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 85 and toplam_not < 90:
  harf_notu = "BA"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 80 and toplam_not < 85:
  harf_notu = "BB"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 75 and toplam_not < 80:
  harf_notu = "CB"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 70 and toplam_not < 75:
  harf_notu = "CC"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 65 and toplam_not < 70:
  harf_notu = "DC"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 60 and toplam_not < 65:
  harf_notu = "DD"
  print("harf notunuz: ",harf_notu)
elif toplam_not >= 55 and toplam_not < 60:
  harf_notu = "FD"
  print("harf notunuz: ",harf_notu,"dersten kaldınız")
elif toplam_not >= 50 and toplam_not < 55:
  harf_notu = "FF"
  print("harf notunuz: ",harf_notu,"dersten kaldınız")
else:
  harf_notu = "FF"
  print("harf notunuz: ",harf_notu,"dersten kaldınız")

