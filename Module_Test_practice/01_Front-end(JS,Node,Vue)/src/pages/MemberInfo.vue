<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const member = ref(null);

const fetchData = async () => {
	const id = route.params.id;
	const BASEURL = `/api/members/${id}`;
	try {
		const response = await axios.get(BASEURL);
		member.value = response.data;
	} catch (error) {
		console.log("에러 발생" + error);
	}
};

fetchData();
</script>

<template>
	<div class="mt-5" v-if="member">
		<img :src="member.photo" class="img" />
		<h4 class="mt-2">{{ member.name }}({{ member.role }})</h4>
		<p>{{ member.desc }}</p>
		<a
			v-if="member.insta && member.insta !== ''"
			class="fa fa-instagram m-1"
			:href="member.insta"
		></a>
		<a
			v-if="member.facebook && member.facebook !== ''"
			class="fa fa-facebook m-1"
			:href="member.facebook"
		></a>
		<a
			v-if="member.youtube && member.youtube !== ''"
			class="fa fa-youtube m-1"
			:href="member.youtube"
		></a>
		<br /><br />
		<router-link to="/members">멤버 목록으로</router-link>
	</div>
</template>

<style scoped></style>
