const fs = require("fs");

const rs = fs.createReadStream("./readMe.txt", "utf-8");

rs.on("data", (chunk) => {
	console.log("new chunk received:");
	console.log(`chunk.length: ${chunk.length},\nchunk: ${chunk}`);
})
	.on("end", () => {
		console.log("finished reading data");
	})
	.on("error", (err) => {
		console.log(`Error reading the file: ${err}`);
	});
