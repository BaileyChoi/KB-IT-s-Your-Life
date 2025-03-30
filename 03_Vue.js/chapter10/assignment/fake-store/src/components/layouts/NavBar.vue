<script setup>
import { computed, reactive } from "vue";
import config from "@/config";
import MenuGroup from "./menu/MenuGroup.vue";

const state = reactive({ isNavShow: false });
const navClass = computed(() => {
  return state.isNavShow
    ? "collapse navbar-collapse show"
    : "collapse navbar-collapse";
});
const changeIsNavShow = () => {
  state.isNavShow = !state.isNavShow;
};
</script>

<template>
  <nav class="navbar navbar-expand-sm bg-info navbar-dark">
    <router-link class="navbar-brand" to="/">
      &nbsp;<i class="fa-solid fa-house"></i>
      {{ config.title }}
    </router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#collapsibleNavbar"
      @click="changeIsNavShow"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div :class="navClass" id="collapsibleNavbar">
      <MenuGroup :menus="config.menus" />
    </div>
  </nav>
</template>
