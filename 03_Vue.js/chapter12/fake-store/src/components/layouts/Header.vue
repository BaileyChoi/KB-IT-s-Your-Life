<script setup>
import config from "@/config";
</script>

<template>
  <div class="jumbotron p-5">
    <h1>{{ config.title }}</h1>
    <p>{{ config.subtitle }}</p>
  </div>
</template>

<style scoped>
.jumbotron {
  background-image: url("@/assets/background.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  color: white;
  text-shadow: 2px 0 black;
  font-weight: bold;
  padding: 2rem;
}
</style>
