<script setup>
import { post } from "@/api/product";
import { reactive, computed } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const category = route.query.category;
const productItem = reactive({ title: "", category });

const isTitleValid = computed(() => productItem.title.trim().length >= 5);

const addProductHandler = async () => {
  if (!confirm("상품을 등록하시겠습니까?")) return;
  const result = await post("/", productItem);
  console.log(result);
  router.push({ name: category });
};
</script>

<template>
  <div class="row">
    <div class="col pb-5">
      <h2><i class="fa-solid fa-plus"></i> 상품 등록</h2>
    </div>
  </div>
  <div class="row">
    <div class="col">
      <div class="form-group">
        <label>카테고리:</label>
        <input type="text" class="form-control" :value="category" readonly />
      </div>
      <div class="form-group">
        <label>상품명:</label>
        <input
          type="text"
          class="form-control"
          v-model="productItem.title"
          placeholder="상품명은 최소 5글자 이상이어야 합니다."
        />
      </div>
      <div class="form-group">
        <label>이미지 경로:</label>
        <input type="text" class="form-control" v-model="productItem.image" />
      </div>
      <div class="form-group">
        <label>설명:</label>
        <textarea
          class="form-control"
          rows="3"
          v-model="productItem.description"
        ></textarea>
      </div>
      <div class="form-group d-flex justify-content-center">
        <button
          type="button"
          class="btn btn-primary me-1"
          @click="addProductHandler"
          :disabled="!isTitleValid"
        >
          <i class="fa-solid fa-check"></i> 확인
        </button>
        <RouterLink :to="{ name: category }" class="btn btn-primary">
          <i class="fa-solid fa-undo"></i> 취소
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
