// * 正確計算出員工的平均薪資，請考慮員工數量會變動的情況

function avg(data){
  const { employees, count } = data;
  const avg = employees.reduce((acc, cur) => acc + cur.salary, 0) / count;
  console.log(`平均薪資: ${avg}`);
}

avg({
  "count": 3,
  "employees":
    [{ "name": "John", "salary": 30000 },
    { "name": "Bob", "salary": 60000 },
    { "name": "Jenny", "salary": 50000 }]
}); // * 46666.666666666664