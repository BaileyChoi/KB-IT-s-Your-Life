<script>
import members from "@/members.json";

export default {
	name: "Members",
	setup() {
		return { members };
	},
};
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
							class="img-thumbnail"
							style="width: 90px; height: 110px"
							:src="m.photo"
							:title="m.name"
						/><br />
						<h6 class="display-7">{{ m.name }}</h6>
					</router-link>
				</div>
			</div>
		</div>
	</div>
</template>
