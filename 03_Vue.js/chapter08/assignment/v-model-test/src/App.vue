<script>
import InputName from "./components/InputName.vue";
export default {
	name: "App",
	components: { InputName },
	data() {
		return { searchName: "John" };
	},
};
</script>

<template>
	<div>
		<InputName v-model:name="searchName" />
		<h3>검색어 : {{ searchName }}</h3>
	</div>
</template>
