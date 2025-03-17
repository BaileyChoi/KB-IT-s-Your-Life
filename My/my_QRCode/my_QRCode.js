document.addEventListener("DOMContentLoaded", () => {
	const textInput = document.getElementById("textUrl");
	const mainColorInput = document.getElementById("mainColor");
	const bgColorInput = document.getElementById("bgColor");
	const sizeInput = document.getElementById("size");
	const marginInput = document.getElementById("margin");
	const formatInputs = document.querySelectorAll("input[name='imageFormat']");
	const form = document.querySelector("form");
	const modal = document.getElementById("modal");
	const modalClose = document.querySelector(".closeBtn");
	const downloadBtn = document.querySelector(".downloadBtn");
	const qrCodeContainer = document.getElementById("qrCodeContainer");

	const mainColorTxt = document.getElementById("mainColorTxt");
	const bgColorTxt = document.getElementById("bgColorTxt");
	const sizeTxt = document.getElementById("sizeTxt");
	const marginTxt = document.getElementById("marginTxt");

	let qrCodeUrl = "";
	let selectedFormat = "";

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
		selectedFormat = Array.from(formatInputs).find(
			(input) => input.checked
		).value;

		if (!text) {
			alert("Please enter a valid URL or text.");
			return;
		}

		modal.style.display = "flex";

		qrCodeUrl = `https://api.qrserver.com/v1/create-qr-code/?data=${text}&size=${size}x${size}&margin=${margin}&color=${mainColor}&bgcolor=${bgColor}&format=${selectedFormat}`;
		qrCodeContainer.innerHTML = `<img src="${qrCodeUrl}" alt="Generated QR Code" />`;
	});

	// Control modal
	modalClose.addEventListener("click", () => {
		modal.style.display = "none";
	});

	// Download QR code
	downloadBtn.addEventListener("click", async () => {
		if (!qrCodeUrl) {
			alert("Please generate a QR code first.");
			return;
		}

		try {
			// Fetch API를 사용하여 이미지 데이터 가져오기
			const response = await fetch(qrCodeUrl);
			const blob = await response.blob();
			const url = URL.createObjectURL(blob);

			// <a> 태그를 사용하여 다운로드 트리거
			const link = document.createElement("a");
			link.href = url;
			link.download = `QRCode.${selectedFormat}`; // 저장될 파일명 지정
			document.body.appendChild(link);
			link.click();

			// 메모리 정리
			URL.revokeObjectURL(url);
			document.body.removeChild(link);
		} catch (error) {
			console.error("QR Code download failed", error);
			alert("Failed to download QR Code. Please try again.");
		}
	});
});
