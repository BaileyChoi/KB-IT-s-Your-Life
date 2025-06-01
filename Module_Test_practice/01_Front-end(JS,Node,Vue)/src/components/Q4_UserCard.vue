<script setup>
const user = {
  name: "홍길동",
  email: "hong@example.com",
  image: new URL("@/assets/dog.jpg", import.meta.url),
};
</script>

<template>
  <div class="card" style="width: 400px">
    <img
      class="card-img-top rounded-circle"
      :src="user.image"
      alt="Card image"
      height="400px"
    />
    <div class="card-body">
      <h4 class="card-title">{{ user.name }}</h4>
      <p class="card-text">{{ user.email }}</p>
      <a href="#" class="btn btn-primary">See Profile</a>
    </div>
  </div>
</template>

<style scoped></style>
