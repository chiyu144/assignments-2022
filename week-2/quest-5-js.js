// * Binary Gap

function maxZeros (nums) {
  // * O(n)
  let count = 0;
  let result = 0;

  // * 如果 0 結尾的 nums 就補個 1 在最後 (方便計算 0 的數量，以 1 跟 1 之間為標記)
  nums[nums.length - 1] === 0 && nums.push(1);

  for(let i = 0; i < nums.length; i++) {
    // * 如果遇到 0，就 +1 計數
    if (nums[i] === 0) {
      count += 1;
    } else {
      // * 遇到 1，就開始比大小
      result = count > result ? count : result
      // * 因為遇到 1 了，計數器要重新計，也已經比完大小了所以可以安心歸 0
      count = 0;
    }
  };

  console.log(`Max Zeros: ${result}`);
}

maxZeros([0, 1, 0, 0]); // * 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // * 4
maxZeros([1, 1, 1, 1, 1]); // * 0
maxZeros([0, 0, 0, 1, 1]) // * 3
maxZeros([1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]) // * 5