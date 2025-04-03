<script setup>
import { get } from "@/api/product";
import ProductAddButton from "@/components/ProductAddButton.vue";
import ProductList from "@/components/ProductList.vue";
import { computed } from "vue";
import { reactive, provide } from "vue";

const states = reactive({ productList: [] });

const fetchProducts = async () => {
	const response = await get("/category/electronics");
	states.productList = response.data;
};

provide(
	"productList",
	computed(() => states.productList)
);

fetchProducts();
</script>

<template>
	<h1><i class="fa-solid fa-tv"></i> 가전</h1>
	<div class="pt-3">
		<ProductList />
		<ProductAddButton category="electronics" />
	</div>
</template>
