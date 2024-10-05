def solve(n, nums, k):
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums[k - 1])

#  pass n and nums and k =3
n = 6
nums = [7, 10, 4, 3, 20, 15]
k = 3
solve(n, nums, k)