<script setup>
import axios from "axios";
import { ref } from "vue";

const url = "/api/users";
const users = ref(null);

const name = ref("");
const age = ref(0);
const phone = ref("");

const requestAPI = async () => {
	try {
		const response = await axios.get(url);
		console.log(response);

		users.value = response.data;
	} catch (e) {
		console.log(e);
	}
};

const addUser = async () => {
	try {
		const response = await axios.post(url, {
			name: name.value,
			age: age.value,
			phone: phone.value,
		});
		console.log(response);
		requestAPI();
	} catch (e) {
		console.log(e);
	}
};

const deleteUser = async (id) => {
	try {
		const response = await axios.delete(`${url}/${id}`);
		console.log(response);
		requestAPI();
	} catch (e) {
		console.log(e);
	}
};
</script>

<template>
	<h1>사용자 목록</h1>
	<button type="button" @click="requestAPI()">조회</button>

	<h2>사용자 정보</h2>
	<table border="1">
		<thead>
			<tr>
				<th>ID</th>
				<th>이름</th>
				<th>나이</th>
				<th>핸드폰</th>
			</tr>
		</thead>
		<tbody>
			<tr v-for="user in users" :id="user.id">
				<td>
					{{ user.id }}
				</td>
				<td>
					{{ user.name }}
				</td>
				<td>
					{{ user.age }}
				</td>
				<td>
					{{ user.phone }}
				</td>
				<td>
					<button @click="deleteUser(user.id)">삭제</button>
				</td>
			</tr>
		</tbody>
	</table>

	<h2>새 사용자 추가</h2>
	<input type="text" placeholder="이름" v-model="name" />
	<input type="number" placeholder="나이" v-model="age" />
	<input type="text" placeholder="핸드폰" v-model="phone" />
	<button @click="addUser">추가</button>
</template>

<style scoped></style>
