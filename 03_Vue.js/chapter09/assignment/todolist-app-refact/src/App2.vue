<script setup>
import { reactive, onMounted } from "vue";
import InputTodo2 from "./components/InputTodo2.vue";
import TodoList from "./components/TodoList.vue";

const ts = new Date().getTime();
const state = reactive({ todoList: [] });

onMounted(() => {
	state.todoList.push({ id: ts, todo: "자전거 타기", completed: false });
	state.todoList.push({ id: ts + 1, todo: "딸과 공원 산책", completed: true });
	state.todoList.push({
		id: ts + 2,
		todo: "일요일 애견 카페",
		completed: false,
	});
	state.todoList.push({ id: ts + 3, todo: "Vue 원고 집필", completed: false });
});

const addTodo = (todo) => {
	if (todo.length >= 2) {
		state.todoList.push({
			id: new Date().getTime(),
			todo: todo,
			completed: false,
		});
	}
};
const deleteTodo = (id) => {
	let index = state.todoList.findIndex((item) => id === item.id);
	state.todoList.splice(index, 1);
};
const toggleCompleted = (id) => {
	let index = state.todoList.findIndex((item) => id === item.id);
	state.todoList[index].completed = !state.todoList[index].completed;
};
</script>

<template>
	<div class="container">
		<div class="card card-body bg-light">
			<div classe="title">:: Todolist App</div>
		</div>
		<div class="card card-default card-borderless">
			<div class="card-body">
				<InputTodo2 @add-todo="addTodo"></InputTodo2>
				<TodoList
					:todoList="state.todoList"
					@delete-todo="deleteTodo"
					@toggle-completed="toggleCompleted"
				></TodoList>
			</div>
		</div>
	</div>
</template>
