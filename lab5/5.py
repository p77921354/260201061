nterms = int(input("How many terms? "))
n1, n2 = 1, 1
count = 0
while count < nterms:
  print(n1,end = " ")
  nth = n1 + n2
  n1 = n2
  n2 = nth
  count += 1

# N = int(input("Number of terms: "))
# T1,T2 = 1,1                         alternative solution
# print("%d %d"%(T1,T2),end = "")
# for i in range(1,N-1):
#   T3 = T1 + T2
#   print(" %d"%T3,end = "")
#   T1 = T2
#   T2 = T3   
