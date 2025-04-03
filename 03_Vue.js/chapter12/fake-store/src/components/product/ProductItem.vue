<script setup>
import { RouterLink } from "vue-router";

defineProps({
  productItem: { Type: Object, required: true },
});
</script>

<template>
  <li class="list-group-item">
    <img
      class="me-2"
      :src="productItem.image"
      alt="사진"
      width="30"
      height="30"
    />
    <RouterLink :to="{ name: 'product/id', params: { id: productItem.id } }">{{
      productItem.title
    }}</RouterLink>
  </li>
</template>

<style scoped>
a {
  text-decoration: none;
}
</style>
