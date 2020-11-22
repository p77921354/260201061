# for i in (0, 1, 2, 3, 4, 5):
#   if i == 2 or i == 4:
#     continue
#   print(i)
#   print("is it really working")
  #continue is used for passing to the next iteration
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)-1):
  if i % 2 != 0:
    print(my_list[i])