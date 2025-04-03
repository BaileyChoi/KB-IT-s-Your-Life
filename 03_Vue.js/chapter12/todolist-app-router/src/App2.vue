<script setup>
import Header from "@/components/Header.vue";
import Loading from "@/components/Loading.vue";
import axios from "axios";
import { computed } from "vue";
import { provide, reactive } from "vue";

const BASEURL = "/api/todos";
const states = reactive({ todoList: [], isLoading: false });

const fetchTodoList = async () => {
	states.isLoading = true;
	try {
		const response = await axios.get(BASEURL);
		if (response.status === 200) {
			states.todoList = response.data;
			states.isLoading = false;
		} else {
			alert("데이터를 불러오는데 실패했습니다.");
		}
	} catch (error) {
		alert("에러발생 :" + error);
	}
};

// 새로운 TodoItem 추가
const addTodo = async ({ todo, desc }, successCallback) => {
	states.isLoading = true;
	try {
		const payload = { todo, desc };
		const response = await axios.post(BASEURL, payload);
		if (response.status === 201) {
			states.todoList.push({ ...response.data, done: false });
			successCallback();
			states.isLoading = false;
		} else {
			alert("Todo 추가 실패");
		}
	} catch (error) {
		alert("에러발생 :" + error);
	}
};

// 기존 TodoItem 변경
const updateTodo = async ({ id, todo, desc, done }, successCallback) => {
	states.isLoading = true;
	try {
		const payload = { id, todo, desc, done };
		const response = await axios.put(BASEURL + `/${id}`, payload);
		if (response.status === 200) {
			let index = states.todoList.findIndex((todo) => todo.id === id);
			states.todoList[index] = payload;
			successCallback();
			states.isLoading = false;
		} else {
			alert("Todo 변경 실패");
		}
	} catch (error) {
		alert("에러발생 :" + error);
	}
};

// 기존 TodoItem 삭제
const deleteTodo = async (id) => {
	states.isLoading = true;
	try {
		const response = await axios.delete(BASEURL + `/${id}`);
		console.log(response.status, response.data);
		if (response.status === 200) {
			let index = states.todoList.findIndex((todo) => todo.id === id);
			states.todoList.splice(index, 1);
		} else {
			alert("Todo 삭제 실패");
		}
	} catch (error) {
		alert("에러발생 :" + error);
	} finally {
		states.isLoading = false;
	}
};

// 기존 TodoItem의 완료여부(done) 값 토글
const toggleDone = async (id) => {
	states.isLoading = true;
	try {
		let todo = states.todoList.find((todo) => todo.id === id);
		let payload = { ...todo, done: !todo.done };
		const response = await axios.put(BASEURL + `/${id}`, payload);
		if (response.status === 200) {
			todo.done = payload.done;
			states.isLoading = false;
		} else {
			alert("Todo 완료 변경 실패");
		}
	} catch (error) {
		alert("에러발생 :" + error);
	}
};

provide(
	"todoList",
	computed(() => states.todoList)
);
provide("actions", {
	fetchTodoList,
	addTodo,
	updateTodo,
	deleteTodo,
	toggleDone,
});

fetchTodoList();
</script>

<template>
	<div class="container">
		<Header />
		<router-view />
		<Loading v-if="states.isLoading" />
	</div>
</template>

<style scoped></style>
