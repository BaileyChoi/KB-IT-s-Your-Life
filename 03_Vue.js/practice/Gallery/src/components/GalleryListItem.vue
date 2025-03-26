<script>
export default {
	name: "GalleryListItem",
	props: { image: Object },
};
</script>

<template>
	<li class="gallery-item" @click="$emit('click')">
		<img :src="image.img" :alt="image.title" class="thumbnail" />
		<p>{{ image.title }}</p>
	</li>
</template>

<style>
.gallery-item {
	cursor: pointer;
	text-align: center;
	padding: 10px;
	border: 1px solid #ddd;
	border-radius: 5px;
	transition: transform 0.2s, box-shadow 0.2s;
}

.gallery-item:hover {
	transform: scale(1.05);
	box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}

.thumbnail {
	width: 100px;
	height: 100px;
	object-fit: cover;
	border-radius: 5px;
}
</style>
