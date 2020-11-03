print(""""

      january : 1
      february : 2
      march : 3
      april : 4
      may : 5
      july : 6
      june : 7
      august : 8
      september : 9
      october : 10
      november : 11
      december : 12
      
      """)

day = int(input("day: "))
month = int(input("which number? "))


if (month == 3 and  20 <= day <= 31) or (month == 4 and 1 <= day <= 30) or (month == 5 and 1 <= day <= 31) or (month == 6 and 1 <= day < 21): 
  print("spring")

elif (month == 6 and 31 >= day > 20) or (month == 7 and 30 >= day >= 1) or (month == 8 and  1 <= day <= 31) or (month == 9 and 1 <= day < 22):
  print("summer")

elif (month == 9 and 30 >= day >= 22) or (month == 10 and 31 >= day >= 1) or (month == 11 and 30 >= day >= 1) or (month == 12 and  1 <= day < 21):
  print("fall")

elif (month == 12 and 31 >= day >= 21) or (month == 1 and 31 >= day >= 1) or (month == 2 and 28 >= day >= 1) or (month == 3 and 20 > day >= 1):
  print("winter")











