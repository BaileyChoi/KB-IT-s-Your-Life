<script setup>
import { ref } from "vue";

const isNavShow = ref(false);
</script>

<template>
	<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
		<span class="navbar-brand ps-3">TodoList App</span>
		<button
			class="navbar-toggler"
			type="button"
			@click="isNavShow = !isNavShow"
		>
			<span class="navbar-toggler-icon"></span>
		</button>
		<div
			:class="
				isNavShow ? 'collapse navbar-collapse show' : 'collapse navbar-collapse'
			"
		>
			<ul class="navbar-nav ps-4">
				<li class="nav-item">
					<router-link class="nav-link" to="/"
						><i class="fa-solid fa-house"></i> Home</router-link
					>
				</li>
				<li class="nav-item">
					<router-link class="nav-link" to="/about"
						><i class="fa-solid fa-circle-info"></i> About</router-link
					>
				</li>
				<li class="nav-item">
					<router-link class="nav-link" to="/todos"
						><i class="fa-solid fa-list"></i> TodoList</router-link
					>
				</li>
			</ul>
		</div>
	</nav>
</template>

<style scoped></style>
