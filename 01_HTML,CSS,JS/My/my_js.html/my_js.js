const ratingState = document.getElementById("ratingState");
const thankState = document.getElementById("thankState");
const rateBtns = document.querySelectorAll("#rateBtn");
const submitBtn = document.getElementById("submitBtn");
const userRating = document.getElementById("userRating");
let userRatingValue = null;
let selectedButton = null;

rateBtns.forEach((btn) => {
	btn.addEventListener("click", (e) => {
		if (selectedButton) {
			selectedButton.classList.remove("active");
		}
		btn.classList.add("active");
		userRatingValue = e.target.textContent;
		selectedButton = btn;
	});
});

submitBtn.addEventListener("click", function () {
	if (userRatingValue) {
		ratingState.style.display = "none";
		thankState.style.display = "flex";
		userRating.textContent = userRatingValue;
	} else {
		console.log("Please select a rating before submitting!");
	}
});
