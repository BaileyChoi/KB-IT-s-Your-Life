import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import About from "@/pages/About.vue";
import TodoList from "@/pages/TodoList.vue";
import AddTodo from "@/pages/AddTodo.vue";
import EditTodo from "@/pages/EditTodo.vue";
import NotFound from "@/pages/NotFound.vue";
import Members from "@/pages/Members.vue";
import MemberInfo from "@/pages/MemberInfo.vue";

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			name: "home",
			component: Home,
		},
		{ path: "/about", name: "about", component: About },
		{ path: "/todos", name: "todos", component: TodoList },
		{ path: "/todos/add", name: "addTodo", component: AddTodo },
		{ path: "/todos/edit/:id", name: "editTodo", component: EditTodo },
		{ path: "/members", component: Members },
		{ path: "/members/:id", component: MemberInfo },
		{ path: "/:paths(.*)*", component: NotFound },
	],
});

export default router;
