fs = require("fs");

fs.rm("./test2/test3/test4", { recursive: true }, (err) => {
	if (err) {
		return console.log(err);
	}
	console.log("folder deleted");
});
