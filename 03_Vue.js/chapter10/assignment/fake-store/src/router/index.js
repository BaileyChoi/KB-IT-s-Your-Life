import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import ElectronicPage from "@/pages/ElectronicPage.vue";
import JewelryPage from "@/pages/JewelryPage.vue";
import MensClothingPage from "@/pages/MensClothingPage.vue";
import WomensClothingPage from "@/pages/WomensClothingPage.vue";

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
