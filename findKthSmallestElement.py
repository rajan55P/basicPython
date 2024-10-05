import random
def solve(n, nums, k):
  k = k - 1
  return quickselect(nums, 0, n - 1, k)

def quickselect(nums, left, right, k):
  if left == right:  # If the list contains only one element
    return nums[left]
  pivot_index = partition(nums, left, right)
  
  if k == pivot_index:
    return nums[k]
  elif k < pivot_index:
    return quickselect(nums, left, pivot_index - 1, k)
  else:
    return quickselect(nums, pivot_index + 1, right, k)

def partition(nums, left, right):
  pivot_index = random.randint(left, right)  # Randomly select a pivot
  pivot_value = nums[pivot_index]
  nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
  store_index = left
  
  for i in range(left, right):
    if nums[i] < pivot_value:
      nums[i], nums[store_index] = nums[store_index], nums[i]
      store_index += 1

  # Move pivot to its final place
  nums[store_index], nums[right] = nums[right], nums[store_index]
  return store_index

n = 6
nums = [7, 10, 4, 3, 20, 15]
k = 3
result = solve(n, nums, k)
print(result)  # Output: 7