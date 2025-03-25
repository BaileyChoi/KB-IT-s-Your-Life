<script>
export default {
	name: "InputName",
	data() {
		return {
			name: "",
		};
	},
	emits: {
		nameChanged: (e) => {
			return e.name && typeof e.name === "string" && e.name.trim().length >= 3
				? true
				: false;
		},
	},
};
</script>

<template>
	<div>
		이름: <input type="text" v-model="name" />
		<button @click="$emit('nameChanged', { name })">이벤트 발신</button>
	</div>
</template>
