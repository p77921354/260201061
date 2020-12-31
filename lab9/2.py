def get_reversed(l):
     if len(l) == 0: 
         return []
     return [l[-1]] + get_reversed(l[:-1])
print(get_reversed([1,2,3,4]))

# def get_reversed(l):
#     if len(l) == 0:           alternative solution
#         return []
#     return [l.pop()] + get_reversed(l)
# print(get_reversed([1,2,3,4]))