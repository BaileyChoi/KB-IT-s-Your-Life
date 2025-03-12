const submitBtn = document.getElementById("submitBtn");

const inputName = ["First Name", "Last Name", "Email", "Password"];
const emailFormat = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

submitBtn.addEventListener("click", (event) => {
	event.preventDefault();

	const input = document.querySelectorAll(".input");
	const inputText = document.querySelectorAll(".inputTxt");

	for (let i = 0; i < input.length; i++) {
		if (input[i].value.trim() === "") {
			input[i].classList.add("empty");
			inputText[i].innerHTML = `${inputName[i]} cannot be empty`;
		} else {
			input[i].classList.remove("empty");
			inputText[i].innerHTML = "";
		}

		if (i == 2 && !input[2].value.match(emailFormat)) {
			input[2].classList.add("empty");
			inputText[2].innerHTML = "Looks like this is not an email";
		}
	}
});
