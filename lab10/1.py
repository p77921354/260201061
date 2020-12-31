def f(n, mult=0):
     if n == 1:
         return 3
     mult += 3
     return mult + f(n-1)  # f(5) = 3 + f(4) = 3+3+f(3)) = 3+3+3+f(2) = 3+3+3+3(f(1)) = 3+3+3+3+3
print(f(5))               #                                                   base case