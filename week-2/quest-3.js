// * 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
// * 不可以使用排序相關的內建函式。

function maxProduct(nums){
  // * O(n^2)

  // * 小於 2 筆整數的就先退貨了
  if (nums.length < 2) return;

  // * 因為會出現負數，所以把 max 先設為一個極小的值，比大小才不會出問題
  let max = -Infinity;

  // * 用雙迴圈實作兩兩相乘 + 比大小
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const temp = nums[i] * nums[j];
      max = temp > max ? temp : (max === -0 ? max = 0 : max); // * 不想看到 "-0" XD||
    };
  };

  console.log(max);
}

maxProduct([5, 20, 2, 6]) // * 120
maxProduct([10, -20, 0, 3]) // * 30
maxProduct([-1, 2]) // * -2
maxProduct([-1, 0, 2]) // * 0
maxProduct([-1, -2, 0]) // * 2
