// * Two Sum

function twoSum(nums, target){
  // * O(n)
  // * Hash Map 法
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    // * target - 目前迴圈跑到的數字 → 可以知道另一個數字會是幾，但不知道它是否存在於 array，存在的話也不知道 index 多少
    let anotherOne = target - nums[i];  

    // * 檢查記錄了每個數字的 index 的 map 物件，如果另一個數字有被記錄在裡面，那就是它了
    // * (第 1 圈 map[anotherOne] 一定會 undefined 因為 map 物件裡還沒有東西，所以第 2 圈開始才會進到這個 if)
    if (map[anotherOne] !== undefined) {
      return [map[anotherOne], i]
    };

    // * 每跑一圈，就用 key-value 紀錄每個數字的 index (方便做檢查)
    map[nums[i]] = i;
  }
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // * show [0, 2] because nums[0] + nums[2] is 9