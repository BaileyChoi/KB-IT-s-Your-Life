<script setup>
import DefaultLayout from "./components/layouts/DefaultLayout.vue";
import Header from "./components/layouts/Header.vue";
import NavBar from "./components/layouts/NavBar.vue";
import Footer from "./components/layouts/Footer.vue";
import { reactive } from "vue";

const state = reactive({
	productMap: {
		electronics: [],
		jewelry: [],
		mensclothing: [],
		womensclothing: [],
	},
});

const getProductList = async (category) => {
	const response = await axios.get(`/api/products/category/${category}`);
	if (response.status === 200) {
		state.productMap[category] = response.data;
	}
};

const addProduct = async (category, product, callback) => {
	const response = await axios.post(`/api/products`, {
		...product,
		category,
	});
	if (response.status === 201) {
		state.productMap[category].push(response.data);
		callback?.();
	}
};

const deleteProduct = async (id) => {
	await axios.delete(`/api/products/${id}`);
	state.productList = state.productList.filter((p) => p.id !== id);
};

const updateProduct = async (product, successCallback) => {
	const response = await axios.put(`/api/products/${product.id}`, product);
	if (response.status === 200) {
		const index = state.productList.findIndex((p) => p.id === product.id);
		state.productList[index] = response.data;
		successCallback?.();
	}
};

// Provide 상태 + 메서드
provide(
	"productList",
	computed(() => state.productList)
);
provide("addProduct", addProduct);
provide("deleteProduct", deleteProduct);
provide("updateProduct", updateProduct);
</script>

<template>
	<DefaultLayout>
		<template v-slot:header><Header /></template>
		<template v-slot:navbar><NavBar /></template>
		<template v-slot:default><RouterView /></template>
		<template v-slot:footer><Footer /></template>
	</DefaultLayout>
</template>
