import { createRouter, createWebHistory } from "vue-router";

import DashboardView from "@/views/DashboardView.vue";
import NotificationView from "@/views/NotificationView.vue";


const router = createRouter({

  history: createWebHistory(),

  routes: [

    {
      path: "/",
      name: "dashboard",
      component: DashboardView
    },

    {
      path: "/notifications",
      name: "notifications",
      component: NotificationView
    }

  ]

});

export default router;