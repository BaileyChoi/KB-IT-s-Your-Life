import { createRouter, createWebHistory } from "vue-router";

import Home from "@/pages/Home.vue";
import About from "@/pages/About.vue";
import Members from "@/pages/Members.vue";
import MemberInfo from "@/pages/MemberInfo.vue";
import Videos from "@/pages/Videos.vue";
import NotFound from "@/pages/NotFound.vue";

const membersIdGuard = (to, from) => {
	// members/:id 경로는 반드시 이전 경로가
	// /members, /members:id 인 경우만 네비게이션 허용함
	if (from.name !== "members" && from.name !== "members/id") {
		return false;
	}
};

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/", component: Home },
		{ path: "/about", component: About },
		{ path: "/members", component: Members },
		{
			path: "/members/:id",
			component: MemberInfo,
			beforeEnter: membersIdGuard,
		},
		{
			path: "/videos",
			component: Videos,
		},
		{ path: "/:paths(.*)*", component: NotFound },
	],
});

router.beforeEach((to) => {
	//to.query에 속성이 존재할 경우 제거된 경로로 재이동
	if (to.query && Object.keys(to.query).length > 0) {
		return { path: to.path, query: {}, params: to.params };
	}
});

router.afterEach((to, from, failure) => {
	if (isNavigationFailure(failure)) {
		console.log("@@ 내비게이션 중단 : ", failure);
		return { name: "home" };
	}
});

export default router;
