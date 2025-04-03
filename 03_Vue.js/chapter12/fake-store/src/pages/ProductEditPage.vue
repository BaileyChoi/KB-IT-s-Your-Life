<script setup>
import { computed, reactive } from "vue";
import { RouterLink, useRoute, useRouter } from "vue-router";
import * as api from "@/api/product";

const router = useRouter();
const route = useRoute();

const { category } = route.query;
const id = parseInt(route.params.id);

const product = reactive({ category });

const isDisable = computed(() => !product.title || product.title.length < 5);

const updateProductHandler = async () => {
  if (!confirm("수정할까요?")) return;
  const result = await api.put("/" + id, product);
  console.log("수정 결과:", result);
  router.push({ name: "product/id", params: { id: product.id } });
};

const fetchProducts = async () => {
  const data = await api.get("/" + id);
  Object.assign(product, data);
  console.log(product);
};

fetchProducts();
</script>

<template>
  <form @submit.prevent="submit" class="mx-auto" style="width: 600px">
    <h2 class="my-5">상품 수정</h2>
    <div class="my-3">
      <label> 카테고리: </label>
      <div class="form-control border-0">
        {{ product.category }}
      </div>
    </div>
    <div class="my-3">
      <label> 상품명*: </label>
      <input type="text" class="form-control" v-model="product.title" />
    </div>
    <div class="my-3">
      <label> 이미지 경로: </label>
      <input type="text" class="form-control" v-model="product.image" />
    </div>
    <div class="my-3">
      <label> 설명: </label>
      <textarea class="form-control" v-model="product.description"></textarea>
    </div>
    <div class="text-center">
      <button
        class="btn btn-primary me-1"
        :disabled="isDisable"
        @click="updateProductHandler"
      >
        <i class="fa-solid fa-check"></i> 확인
      </button>
      <RouterLink
        :to="{ name: 'product/id', params: { id: product.id } }"
        class="btn btn-primary"
      >
        <i class="fa-solid fa-undo"></i> 취소
      </RouterLink>
    </div>
  </form>
</template>

<style scoped></style>
