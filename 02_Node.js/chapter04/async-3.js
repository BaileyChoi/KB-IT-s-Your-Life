const fs = require("fs");

fs.readdir("./", (err, files) => {
	if (err) {
		return console.log(err);
	}
	console.log(files);
});
console.log("Code is done.");
