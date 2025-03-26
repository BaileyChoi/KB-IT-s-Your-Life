<script>
export default {
	name: "Child1",
	created() {
		console.log("Child1 : ", this.$style);
	},
};
</script>

<style module>
.child {
	background-color: khaki;
	border: solid 1px black;
	margin: 1.5em;
	padding: 1em;
}
</style>

<template>
	<div :class="$style.child">
		<h2>Child1</h2>
	</div>
</template>
