<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const contacts = ref([]);

const fetchContacts = async () => {
	const BASEURL = "/api/contacts";
	try {
		const response = await axios.get(BASEURL);
		contacts.value = response.data;
	} catch (error) {
		console.log(error);
	}
};

fetchContacts();
</script>

<template>
	<div class="m-2">
		<h3><i class="fa-solid fa-address-book"></i> 연락처</h3>
		<br />
		<table>
			<tr>
				<th>id</th>
				<th>name</th>
				<th>tel</th>
			</tr>
			<tr v-for="c in contacts" :key="c.id">
				<td>{{ c.id }}</td>
				<td>
					<img :src="c.photo" alt="photo" class="rounded-circle" width="20" />
					<router-link :to="'/contacts/detail/' + c.id">{{
						c.name
					}}</router-link>
				</td>
				<td>{{ c.tel }}</td>
			</tr>
		</table>
		<button
			class="btn btn-sm btn-primary"
			@click="router.push('/contacts/write')"
		>
			<i class="fa-solid fa-pen-to-square"></i> 새 연락처
		</button>
	</div>
</template>

<style scoped>
table {
	width: 100%;
}
button {
	float: right;
	margin-right: 20px;
}
</style>
