<script setup>
defineProps({
	productItem: { Type: Object, required: true },
});
</script>

<template>
	<li class="list-group-item">
		<img
			class="mr-5"
			:src="productItem.image"
			alt="사진"
			width="40"
			height="40"
		/>
		<span>{{ productItem.title }}</span>
	</li>
</template>

<style scoped></style>
