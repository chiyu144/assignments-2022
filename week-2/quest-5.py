# 計算連續出現 0 的最大長度

def maxZeros(nums):
  count = 0
  result = 0

  nums[len(nums) - 1] == 0 and nums.append(1)

  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
    else:
      result = count if count > result else result
      count = 0
  
  print(f"Max Zeros: {result}")

maxZeros([0, 1, 0, 0]) # 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 4
maxZeros([1, 1, 1, 1, 1]) # 0
maxZeros([0, 0, 0, 1, 1]) # 3

maxZeros([1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]) # 5