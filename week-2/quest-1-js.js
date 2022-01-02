// * 使用迴圈計算最小值到最大值之間，所有整數的總和。

function calculate(min, max){
  let result = 0;
  for(let i = Math.ceil(min); i <= max; i++) {
    result += i
  };
  console.log(result);
}

calculate(1, 3); // * 6
calculate(4, 8); // * 30
calculate(-1, 1); // * 0
calculate(1.6, 10.7); // * 54
calculate(0.1, 1); // * 1
calculate(0, 100); // * 5050
