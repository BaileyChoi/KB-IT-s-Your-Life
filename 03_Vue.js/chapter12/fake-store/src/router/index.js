import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import ElectronicPage from "@/pages/ElectronicPage.vue";
import JewelryPage from "@/pages/JewelryPage.vue";
import MensClothingPage from "@/pages/MensClothingPage.vue";
import WomensClothingPage from "@/pages/WomensClothingPage.vue";
import ProductDetailPage from "@/pages/ProductDetailPage.vue";
import ProductWritePage from "@/pages/ProductWritePage.vue";
import ProductEditPage from "@/pages/ProductEditPage.vue";

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
			path: "/jewelry",
			name: "jewelry",
			component: JewelryPage,
		},
		{
			path: "/mensclothing",
			name: "men's clothing",
			component: MensClothingPage,
		},
		{
			path: "/womensclothing",
			name: "women's clothing",
			component: WomensClothingPage,
		},
		{ path: "/product/:id", name: "product/id", component: ProductDetailPage },
		{
			path: "/product/write",
			name: "product/write",
			component: ProductWritePage,
		},
		{
			path: "/product/edit:id",
			name: "product/edit",
			component: ProductEditPage,
		},
	],
});
export default router;
