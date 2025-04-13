<script setup>
import { reactive, onMounted, ref } from "vue";

const ts = new Date().getTime();
const todo = ref("");
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

const addTodo = () => {
  if (todo.value.length >= 2) {
    state.todoList.push({
      id: new Date().getTime(),
      todo: todo.value,
      completed: false,
    });
    todo.value = "";
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
      <div class="title">:: TodoList App</div>
    </div>
    <div class="card card-default card-borderless">
      <div class="card-body">
        <div class="row mb-3">
          <div class="col">
            <div class="input-group">
              <input
                type="text"
                class="form-control"
                placeholder="할 일을 입력하세요"
                v-model.trim="todo"
                @keyup.enter="addTodo()"
              />
              <span class="btn btn-primary input-group-addon" @click="addTodo()"
                >추가</span
              >
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <ul class="list-group">
              <li
                v-for="todoitem in state.todoList"
                :key="todoitem.id"
                class="list-group-item"
                :class="{ 'list-group-item-success': todoitem.completed }"
                @click="toggleCompleted(todoitem.id)"
              >
                <span
                  class="pointer"
                  :class="{ 'todo-done': todoitem.completed }"
                >
                  {{ todoitem.todo }} {{ todoitem.completed ? "(완료)" : "" }}
                </span>
                <span
                  class="float-end badge bg-secondary pointer"
                  @click.stop="deleteTodo(todoitem.id)"
                  >삭제</span
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.title {
  text-align: center;
  font-weight: bold;
  font-size: 20pt;
}
.todo-done {
  text-decoration: line-through;
}
.container {
  padding: 10px 10px 10px 10px;
}
.panel-borderless {
  border: 0;
  box-shadow: none;
}
.pointer {
  cursor: pointer;
}
</style>
