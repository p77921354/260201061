def get_evens_recursive(l):
    if len(l) == 0:
        return []
    else:
        if l[0] % 2 == 0:
            return [l.pop(0)] + get_evens_recursive(l[1:])
        else:
            return get_evens_recursive(l[1:])

def get_evens(even_list):
    count = 0
    while count <= len(even_list):
        count += 1
    return count

print(get_evens(get_evens_recursive([1,2,3,4])))

# def get_evens_recursive(l, c=0):
#     if len(l) == 0:
#         return c
#     current = l.pop()           alternative solution
#     if current % 2 == 0:
#         c += 1
#     return get_evens_recursive(l, c)

# def get_evens(l):
#     return get_evens_recursive(l, c=0)

# print(get_evens([1,2,3,4,5,6,7,8]))
