<script>
export default {
	name: "CheckboxItem",
	props: {
		id: [Number, String],
		name: String,
		checked: {
			type: Boolean,
			required: false,
			default: false,
		},
	},
};
</script>

<template>
	<li><input type="checkbox" :checked="idol.check" />{{ idol.name }}</li>
</template>
