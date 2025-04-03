<script setup>
import { reactive, computed } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const category = route.query.category;
const productItem = reactive({ title: "", description: "", category });

const isTitleValid = computed(() => productItem.title.trim().length >= 5);

const addProductHandler = () => {
	if (!confirm("상품을 등록하시겠습니까?")) return;

	// addProduct();

	router.push(`/${category}`);
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
				<input
					type="text"
					class="form-control"
					id="category"
					:value="category"
					readonly
				/>
			</div>
			<div class="form-group">
				<label htmlFor="desc">상품명:</label>
				<input
					type="text"
					class="form-control"
					id="title"
					v-model="productItem.title"
					placeholder="상품명은 최소 5글자 이상이어야 합니다."
				/>
			</div>
			<div class="form-group">
				<label htmlFor="desc">이미지 경로:</label>
				<input type="file" class="form-control" id="image" />
			</div>
			<div class="form-group">
				<label htmlFor="desc">설명:</label>
				<textarea
					class="form-control"
					rows="3"
					id="desc"
					v-model="productItem.description"
				></textarea>
			</div>
			<div class="form-group d-flex justify-content-center">
				<button
					type="button"
					class="btn btn-primary m-1"
					@click="addProductHandler"
					:disabled="!isTitleValid"
				>
					<i class="fa-solid fa-check"></i> 확인
				</button>
				<button
					type="button"
					class="btn btn-primary m-1"
					@click="router.push(`/${category}`)"
				>
					<i class="fa-solid fa-rotate-left"></i> 취소
				</button>
			</div>
		</div>
	</div>
</template>

<style scoped></style>
