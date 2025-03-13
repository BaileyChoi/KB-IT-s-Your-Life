const fs = require("fs");

fs.readFileSync("example.txt", "utf-8", (err, data) => {
	if (err) {
		return console.log(err);
	}
	console.log(data);
});
console.log("코드 끝");
