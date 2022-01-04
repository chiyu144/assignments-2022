# Two Sum

def twoSum(nums, target):
  map = {}

  for i in range(len(nums)):
    anotherOne = target - nums[i]
    if anotherOne in map:
      return [map[anotherOne], i]
    map[nums[i]] = i

result = twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
