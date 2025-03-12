async function init() {
	try {
		const response = await fetch("http://jsonplaceholder.typicode.com/users");
		const users = await response.json();
		console.log("users >", users);
	} catch (err) {
		console.log(err);
	}
}

init();
