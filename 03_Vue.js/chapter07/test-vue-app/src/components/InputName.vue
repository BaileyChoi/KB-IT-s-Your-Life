<template>
	<div style="border: solid 1x gray; padding: 5px">
		이름: <input type="text" v-model="name" />
		<button @click="$emit('nameChanged', { name })">이벤트 발신</button>
	</div>
</template>
<script>
export default {
	name: "InputName",
	// emits: ['nameChanged1'],
	emits: {
		namedChanged: (e) => {
			return e.name && typeof e.name === "string" && e.name.trim().length >= 3
				? true
				: false;
		},
	},
	data() {
		return { name: "" };
	},
};
</script>
