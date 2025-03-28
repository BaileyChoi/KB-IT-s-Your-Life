import HomePage from "@/pages/HomePage.vue";
import ElectronicPage from "@/pages/ElectronicPage.vue";
import JeweleryPage from "@/pages/JeweleryPage.vue";
import MensClothingPage from "@/pages/MensClothingPage.vue";
import WomensClothingPage from "@/pages/WomensClothingPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: "/",
			name: "home",
			component: HomePage,
		},
		{
			path: "/electronics",
			name: "electronics",
			component: ElectronicPage,
		},
		{
			path: "/jewelery",
			name: "jewelery",
			component: JeweleryPage,
		},
		{
			path: "/mensclothing",
			name: "mensclothing",
			component: MensClothingPage,
		},
		{
			path: "/womensclothing",
			name: "womensclothing",
			component: WomensClothingPage,
		},
	],
});

export default router;
