import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/buscar",
      name: "buscar",
      component: () => import("../views/BuscarOperadorasView.vue"),
    },
    {
      path: "/adicionar",
      name: "adicionar",
      component: () => import("../views/AdicionarOperadoraView.vue"),
    },
  ],
});

export default router;
