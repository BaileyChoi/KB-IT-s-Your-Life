<script setup>
import axios from "axios";
import { ref, computed, watch } from "vue";

const contacts = ref(null);
const pageno = ref(1);
const pagesize = 5;
const totalcount = ref(0);

const totalPages = computed(() => Math.ceil(totalcount.value / pagesize));

const requestAPI = async () => {
	// const url = "/api/contacts";
	const url = "https://contactsvc.bmaster.kro.kr/contacts";

	try {
		const response = await axios.get(url, {
			params: {
				pageno: pageno.value,
				pagesize: pagesize,
			},
		});

		contacts.value = response.data.contacts;
		totalcount.value = response.data.totalcount;
		console.log("응답: ", contacts.value);
	} catch (e) {
		console.log("에러: ", e.message);
	}
};

// 페이지 번호가 바뀌면 자동 호출
watch(pageno, requestAPI);

// 첫 로딩 시 한 번 실행
requestAPI();
</script>

<template>
	<div class="container">
		<h2>연락처 목록 (페이지: {{ pageno }} / {{ totalPages }})</h2>
		<ul v-if="contacts.length">
			<li v-for="c in contacts" :key="c.no">
				<p>no : {{ c.no }}</p>
				<p>name : {{ c.name }}</p>
				<p>tel : {{ c.tel }}</p>
				<p>address : {{ c.address }}</p>
			</li>
		</ul>
		<p v-else>데이터를 불러오는 중...</p>

		<!-- 페이지네이션 -->
		<div style="margin-top: 20px">
			<button @click="pageno--" :disabled="pageno <= 1">이전</button>
			<button @click="pageno++" :disabled="pageno >= totalPages">다음</button>
		</div>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
}
h2 {
	margin-bottom: 20px;
}
li {
	list-style: none;
	background-color: bisque;
	border-radius: 20px;
	padding: 10px;
	margin-bottom: 20px;
}
</style>
