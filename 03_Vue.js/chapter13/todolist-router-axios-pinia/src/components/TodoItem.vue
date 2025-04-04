<script setup>
import { useRouter } from "vue-router";
import { useTodoListStore } from "@/store/todoList";

defineProps({
	todoItem: { Type: Object, required: true },
});

const router = useRouter();

const todoListStore = useTodoListStore();
const { deleteTodo, toggleDone } = todoListStore;
</script>

<template>
	<li
		:class="
			todoItem.done
				? 'list-group-item list-group-item-success'
				: 'list-group-item'
		"
	>
		<span
			:class="todoItem.done ? 'todo-done pointer' : 'pointer'"
			@click="toggleDone(todoItem.id)"
		>
			{{ todoItem.todo }}
			{{ todoItem.done ? "(완료)" : "" }}
		</span>
		<span
			class="float-end badge bg-secondary pointer m-1"
			@click="router.push(`/todos/edit/${todoItem.id}`)"
		>
			<i class="fa-solid fa-pencil"> 편집</i></span
		>
		<span
			class="float-end badge bg-secondary pointer m-1"
			@click="deleteTodo(todoItem.id)"
		>
			<i class="fa-solid fa-trash"> 삭제</i></span
		>
	</li>
</template>

<style scoped></style>
