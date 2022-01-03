# 使用迴圈計算最小值到最大值之間，所有整數的總和。

import math

# 跟 JS 不同，range 不接受浮點數，所以用 math 處理
# max 也要處理因為不像 JS 那樣直接寫條件 (一度忘了 max)

def calculate(min, max):
  result = 0
  for i in range(math.ceil(min), math.floor(max) + 1):
    result += i
  print(result)

calculate(1, 3) # 6
calculate(4, 8) # 30
calculate(-1, 1) # 0
calculate(1.6, 10.7) # 54
calculate(0.1, 1) # 1
calculate(0, 100) # 5050