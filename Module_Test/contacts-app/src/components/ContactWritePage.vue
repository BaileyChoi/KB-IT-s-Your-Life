<script setup>
import axios from "axios";
import { reactive } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const contactItem = reactive({ name: "", tel: "", address: "", photo: "" });
const BASEURL = "/api/contacts";

const writeContact = async ({ name, tel, address, photo }) => {
	try {
		const payload = { name, tel, address, photo };
		if (confirm("이 상태로 추가하시겠습니까?")) {
			await axios.post(BASEURL, payload);
			router.push("/contacts");
		}
	} catch (error) {
		console.log(error);
	}
};

const submitHandler = (e) => {
	e.preventDefault();
	let { name, tel } = contactItem;
	if (!name || name.trim() === "") {
		alert("이름은 필수 요소입니다.");
		return;
	} else if (!tel || tel.trim() === "") {
		alert("전화번호는 필수 요소입니다.");
		return;
	}
	writeContact({ ...contactItem });
};
</script>

<template>
	<div class="m-2">
		<h3><i class="fa-solid fa-pen-to-square"></i> 새 연락처</h3>
		<form>
			<label>name:</label>
			<input
				type="text"
				class="form-control"
				placeholder="이름을 입력하세요."
				v-model="contactItem.name"
			/>
			<label>tel:</label>
			<input
				type="text"
				class="form-control"
				placeholder="전화번호를 입력하세요."
				v-model="contactItem.tel"
			/>
			<label>address:</label>
			<input
				type="text"
				class="form-control"
				placeholder="주소를 입력하세요."
				v-model="contactItem.address"
			/>
			<label>photo url:</label>
			<input
				type="text"
				class="form-control"
				placeholder="사진의 url을 입력하세요."
				v-model="contactItem.photo"
			/>
		</form>
		<div class="buttonWrap">
			<button
				type="submit"
				class="btn btn-sm btn-primary me-1"
				@click="submitHandler"
			>
				<i class="fa-solid fa-check"> 확인</i>
			</button>
			<button
				type="button"
				class="btn btn-sm btn-primary"
				@click="router.push('/contacts')"
			>
				<i class="fa-solid fa-rotate-left"> 취소</i>
			</button>
		</div>
	</div>
</template>

<style scoped>
label {
	margin-top: 10px;
}
.buttonWrap {
	display: flex;
	justify-content: center;
	margin-top: 10px;
}
</style>
