import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Submit from "@/components/Submit.vue";
import Dashboard from "@/components/Dashboard.vue";
import ProjectView from "@/components/ProjectView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Dashboard,
    children: [
      {
        path: "/",
        name: "Projects",
        component: ProjectView,
      },
      {
        path: "/submit",
        name: "Submit",
        component: Submit,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
