const hello = (name) => {
	console.log(`${name} 안녕~`);
};

module.exports = hello;

// 더 짧은 버전
exports.hello = (name) => {
	console.log(`${name} 안녕~`);
};
