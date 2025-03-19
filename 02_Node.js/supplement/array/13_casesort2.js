const country = ["korea", "USA", "Japan", "China"];
console.log("before = " + country);

country.sort(function (left, right) {
	let left2 = left.toLocaleLowerCase();
	let right2 = right.toLocaleLowerCase();
	if (left2 < right2) return -1;
	if (left2 > right2) return 1;
	return 0;
});

console.log("after = " + country);
