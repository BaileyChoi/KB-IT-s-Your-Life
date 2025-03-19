const arr = [1, 2, 3, 4, 5];
const result = arr.reduce((acc, cur, idx) => (acc += cur), 0);
console.log(result);

const arr2 = [1, 2, 3, 4, 5];
const result2 = arr2.reduce((acc, cur, idx) => (acc += cur), 10);
console.log(result2);

const arr3 = [1, 2, 3, 4, 5];
const result3 = arr2.reduce((acc, cur, idx) => (acc += cur));
console.log(result3);
