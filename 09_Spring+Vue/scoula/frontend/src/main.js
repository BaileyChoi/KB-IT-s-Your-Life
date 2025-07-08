import "./assets/main.css";
import "bootstrap/dist/css/bootstrap.css";
import "vue-awesome-paginate/dist/style.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import VueAwesomePaginate from "vue-awesome-paginate";

import App from "./App.vue";
import router from "./router";
import { useKakao } from "vue3-kakao-maps";

const rest_api_key = "d4a73e9455bb1a2570daaa2c91634efb";
useKakao(rest_api_key, ["services"]);

const app = createApp(App);

app.use(VueAwesomePaginate);
app.use(createPinia());
app.use(router);

app.mount("#app");
