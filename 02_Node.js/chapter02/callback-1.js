const order = (coffee, callback) => {
	console.log(`${coffee} 주문 접수`);
	setTimeout(() => {
		if (!isNaN(coffee)) console.log("완료하지 못했습니다.");
		else callback(coffee);
	}, 3000);
};

const display = (result) => {
	console.log(`${result} 완료!!`);
};

order("카페라떼", display);
