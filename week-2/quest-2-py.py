# 正確計算出員工的平均薪資，請考慮員工數量會變動的情況

from operator import itemgetter
from functools import reduce

def avg(data):
  # PY 解構賦值研究:
  # attrgetter 是用 Key 取值，但不能對 Dict Object 取，
  # itemgetter 是用 index，所以要照順序寫，JS 的話順序可以亂擺
  count, employees = itemgetter('count', 'employees')(data)

  # 使用 PY 的 reduce，設定 lambda 函式告訴 PY 說是要加 employees 裡面每人的薪水
  # 然後設定初始值為 0 (同樣都數字才可相加)，再除以人數
  avg = reduce(lambda x, y: x + y['salary'], employees, 0) / count

  print(avg)

avg({
  "count": 3,
  "employees":
    [{ "name": "John", "salary": 30000 },
    { "name": "Bob", "salary": 60000 },
    { "name": "Jenny", "salary": 50000 }]
}) # 46666.666666666664