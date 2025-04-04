<script setup>
import { useTodoListStore } from "@/store/todoList";
import { reactive } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const { addTodo } = useTodoListStore();
const todoItem = reactive({ todo: "", desc: "" });

const addTodoHandler = () => {
	let { todo } = todoItem;
	if (!todo || todo.trim() === "") {
		alert("할 일을 입력해주세요.");
		return;
	}

	addTodo({ ...todoItem }, () => {
		router.push("/todos");
	});
};
</script>

<template>
	<div class="row">
		<div class="col p-3">
			<h2>할일 추가</h2>
		</div>
		<div class="row">
			<div class="col">
				<div class="form-group">
					<label htmlFor="todo">할일 :</label>
					<input
						type="text"
						class="form-control"
						id="todo"
						v-model="todoItem.todo"
					/>
				</div>
				<div class="form-group">
					<label htmlFor="desc">설명 :</label>
					<textarea
						class="form-control"
						rows="3"
						id="desc"
						v-model="todoItem.desc"
					></textarea>
				</div>
				<div class="form-group">
					<button
						type="button"
						class="btn btn-primary m-1"
						@click="addTodoHandler"
					>
						<i class="fa-solid fa-plus"></i> 추가
					</button>
					<button
						type="button"
						class="btn btn-primary m-1"
						@click="router.push('/todos')"
					>
						<i class="fa-solid fa-xmark"></i> 취소
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped></style>
