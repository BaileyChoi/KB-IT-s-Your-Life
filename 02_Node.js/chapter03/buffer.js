const fs = require("fs");

fs.readFile("example.txt", (err, data) => {
	if (err) {
		return console.error(err);
	}
	console.log(data);
	console.log("\n");
	console.log(data.toString());
});
