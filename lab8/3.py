import random
random.seed(12)

def get_rand_list(b,e,N):
  r_list = random.sample(range(b,e),N)
  return r_list

def get_overlap(L1,L2):
  L3 = []
  for num in L1:
    if num in L2:
      L3.append(num)
  return L3

def main():
  list1 = get_rand_list(0,10,5)
  list2 = get_rand_list(0,10,5)
  print(list1) 
  print(list2)
  list3 = get_overlap(list1,list2)
  print(list3)

main() 
