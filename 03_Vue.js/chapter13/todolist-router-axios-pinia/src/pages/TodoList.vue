<script setup>
import TodoItem from "@/components/TodoItem.vue";
import { useTodoListStore } from "@/store/todoList";
import { computed } from "vue";

const todoListStore = useTodoListStore();
const { fetchTodoList } = todoListStore;
const doneCount = computed(() => todoListStore.doneCount);
const todoList = computed(() => todoListStore.todoList);
</script>

<template>
	<div class="row">
		<div class="col p-3">
			<router-link class="btn btn-primary" to="/todos/add">
				할 일 추가
			</router-link>
			<button class="btn btn-primary ms-1" @click="fetchTodoList">
				새로 고침
			</button>
		</div>
	</div>
	<div class="row">
		<div class="col">
			<span
				><i class="fa-solid fa-check-to-slot"></i> 완료된 할 일 :
				{{ doneCount }} / {{ todoList.length }}</span
			>
			<ul class="list-group">
				<TodoItem
					v-for="todoItem in todoList"
					:key="todoItem.id"
					:todoItem="todoItem"
				/>
			</ul>
		</div>
	</div>
</template>

<style scoped></style>
