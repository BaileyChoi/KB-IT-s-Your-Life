<script setup>
import { get, remove } from "@/api/product";
import { ref } from "vue";
import { RouterLink, useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const id = parseInt(route.params.id);
const productItem = ref({});

const removeProductHandler = async () => {
  if (!confirm("상품을 삭제하시겠습니까?")) return;
  const result = await remove("/" + id);
  console.log(result);
  router.push({ name: productItem.value.category });
};

const fetchProducts = async () => {
  productItem.value = await get("/" + id);
  console.log(productItem.value);
};

fetchProducts();
</script>

<template>
  <h3>{{ productItem.title }}</h3>
  <div>{{ productItem.category }}</div>
  <div class="text-end">
    가격: ${{ productItem.price }} /
    <i class="fa-solid fa-heart text-danger"></i> 평점:
    {{ productItem.rating && productItem.rating.rate }} ({{
      productItem.rating && productItem.rating.count
    }}
    명)
  </div>
  <div>
    <img :src="productItem.image" width="100px" />
  </div>
  <div class="text-center my-5">
    <RouterLink
      class="btn btn-primary me-1"
      :to="{ name: productItem.category }"
    >
      <i class="fa-solid fa-list"></i> 목록
    </RouterLink>
    <RouterLink
      class="btn btn-primary me-1"
      :to="{ name: 'product/edit', params: { id: productItem.id } }"
    >
      <i class="fa-solid fa-pen-to-square"></i> 수정
    </RouterLink>
    <button class="btn btn-danger me-1" @click="removeProductHandler">
      <i class="fa-regular fa-trash-can"></i> 삭제
    </button>
  </div>
</template>

<style scoped></style>
