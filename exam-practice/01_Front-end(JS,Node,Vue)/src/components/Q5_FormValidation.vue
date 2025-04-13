<script setup>
import { ref } from "vue";

const userName = ref("");
const userEmail = ref("");

const handleSubmit = (e) => {
  e.preventDefault();
  if (!userName.value) {
    alert("이름을 입력해주세요");
  } else if (!userEmail.value.includes("@")) {
    alert("유효한 이메일을 입력해주세요");
  } else {
    alert("제출 완료!");
  }
};
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <label>이름(name)</label>
    <input type="text" id="name" class="form-control" v-model.trim="userName" />
    <label>이메일(email)</label>
    <input
      type="email"
      id="email"
      class="form-control"
      v-model.trim="userEmail"
    />
    <button type="submit">제출</button>
  </form>
</template>

<style scoped></style>
