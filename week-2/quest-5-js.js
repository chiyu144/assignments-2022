// * Binary Gap

function maxZeros (nums) {
  // * O(n)
  let result = 0;

  // * 紀錄上一個遇到 1 的位置 (先判斷第一個數字是否為 1，是的話就先記著了，否的話就設 -1 代表還沒有遇到 1)
  let lastOne = nums[0] === 1 ? 0 : -1;

  // * 如果遇到 1，並且先前已經有遇過 1 (有上一個 1 的位置)了
  // * 就用目前的 1 跟上一個 1 的位置相減 → 得到距離 → 跟 result 內存的數據比大小得到結果 
  for(let i = 0; i < nums.length; i++) {
    if (nums[i] === 1 && lastOne !== -1) {
      result = i - lastOne > result ? i - lastOne : result;
      lastOne = i;
    }
  };

  console.log(`Max Zeros: ${result}`);
}

maxZeros([0, 1, 0, 0]); // * 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // * 4
maxZeros([1, 1, 1, 1, 1]); // * 0
maxZeros([0, 0, 0, 1, 1]) // * 3