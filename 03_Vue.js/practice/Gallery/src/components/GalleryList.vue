<script>
import GalleryListItem from "./GalleryListItem.vue";

export default {
	name: "GalleryList",
	components: {
		GalleryListItem,
	},
	inject: ["images"],
};
</script>

<template>
	<ul class="gallery-list">
		<GalleryListItem v-for="img in images" :key="img.id" :image="img" />
	</ul>
</template>

<style>
.gallery-list {
	display: flex;
	justify-content: center;
	gap: 10px;
	padding: 0;
	list-style: none;
}
</style>
