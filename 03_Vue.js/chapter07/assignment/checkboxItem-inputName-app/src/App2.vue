<script>
import CheckboxItem from "./components/CheckboxItem.vue";

export default {
	name: "App",
	components: {
		CheckboxItem,
	},
	data() {
		return {
			idols: [
				{ id: 1, name: "BTS", checked: true },
				{ id: 2, name: "Black Pink", checked: false },
				{ id: 3, name: "EXO", checked: true },
				{ id: 4, name: "ITZY", checked: false },
			],
		};
	},
};
</script>

<template>
	<div>
		<h2>관심 있는 K-POP 가수</h2>
		<hr />
		<ul>
			<CheckboxItem v-for="idol in idols" :key="idol.id" :idol="idol" />
		</ul>
	</div>
</template>
