// * Two Sum
// * 挑戰用 O(n)

function twoSum(nums, target){
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    let anotherOne = target - nums[i];
    if (map[anotherOne] !== undefined) {
      return [map[anotherOne], i]
    };
    map[nums[i]] = i;
  }
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // * show [0, 2] because nums[0] + nums[2] is 9