const c = require("ansi-colors");

function hello(name) {
	console.log("Hello", c.red(name), "!!");
}

hello("Bingbong");
