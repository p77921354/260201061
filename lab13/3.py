def selectionSort(liste,iter_num):
   
    for step in range(len(liste)):
        min_idx = step
        iter_num += 1
        for i in range(step + 1, len(liste)):
            if liste[i] < liste[min_idx]:
                min_idx = i
        (liste[step], liste[min_idx]) = (liste[min_idx], liste[step])


numbers = [43, 342, 343, 2, 34]
selectionSort(numbers,iter_num = 0)
print(numbers)

def mergeSort(arr,iter_num):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            iter_num += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
