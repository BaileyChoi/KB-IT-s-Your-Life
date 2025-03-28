<script>
import { useRoute } from "vue-router";

export default {
	name: "Videos",
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
		<h2>Videos</h2>
		<p>요청 경로 (Options API) : {{ $route.fullPath }}</p>
	</div>
</template>
