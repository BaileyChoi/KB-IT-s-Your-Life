<script setup>
import { inject, reactive } from "vue";
import { useRoute, useRouter } from "vue-router";

const todoList = inject("todoList");
const { updateTodo } = inject("actions");
const router = useRouter();
const currentRoute = useRoute();

const matchedTodoItem = todoList.value.find(
	// (item) => item.id === parseInt(currentRoute.params.id)
	(item) => item.id === currentRoute.params.id
);
if (!matchedTodoItem) {
	router.push("/todos");
}
const todoItem = reactive({ ...matchedTodoItem });

const updateTodoHandler = () => {
	let { todo } = todoItem;
	if (!todo || todo.trim() === "") {
		alert("할 일을 입력해주세요.");
		return;
	}
	// updateTodo({ ...todoItem });
	// router.push("/todos");
	updateTodo({ ...todoItem }, () => {
		router.push("/todos");
	});
};
</script>

<template>
	<div class="row">
		<div class="col p-3">
			<h2>할일 수정</h2>
		</div>
		<div class="row">
			<div class="col">
				<div class="form-group">
					<label htmlFor="todo">할일:</label>
					<input
						type="text"
						class="form-control"
						id="todo"
						v-model="todoItem.todo"
					/>
				</div>
				<div class="form-group">
					<label htmlFor="desc">설명:</label>
					<textarea
						class="form-control"
						rows="3"
						id="desc"
						v-model="todoItem.desc"
					></textarea>
				</div>
				<div class="form-group">
					<label htmlFor="done">완료여부 : </label>&nbsp;
					<input type="checkbox" v-model="todoItem.done" />
				</div>
			</div>
			<div class="form-group">
				<button
					type="button"
					class="btn btn-primary m-1"
					@click="updateTodoHandler"
				>
					<i class="fa-solid fa-pencil"> 수정</i>
				</button>
				<button
					type="button"
					class="btn btn-primary m-1"
					@click="router.push('/todos')"
				>
					<i class="fa-solid fa-xmark"> 취소</i>
				</button>
			</div>
		</div>
	</div>
</template>

<style scoped></style>
