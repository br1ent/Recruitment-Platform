import { createRouter, createWebHistory } from 'vue-router'
import HomePageView from "@/views/home/HomePageView.vue";
import ExternalView from "@/views/recruitment/external/ExternalView.vue";
import InternView from "@/views/recruitment/intern/InternView.vue";
import CampusView from "@/views/recruitment/campus/CampusView.vue";
import NotFoundView from "@/views/error/NotFoundView.vue";
import LoginView from "@/views/user/LoginView.vue";
import RegisterView from "@/views/user/RegisterView.vue";
import ResetPasswordView from "@/views/user/ResetPasswordView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      component: HomePageView,
      name: "home-index",
    },
    {
      path: '/recruitment/external',
      component: ExternalView,
      name: "external-index",
    },
    {
      path: '/recruitment/intern',
      component: InternView,
      name: "intern-index",
    },
    {
      path: '/recruitment/campus',
      component: CampusView,
      name: "campus-index",
    },
    {
      path: '/user/login',
      component: LoginView,
      name: "login-index",
    },
    {
      path: '/user/register',
      component: RegisterView,
      name: "register-index",
    },
    {
      path: '/user/resetpwd',
      component: ResetPasswordView,
      name: "resetpwd-index",
    },
    {
      path: '/404',
      component: NotFoundView,
      name: "error-index",
    }
  ],
})

export default router
