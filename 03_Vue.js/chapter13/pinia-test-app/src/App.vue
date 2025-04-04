<script setup>
import { ref, computed } from "vue";
import { useCounterStore } from "./stores/counter";
import { useTodoListStore } from "./stores/todoList";

// store 테스트
const store = useCounterStore();
const { increment } = store;
const count = computed(() => store.count);
increment();
// console.log(count);

// todoList 테스트
const todo = ref("");

const todoListStore = useTodoListStore();
const { todoList, addTodo, deleteTodo, toggleTodo } = todoListStore;

const doneCount = computed(() => todoListStore.doneCount);

const addTodoHandler = () => {
	addTodo(todo.value);
	todo.value = "";
};
</script>

<template>
	<!-- <div>
		<h2>Store 테스트</h2>
		{{ store.count }} / {{ store.doubleCount }}
		<br />
		{{ count }}
	</div> -->
	<div>
		<h2>TodoList 테스트(Composition API)</h2>
		<hr />
		할 일 추가 :
		<input type="text" v-model="todo" />
		<button @click="addTodoHandler">추가</button>
		<hr />
		<ul>
			<li v-for="todoItem in todoList">
				<span style="cursor: pointer" @click="toggleTodo(todoItem.id)">
					{{ todoItem.todo }} {{ todoItem.done ? "(완료)" : "" }}
				</span>
				&nbsp;&nbsp;&nbsp;
				<button @click="deleteTodo(todoItem.id)">삭제</button>
			</li>
		</ul>
		<div>완료된 할 일 수 : {{ doneCount }}</div>
	</div>
</template>

<style scoped></style>
