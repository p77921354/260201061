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
    