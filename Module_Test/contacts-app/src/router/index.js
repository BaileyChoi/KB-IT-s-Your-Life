import ContactDetailPage from "@/components/ContactDetailPage.vue";
import ContactEditPage from "@/components/ContactEditPage.vue";
import ContactListPage from "@/components/ContactListPage.vue";
import ContactWritePage from "@/components/ContactWritePage.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			name: "home",
			redirect: "/contacts",
		},
		{
			path: "/contacts",
			name: "contacts",
			component: ContactListPage,
		},
		{
			path: "/contacts/detail/:id",
			name: "contacts/detail",
			component: ContactDetailPage,
		},
		{
			path: "/contacts/write",
			name: "contacts/write",
			component: ContactWritePage,
		},
		{
			path: "/contacts/edit/:id",
			name: "contacts/edit",
			component: ContactEditPage,
		},
	],
});

export default router;
