<script setup>
import { get } from "@/api/product";
import ProductAddButton from "@/components/product/ProductAddButton.vue";
import ProductList from "@/components/product/ProductList.vue";
import { reactive } from "vue";

const category = "electronics";
const state = reactive({ productList: [] });

const fetchProducts = async () => {
  state.productList = await get("/category/" + category);
};

fetchProducts();
</script>

<template>
  <h1><i class="fa-solid fa-tv"></i> 가전</h1>
  <div class="pt-3">
    <ProductList :products="state.productList" />
    <ProductAddButton :category="category" />
  </div>
</template>
