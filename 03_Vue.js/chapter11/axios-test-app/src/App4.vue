<script setup>
import axios from "axios";
const requestAPI = async () => {
	const url = "/api/todos";
	let data = { todo: "윗몸일으키기 3세트", desc: "너무 빠르지 않게..." };
	const resp1 = await axios.post(url, data);
	console.log(resp1.data);

	// 변경사항 확인
	const response = await axios.get(url);
	console.log("# 응답객체 : ", response);
};
requestAPI();
</script>

<template>
	<div>
		<h2>콘솔을 확인합니다.</h2>
	</div>
</template>
