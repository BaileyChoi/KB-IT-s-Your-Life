import { defineStore } from "pinia";
import { reactive, computed } from "vue";
import axios from "axios";

export const useTodoListStore = defineStore("todoList", () => {
  const BASEURI = "/api/todos";
  const states = reactive({ todoList: [], isLoading: false });

  const todoList = computed(() => states.todoList);
  const isLoading = computed(() => states.isLoading);
  const doneCount = computed(() => {
    const filtered = states.todoList.filter(
      (todoItem) => todoItem.done === true
    );
    return filtered.length;
  });

  const fetchTodoList = async () => {
    states.isLoading = true;
    try {
      const response = await axios.get(BASEURI);
      if (response.status === 200) {
        states.todoList = response.data;
      } else {
        alert("Todo 불러오기 실패함");
      }
    } catch (error) {
      alert("에러발생 :" + error);
    } finally {
      states.isLoading = false;
    }
  };

  const addTodo = async ({ todo, desc }, successCallback) => {
    states.isLoading = true;
    try {
      const payload = { todo, desc };
      const response = await axios.post(BASEURI, payload);
      if (response.status === 201) {
        states.todoList.push({ ...response.data, done: false });
        successCallback();
      } else {
        alert("Todo 추가 실패함");
      }
    } catch (error) {
      alert("에러발생 :" + error);
    } finally {
      states.isLoading = false;
    }
  };

  const updateTodo = async ({ id, todo, desc, done }, successCallback) => {
    states.isLoading = true;
    try {
      const payload = { id, todo, desc, done };
      const response = await axios.put(BASEURI + `/${id}`, payload);
      if (response.status === 200) {
        let index = states.todoList.findIndex((todo) => todo.id === id);
        states.todoList[index] = payload;
        successCallback();
      } else {
        alert("Todo 변경 실패함");
      }
    } catch (error) {
      alert("에러발생 :" + error);
    } finally {
      states.isLoading = false;
    }
  };

  const deleteTodo = async (id) => {
    states.isLoading = true;
    try {
      const response = await axios.delete(BASEURI + `/${id}`);
      if (response.status === 200) {
        let index = states.todoList.findIndex((todo) => todo.id === id);
        states.todoList.splice(index, 1);
      } else {
        alert("Todo 삭제 실패함");
      }
    } catch (error) {
      alert("에러발생 :" + error);
    } finally {
      states.isLoading = false;
    }
  };

  const toggleDone = async (id) => {
    states.isLoading = true;
    try {
      let todo = states.todoList.find((todo) => todo.id === id);
      let payload = { ...todo, done: !todo.done };
      const response = await axios.put(BASEURI + `/${id}`, payload);
      if (response.status === 200) {
        todo.done = payload.done;
      } else {
        alert("Todo 완료 변경 실패함");
      }
    } catch (error) {
      alert("에러발생 :" + error);
    } finally {
      states.isLoading = false;
    }
  };

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
