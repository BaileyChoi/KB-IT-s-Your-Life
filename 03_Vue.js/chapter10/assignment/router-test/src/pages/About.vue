<script>
import { useRoute } from "vue-router";

export default {
	name: "About",
	created() {
		console.log(this.$route);
	},
	setup() {
		const currentRoute = useRoute();
		return { currentRoute };
	},
};
</script>

<template>
	<div class="card card-body">
		<h2>About</h2>
		<p>요청 경로 (Composition API): {{ currentRoute.fullPath }}</p>
	</div>
</template>
