fs = require("fs");

const data = fs.readFileSync("./example.txt", "utf-8");

if (fs.existsSync("text-1.txt")) {
	console.log("file already exits");
} else {
	fs.writeFile("./text-1.txt", data, (err) => {
		if (err) {
			return console.log(err);
		}
	});
}
