<template>
	<div>
		<h2>관심 있는 K-POP 가수?</h2>
		<hr />
		<ul>
			<CheckboxItem v-for="idol in idols" :key="idol.id" :idol="idol" />
		</ul>
	</div>
</template>

<script>
import CheckboxItem from "./components/CheckboxItem2.vue";

export default {
	name: "App",
	components: { CheckboxItem },
	data() {
		return {
			idols: [
				{ id: 1, name: "방탄소년단", checked: false },
				{ id: 2, name: "블랙핑크", checked: true },
				{ id: 3, name: "엑소", checked: false },
				{ id: 4, name: "있지", checked: true },
			],
		};
	},
};
</script>
