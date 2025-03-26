<script>
export default {
	name: "GalleyView",
	props: {
		selectedImage: Object,
	},
};
</script>

<template>
	<div class="gallery-view">
		<img
			v-if="selectedImage"
			:src="selectedImage.img"
			:alt="selectedImage.title"
			class="large-image"
		/>
		<p v-if="selectedImage">{{ selectedImage.title }}</p>
		<p v-else>이미지를 선택하세요</p>
	</div>
</template>

<style>
.gallery-view {
	text-align: center;
	margin-bottom: 20px;
}
.large-image {
	width: 500px;
	height: auto;
	border-radius: 10px;
	box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}
</style>
