numbers = [13, 1, 27, 33, 14, 26, 72, 48, 16, 15, 6, 64, 79, 3, 39,73, 93, 68, 41, 87, 28, 97,
67, 20, 29, 9, 12, 94, 94, 96, 88, 69, 49, 78, 91, 2, 47, 87, 29, 79, 18, 55, 88, 67,
37, 26, 51, 84, 85, 7, 84, 96, 91, 16, 28, 45, 98, 11, 92, 43, 59, 31, 58, 39, 76, 45,
26, 57, 52, 40, 82, 54, 94, 96, 4, 76, 6, 2, 44, 79, 56, 19, 71, 62, 10, 79, 86, 98,
5, 13, 5, 37, 17, 74, 75, 43, 46, 51, 94, 38, 30, 13, 5, 94, 4, 22, 6, 44, 40, 53, 69,
88, 41, 2, 54, 50, 21, 68, 81, 69]

def selectionSort(liste,iter_num):
    for step in range(len(liste)):
        min_idx = step
        for i in range(step + 1, len(liste)):
            iter_num += 1
            if liste[i] < liste[min_idx]:
                min_idx = i
        iter_num += 1
        (liste[step], liste[min_idx]) = (liste[min_idx], liste[step])
              
    return iter_num


a = selectionSort(numbers,iter_num= 0)
print("number of steps with selection sort:",a) # total number of iterations with this list is 15, with any list, it is number of elements(number of iterations with main for loop) + ((n-1)*(n-2))/2, n is number of elements in list

def merge_sort(num_list,count_iter):
    size = len(num_list)
    if size > 1:
        middle = size // 2
        left_sub_list = num_list[:middle]
        right_sub_list = num_list[middle:]
 
        merge_sort(left_sub_list,count_iter)  # separates to sublists until num_list has 
        merge_sort(left_sub_list,count_iter)   #  two elements                                        
        p = 0 # index of left_sub_list
        q = 0 # index of right_sub_list
        r = 0 # index of num_list
 
        left_size = len(left_sub_list)
        right_size = len(right_sub_list)
        while p < left_size and q < right_size: # while indices are less than two sublists
            if left_sub_list[p] < right_sub_list[q]:  # if left lists element is less than right list element 
              num_list[r] = left_sub_list[p] # update num_lists with corresponding element
              p += 1                          # increment p to look in the elements in left list and compare them to right lists unchanged elemet
            else:
                num_list[r] = right_sub_list[q] # same thing with left_list but now it is done on right list
                q += 1
            count_iter += 1         # increment number of iterations with every step
            r += 1
        
        return count_iter  # number of iterations were incremented with every while loop
 
num=merge_sort(numbers,count_iter = 0)
print(numbers)
print("number of steps:",num)

# final result: merge sort is more efficient compared to selection sort