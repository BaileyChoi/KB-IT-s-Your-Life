<script setup>
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import { ref } from "vue";

const route = useRoute();
const router = useRouter();
const BASEURL = "/api/contacts";
const id = route.params.id;

const contact = ref({});

const fetchContact = async () => {
	try {
		const response = await axios.get(BASEURL + `/${id}`);
		contact.value = response.data;
	} catch (error) {
		console.log(error);
	}
};

const deleteContact = async () => {
	try {
		if (confirm("정말 삭제하시겠습니까?")) {
			await axios.delete(BASEURL + `/${id}`);
			router.push("/contacts");
		}
	} catch (error) {
		console.log(error);
	}
};

fetchContact();
</script>

<template>
	<div class="m-2">
		<h3><i class="fa-solid fa-address-card"></i> 연락처</h3>
		<div class="d-flex">
			<img :src="contact.photo" alt="photo" width="130px" height="130px" />
			<table class="ms-5">
				<tr>
					<td>ID</td>
					<td>{{ contact.id }}</td>
				</tr>
				<tr>
					<td>name</td>
					<td>{{ contact.name }}</td>
				</tr>
				<tr>
					<td>tel</td>
					<td>{{ contact.tel }}</td>
				</tr>
				<tr>
					<td>address</td>
					<td>{{ contact.address }}</td>
				</tr>
				<tr>
					<button
						class="btn btn-sm btn-primary"
						@click="router.push('/contacts')"
					>
						<i class="fa-solid fa-list"> 목록</i>
					</button>
					<button
						class="btn btn-sm btn-primary"
						@click="router.push('/contacts/edit/' + id)"
					>
						<i class="fa-solid fa-pen-to-square"> 수정</i>
					</button>
					<button class="btn btn-sm btn-danger" @click="deleteContact">
						<i class="fa-solid fa-trash-can"> 삭제</i>
					</button>
				</tr>
			</table>
		</div>
	</div>
</template>

<style scoped>
img {
	border-radius: 10px;
}

button {
	margin: 10px 0 0 2px;
}
</style>
