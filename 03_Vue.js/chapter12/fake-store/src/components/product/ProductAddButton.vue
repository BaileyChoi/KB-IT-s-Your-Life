<script setup>
import { useRouter } from "vue-router";

const props = defineProps({
  category: { type: String, required: true },
});

const router = useRouter();

const goToAddPage = () => {
  router.push({
    path: "product/write",
    query: {
      category: props.category,
    },
  });
};
</script>

<template>
  <button class="btn btn-primary float-end my-2" @click="goToAddPage">
    <i class="fa-solid fa-plus"></i> 상품 등록
  </button>
</template>

<style scoped></style>
