new_array = [7,3,9,12,11]

def selectionSort(new_array):
    l = len(new_array)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if new_array[min_index] > new_array[j]:
                min_index = j
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]