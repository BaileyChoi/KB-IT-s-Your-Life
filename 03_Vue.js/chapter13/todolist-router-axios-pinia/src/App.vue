<script setup>
import Header from "@/components/Header.vue";
import Loading from "@/components/Loading.vue";
import { useTodoListStore } from "./store/todoList";
import { computed } from "vue";

const todoListStore = useTodoListStore();
const isLoading = computed(() => todoListStore.isLoading);
const fetchTodoList = todoListStore.fetchTodoList;

fetchTodoList();
</script>

<template>
	<div class="container">
		<Header />
		<router-view />
		<Loading v-if="isLoading" />
	</div>
</template>

<style scoped></style>
