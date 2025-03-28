import { createRouter, createWebHistory } from "vue-router";

import Home from "@/pages/Home.vue";
import About from "@/pages/About.vue";
import Members from "@/pages/Members.vue";
import MemberInfo from "@/pages/MemberInfo.vue";
import Videos from "@/pages/Videos.vue";
import VideoPlayer from "@/pages/VideoPlayer.vue";
import NotFound from "@/pages/NotFound.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/", name: "home", component: Home },
		{ path: "/about", name: "about", component: About },
		{ path: "/members", name: "members", component: Members },
		{ path: "/members/:id", name: "members/id", component: MemberInfo },
		{
			path: "/videos",
			name: "songs",
			component: Videos,
			children: [{ path: ":id", name: "songs/id", component: VideoPlayer }],
		},
		{ path: "/:paths(.*)*", name: "NotFound", component: NotFound },
	],
});
export default router;
