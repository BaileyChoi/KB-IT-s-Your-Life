document.addEventListener("DOMContentLoaded", () => {
	const textInput = document.getElementById("textUrl");
	const mainColorInput = document.getElementById("mainColor");
	const bgColorInput = document.getElementById("bgColor");
	const sizeInput = document.getElementById("size");
	const marginInput = document.getElementById("margin");
	const formatInputs = document.querySelectorAll("input[name='imageFormat']");
	const form = document.querySelector("form");
	const qrCodeContainer = document.getElementById("qrCodeContainer");

	const mainColorTxt = document.getElementById("mainColorTxt");
	const bgColorTxt = document.getElementById("bgColorTxt");
	const sizeTxt = document.getElementById("sizeTxt");
	const marginTxt = document.getElementById("marginTxt");

	// Update displayed values
	mainColorInput.addEventListener(
		"input",
		() => (mainColorTxt.textContent = mainColorInput.value)
	);
	bgColorInput.addEventListener(
		"input",
		() => (bgColorTxt.textContent = bgColorInput.value)
	);
	sizeInput.addEventListener(
		"input",
		() => (sizeTxt.textContent = `${sizeInput.value} x ${sizeInput.value}`)
	);
	marginInput.addEventListener(
		"input",
		() => (marginTxt.textContent = `${marginInput.value}px`)
	);

	// Handle form submission
	form.addEventListener("submit", (e) => {
		e.preventDefault();

		const text = encodeURIComponent(textInput.value.trim());
		const mainColor = mainColorInput.value.replace("#", "");
		const bgColor = bgColorInput.value.replace("#", "");
		const size = sizeInput.value;
		const margin = marginInput.value;
		const format =
			Array.from(formatInputs).find((input) => input.checked)?.value || "png";

		if (!text) {
			alert("Please enter a valid URL or text.");
			return;
		}

		const qrCodeUrl = `https://api.qrserver.com/v1/create-qr-code/?data=${text}&size=${size}x${size}&margin=${margin}&color=${mainColor}&bgcolor=${bgColor}&format=${format.toLowerCase()}`;

		qrCodeContainer.innerHTML = `<img src="${qrCodeUrl}" alt="Generated QR Code" />`;
	});
});
