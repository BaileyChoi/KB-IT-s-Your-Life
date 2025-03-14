let add = function (x, y) {
	this.result = x + y;
};

let obj = {};

add.apply(obj, [1, 4]);
console.log(obj);

add.call(obj, 2, 4);
console.log(obj);

add = add.bind(obj);
add(3, 4);
console.log(obj);
