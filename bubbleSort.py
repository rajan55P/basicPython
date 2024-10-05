my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    for j in range(n-i-1):
        if my_array[j] < my_array[j+1] :
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Bubble Sorted Array= ", my_array)


new_array = [7,3,9,12,11]
len = len(new_array)
for i in range(len):
    swapped_flag = False
    for j in range(0, len-i-1):
        if new_array[j] > new_array[j+1] :
            new_array[j], new_array[j+1] = new_array[j+1], new_array[j]
            swapped_flag = True
    if swapped_flag == False:
        break
print(" Bubble Sorted Array with Improvement = ", new_array)