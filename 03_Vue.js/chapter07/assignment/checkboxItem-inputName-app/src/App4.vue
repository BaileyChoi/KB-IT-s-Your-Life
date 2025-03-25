<script>
import InputName from "./components/InputName.vue";

export default {
	name: "App",
	components: {
		InputName,
	},
	data() {
		return { nameData: "" };
	},
	methods: {
		nameChangedHandler(e) {
			this.nameData = e.name;
		},
	},
};
</script>

<template>
	<div>
		<InputName @nameChanged="nameChangedHandler" />
		<br />
		<h3>정보: {{ nameData }}</h3>
	</div>
</template>
