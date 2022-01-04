# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 不可以使用排序相關的內建函式。

from math import inf

def maxProduct(nums):
  if len(nums) < 2: return

  max = -inf

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      temp = nums[i] * nums[j]
      max = temp if temp > max else max
  
  print(max)


maxProduct([5, 20, 2, 6]) # 120
maxProduct([10, -20, 0, 3]) # 30
maxProduct([-1, 2]) # -2
maxProduct([-1, 0, 2]) # 0
maxProduct([-1, -2, 0]) # 2