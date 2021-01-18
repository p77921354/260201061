numbers1 = set([2,3,4,20,5,5,15])
numbers2 = set([10,20,20,15,30,40])

difference1 = numbers1.difference(numbers2)
difference2 = numbers2.difference(numbers1)
for i in difference1:
  numbers1.remove(i)
intersection = numbers1
print(intersection)
union_of_set = numbers1.union(numbers2)
print(union_of_set)