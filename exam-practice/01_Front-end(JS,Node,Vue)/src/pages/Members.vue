<script setup>
import axios from "axios";
import { ref } from "vue";

const members = ref([]);

const fetchData = async () => {
	const BASEURL = "/api/members";
	try {
		const response = await axios.get(BASEURL);
		members.value = response.data;
	} catch (error) {
		console.log("에러 발생" + error);
	}
};

const deleteMember = async (id) => {
	if (confirm("정말 삭제?")) {
		await axios.delete(`/api/members/${id}`);
		await fetchData();
	}
};

fetchData();
</script>

<template>
	<div>
		<h2 class="m-4">이날치 멤버</h2>
		<div class="container">
			<div class="row">
				<div
					v-for="m in members"
					:key="m.id"
					class="col-6 col-xs-6 col-sm-4 col-md-3 col-lg-2"
				>
					<router-link :to="'/members/' + m.id">
						<img
							class="img-thumbnail rounded-circle"
							style="width: 90px; height: 110px"
							:src="m.photo"
							:title="m.name"
						/><br />
						<h6 class="display-7">{{ m.name }}</h6>
					</router-link>
					<button
						class="btn btn-sm btn-danger mt-2"
						@click="deleteMember(m.id)"
					>
						삭제
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped></style>
