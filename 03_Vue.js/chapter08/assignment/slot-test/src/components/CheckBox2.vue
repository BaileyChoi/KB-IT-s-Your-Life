<script>
export default {
	name: "CheckBox1",
	props: ["id", "checked", "label"],
};
</script>

<template>
	<div>
		<input
			type="checkbox"
			:value="id"
			:checked="checked"
			@change="$emit('check-changed', { id, checked: $event.target.checked })"
		/>
		<slot>Item</slot>
	</div>
</template>
