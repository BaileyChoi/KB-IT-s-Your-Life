<script setup>
import { get } from "@/api/product";
import ProductList from "@/components/ProductList.vue";
import { computed } from "vue";
import { reactive, provide } from "vue";

const states = reactive({ productList: [] });

const fetchProducts = async () => {
	const response = await get("/category/jewelery");
	states.productList = response.data;
};

provide(
	"productList",
	computed(() => states.productList)
);

fetchProducts();
</script>

<template>
	<h1>
		주얼리
		<i class="fa-solid fa-gem"></i>
	</h1>
	<ProductList />
</template>
