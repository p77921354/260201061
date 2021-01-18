def merge(lst1, lst2, lst3):
# merge sorted lists lst1 and lst2 into lst3
  i1, i2, i3 = 0, 0, 0
  n1, n2 = len(lst1), len(lst2)
  count = 0
# Loop while both lst1 and lst2 have more items
  while i1 < n1 and i2 < n2:
    if lst1[i1] < lst2[i2]:
      lst3[i3] = lst1[i1]
      i1 = i1 + 1
      count += 1
  else:
    lst3[i3] = lst2[i2]
    i2 = i2 + 1
    i3 = i3 + 1
    count += 1
  while i1 < n1:
    lst3[i3] = lst1[i1]
    i1 = i1 + 1
    i3 = i3 + 1
    count += 1
  while i2 < n2:
    lst3[i3] = lst2[i2]
    i2 = i2 + 1
    i3 = i3 + 1
    count += 1
    