import { defineStore } from "pinia";
import { reactive, computed } from "vue";
import axios from "axios";

export const useTodoListStore = defineStore("todoList", () => {
	const BASEURI = "/api/todos";
	const states = reactive({ todoList: [], isLoading: false });

	// TodoList 목록 조회
	const fetchTodoList = async () => {
		states.isLoading = true;
		try {
			const response = await axios.get(BASEURI);
			if (response.status === 200) {
				states.todoList = response.data;
			} else {
				alert("데이터를 불러오는데 실패했습니다.");
			}
		} catch (error) {
			alert("에러발생 :" + error);
		} finally {
			states.isLoading = false;
		}
	};

	// 새로운 TodoItem 추가
	const addTodo = async ({ todo, desc }, successCallback) => {
		states.isLoading = true;
		try {
			const payload = { todo, desc };
			const response = await axios.post(BASEURI, payload);
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
			const response = await axios.put(BASEURI + `/${id}`, payload);
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
			const response = await axios.delete(BASEURI + `/${id}`);
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
			const response = await axios.put(BASEURI + `/${id}`, payload);
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

	const todoList = computed(() => states.todoList);
	const isLoading = computed(() => states.isLoading);
	const doneCount = computed(() => {
		const filterd = states.todoList.filter(
			(todoItem) => todoItem.done === true
		);
		return filterd.length;
	});

	return {
		todoList,
		isLoading,
		doneCount,
		fetchTodoList,
		addTodo,
		updateTodo,
		deleteTodo,
		toggleDone,
	};
});
