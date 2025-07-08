<script setup>
const props = defineProps({
	travel: { type: Object, required: true },
});

// console.log(props.travel.images);

const background = {
	// 첫번째 이미지를 배경 이미지로 설정
	backgroundImage: `url('${props.travel.images[0].url}')`,
};
</script>

<template>
	<div
		class="travel-header mb-4 d-flex justify-content-center align-items-center"
		:style="background"
	>
		<h1>[{{ travel.district }}] {{ travel.title }}</h1>
	</div>
</template>

<style scoped>
.travel-header {
	height: 300px;
	background-repeat: no-repeat;
	background-position: center;
	background-size: cover;
	color: white;
}
</style>
