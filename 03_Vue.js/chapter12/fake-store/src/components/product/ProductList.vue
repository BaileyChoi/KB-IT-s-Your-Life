<script setup>
import ProductItem from "./ProductItem.vue";

const props = defineProps({
  products: { type: Array, required: true },
});
</script>

<template>
  <div class="row">
    <div class="col">
      <ul class="list-group">
        <ProductItem
          v-for="productItem in products"
          :key="productItem.id"
          :productItem="productItem"
        />
      </ul>
    </div>
  </div>
</template>

<style scoped></style>
