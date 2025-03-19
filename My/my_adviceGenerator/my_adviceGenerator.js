const adviceId = document.getElementById("adviceId");
const advice = document.getElementById("advice");
const dice = document.querySelector(".dice");

dice.addEventListener("click", () => {
	const Http = new XMLHttpRequest();

	let apiUrl = "https://api.adviceslip.com/advice";

	Http.open("GET", apiUrl);
	Http.send();
	Http.onreadystatechange = () => {
		if (Http.readyState === 4 && Http.status === 200) {
			try {
				const response = JSON.parse(Http.responseText);
				console.log(response);

				adviceId.innerHTML = `Advice #${response.slip.id}`;
				advice.innerHTML = `"${response.slip.advice}"`;
			} catch (err) {
				console.log(err);
			}
		} else if (Http.readyState === 4) {
			console.log("Error: ", Http.status);
		}
	};
});
