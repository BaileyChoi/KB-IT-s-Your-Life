const c = require("ansi-colors");

function hello(name) {
	console.log("Hello", c.cyanBright(name), "!!");
}

hello("Bingbong");
