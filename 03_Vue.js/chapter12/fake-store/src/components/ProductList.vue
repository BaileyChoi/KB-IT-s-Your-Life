<script setup>
import { inject } from "vue";
import ProuductItem from "./ProuductItem.vue";

const productList = inject("productList");
</script>

<template>
	<div class="row">
		<div class="col">
			<ul class="list-group">
				<ProuductItem
					v-for="productItem in productList"
					:key="productItem.id"
					:productItem="productItem"
				/>
			</ul>
		</div>
	</div>
</template>

<style scoped></style>
