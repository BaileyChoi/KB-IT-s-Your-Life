<script>
import { useRoute } from "vue-router";
import members from "@/members.json";

export default {
	name: "MemberInfo",
	setup() {
		const currentRoute = useRoute();
		const id = parseInt(currentRoute.params.id, 10);
		const member = members.find((m) => m.id === id);
		return { currentRoute, member };
	},
};
</script>

<template>
	<div class="card card-body">
		<h2>Member Info</h2>
		<div>
			경로 패턴: /members/:id<br />
			요청 경로: {{ currentRoute.path }}<br />
			id 값: {{ currentRoute.params.id }}<br />
		</div>
	</div>

	<div className="mt-5">
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
