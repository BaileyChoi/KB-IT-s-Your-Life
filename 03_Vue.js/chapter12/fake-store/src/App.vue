<script setup>
import DefaultLayout from "./components/layouts/DefaultLayout.vue";
import Header from "./components/layouts/Header.vue";
import NavBar from "./components/layouts/NavBar.vue";
import Footer from "./components/layouts/Footer.vue";
</script>

<template>
  <DefaultLayout>
    <template v-slot:header><Header /></template>
    <template v-slot:navbar><NavBar /></template>
    <template v-slot:default><RouterView /></template>
    <template v-slot:footer><Footer /></template>
  </DefaultLayout>
</template>
