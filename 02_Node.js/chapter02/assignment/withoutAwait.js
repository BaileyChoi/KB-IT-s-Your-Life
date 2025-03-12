fetch("http://jsonplaceholder.typicode.com/users")
	.then((response) => response.json())
	.then((data) => console.log("data > ", data))
	.catch((err) => console.log(err));
